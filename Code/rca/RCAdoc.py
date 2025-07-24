from tabulate import tabulate
import re
# from memory_profiler import profile

import os
import sys

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from _common import Settings, Common_func
try:
    from _base_rca import Base
except Exception as e:
    from rca._base_rca import Base

# Class & LLM setup
St = Settings()
Cf = Common_func()


class RCAdoc(Base):
    """RCAdoc class
    The class has functions related to root cause analysis for RAG.
    """
    def __init__(self,  
                db_dir_path=None, embeddings=None,
                filename_progress=None, filename_dump=None,
                llm=None, n_max_workers=St.N_MAX_WORKERS):
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
        self.k_neighbor = 10
        self.db_candidate = None
        self.set_doc_type(St.DOC_TYPE_TSG)
        
    def set_doc_type(self, doc_type):
        """
        This function sets type of document.

        Parameters
        ----------
        doc_type : int

        Returns
        -------
        None
        """
        self.doc_type = doc_type

    def analysis(self, query):
        """This function get list of response about previous incident

        Parameters
        ----------
        :param progress_file : progress report file
        :type progress_file : str
        :param db : Database
        :type db : FAISS
        :param query : query
        :type query : str
        :param query : query
        :type query : str
        :param language : language of query
        :type language : int
        
        Returns
        -------
        :return status
        :rtype int
        :rtype list
        :raises None
        """

        # self.progress.progress('Start detecting previous incident @analysis')

        # check query
        if not self._check_query(query) == St.SUCCESS:
            return St.ERR_RCA_MAIN_ARG

        # Get response list for tsg
        import subprocess, pickle
        
        input_prompt = {"query": query, "db_doc": self.udb.db}
        with open('LLM/input_prompt.bin', 'wb') as p:
            pickle.dump(input_prompt, p)
            
        
        # .exe file
        exe_path = r'LLM/prompts.exe'
        # MODE
        MODE = 5

        result = subprocess.run([exe_path, str(MODE), str(self.doc_type), str(0)], 
                                cwd=os.path.join(parent_dir, 'LLM'),
                                capture_output=True,
                                text=True)

        if "Successfully done!" in result.stdout:
            with open('LLM/output_prompt.bin', 'rb') as p:
                output_prompt = pickle.load(p)
            # output_prompt = {"response_list": response_list , "input_token": input_token_sum, "output_token": output_token_sum}
            response_list = output_prompt["response_list"]
            input_token = output_prompt["input_token"]
            output_token = output_prompt["output_token"]
        else:
            raise ValueError(result.stderr)
     
        # self.progress.progress('End detecting previous incident @analysis')

        return 0, response_list, input_token, output_token
    
    def create_summary(self, response_list, query_lang):
        """This function create and add summary to response_list

        Parameters
        ----------
        :param response_list : list of responses of LLM
        :type response_list : list
        :param query_lang : language of query 
        :type query_lang : int
        
        Returns
        -------
        :return list of response with summary
        :rtype list
        :raises None
        """
        response_list.append({"Summary":""})
        return St.SUCCESS, response_list
