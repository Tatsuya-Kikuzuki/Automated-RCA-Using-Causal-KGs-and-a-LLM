import csv
import os
import sys
import pandas as pd

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from _common import Settings
from utilDB._Document import Read_document

# Class & LLM setup
St = Settings()


class CSV(Read_document):
    """CSV class
    This class loads CSV files and splits sentences for FAISS.
    """
    def __init__(self,
                db_dir_path,
                filename_dump, 
                llm, 
                n_max_workers=St.N_MAX_WORKERS,
                chunk_size_tsg=St.CHUNK_SIZE_TSG,
                chunk_size_spec=St.CHUNK_SIZE_SPEC):
        """
        Initialize class

        Parameters
        ----------
        db_dir_path : str
            path of DB directory
        filename_dump : str
            filename of dump (CSV)
        llm : UtilAI
            LLM utility class
        n_max_workers : int
            degree of parallelism of processing
        chunk_size_tsg : int
            the number of characters when splitting a sentence @TSG
        chunk_size_spec : int
            the number of characters when splitting a sentence @SPEC

        Returns
        -------
        None
        """
        super().__init__(
            db_dir_path, 
            filename_dump, 
            llm, n_max_workers,
            chunk_size_tsg, chunk_size_spec)

    def doc_list(self):
        """
        a function that returns a list of chunks after splitting

        Parameters
        ----------
        None

        Returns
        -------
        list
            list of chunks
        """
        return self.doc_sentences + self.doc_dfs

    def read(self, filename: str):
        """
        This function reads CSV file

        Parameters
        ----------
        filename : str
            filename of CSV file

        Returns
        -------
        int
            error status (0-: normal, 100-: error)
        str
            error message
        """
        # check extension
        if not self._detect_file_extension(filename, St.EXT_CSV):
            # self.log.dump("[ERROR]", "[read](1)", 'invalid file')
            return St.ERR_READ, 'invalid file'

        # read csv
        status, err_message, self.document = self.read_csv(filename, 'cp932')
        if not status == St.SUCCESS:
            if 'cp932' in str(err_message):
                status, err_message, self.document =\
                    self.read_csv(filename, 'utf-8')
                if not status == St.SUCCESS:
                    self.log.dump("[ERROR]", "[read](2)", err_message)
                    return St.ERR_READ, err_message
                else:
                    pass
            else:
                self.log.dump("[ERROR]", "[read](3)", err_message)
                return St.ERR_READ, err_message
        else:
            pass

        # split document
        try:
            pass
        except Exception as e:
            self.log.dump("[ERROR]", "[read](4)", err_message)
            return St.ERR_READ, e

        return St.SUCCESS, ''

    def split(self, divide_set, doc_type):
        """
        This function splits a sentence

        Parameters
        ----------
        divide_set : int
            mode of divide (chunk : 0, section : 1)
        doc_type : int
            type of document (TSG : 0, SPEC : 1)

        Returns
        -------
        int
            error status (0-: normal, 100-: error)
        str
            error message
        int 
            result of dividing process (fault : 0, success : 1)
        """
        # 文書分割
        # doc_sentences = []
        divide_result = St.DIVIDE_RESULT_FAULT
        if divide_set == St.DIVIDE_SET_SECTION:
            # divide text @ section
            pass

        if divide_result == St.DIVIDE_RESULT_FAULT:
            # divide text @ chunk
            try:
                status, err_message, self.doc_sentences =\
                    self.split_chunk(doc_type)
                if not status == St.SUCCESS:
                    return status, err_message, divide_result
            except Exception as e:
                self.log.dump("[ERROR]", "[split](1)", e)
                return St.ERR_SPLIT, e, divide_result

        # Tableをチャンク分割
        self.doc_dfs = []

        return St.SUCCESS, '', divide_result

    def split_chunk(self, doc_type):
        """
        This function splits a sentence into chunks.

        Parameters
        ----------
        doc_type : int
            type of document (TSG : 0, SPEC : 1)

        Returns
        -------
        int
            error status (0-: normal, 100-: error)
        str
            error message
        list 
            list of chunks
        """
        # チャンク分割
        doc_sentences = []

        for row in self.document:
            if len(row) == 0:
                pass
            elif len(row) == 1:
                # only document
                doc_sentences += [["", row[0]]]
            elif len(row) == 2:
                # document + title
                doc_sentences += [[row[1], row[0]]]
            elif len(row) > 2:
                # _dump("[ERROR]",
                #        "[_read_csv]",
                #        "CSV format error")
                # doc読み込みエラー
                err_message = "CSV format error"
                self.log.dump("[ERROR]", "[split_chunk]", err_message)
                return St.ERR_READ, err_message, []

        return St.SUCCESS, '', doc_sentences

    def read_csv(self, filename, encoding):
        """
        This function reads csv file.

        Parameters
        ----------
        filename : str
            filename of csv file
        encoding : str
            encoding (cp932, utf-8)
        Returns
        -------
        int
            error status (0-: normal, 100-: error)
        str
            error message
        dict
            list of documents
        """
        try:
            df_data = pd.read_csv(
                filename,  
                header=None, 
                names=['incident', 'title'], 
                encoding=encoding).fillna('')
            document = df_data[df_data['incident'] != ''].values

            #with open(filename, "r", encoding=encoding) as f:
            #    document = [row for row in csv.reader(f)]

        except Exception as e:
            return St.ERR_READ, e, None
        return St.SUCCESS, '', document

##############################################################################
# Test


if __name__ == '__main__':
    pass
