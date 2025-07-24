import os
import json
from datetime import datetime
import statistics
from langchain import schema
from langchain.vectorstores import FAISS
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from utilDB._Document import Read_document
from utilDB._CSV import CSV
from _common import Settings, Common_func

# Class & LLM setup
St = Settings()
Cf = Common_func()

# DEBUG mode
DEBUG_DOC = False
DEBUG_REPORT = False


class UtilDB:
    """UtilDB class
    This class is a function that creates a database.
    The database is created using FAISS. It takes documents as input, 
    splits them into chunks, and registers them in the database.
    """
    def __init__(self,
                embeddings,
                db_dir_path,
                filename_progress=None,
                filename_dump=None,
                llm=None,
                n_max_workers=St.N_MAX_WORKERS,
                chunk_size_tsg=None,
                chunk_size_spec=None):
        """
        Initialize class

        Parameters
        ----------
        embeddings : embedding
            embedding parameter
        db_dir_path : str
            path of DB directory
        filename_dump : str
            filename of dump (CSV)
        filename_progress : str
            filename of progress file
        llm : UtilAI
            LLM utility class
        n_max_workers : int
            degree of parallelism of processing
        stop_db_file : str
            filename of stop file
        chunk_size_tsg : int
            the number of characters when splitting a sentence @TSG
        chunk_size_spec : int
            the number of characters when splitting a sentence @SPEC

        Returns
        -------
        None
        """
        self.md_dir_path = db_dir_path
        self.db_dir_path = os.path.join(db_dir_path, 'db_doc')
        self.filename_dump = filename_dump
        
        self.llm = llm
        if self.llm is not None:
            self.llm.set_logger(db_dir_path, filename_dump)

        self.n_max_workers = n_max_workers
        self.embeddings = embeddings
        self.db = None
        self.k_neighbor = St.K_NEIGHBOR
        
        if chunk_size_tsg is None:
            self.chunk_size_tsg=St.CHUNK_SIZE_TSG
        else:
            self.chunk_size_tsg = chunk_size_tsg
        if chunk_size_spec is None:
            self.chunk_size_spec = St.CHUNK_SIZE_SPEC
        else:
            self.chunk_size_spec = chunk_size_spec
       

    def initialize(self, persona):
        filename = os.path.join(self.md_dir_path, 'metadata.json')
        if not os.path.exists(filename):
            os.makedirs(self.md_dir_path, exist_ok=True)
            metadata = {
                'version': '1.0.1',
                'field': persona,
                'cat_list': [],
                'UID': 0
                }
            with open(filename, 'w', encoding='utf8') as f:
                json.dump(metadata, f)


    def add(self,
            doc_file_path: str,
            doc_file_name: str,
            doc_type: int,
            divide_set: int,
            translate_language: int):
        """
        Read a document file,
        transform it to the langchain.schema.Document format,
        and register it to the langchain.vectorstores.FAISS database.

        Parameters
        ----------
        progress_db_file : str
            file path of progress file
        doc_file_path : str
            file path of the document
        doc_file_name : str
            file name of the document. It will be registered as "source".
        self.db_dir_path : str
            file path of the database
        doc_type : int
            document type. 0 (Trouble shooting guide) or
            1 (Specification, Manual).
            It will be registered as "doc_type".
        divide_set : int
            setting of document division.
            0 (fixed length) or 1 (based on sections).
        translate_language : int
            translation. 0(no translation) or 1 (translate to Japanese)
            or 2 (translate to English)

        Returns
        -------
        int
            error status (0-: normal, 100-: error)
        int
            result of document division. 0 (fixed length) or
            1 (based on sections).
            It was registered as "divide_result".
        """

        #output
        divide_result = -1
        uid_doc = 0

        # read file
        docs, divide_result, err_message =\
            self.read(doc_file_path, doc_file_name,
                      divide_set, doc_type, uid_doc)

        try:
            # 追加登録
            db = FAISS.from_documents(docs, self.embeddings)
            db.save_local(self.db_dir_path)
            self.db = db


        except Exception as e:
            # self.log.dump("[ERROR]", "[add]", str(e))
            # 不明なエラー
            status = St.ERR_DB_MAIN_UNEXPECTED
            return status, 0, 0, 0

        return St.SUCCESS_DB_ADD, divide_result



    def load_db(self):
        """
        This function load DB

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        if self.db is None:
            self.db = FAISS.load_local(self.db_dir_path, self.embeddings, allow_dangerous_deserialization=True)

    def read(
            self,
            doc_file_path,
            doc_file_name,
            divide_set,
            doc_type,
            uid_doc
            ):
        """
        This function load DB

        Parameters
        ----------
        doc_file_path : str
            path of document
        doc_file_name : str
            filename of document
        divide_set : int
            mode of divide (chunk : 0, section : 1)
        doc_type : int
            type of document (TSG : 0, SPEC : 1)
        uid_doc : int
            unique ID of document

        Returns
        -------
        list
            list of documents
        int
            result of document division. 0 (fixed length) or 1 (based on sections).         
        str
            error message
        
        """

        # Start reading
        doc = Read_document(self.md_dir_path, self.filename_dump, self.llm)

        # _progress(progress_db_file, "0: Start processing")
        if doc._detect_file_extension(doc_file_path, St.EXT_CSV):
            doc = CSV(self.md_dir_path,
                      self.filename_dump,
                      self.llm,
                      n_max_workers=self.n_max_workers,
                      chunk_size_tsg=self.chunk_size_tsg,
                      chunk_size_spec=self.chunk_size_spec)
            doc_extension = St.ID_EXT_CSV
        else:
            return None, 0, 'doc format error'

        # read document
        _, _ = doc.read(doc_file_path)
        _, _, divide_result = doc.split(
            divide_set,
            doc_type
            )
        
        # register document
        docs, _ = self._reg_document(
            doc.doc_list(),
            doc_file_name,
            doc_type,
            divide_result,
            doc_extension,
            uid_doc
            )

        return docs, divide_result, ''

    def load_metadata(self) -> tuple[int, dict]:
        """
        This function loads metadata file for DB.

        Parameters
        ----------
        file_path : str
            file path

        Returns
        -------
        int
            error status (0-: normal, 500-: error)
        dict
            metadata('field':str, 'cat_list':[str,...])
        """
        filename = os.path.join(self.md_dir_path, St.FILENAME_METADATA)
        if not os.path.exists(filename):
            return St.ERR_DB_LOAD_MD, {}

        with open(filename, 'r', encoding='utf8') as f:
            metadata = json.load(f)
        return St.SUCCESS, metadata


    def _reg_document(self,
                      doc_list: list[list[str]],
                      doc_file_name: str,
                      doc_type: int,
                      divide_result: int,
                      doc_extension: int,
                      uid_doc: int
                      ) -> tuple[list[schema.Document], int]:
        """
        Register documents to the langchain.schema.Document format

        Parameters
        ----------
        doc_list : list[list[str]]
            document list. list of [title, document].
            It will be registered as [title, original_content].
        doc_file_name : str
            file name of document. It will be registered as "source".
        doc_type : int
            document type. 0 (Trouble shooting guide) or
            1 (Specification, Manual).
            It will be registered as "doc_type".
        divide_result : int
            result of document division. 0 (fixed length) or
            1 (based on sections).
            It will be registered as "divide_result".
        doc_extension : int
            file extension
            (0: others, 1: ".doc" or ".docx", 2: ".pdf", 3: ".txt", 4: ".csv").
            It will be registered as "doc_extension".

        Returns
        -------
        list[langchain.schema.Document]
            document list. list of [langchain.schema.Document].
        int
            detected language (0: others, 1: Japanese, 2: English) of
            the document.
            It was registered as "language".
        """
        time_now = datetime.now().strftime('%Y/%m/%d,%H:%M')

        # To check language
        lang_count_arr = []
        for each_doc in doc_list:
            each_txt = each_doc[1]
            if len(lang_count_arr) < 10:
                lang_result = Cf.detect_language(each_txt)
                if lang_result == 0:
                    pass
                else:
                    lang_count_arr.append(lang_result)
        language = statistics.mode(lang_count_arr)

        # 重複削除
        # doc_list = list(dict.fromkeys(doc_list))

        # idなどを付与。[ID, title, text, abstract, English text, num token]
        doc_list = [['sentence{}_{}'.format(uid_doc, i),
                     x[0],
                     x[1],
                     x[1],  # _abstract(x[1]),
                     x[1],  # _common.Translate(x[1])[3],
                     0
                     ]
                    for i, x in enumerate(doc_list)]
        

        # document登録
        docs = []
        for x in doc_list:
            docs.append(
                schema.Document(
                    page_content=x[4],
                    metadata={
                        "field": "",
                        "cat_list": [],

                        "source": doc_file_name,
                        "doc_type": doc_type,
                        "language": language,
                        "divide_result": divide_result,
                        "time_upload": time_now,
                        "doc_extension": doc_extension,

                        "title": x[1],
                        "num_token": x[5],
                        "need_read": [],
                        "original_content": x[2],
                        "abstract": x[3],
                        "ID": x[0]
                    }
                )
            )

        return docs, language
    
    def check_db(self) -> tuple[int, str, list, dict, list]:
        """
        get and check database

        Parameters
        ----------
        self.db_dir_path : str
            file path of database

        Returns
        -------
        int
            error status (0-: normal, 200-: error)
        str
            field of the incident
        list
            category list of the incident
        dict
            database content (key: dict_key, value: langchain.schema.Document)
        list
            database content (list)
        """

        # DB check
        fn_faiss = os.path.join(self.db_dir_path, 'index.faiss')
        if os.path.isfile(fn_faiss):
            try:
                self.load_db()
            except Exception as e:
                # self.log.dump("[ERROR]", "[check_db]", str(e))
                # DBフォーマットエラー
                status = St.ERR_DB_CHECK_DB_DB_FORMAT
                return status, "", [], {}, []
        else:
            # DB存在せず
            status = St.ERR_DB_CHECK_DB_NOT_EXIST
            return status, "", [], {}, []

        # initial setting
        content_dict = self.db.docstore._dict
        db_key_list = list(content_dict.keys())
        content_list = []
        cat_list = []
        field_com = ""
        cat_list_com = []

        # metadata
        state_file, metadata_file = self.load_metadata()
        field_com = metadata_file['field']

        # extract all documents
        for dict_key in db_key_list:
            # Check if "source" was already registered to content_list
            source_exist_flg = False
            current_doc = content_dict[dict_key]
            current_source = current_doc.metadata['source']
            for j, content_list_j in enumerate(content_list):
                if content_list_j["source"] == current_source:
                    source_exist_flg = True
                    break

            if source_exist_flg:
                # "source" was already registered to content_list
                # Therefore, current_doc will be added to doc_list
                content_list[j]["doc_list"].append(
                    {"doc": current_doc.page_content,
                     "title": current_doc.metadata["title"],
                     "num_token": current_doc.metadata["num_token"],
                     "need_read": current_doc.metadata["need_read"],
                     "original_content":
                         current_doc.metadata["original_content"],
                     "abstract": current_doc.metadata["abstract"],
                     "ID": current_doc.metadata["ID"],
                     "dict_key": dict_key},
                    )
            else:
                # "source" was not registered to content_list yet
                # Therefore, current_source will be registered

                # field and cat_list are not extracted yet
                field = current_doc.metadata["field"]
                cat_list = current_doc.metadata["cat_list"]
                if field != "":
                    field_com = field
                if cat_list != []:
                    cat_list_com = cat_list

                content_list.append(
                    {
                        "source": current_source,
                        "doc_type": current_doc.metadata["doc_type"],
                        "language": current_doc.metadata["language"],
                        "divide_result":
                            current_doc.metadata["divide_result"],
                        "time_upload":
                            current_doc.metadata["time_upload"],
                        "doc_extension":
                            current_doc.metadata["doc_extension"],
                        "field":
                            field,
                        "cat_list":
                            cat_list,
                        "doc_list": [{"doc": current_doc.page_content,
                                      "title":
                                          current_doc.metadata["title"],
                                      "num_token":
                                          current_doc.metadata["num_token"],
                                      "need_read":
                                          current_doc.metadata["need_read"],
                                      "original_content":
                                          current_doc.metadata[
                                            "original_content"],
                                      "abstract":
                                          current_doc.metadata["abstract"],
                                      "ID":
                                          current_doc.metadata["ID"],
                                      "dict_key":
                                          dict_key}],
                    }
                )

        status = St.SUCCESS
        return status, field_com, cat_list_com, content_dict, content_list


class UtilDB_KG(UtilDB):
    """UtilDB_KG class
    This class is a function that creates a database.
    The database is created using FAISS. It takes documents as input, 
    splits them into chunks, and registers them in the database.
    It investigates the chunks and creates a logic tree.
    """
    def __init__(self, 
                 embeddings,
                 db_dir_path,
                 filename_progress=None,
                 filename_dump=None,
                 llm=None,
                 n_max_workers=St.N_MAX_WORKERS,
                 chunk_size_tsg=None,
                 chunk_size_spec=None):
        """
        Initialize class

        Parameters
        ----------
        embeddings : embedding
            embedding parameter
        db_dir_path : str
            path of DB directory
        filename_dump : str
            filename of dump (CSV)
        filename_progress : str
            filename of progress file
        llm : UtilAI
            LLM utility class
        n_max_workers : int
            degree of parallelism of processing
        stop_db_file : str
            filename of stop file
        chunk_size_tsg : int
            the number of characters when splitting a sentence @TSG
        chunk_size_spec : int
            the number of characters when splitting a sentence @SPEC

        Returns
        -------
        None
        """

        self.md_dir_path = db_dir_path
        self.db_dir_path = os.path.join(db_dir_path, 'db_kg')
        self.filename_dump = filename_dump
        
        self.llm = llm
        if self.llm is not None:
            self.llm.set_logger(db_dir_path, filename_dump)

        self.n_max_workers = n_max_workers
        self.embeddings = embeddings
        self.db = None
        self.k_neighbor = St.K_NEIGHBOR
        
        if chunk_size_tsg is None:
            self.chunk_size_tsg=St.CHUNK_SIZE_TSG
        else:
            self.chunk_size_tsg = chunk_size_tsg
        if chunk_size_spec is None:
            self.chunk_size_spec = St.CHUNK_SIZE_SPEC
        else:
            self.chunk_size_spec = chunk_size_spec
      
        
        # create directory
        # DB check
        fn_faiss = os.path.join(self.db_dir_path, 'index.faiss')
        if os.path.isfile(fn_faiss):
            pass
        else:
            db = FAISS.from_texts(["1"], self.embeddings, ids=[1])
            db.delete([1])
            db.save_local(self.db_dir_path)

if __name__ == '__main__':
    pass
