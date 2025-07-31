# Root Cause Analysis for Wireless Networks Using Causal Knowledge Graphs and an LLM
Root cause analysis (RCA) is a critical task in incident management of wireless networks. Although it is essential for restoration and maintenance of performance, it often demands extensive and time-consuming efforts.
Existing RCA approaches, including rule-based and troubleshooting-based methods, cannot analyze causal relationships across multiple incident tickets.
However, this capability is essential for comprehensive and accurate RCA considering that incidents or performance deterioration in wireless networks are caused by a cascade of various factors, such as software/hardware/environmental issues, and interactions between multiple base stations and UEs.
To address this challenge, we propose a novel framework for automated RCA based on incident tickets, that extracts causal knowledge graphs (KGs) from documents using a large language model (LLM) and uses them for inference.
Because of our step-by-step method for constructing causal KGs optimized for RCA, it automatically constructs KGs including events causality across multiple documents.
Comparative evaluations with the conventional retrieval-augmented generation approach demonstrate that our framework achieves a significant improvement in 5-point scale evaluation scores by human experts for comprehensiveness (from 2.79 to 3.18), hallucination mitigation (from 3.09 to 3.31), and explainability (from 2.69 to 3.12).

To learn more about our framework of causal KGs and how it can be used to enhance root cause analysis, please visit the [Fujitsu Tech Blog](https://blog-en.fltech.dev/entry/2024/10/11/kgrca-en/).

![Flow](https://github.com/user-attachments/assets/b07df305-a026-4324-9f3c-db464c8398a1)

# How to use the code

0. Before start
    1. Install python (3.10.X or 3.11.X are recommended)
    2. Install required python packages (See `Code/OSS.csv`)
    3. Edit LLM settings (`Code/LLM/config.yaml`). It uses Azure OpenAI API.
    4. Install `graphviz` if you want to visualize KGs. Visit and follow [Graphviz page](https://graphviz.org/download/). After installation, type dot -V and confirm that the version of `graphviz` can be checked.
1. DB construction
    1. Put a document (e.g., a troubleshooting document) to be uploaded as knowledge graphs in `Code/input_doc` directory. Only csv file is supported on this environment.
    2. Run the code `Code/constructDB.py`, and you can see DB in `Code/db` directory.
2. KG visualization (can be skipped)
    1. Run the code `Code/visualizeKG.py`, and you can see visualized KG by opening `Code/db/db_kg/db_kg_view.pdf`.
3. Inference
    1. Put queries in `Code/input_query` directory. Only text file (.md is recommended) is supported on this environment.
    2. Run the code `Code/infer.py`, and you can see responses in `Code/output_query` directory.


# Demonstration

We put two demonstration projects.
- `Result/UI_App`: Usecase of installing and using UI application
- `Result/5G_RU`: Usecase of operation test of 5G RU including interoperability test between 5G-DU and it

![KG example](https://github.com/user-attachments/assets/094a21fd-5e3b-4f62-904d-d11fc560800f)




# Repository Overview
| Name | (Sub name) | Category | (Sub category) | Description |
| ----------- | ----------- | ----------- | ----------- | ----------- |
| `Code`        | `/constructDB.py` | Code | Main   | Construct DB for both RAG and KG |
| `Code`        | `/visualizeKG.py` | Code | Main   | Visualize KG with PDF-style |
| `Code`        | `/infer.py`       | Code | Main   | Infer the root cause based on both RAG and KG |
| `Code`        | `/LLM`            | Code | Module | Module to execute LLM-related function |
| `Code`        | `/_common.py`     | Code | Module | Module to execute common function |
| `Code`        | `/utilDB.py`      | Code | Module | Module to execute DB-related function |
| `Code`        | `/utilKG.py`      | Code | Module | Module to execute KG-related function |
| `Code`        | `/rca.py`         | Code | Module | Module to execute inference function |
| `Code`        | `/db`             | Doc  | DB     | Database of both RAG and KG |
| `Code`        | `/input_doc`      | Doc  | Document   | Input documents (incident tickets) to be uploaded to DB |
| `Code`        | `/input_query`    | Doc  | Query   | Input query|
| `Code`        | `/output_query`   | Doc  | Response   | Response from LLM based on input query and databases |
| `Code`        | `/OSS.csv`        | Doc  | OSS   | OSS list used by our repo |
| `Result`      | `/UI_App`         | Demo  || Usecase of installing and using UI application |
| `Result`      | `/5G_RU`          | Demo  || Usecase of operation test of 5G RU including interoperability test between 5G-DU and it |
| `Result`      | `/5G_RU_real(extracted)`          | Result || Extract of real internal documents, queries, analisis results, and evaluation score sheets in the usecase of 5G_RU |
| `README.md` || README  || You are here! |
| `LICENSE` || LICENSE  || LICENSE document |


# Required python packages
- python (3.10.X or 3.11.X are recommended)
- python packages listed in `Code/OSS.csv`

# Publication
- Tatsuya Kikuzuki, Akihiro Wada, Yoshihiro Okawa, and Masatoshi Ogawa, "Root Cause Analysis for Wireless Networks Using Causal Knowledge Graphs and an LLM," submitted for publication. 

# Contacts
- Tatsuya Kikuzuki: kikuzuki{at}fujitsu.com
