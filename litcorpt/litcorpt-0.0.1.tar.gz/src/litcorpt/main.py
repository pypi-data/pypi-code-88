#!/usr/bin/env python

"""Entry point for Literary corpus in Portuguese"""

import shutil
import os
import re
import tempfile
import datetime
from urllib.parse import urlparse
from pathlib import Path

from tinydb import TinyDB

import litcorpt.settings as settings
import litcorpt.utils
import litcorpt.crawlers.gutenberg as gutenberg


#%%
def retrieve_corpus(verbose=False):
    """This function assures that corpus is available in LITCORPUSPT_DATAPATH.
    If not it will download it.

    TODO:
        (Igor): Return False or raise, if, for some reason, isn't able to
                makes corpus available. Right now is always returning True
    """
    checkin_file = os.path.join(settings.LITCORPUSPT_DATAPATH, 'last.txt')
    if not os.path.exists(checkin_file):

        litcorpuspt_url ="https://github.com/igormorgado/litcorpt_data/archive/refs/heads/main.zip"

        if verbose :
            print(f"Corpus not found in {settings.LITCORPUSPT_DATAPATH}.")

        Path(settings.LITCORPUSPT_DATAPATH).mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory() as tmpdirname:
            # Build destination filepath
            filename = 'main.zip'
            download_filepath = os.path.join(tmpdirname, filename)

            if verbose:
                print(f"Downloading from {litcorpuspt_url}")
            # Download corpus
            filepath, _ = litcorpt.utils.download_file(litcorpuspt_url, download_filepath)

            if verbose:
                print(f"Extracting to {settings.LITCORPUSPT_DATAPATH}")
            # Extract Corpus
            shutil.unpack_archive(filepath, settings.LITCORPUSPT_DATAPATH, "zip")

        # Fill the success timestamp
        with open(checkin_file, 'w') as checkin_fd:
            now = datetime.datetime.now()
            timestamp = f'{now.year}{now.month}{now.day}{now.hour}{now.minute}{now.second}'
            checkin_fd.write(timestamp)

        if verbose:
            print(f"Completed at {str(now)}.")
    else:
        # Corpus found
        if verbose:
            print(f"Corpus found in {settings.LITCORPUSPT_DATAPATH}.")

    return True

#%%
def load_corpus(verbose=False):
    """Load corpus. Download if needed. Returns a pandas dataframe
    with corpus or None on fail.

    Outputs:
        corpus (tinyDB): Corpus as pandas dataframe or None
    """

    # Makes sure corpus if available otherwise return None
    if not retrieve_corpus(verbose=verbose):
        return None

    corpusdb_filename = 'corpus.db'
    corpusdb_filepath = os.path.join(settings.LITCORPUSPT_DATAPATH,
                                     corpusdb_filename)

    if not os.path.exists(corpusdb_filepath):
        # zip dirname is: repository-branch
        litcorpuspt_dirname = "litcorpt_data-main"

        gutenberg_dir = 'gutenberg_org'
        settings.GUTENBERG_DATAPATH = os.path.join(settings.LITCORPUSPT_DATAPATH,
                                                   litcorpuspt_dirname,
                                                   gutenberg_dir)

        # dominiopublico_dir = 'dominiopublico_gov_br'
        # settings.DOMINIOPUBLICO_DATAPATH = os.path.join(settings.LITCORPUSPT_DATAPATH,
        #                                                 litcorpuspt_dirname,
        #                                                 dominiopublico_dir)


        gutenberg_books = gutenberg.load(verbose=verbose)

        corpus = gutenberg_books

        corpusdb = TinyDB(corpusdb_filepath)

        if verbose:
            print("Building corpus dataset")
        corpusdb.insert_multiple( metadata for bookid, metadata in corpus.items())
    else:
        if verbose:
            print("Loading corpus dataset")
        corpusdb = TinyDB(corpusdb_filepath)

    return corpusdb


#%%
if __name__ == '__main__':
    pass
