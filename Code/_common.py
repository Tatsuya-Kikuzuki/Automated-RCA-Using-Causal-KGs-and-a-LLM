import yaml
from langdetect import detect

##############################################################################

class Settings:
    """Setting class
    This class contains parameters and error codes that are commonly used 
    throughout the entire system.
    """
    def __init__(self):
        """
        Initialize class

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        # static parameters
        self.VERSION = '1.0.1'

        # error
        self.SUCCESS = 0
        self.SUCCESS_DB_ADD = 1
        self.SUCCESS_DB_T_EXT_OVERW = 1
        self.SUCCESS_DB_T_EXT_NO_CAT_LIST = 2
        self.SUCCESS_DB_T_EXT_NO_DB = 3
        self.SUCCESS_STOP = 4

        self.ERR_DB_MAIN_UNEXPECTED = 100
        self.ERR_DB_MAIN_ARG = 101
        self.ERR_DB_MAIN_ALREADY_EXIST = 102
        self.ERR_DB_MAIN_EXTENSION = 103
        self.ERR_DB_MAIN_DOC_FORMAT = 104
        self.ERR_DB_MAIN_DB_FORMAT = 105
        self.ERR_DB_MAIN_DB_METADATA = 106
        self.ERR_DB_MAIN_METADATA = 107
        self.ERR_DB_MAIN_MAKE_KG = 108
        self.ERR_DB_MAIN_TOKEN_LIMIT = 109
        self.ERR_DB_MAIN_FIELD = 110
        self.ERR_DB_MAIN_TSG_NOT_FOUND = 111
        self.ERR_DB_MAIN_SPEC_ALREADY_EXIST = 112
        
        self.ERR_DB_CHECK_DB_UNEXPECTED = 200
        self.ERR_DB_CHECK_DB_ARG = 201
        self.ERR_DB_CHECK_DB_NOT_EXIST = 202
        self.ERR_DB_CHECK_DB_DB_FORMAT = 203

        self.ERR_DB_DELETE_UNEXPECTED = 300
        self.ERR_DB_DELETE_ARG = 301
        self.ERR_DB_DELETE_NOT_EXIST = 302
        self.ERR_DB_DELETE_DB_FORMAT = 303
        self.ERR_DB_DELETE_NO_FILE = 304
        self.ERR_DB_DELETE_DB_METADATA = 305

        self.ERR_DB_T_CAND_UNEXPECTED = 400
        self.ERR_DB_T_CAND_ARG = 401
        self.ERR_DB_T_CAND_COUNT_MAX = 402

        self.ERR_DB_T_EXT_UNEXPECTED = 500
        self.ERR_DB_T_EXT_ARG = 501
        self.ERR_DB_T_EXT_NOT_EXIST = 502
        self.ERR_DB_T_EXT_DB_FORMAT = 503
        # self.ERR_DB_T_EXT_DOC_TYPE = 504
        self.ERR_DB_T_EXT_DB_METADATA = 505
        self.ERR_DB_T_EXT_COUNT_MAX = 506
        self.ERR_DB_T_EXT_METADATA = 507

        self.ERR_RCA_MAIN_UNEXPECTED = 600
        self.ERR_RCA_MAIN_ARG = 601
        self.ERR_RCA_MAIN_NOT_EXIST = 602
        self.ERR_RCA_MAIN_NO_DB = 603
        # self.ERR_RCA_MAIN_ = 604
        self.ERR_RCA_MAIN_MODIFY = 605
        self.ERR_RCA_MAIN_PREV = 606
        self.ERR_RCA_MAIN_NEW = 607
        self.ERR_RCA_MAIN_METADATA = 608
        self.ERR_RCA_MAIN_NO_DOC = 609
        self.ERR_RCA_MAIN_KG_UNEXPECTED = 610
        self.ERR_RCA_MAIN_KG_NOT_EXIST = 611
        self.ERR_RCA_MAIN_KG_DB_NOT_EXIST = 612
        self.ERR_RCA_MAIN_KG_NO_INCIDENT = 613
        self.ERR_RCA_MAIN_INPUT_FORMAT = 614
        self.ERR_RCA_MAIN_QUERY_WORD_LIMIT = 615
        self.ERR_RCA_MAIN_CREATE_SUMMARY = 616
        self.ERR_RCA_MAIN_KG_CREATE_SUMMARY = 617
        self.WARNING_RCA_MAIN_LANGUAGE = 1

        self.ERR_DB_SAVE_MD = 700
        self.ERR_DB_LOAD_MD = 800

        self.ERR_READ = 101
        self.ERR_SPLIT = 102
        self.ERR_METADATA_FILE_MAIN = 107
        self.ERR_FOLDER_NOT_FOUND_MAIN = 108
        self.ERR_METADATA_FILE_MDS = 700
        self.ERR_METADATA_FILE_MDL = 800
        self.ERR_METADATA_FILE_TEC = 507

        self.ERR_RCA = 1000
        self.WARNING_LANG = 10
        self.WARNING_RCA = 10
        self.WARNING_DB_ALREADY_EXIST = 10
        

        # extension flag
        self.EXT_DOC = '.doc'
        self.EXT_DOCX = '.docx'
        self.EXT_PDF = '.pdf'
        self.EXT_TXT = '.txt'
        self.EXT_CSV = '.csv'

        self.ID_EXT_DOC = 1
        self.ID_EXT_DOCX = 1
        self.ID_EXT_PDF = 2
        self.ID_EXT_TXT = 3
        self.ID_EXT_CSV = 4

        # language
        self.LANG_ENGLISH = 2
        self.LANG_JAPANESE = 1
        self.LANG_OTHER = 0

        # mode KG
        self.MODE_FAST = 0
        self.MODE_SLOW = 1

        # flag for DB
        self.DIVIDE_SET_SECTION = 1
        self.DIVIDE_SET_CHUNK = 0
        self.DOC_TYPE_SPEC = 1
        self.DOC_TYPE_TSG = 0
        self.DIVIDE_RESULT_SUCCESS = 1
        self.DIVIDE_RESULT_FAULT = 0

        # parameter
        self.N_MAX_WORKERS = 10
        self.CHUNK_SIZE_TSG = 300
        self.CHUNK_SIZE_TSG_KG = 5000
        self.CHUNK_SIZE_SPEC = 3000        
        self.K_NEIGHBOR = 10

        self.THRE_POSSIBILITY = 50
        self.FILENAME_METADATA = 'metadata.json'
        self.FILENAME_KG_BIN = 'kgs.bin'
        self.PATH_INTERFACE = 'interface'

        # debug mode
        self.DEBUG_REPORT_KG = False
        self.DEBUG_PICKLE_KG = True
        self.DEBUG_REPORT_LLM = False

##############################################################################

# Class & LLM setup
St = Settings()

##############################################################################

class Common_func:
    """Common_func class
    This class contains functions that are commonly used 
    throughout the entire system.
    """
    def __init__(self):
        """
        Initialize class

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.Set = Settings()

    def load_config(self, filename):
        """
        This function loads config file.

        Parameters
        ----------
        filename : str
            filename of config file.

        Returns
        -------
        dict
            config data
        """
        with open(filename, 'r') as f:
            return yaml.safe_load(f)

    def detect_language(self, text: str) -> int:
        """
        detect language of text

        Parameters
        ----------
        text : str
            input text

        Returns
        -------
        int
            detected language (0: others, 1: Japanese, 2: English)
        """
        try:
            if text == "":
                return self.Set.LANG_OTHER
            else:
                # detect the language
                language = detect(text)
                if language == "en":
                    return self.Set.LANG_ENGLISH
                elif language == "ja":
                    return self.Set.LANG_JAPANESE
                else:
                    return self.Set.LANG_OTHER

        except Exception as e:
            print(str(e))
            # _dump("[ERROR]", "[detect_language]", str(e))
            return 0

    def any_kg(self, kg_check):
        """
        This function determines whether KG data is present.

        Parameters
        ----------
        kg_check : dict
            kg data
        
        Returns
        -------
        bool
            flag (True: present, False: not present)
      
        """
        try:
            if len(kg_check["nodes"]) > 0:
                return True
            else:
                return False      
        except:
            return False
