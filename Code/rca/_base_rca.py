import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from _common import Settings, Common_func

# Class & LLM setup
St = Settings()
Cf = Common_func()


class Base:
    """Base class
    The class has basic functions related to root cause analysis.
    """
    def __init__(
            self, embeddings,
            db_dir_path,
            filename_progress, filename_dump,
            llm, n_max_workers=St.N_MAX_WORKERS):
        """
        Initialize class

        Parameters
        ----------
        embeddings : embedding
            embedding parameter
        db_dir_path : str
            path of DB directory
        filename_progress : str
            filename of progress file
        filename_dump : str
            filename of dump (CSV)
        llm : UtilAI
            LLM utility class
        n_max_workers : int
            degree of parallelism of processing

        Returns
        -------
        None
        """
        self.filename_progress = filename_progress
        self.filename_dump = filename_dump
        self.embeddings = embeddings
        self.llm = llm
        self.n_max_workers = n_max_workers

    def load_udb(self, udb, db_file_path):
        """
        This function loads UtilDB class.

        Parameters
        ----------
        udb : UtilDB
            Utility class for DB
        db_file_path : str
            path of DB directory

        Returns
        -------
        int
            error status (0: normal, 600-: error)

        """
        self.udb = udb
        # self.udb.load_embedded_model()

        try:
            self.udb.load_db()
        except Exception as e:
            self.log.dump("[ERROR]", "[load_db](1)", e)
            return St.ERR_RCA_MAIN_UNEXPECTED

        status, metadata = self.udb.load_metadata()
        if not status == St.SUCCESS:
            e = 'not found metadata.json'
            self.log.dump("[ERROR]", "[load_db](2)", e)
            return status

        self.field = metadata['field']
        self.cat_list = metadata['cat_list']

        if self.field == '':
            self.log.dump("[ERROR]", "[load_db](2)", 'error of field')
            status = St.ERR_RCA_MAIN_ARG

        try:
            self.language_field = Cf.detect_language(self.field)
        except Exception as e:
            self.log.dump("[ERROR]", "[load_db](3)", e)
            return St.ERR_RCA_MAIN_UNEXPECTED

        return St.SUCCESS

    def _check_query(self, query):
        """
        This function determines the language of the query.

        Parameters
        ----------
        query : str
            query

        Returns
        -------
        int
            error status (0: normal, 100-: error)
        """
        self.query = query
        try:
            self.language_query = Cf.detect_language(query)
        except Exception as e:
            self.log.dump("[ERROR]", "[check_query]", e)
            return St.ERR_RCA
        return St.SUCCESS
