# -*- coding: utf-8 -*-

print("Initializing...")

# import from local directory
from utilDB.UtilDB import UtilDB, UtilDB_KG
from utilKG.UtilKG import UtilKG
from rca import RCAdoc
from rca import RCAkg

import os, sys, pickle
import time
from datetime import datetime
import re
from langchain.embeddings import HuggingFaceEmbeddings

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

# fixed parameters
DB_DIR_PATH     = "db"
INPUT_QUERY     = "input_query"
OUTPUT_QUERY     = "output_query"
MODE_KG         = 0     # 0 (Low Cost) or 1 (Normal)
PERSONA         = "RU and DU interoperability test"
RAG_DEL = "# RAG answer"
KG_DEL = "# KG answer"
REF_DEL = "# References"
CONF_THRE = 75
SEARCH_INPUT = "input_token: [\d]+,"
SEARCH_OUTPUT = "output_token: [\d]+,"
EMBEDDED_MODEL_NAME = "intfloat/multilingual-e5-large"
EMBEDDINGS = HuggingFaceEmbeddings(model_name=EMBEDDED_MODEL_NAME)

# query list
try:
    input_query_list = os.listdir(INPUT_QUERY)
except Exception as e:
    print(str(e))
    input_query_list = []
query_list = []
for input_query in input_query_list:
    input_path = os.path.join(INPUT_QUERY, input_query)
    output_path = os.path.join(OUTPUT_QUERY, input_query)
    with open(input_path, "r", encoding='utf-8') as f:
        query = f.read()
        if (RAG_DEL in query) and (KG_DEL in query):
            pass
        else:
            query_list.append({"doc_file_path": input_path,
                               "res_file_path": output_path,
                               "query": query
                               })
if len(query_list) == 0:
    raise ValueError("No queries found")

def write_nl(add_txt, org_txt):
    return org_txt + add_txt + "\n"

def _check_db_doc(db_dir_path: str):
    """
    get and check database

    Parameters
    ----------
    db_dir_path : str
        file path of database

    Returns
    -------
    list[int]
        error status (0-: normal, 200-: error)
    str
        field of the incident
    list
        category list of the incident
    dict
        Doc database content (key: dict_key, value: langchain.schema.Document)
    dict
        KG database content (key: dict_key, value: langchain.schema.Document)
    list
        Doc database content (list)
    list
        KG database content (list)
    dict
        unified KG
    str
        for visualization. tentative!
    """
    
    udb = UtilDB(
        embeddings=EMBEDDINGS,
        db_dir_path=db_dir_path
        )

    try:
        status_doc, field, cat_list, content_dict_doc, content_list_doc =\
            udb.check_db()
    except Exception as e:
        raise ValueError("DB load error: " + str(e))

    return status_doc, field, cat_list, content_dict_doc, content_list_doc, udb


def _check_db_kg(db_dir_path: str):
    """
    get and check database

    Parameters
    ----------
    db_dir_path : str
        file path of database

    Returns
    -------
    list[int]
        error status (0-: normal, 200-: error)
    str
        field of the incident
    list
        category list of the incident
    dict
        Doc database content (key: dict_key, value: langchain.schema.Document)
    dict
        KG database content (key: dict_key, value: langchain.schema.Document)
    list
        Doc database content (list)
    list
        KG database content (list)
    dict
        unified KG
    str
        for visualization. tentative!
    """
    
    udb_kg = UtilDB_KG(
        embeddings=EMBEDDINGS,
        db_dir_path=db_dir_path
        )

    try:
        status_kg, field, cat_list, content_dict_kg, content_list_kg, \
            = udb_kg.check_db()
    except Exception as e:
        raise ValueError("DB load error: " + str(e))

    # kg
    ukg = UtilKG(
        embeddings=EMBEDDINGS,
        db_dir_path=db_dir_path
        )
    kg_all = ukg.load_dir()
    tentative_IF = "tentative_IF"

    return status_kg, field, cat_list, content_dict_kg, content_list_kg, \
            kg_all, tentative_IF, udb_kg
            
def _query_num_words_check(query, max_words):
    # Remove punctuation, lowercase
    query_count = re.sub(r'[^\w\s]', '', query).lower()
    words = query_count.split()
    if len(words) > int(round(max_words/2)):
        return False
    return True


def _main_doc(
              db_dir_path, udb,
              query,
              option_update_query
              ):
    """This function creates a prompt
    :param progress_chat_file : progress report file
    :type progress_chat_file : str
    :param stop_chat_file : file path of stop file to force the process to stop
    :type stop_chat_file : str
    :param db_dir_path : file path of database
    :type db_dir_path : str
    :param query : query
    :type query : str
    :param option_doc : Whether or not to execute detecting
        related previous incidents.
    :type option_doc : bool
    :param option_kg : Whether or not to execute detecting
        root causes using kg.
    :type option_kg : bool
    :param option_update_query : Whether or not to execute updating query.
    :type option_update_query : bool
    :param progress : progress
    :type prog_percent : class (instance)
    :param prog_percent_list_doc : list of progress percentage
    :type prog_percent_list_doc : list[int]
    :return Success/failure
    :rtype int
    :return list of response
    :rtype list
    :return language of query(0:English, 1:Else)
    :rtype int
    :return Whether the language of the database and the query are compatible.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting previous incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting new incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :raises None
    """

    # Result parameter
    status = -100
    response_list = []
    check_language = 1
    check_incident = 1
    language = 0

    rcad = RCAdoc(db_dir_path=db_dir_path)
    status = rcad.load_udb(udb=udb, db_file_path=db_dir_path)


    status, response_list, input_token, output_token = rcad.analysis(query)
    language = rcad.language_query

    status, response_list = rcad.create_summary(response_list, language)

    return status, response_list, language, \
        check_language, check_incident, input_token, output_token


def _main_kg(
             db_dir_path, udb_kg, kg,
             query,
             option_update_query
             ):
    """This function creates a prompt
    :param progress_chat_file : progress report file
    :type progress_chat_file : str
    :param stop_chat_file : file path of stop file to force the process to stop
    :type stop_chat_file : str
    :param db_dir_path : file path of database
    :type db_dir_path : str
    :param query : query
    :type query : str
    :param option_doc : Whether or not to execute detecting
        related previous incidents.
    :type option_doc : bool
    :param option_kg : Whether or not to execute detecting
        root causes using kg.
    :type option_kg : bool
    :param option_update_query : Whether or not to execute updating query.
    :type option_update_query : bool
    :param progress : progress
    :type prog_percent : class (instance)
    :param prog_percent_list_kg : list of progress percentage
    :type prog_percent_list_kg : list[int]
    :return Success/failure
    :rtype int
    :return list of response
    :rtype list
    :return language of query(0:English, 1:Else)
    :rtype int
    :return Whether the language of the database and the query are compatible.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting previous incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting new incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :raises None
    """

    # Result parameter
    status = -100
    response_list = []
    input_token = 0
    output_token = 0
    check_language = 1
    check_incident = 1
    language = 0

    try:
        # new incident module
        rcak = RCAkg()

        status, response_list, input_token, output_token = \
            rcak.main(
                kg=kg,
                query=query,
            )
    except Exception as e:
        # log.dump("[ERROR]", "[main](3)", e)
        pass
    
    # Add ref_doc_file value (reference files)
    # udb = UtilDB_KG(
    #     embeddings=EMBEDDINGS,
    #     db_dir_path=db_dir_path,
    #     filename_progress=progress_chat_file,
    #     filename_dump=FILENAME_DUMP,
    #     llm=ua, n_max_workers=St.N_MAX_WORKERS,
    #     stop_db_file=stop_chat_file)
    _, _, _, _, content_list = udb_kg.check_db()
    for i, response in enumerate(response_list):
        if "ref_ID" in response:
            try:
                ref_doc_file = []
                for k,v in (eval(response["ref_ID"])).items():
                    for each_id in v:
                        source = _find_source(each_id, content_list)
                        if source is not None:
                            ref_doc_file.append(source)
            except Exception as e:
                print(e)
                ref_doc_file = []
            response_list[i]["ref_doc_file"] = str(ref_doc_file)
                        
    return status, response_list, language, \
        check_language, check_incident, input_token, output_token
        
def _find_source(id_doc, content_list):
    find_flg = False
    try:
        for doc_file in content_list:
            current_source = doc_file["source"]
            for chunk in doc_file["doc_list"]:
                if id_doc == chunk["ID"]:
                    source = current_source
                    find_flg = True
                    break
            if find_flg:
                break
        if find_flg:
            return source
        else:
            print("source not found")
            return None
    except Exception as e:
        print(e)
        return None

def rca_res(
         db_dir_path,
         query,
         udb,
         kg,
         option_doc,
         option_kg,
         option_update_query,
         max_words=400
         ):
    """This function creates a prompt
    :param progress_chat_file : progress report file
    :type progress_chat_file : str
    :param stop_chat_file : file path of stop file to force the process to stop
    :type stop_chat_file : str
    :param db_dir_path : file path of database
    :type db_dir_path : str
    :param query : query
    :type query : str
    :param option_doc : Whether or not to execute detecting
        related previous incidents.
    :type option_doc : bool
    :param option_kg : Whether or not to execute detecting
        root causes using kg.
    :type option_kg : bool
    :param option_update_query : Whether or not to execute updating query.
    :type option_update_query : bool
    :return Success/failure
    :rtype int
    :return list of response
    :rtype list
    :return language of query(0:English, 1:Else)
    :rtype int
    :return Whether the language of the database and the query are compatible.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting previous incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :return Whether the function of detecting new incidents is used.
        (0:valid, 1:invalid)
    :rtype int
    :raises None
    """
    
    # Result parameter
    status = -100
    response_list = [[], []]
    response_list_doc = []
    response_list_kg = []
    check_language = 1
    check_doc_incident = 1
    check_kg_incident = 1
    language = 0
    input_token_sum = 0
    output_token_sum = 0

    try:
        
        if not option_doc and not option_kg:
            # Exception
            # status = St.ERR_RCA_MAIN_ARG
            raise ValueError("Invalid option")

        status = _query_num_words_check(query,max_words)

        if not status:
            raise ValueError("Query tokens too much")

        if option_doc:
            # doc response
            status, response_list_doc, language, \
                check_language, check_doc_incident, input_token, output_token = \
                _main_doc(
                    db_dir_path, udb,
                    query,
                    option_update_query
                )

            if not status == 0:
                return status, response_list, language, \
                    check_language, check_doc_incident, check_kg_incident, input_token_sum, output_token_sum
            
            input_token_sum += input_token
            output_token_sum += output_token

        if option_kg:
            # kg response
            status, response_list_kg, language, \
                check_language, check_kg_incident, input_token, output_token = \
                _main_kg(
                    db_dir_path, udb, kg,
                    query,
                    option_update_query
                )

            if not status == 0:
                return status, response_list, language, \
                    check_language, check_doc_incident, check_kg_incident, input_token_sum, output_token_sum
            
            input_token_sum += input_token
            output_token_sum += output_token

        response_list = [response_list_doc, response_list_kg]

        return status, response_list, language, \
            check_language, check_doc_incident, check_kg_incident, input_token_sum, output_token_sum

    
    except Exception as e:
        # log.dump("[ERROR]", "[main]", str(e))
        print(str(e))
        status = -100
        return status, response_list, language, \
            check_language, check_doc_incident, check_kg_incident, input_token_sum, output_token_sum
            

if __name__ == '__main__':
    
    # check DB
    status_doc, field, _, content_dict_doc, content_list_doc, udb =\
        _check_db_doc(DB_DIR_PATH)
    status_kg, field, _, content_dict_kg, content_list_kg, \
        kg_all, tentative_IF, udb_kg = _check_db_kg(DB_DIR_PATH)
            

    all_count = len(query_list) * 2
    count = 0
    
    print("Start analyzing...")
    print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
    
    for query_dict in query_list:
        ref_ID_list_doc = []
        ref_ID_list_kg = []
        
        query = query_dict["query"]
        doc_file_path = query_dict["doc_file_path"]
        res_file_path = query_dict["res_file_path"]
        
        with open(res_file_path, 'a', encoding='UTF-8') as f:
            f.write(query)
        
        time0 = time.time()
        'Create response with RAG'
        # chat_rca.main
        status3_1, response_list_doc, _, _, _, _, input_token, output_token\
            = rca_res(
                db_dir_path=DB_DIR_PATH,
                query=query,
                udb=udb,
                kg=kg_all,
                option_doc=True,
                option_kg=False,
                option_update_query=False
                )
        
        time1 = time.time()
        
        # input_token = token_extract(db_dir_path, SEARCH_INPUT, 12)
        # output_token = token_extract(db_dir_path, SEARCH_OUTPUT, 13)
        # input_token = 0
        # output_token = 0
        
        len_res = len(response_list_doc[0])
        rag_res = write_nl("\n\n" + RAG_DEL, "")
        rag_res = write_nl("## Information (RAG)", rag_res)
        rag_res = write_nl("- Datetime (RAG): " + str(datetime.now()), rag_res)  
        time_doc = time1 - time0
        rag_res = write_nl("- Processing time [s] (RAG): " + str(time_doc), rag_res)
        rag_res = write_nl("- input_token (RAG): " + str(input_token), rag_res)
        rag_res = write_nl("- output_token (RAG): " + str(output_token), rag_res)
        
        if len_res > 0:
            # summary = response_list_doc[0][len_res - 1]["Summary"]
            # rag_res = write_nl("- Summary (RAG): " + summary, rag_res)  
            # rag_res = write_nl("\n\n", rag_res)
            
            rag_res = write_nl("## Response (RAG)", rag_res)
            res_idx = 0
            for response_doc in response_list_doc[0][:-1]:
                res_idx += 1
                ref_ID = response_doc["ref_ID"]
                ref_ID_list_doc.append(ref_ID)
                content = response_doc["content"]
                
                rag_res = write_nl("### response " + str(res_idx) + " (RAG)", rag_res)
                rag_res = write_nl("- ref " + str(res_idx) + " (RAG): " + "[" + ref_ID + "](#" + ref_ID + ")", rag_res)
                rag_res = write_nl("- response " + str(res_idx) + " (RAG): " + content, rag_res)
            
        with open(res_file_path, 'a', encoding='UTF-8') as f:
            f.write(rag_res)

        count += 1
        print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
        
        time2 = time.time()
        'Create response with KG'
        # chat_rca.main
        status3_2, response_list_kg, _, _, _, _, input_token, output_token\
            = rca_res(
                db_dir_path=DB_DIR_PATH,
                query=query,
                udb=udb_kg,
                kg=kg_all,
                option_doc=False,
                option_kg=True,
                option_update_query=False
                )
        time3 = time.time()
        
        # input_token = token_extract(db_dir_path, SEARCH_INPUT, 12)
        # output_token = token_extract(db_dir_path, SEARCH_OUTPUT, 13)
        # input_token = 0
        # output_token = 0
        with open(DB_DIR_PATH + '/db_kg/token_info.bin', 'rb') as p:
            token_info = pickle.load(p)
        input_token += token_info["input_token"]
        output_token += token_info["output_token"]

        len_res = len(response_list_kg[1])
        kg_res = write_nl("\n\n" + KG_DEL, "")
        kg_res = write_nl("## Information (KG)", kg_res)
        kg_res = write_nl("- Datetime (KG): " + str(datetime.now()), kg_res)  
        time_kg = time3 - time2
        kg_res = write_nl("- Processing time [s] (KG): " + str(time_kg), kg_res)
        kg_res = write_nl("- input_token (KG): " + str(input_token), kg_res)
        kg_res = write_nl("- output_token (KG): " + str(output_token), kg_res)
        md_list = ""
        sum_txt = "### summary of root cause candidates (KG)\n"
        
        if len_res > 0:
            # summary = response_list_kg[1][len_res - 1]["Summary"]
            # kg_res = write_nl("- Summary (KG): " + summary, kg_res)  
            # kg_res = write_nl("\n\n", kg_res)
            
            kg_res = write_nl("## Response (KG)", kg_res)            
            
            res_idx = 0
            rc_list_seen = []
            for response_kg in response_list_kg[1][:-1]:
                
                content = response_kg["ref_kg"]
                rc_list = re.findall(r"\d. \*.*\*. &nbsp", content)
                rc_sentence_list = re.findall(r"\d. \*.*\*. &nbsp.*\n", content)
                seen_bool = list(range(len(rc_list)))
                for i, rc in enumerate(rc_list):
                    rc_list[i] = re.findall(r"\*.*\*. &nbsp", rc)[0][1:-8]
                    if rc_list[i] in rc_list_seen:
                        # Root cause is already seen in previous analysis
                        seen_bool[i] = True
                        content = content.replace(rc_sentence_list[i], "")
                    else:
                        seen_bool[i] = False
                        rc_list_seen.append(rc_list[i])
                        sum_txt = write_nl("- *" + rc_list[i] + "* [response " + str(res_idx+1) + "] (KG)", sum_txt)
                if seen_bool.count(True) == len(seen_bool):
                    pass
                else:
                    res_idx += 1
                
                    ref_IDs = re.findall(r"sentence\d*_\d*", content)
                    ref_IDs = list(set(ref_IDs))
                    ref_ID_list_kg += ref_IDs
                    for ref_ID in ref_IDs:
                        content = content.replace(ref_ID, "["+ref_ID+"](#"+ref_ID+")")
    
                    md_list = write_nl("### response " + str(res_idx) + " (KG): \n" + content, md_list)
            
        kg_res = write_nl(sum_txt, kg_res)
        kg_res = write_nl(md_list, kg_res)
        with open(res_file_path, 'a', encoding='UTF-8') as f:
            f.write(kg_res)

        count += 1
        print("\r" + "[{}]".format("#"*count + " "*(all_count-count)) + " :" + str(count) + "/" + str(all_count), end="")
        
        time4 = time.time()
        
        
        ref_res = write_nl("\n\n" + REF_DEL, "")
        ref_ID_list_doc = list(set(ref_ID_list_doc))
        ref_ID_list_kg = list(set(ref_ID_list_kg))
        # ref_ID_list_kg_low = list(set(ref_ID_list_kg_low))
        for ref_ID_doc in ref_ID_list_doc:
            original_content = "NO DOC"
            for each_doc in content_list_doc[0]["doc_list"]:
                if each_doc["ID"] == ref_ID_doc:
                    original_content = each_doc["original_content"]
                    break
            ref_res = write_nl("## " + ref_ID_doc, ref_res)
            ref_res = write_nl(original_content, ref_res)
        for ref_ID_kg in ref_ID_list_kg:
            original_content = "NO DOC"
            for each_doc in content_list_kg[0]["doc_list"]:
                if each_doc["ID"] == ref_ID_kg:
                    original_content = each_doc["original_content"]
                    break
            ref_res = write_nl("## " + ref_ID_kg, ref_res)
            ref_res = write_nl(original_content, ref_res)
        # for ref_ID_kg in ref_ID_list_kg_low:
        #     original_content = "NO DOC"
        #     for each_doc in content_list_kg2[0]["doc_list"]:
        #         if each_doc["ID"] == ref_ID_kg:
        #             original_content = each_doc["original_content"]
        #             break
        #     ref_res = write_nl("## " + ref_ID_kg, ref_res)
        #     ref_res = write_nl(original_content, ref_res)
        
        with open(res_file_path, 'a', encoding='UTF-8') as f:
            f.write(ref_res)
