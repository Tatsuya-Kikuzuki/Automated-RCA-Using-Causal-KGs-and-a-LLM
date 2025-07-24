# -*- coding: utf-8 -*-
import os
import re
from langchain.text_splitter import RecursiveCharacterTextSplitter
import concurrent.futures
import sys

# NOTE:for async
import asyncio

current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(current_dir)
sys.path.append(parent_dir)

from _common import Settings, Common_func

# Class & LLM setup
St = Settings()
Cf = Common_func()


class Read_document:
    """Read_document class
    This class loads files and splits sentences for FAISS.
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

        self.TEXT_SPLITTER_CHUNK =\
            RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=chunk_size_tsg,
                chunk_overlap=50
                )
        self.TEXT_SPLITTER_SPEC =\
            RecursiveCharacterTextSplitter.from_tiktoken_encoder(
                chunk_size=chunk_size_spec,
                chunk_overlap=50
                )

        self.document = None
        self.dfs = None
        self.doc_sentences = None
        self.doc_dfs = None
        self.llm = llm
        self.db_dir_path = db_dir_path
        self.filename_dump = filename_dump
        self.n_max_workers = n_max_workers
        
        # llm process mode
        self.llm_proc_mode = "THREAD"

    def read(self):
        """
        This function reads file

        Parameters
        ----------
        None

        Returns
        -------
        None

        """
        pass

    def _detect_file_extension(self, filename: str, ext_type: str) -> bool:
        """
        _summary_

        Parameters
        ----------
        filename : str
            file
        ext_type : str
            extension

        Returns
        -------
        bool
            check extension
        """
        # get the extension of the file
        _, doc_extension_raw = os.path.splitext(filename)

        # decide the extension
        is_extension = None
        if (doc_extension_raw == ext_type):
            is_extension = True
        else:
            is_extension = False
        return is_extension

##############################################################################
# Test


if __name__ == '__main__':
    pass
