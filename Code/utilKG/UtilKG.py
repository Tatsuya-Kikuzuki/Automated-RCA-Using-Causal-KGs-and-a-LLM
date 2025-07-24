import os
import sys
import copy
import networkx as nx

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from _common import Settings, Common_func

# Class & LLM setup
St = Settings()
Cf = Common_func()

CHAT_RCA_LONG_QUERY = True # True: use long query, False: use short query
CHAT_RCA_CONFIDENCE_TH = 80
DEDUPLICATE_ANSWER_KEY = True # extract unique answer key from chat rca answer
MAX_KG_PER_TSG = 2 # setting for sample run
CONFIG_EVENT    = "incident"
NUM_TRY         = 5 # setting for run
RATIO_THRE = 0.995
PARRA = True

if St.DEBUG_PICKLE_KG:
    import pickle

def _loop_check(kg_local: dict, relation_list: list) -> tuple[list, list]:
    """
    Check whether there is a loop in the KG

    Parameters
    ----------
    kg_local : dict
        knowledge graph
    relation_list : list
        list of relations needed to detect the loop

    Returns
    -------
    list
        node list which has loop. e.g., [['3'], ['5', '2'], ['2', '3', '1']]
    list
        edge list which has loop.
        e.g., [[['7', 'causes']], [['4', 'indicates'], ['5', 'causes']],
            [['1', 'causes'], ['2', 'causes'],
                ['6', 'causes'], ['7', 'causes']]]
    """
    g_list = []
    edge_attributes = {}
    
    for edge in kg_local["edges"]:
        if edge["relation"] in relation_list:
            edge_tuple = (edge["source"], edge["target"])
            g_list.append(edge_tuple)
            edge_attributes[edge_tuple] = {
                "id": edge["id"],
                "relation": edge["relation"]
                }

    G = nx.DiGraph(g_list)
    nx.set_edge_attributes(G, edge_attributes)

    cycle_list = []
    cycle_relation_list = []
    for cycle in nx.simple_cycles(G):
        cycle_relation = []
        for i in range(len(cycle)):
            u = cycle[i]
            v = cycle[(i + 1) % len(cycle)]
            edge_data = G.get_edge_data(u, v)
            cycle_relation.append([edge_data["id"], edge_data["relation"]])
        cycle_list.append(cycle)
        cycle_relation_list.append(cycle_relation)

    return cycle_list, cycle_relation_list

def _loop_del_integration(kg_unified: dict) -> dict:
    """
    Remove loops of one event in the knowledge graphs

    Parameters
    ----------
    kg_unified : dict
        knowledge graph

    Returns
    -------
    dict
        knowledge graph that loops of one event are removed.
    """
    
    # delete loop of event-A <=> event-A (should not happen)
    cycle_list_local, cycle_relation_list_local = \
        _loop_check(kg_unified,
                    ["causes", "indicates"]
                    )

    for cycle_i, cycle_local in enumerate(cycle_list_local):
        # loop of event-A <=> event-A?
        delete_edges_list = []
        if len(cycle_local) == 1:
            print("WARNING: Loop between one event")
            for relation_local in cycle_relation_list_local[cycle_i]:
                delete_edges_list.append(relation_local[0])
        # delete edges in the loop of one event
        for delete_edges_i in delete_edges_list:
            del kg_unified["edges"][eval(delete_edges_i) - 1]
            for kg_edge_i, kg_edge_local in enumerate(kg_unified["edges"]):
                if eval(kg_edge_local["id"]) > eval(delete_edges_i):
                    kg_unified["edges"][kg_edge_i]["id"] = \
                        str(eval(kg_edge_local["id"]) - 1)
            for kg_cond_i, kg_cond_local in \
                    enumerate(kg_unified["conditions"]):
                for kg_cond_edge_i, kg_cond_edge_local in \
                        enumerate(kg_cond_local["edges"]):
                    if kg_cond_edge_local == delete_edges_i:
                        del_id = kg_cond_edge_i
                    else:
                        if eval(kg_cond_edge_local) > eval(delete_edges_i):
                            kg_unified["conditions"][kg_cond_i][
                                "edges"][kg_cond_edge_i] = \
                                str(eval(kg_cond_edge_local) - 1)
                del kg_unified["conditions"][kg_cond_i]["edges"][del_id]
                
    return kg_unified


class UtilKG:
    """UtilKG class
    This class handles knowledge graphs. 
    It extracts instances from text chunks and converts the extracted instances 
    into a knowledge graph. The knowledge graphs are then integrated 
    into a single knowledge graph.
    """
    def __init__(self,
                 embeddings,
                 db_dir_path,
                 filename_progress=None,
                 filename_dump=None,
                 llm=None,
                 n_max_workers=St.N_MAX_WORKERS,
                 address_neo4j=None):
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
        stop_db_file : str
            filename of stop file
        address_neo4j : str
            address of neo4j
        Returns
        -------
        None
        """
        self.db_dir_path = db_dir_path
        self.db_dir_path_kg = os.path.join(db_dir_path, 'db_kg')
        self.filename_dump = filename_dump
        self.filename_progress = filename_progress
        self.kgs = []
        self.logs = []

        self.llm = llm
        if self.llm is not None:
            self.llm.set_logger(db_dir_path, filename_dump)

        self.n_max_workers = n_max_workers
        self.embeddings = embeddings
   

    def preprocess(self, incidents):
        """
        This function performs preprocessing before creating a knowledge graph. 
        It primarily extracts incidents from text chunks.

        Parameters
        ----------
        incidents : list
            list of incidents

        Returns
        -------
        int
            error status (0: normal, 100-: error)
        int
            detected language (0: others, 1: Japanese, 2: English)
        """
        
        import subprocess

        # .exeファイルのパス
        exe_path = r'LLM/prompts.exe'
        # MODE
        MODE = 1
        # 出力のための処理
        doc_list=[]
        
        
        all_count = len(incidents)
        count = 0
        print("2. Preprocessing documents...")
        print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")

        for incident in incidents:
            
            with open('LLM/input_prompt.bin', 'wb') as p:
                pickle.dump(incident['incident'], p)
            # with open('LLM/input_prompt.txt', 'w') as f:
            #     print(incident['incident'], file=f)
        
            result = subprocess.run([exe_path, str(MODE)], 
                                    cwd=os.path.join(parent_dir, 'LLM'),
                                    capture_output=True,
                                    text=True)
    
            if "Successfully done!" in result.stdout:
                with open('LLM/output_prompt.bin', 'rb') as p:
                    output_prompt = pickle.load(p)
                response = output_prompt["response"]
                input_token = output_prompt["input_token"]
                output_token = output_prompt["output_token"]
                # with open('LLM/output_prompt.txt', 'r') as f:
                #     response = f.read()
            else:
                raise ValueError(result.stderr)
            
            doc_list.append({
                'uid':incident['uid'],
                'doc':response,
                'language':incident['language'],
                'input_token_pre':input_token,
                'output_token_pre':output_token
                })
            
            count += 1
            print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
                
        self.incidents = incidents
        self.doc_methods_mod = doc_list
        status = St.SUCCESS
        return status, incident['language']
    
    def make_kg(self, doc_id, doc_type_name, doc, domain, language):
        """
        This function makes KG from an incident.

        Parameters
        ----------
        doc_id : int
            id of document
        doc_type_name : str
            type of document
        doc : str
            document
        domain : str
            domain of document
        language : int
            language (0: others, 1: Japanese, 2: English)

        Returns
        -------
        int
            error status (0: normal, 100-: error)
      
        """
        # make KG
        # paramter
        status = St.ERR_DB_MAIN_UNEXPECTED

        try:
            status, kg, log = self._make_kg(
                doc_id, 
                doc_type_name, 
                doc, 
                domain, 
                language)
            if not Cf.any_kg(kg):
                self.log.dump(
                    "[WARNING]", "[main]", 'no kg: ' + str(doc_id))
            else:
                self.kgs.append(kg)
                self.logs.append(log)
            
        except Exception as e:
            print(e)
            self.log.dump("[ERROR]", "[main]", '_make_kg:{}'.format(str(e)))
            status = St.ERR_DB_MAIN_UNEXPECTED
            return status

        return status

    def load_kg(self):
        """
        This function loads the already registered knowledge graph 
        and merge it with the current knowledge graph.

        Parameters
        ----------
        None

        Returns
        -------
        int
            error status (0: normal, 100-: error)
      
        """

        status = St.SUCCESS

        # add old kgs
        #_, userid = os.path.split(self.db_dir_path.rstrip('/'))
        #print('userid:{}'.format(userid))
        try:
            kgs_old = self.load_dir()
            if Cf.any_kg(kgs_old):               
                self.kgs.append(kgs_old)
        except:
            self.log.dump("[ERROR]", "[main]", 'load_kg')
            status = St.ERR_DB_MAIN_UNEXPECTED
            return status
   

        return status
    
    def add_vec_kgs(self):
        """
        The function adds sentence vectors to each node 
        in the knowledge graph.

        Parameters
        ----------
        None

        Returns
        -------
        list
            list of error status (0: normal, 100-: error)
      
        """
        
        status_list = []
        for kg_i, kg in enumerate(self.kgs):
            status, self.kgs[kg_i] = self._add_vec_kg(kg)
            status_list.append(status)
        return status_list
    
    def _add_vec_kg(self, kg_before):
        """
        The function adds sentence vectors to each node 
        in the knowledge graph.

        Parameters
        ----------
        kg_before : dict
            knowledge graph

        Returns
        -------
        int
            error status (0: normal, 100-: error)
        dict
            word vector
      
        """
        
        try:
            kg_w_vec = copy.deepcopy(kg_before)
            VECTOR_KEY = 'vec'
 
            # Search the nodes which don't include VECTOR_KEY
            idx_list = []
            ent_list = []
            for node_i, node in enumerate(kg_w_vec["nodes"]):
                if VECTOR_KEY not in node:
                    idx_list.append(node_i)
                    ent_list.append(node["label"])

            # Embedding    
            ent_vec_list = self.embeddings.embed_documents(ent_list)
            
            # Add the key 
            for idx_i, node_i in enumerate(idx_list):
                kg_w_vec["nodes"][node_i][VECTOR_KEY] = ent_vec_list[idx_i]

            status = St.SUCCESS
        except Exception as e:
            self.log.dump("[ERROR]", "[add_vec]", 'add_vec:{}'.format(e))
            status = St.ERR_DB_MAIN_UNEXPECTED
            kg_w_vec = {}

        return status, kg_w_vec

    def save_kg(self):
        """
        The function saves the knowledge graph.

        Parameters
        ----------
        None

        Returns
        -------
        int
            error status (0: normal, 100-: error)
      
        """
        status = St.SUCCESS
        
        try:
            self.kg_integrated = _loop_del_integration(self.kg_integrated)
        except Exception as e:
            print(str(e))
            # self.log.dump("[WARNING]", "[main]", 'save_kg:{}'.format(e))

        # save kg
        try:
            self.save_dir(kgs=self.kg_integrated)
        except Exception as e:
            # self.log.dump("[ERROR]", "[main]", 'save_kg:{}'.format(e))
            print(str(e))
            status = St.ERR_DB_MAIN_UNEXPECTED
            return status
        return status


    def _make_kg(
        self,
        doc_id: str, 
        doc_type: str, 
        doc: str, 
        domain: str, 
        language: int):
        """
        This function make kg.

        Parameters
        ----------
        doc_id :str
            document id
        doc_type :str
            document type
        domain :str
            domain of document
        language :int
            flag of language

        Returns
        -------
        dict
            kg
        """

        import subprocess

        # .exeファイルのパス
        exe_path = r'LLM/prompts.exe'
        # MODE
        MODE = 2
        # 出力のための処理
        log_list=[]

        with open('LLM/input_prompt.bin', 'wb') as p:
            pickle.dump(doc, p)
        # with open('LLM/input_prompt.txt', 'w') as f:
        #     print(doc, file=f)
            
        for _i in range(NUM_TRY):
            
            result = subprocess.run([exe_path, str(MODE), str(doc_id), str(doc_type), str(domain), str(language)], 
                                    cwd=os.path.join(parent_dir, 'LLM'),
                                    capture_output=True,
                                    text=True)
    
            if "Successfully done!" in result.stdout:
                with open('LLM/output_prompt.bin', 'rb') as p:
                    log_each = pickle.load(p)
            else:
                raise ValueError(result.stderr)
            
            log_list.append(log_each)
        
        best_score = -100000.0
        best_kg = {}
        best_ana = ""
        best_score_dict = {
            "llm_sim_score": 0,
            "cosine_sim_score": 0}
        
        for each_log in log_list:
            cosine_sim_score_local = each_log["score_cos"]
            llm_sim_score_local = each_log["score_llm"]

            current_score = llm_sim_score_local * 10000 + cosine_sim_score_local
            if current_score > best_score:
                best_score = current_score
                best_score_dict = {"llm_sim_score": llm_sim_score_local,
                                "cosine_sim_score": cosine_sim_score_local}
                best_kg = each_log["kg"].copy()
                best_ana = each_log["analysis"]
                best_chat_log   = each_log["chat_log"]

        best_score_dict["best_kg"] = best_kg
        best_score_dict["best_ana"] = best_ana
        best_score_dict["best_chat_log"] = best_chat_log
        log_list.append(best_score_dict)

        return St.SUCCESS, best_kg, log_list
      
    def load_userid(self, userid='userid', filename=St.FILENAME_KG_BIN):
        """
        This function loads kg.

        Parameters
        ----------
        file_path : str
            file path(not used)
        filename : str
            filename (not used)

        Returns
        -------
        dict
            {'nodes':{}, 'edges':{}, 'conditions':{}}
        """
        # Load
        try:
            filename_kg = os.path.join(self.db_dir_path_kg, filename)
            if not os.path.isfile(filename_kg):
                return {}

            with open(filename_kg, 'rb') as p:
                kgs = pickle.load(p)

        except Exception as e:
            # self.log.dump("[WARNING]", "[load_kg]", str(e))
            print(str(e))
            kgs = {}       

        return kgs        

    def load_dir(self, filename=St.FILENAME_KG_BIN):
        """
        This function loads kg.

        Parameters
        ----------
        filename : str
            filename (not used)

        Returns
        -------
        dict
            {'nodes':{}, 'edges':{}, 'conditions':{}}
        """
        # Load
        _, userid = os.path.split(self.db_dir_path.rstrip('/'))
        return self.load_userid(userid=userid, filename=filename)
    
    def delete_userid(self, userid='userid', filename=St.FILENAME_KG_BIN):
        """
        This function delete kg.

        Parameters
        ----------
        file_path : str
            file path(not used)
        filename : str
            filename (not used)

        """
        #delete
        
        file = os.path.join(self.db_dir_path_kg, filename)
        if os.path.isfile(file):    
            os.remove(file)
        else:
            # print(f'{self.db_dir_path_kg} does not exist')
            pass
        
    def save_userid(self, userid='userid',
                    filename=St.FILENAME_KG_BIN, kgs=None):
        """
        This function saves kg.

        Parameters
        ----------
        file_path : str
            file path(not used)
        filename : str
            filename (not used)
        kgs : None
            kgs
        Returns
        -------
        None
        """
        # Save
        if not Cf.any_kg(kgs):
            kgs = {}
        self.delete_userid(userid=userid)
        with open(os.path.join(self.db_dir_path_kg, filename), 'wb') as p:
            pickle.dump(kgs, p)
            
    def save_dir(self, filename=St.FILENAME_KG_BIN, kgs=None):
        """
        This function saves kg.

        Parameters
        ----------
        filename : str
            filename (not used)
        kgs : None
            kgs
        Returns
        -------
        None
        """
        # Save
        _, userid = os.path.split(self.db_dir_path.rstrip('/'))    
        self.save_userid(userid=userid, filename=filename, kgs=kgs)
