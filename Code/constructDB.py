# -*- coding: utf-8 -*-

print("Initializing...")

# Import modules from local directory
from utilDB.UtilDB import UtilDB, UtilDB_KG
from utilKG.UtilKG import UtilKG

# Import modules
import os, sys, pickle
from langchain.embeddings import HuggingFaceEmbeddings

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

# Fixed parameters
INPUT_DOC       = "input_doc"   # Directory of input document
DB_DIR_PATH     = "db"  # Directory of database
INPUT_QUERY     = "input_query"     # Directory of input query
MODE_KG         = 0     # 0 (Low Cost) or 1 (Normal)
PERSONA         = "RU and DU interoperability test"     # LLM persona
EMBEDDED_MODEL_NAME = "intfloat/multilingual-e5-large"
EMBEDDINGS = HuggingFaceEmbeddings(model_name=EMBEDDED_MODEL_NAME)

# Register doc
doc_list_doc = []
doc_list_kg = []
input_doc = os.listdir(INPUT_DOC)[0]
input_path = os.path.join(INPUT_DOC, input_doc)
doc_list_doc.append({"doc_file_path": input_path,
                     "doc_file_name": input_doc,
                     "divide_set": 1
                     }
                    )
doc_list_kg.append({"doc_file_path": input_path,
                    "doc_file_name": input_doc,
                    "doc_type": 0
                    }
                   )

# Register query list
query_list = []
for input_query in os.listdir(INPUT_QUERY):
    input_path = os.path.join(INPUT_QUERY, input_query)
    with open(input_path, "r", encoding='utf-8') as f:
        query = f.read()
        if ("# RAG answer" in query) and ("# KG answer" in query):
            pass
        else:
            query_list.append({"doc_file_path": input_path,
                               "query": query
                               })

def _make_kg_tsg(udb_kg, ukg, doc_list, mode_kg):
    """
    A function that creates a knowledge graph from a TSG document.

    Parameters
    ----------
    udb_kg : UtilDB_KG
        DB utility class for KG
    ukg : UtilKG
        KG utility class
    doc_list : list
        list of documents (type0)
    mode_kg : int
        KG creation mode.
        0 (fast but course), 1 (slow but fine)       

    Returns
    -------
    UtilKG
        KG utility class
    int
        error status (0-: normal, 100-: error)
    Progress
        progress class
    """

    #------------------------------- make KG --------------------------------#
    ukg,language, incidents, status, input_token_sum, output_token_sum = \
        _make_kg_tsg_each(udb_kg, ukg, doc_list, mode_kg)

    # add vectors
    _status_list = ukg.add_vec_kgs()

    #load old KGs            
    status = ukg.load_kg()
    #----------------------------- integrate KG -----------------------------#
    
    import subprocess

    # path of .exe file
    exe_path = r'LLM/prompts.exe'
    # MODE
    MODE = 3
    
    all_count = len(ukg.kgs) - 1
    count = 0
    print("\n4. Unifying all KGs...")
    print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
    
    log_list_list = []
    #integrate KGs
    if not len(ukg.kgs) == 0:
        kg_unified = ukg.kgs[0]
        for idx, kg in enumerate(ukg.kgs[1:]):
            input_prompt = {"kg_i": kg_unified, "kg_j": kg, "docs_dict": incidents}
            with open('LLM/input_prompt.bin', 'wb') as p:
                pickle.dump(input_prompt, p)
                
            result = subprocess.run([exe_path, str(MODE), str(language)], 
                                    cwd=os.path.join(current_dir, 'LLM'),
                                    capture_output=True,
                                    text=True)
    
            if "Successfully done!" in result.stdout:
                with open('LLM/output_prompt.bin', 'rb') as p:
                    output_prompt = pickle.load(p)
                
                kg_unified = output_prompt["kg_unified"]
                log_list = output_prompt["log_list"]

                log_list_list.append(log_list.copy())
                
                input_token_sum += output_prompt["input_token"]
                output_token_sum += output_prompt["output_token"]
            
            else:
                raise ValueError(result.stderr)
            
            count += 1
            print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
    
    ukg.kg_integrated = kg_unified
    
    # save kg
    status = ukg.save_kg()
 
    return ukg, status, input_token_sum, output_token_sum

def _make_kg_tsg_each(udb_kg, ukg, doc_list, mode_kg):
    """
    

    Parameters
    ----------
    udb_kg : UtilDB_KG
        DB utility class for KG
    ukg : UtilKG
        KG utility class
    doc_list_type0 : list
        list of documents (type0)
    mode_kg : int
        KG creation mode.
        0 (fast but course), 1 (slow but fine)    
    progress : Progress
        progress class       

    Returns
    -------
    UtilKG
        KG utility class
    int
        error status (0-: normal, 100-: error)
    Progress
        progress class
    """

    #------------------------------- make KG --------------------------------#
    # get db data
    _, field, _, _, content_list =\
            udb_kg.check_db()

    ## extract incidents
    incidents = []
    for doc_i_type0, doc in enumerate(doc_list):
        for content in content_list:
            if content['source'] == doc['doc_file_name']:
                for d in content['doc_list']:
                    incidents.append({
                        'uid':d['ID'], 
                        'incident':d['doc'], 
                        'language':content['language'],
                        'is_ext':True
                    })
    
    # preprocessing incidents
    status, language = ukg.preprocess(incidents)

    # entty data for constructing spec kg
    input_token_sum = 0
    output_token_sum = 0
    doc_id_list, doc_type_name_list, doc_list, \
        domain_list, language_list =\
        [], [], [], [], []
    for idx, doc_mm in enumerate(ukg.doc_methods_mod):
        if doc_mm is None:
            continue
        
        doc_id_list.append(doc_mm['uid'])
        doc_type_name_list.append("TSG")
        doc_list.append(doc_mm['doc'])
        domain_list.append(field)
        language_list.append(language)
        
        input_token_sum += doc_mm['input_token_pre']
        output_token_sum += doc_mm['output_token_pre']
    
    all_count = len(doc_list)
    count = 0
    print("\n3. Constructing causal KG of each document...")
    print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
    
    ## make kg
    for doc_id, doc_type_name, doc, domain, language in\
        zip(doc_id_list,
            doc_type_name_list,
            doc_list,
            domain_list,
            language_list):
        #make KG
        status = ukg.make_kg(
            doc_id,
            doc_type_name,
            doc,
            domain,
            language
            )
        
        count += 1
        print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
    
    for log_list in ukg.logs:
        for log_each in log_list:
            if "input_token" in log_each:
                input_token_sum += log_each["input_token"]
                output_token_sum += log_each["output_token"]

    return ukg, language, incidents, status, input_token_sum, output_token_sum


# Main start        
if __name__ == '__main__':
    
    # Construct DB based on doc_list
    if True:
        if len(doc_list_doc) > 0:
            # Documents exist
            
            print("1. Constructing vector database...")
            
            # DB for RAG
            udb = UtilDB(
                embeddings=EMBEDDINGS,
                db_dir_path=DB_DIR_PATH
                )
            udb.initialize(PERSONA)
            
            for idx, doc_dict in enumerate(doc_list_doc):
                doc_file_path = doc_dict["doc_file_path"]
                doc_file_name = doc_dict["doc_file_name"]
                divide_set = doc_dict["divide_set"]

                # add DB
                _, _ =\
                    udb.add(
                        doc_file_path=doc_file_path,
                        doc_file_name=doc_file_name,
                        doc_type=0,
                        divide_set=divide_set,
                        translate_language=0
                        )

            # DB for KG
            udb_kg = UtilDB_KG(
                embeddings=EMBEDDINGS,
                db_dir_path=DB_DIR_PATH,
                filename_progress="progress_db.csv",
                filename_dump='_dump_db_default.csv',
                )
            
            for idx, doc_dict in enumerate(doc_list_kg):
                doc_file_path = doc_dict["doc_file_path"]
                doc_file_name = doc_dict["doc_file_name"]
                doc_type = doc_dict["doc_type"]

                # add DB
                _, _ =\
                    udb_kg.add(
                        doc_file_path=doc_file_path,
                        doc_file_name=doc_file_name,
                        doc_type=doc_type,
                        divide_set=0,
                        translate_language=0
                        )
            
            
            # KG class setup
            ukg = UtilKG(
                embeddings=EMBEDDINGS,
                db_dir_path=DB_DIR_PATH,
                filename_progress="progress_db.csv",
                filename_dump='_dump_db_default.csv'
                )
            
            # KG construction
            ukg, _, input_token, output_token = _make_kg_tsg(
                    udb_kg, ukg, 
                    doc_list_kg,
                    MODE_KG)
            
            token_info = {"input_token": input_token, "output_token": output_token}
            with open(DB_DIR_PATH + '/db_kg/token_info.bin', 'wb') as p:
                pickle.dump(token_info, p)
            
            # Finish
            print("\nDB constructed")

        else:
            # No documents
            print("Put documents(csv) in " + INPUT_DOC)
