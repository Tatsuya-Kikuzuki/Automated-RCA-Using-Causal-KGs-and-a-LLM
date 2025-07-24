##############################################################################
# -*- coding: utf-8 -*-

from _common import Settings, Common_func
import os
import sys


##############################################################################
# parameter
# EMBED_MODEL = "intfloat/multilingual-e5-large"
# model = SentenceTransformer(EMBED_MODEL)
COS_THRE = 0.85
NUM_TRIAL = 3
BRANCH_MAX = 100
HOP_MAX = 20
CNT_ENT_MAX = 1000
AND_SEARCH_MAX = 5
NUM_PATH_MAX = 15
VIZ_KG_PLUS_1HOP = True
TOP_K = 3

##############################################################################

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)


# Class & LLM setup
St = Settings()
Cf = Common_func()


class RCAkg:
    """RCAkg class
    This class is designed to perform root cause analysis using a knowledge graph.
    """
    def __init__(self,
                 db_dir_path=None,
                 filename_progress=None, filename_dump=None,
                 embeddings=None, llm=None):
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
        pass

##############################################################################
    # Main function
    def main(self,
             kg: dict,
             query: str
             ):
        """
        According to input query, 
        search similar entities in knowledge graph (DB), 
        make RCA path(es) generated from the searched entities, 
        and response answer of analysis results of those RCA path(es).

        Parameters
        ----------
        progress_file : str
            progress report file
        kg : dict
            knowledge graph
        db_dir_path : str
            file path of the database
        query : str
            input query describing incidents. e.g., "PTP unlocked" 
        progress : instance of Progress() defined in _common.py
            progress of chat_rca
        prog_percent_list_kg : list
            list of progress percentage
        top_k : int (default=3)
            number of entities retrieved in order of cosine similarity

        Returns
        -------
        int
            error status (0: normal, 600-: error)
        str
            response document of RCA results
        int
            language of query(0:English, 1:Japanese, 2:Else)
        int
            Whether the language of the database and the query are compatible.
            (0:valid, 1:invalid)
        """
        
        # Get response list for tsg
        import subprocess, pickle
        
        input_prompt = {"query": query, "kg": kg}
        with open('LLM/input_prompt.bin', 'wb') as p:
            pickle.dump(input_prompt, p)
            
        # .exe file
        exe_path = r'LLM/prompts.exe'
        # MODE
        MODE = 4

        result = subprocess.run([exe_path, str(MODE), str(0)], 
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
