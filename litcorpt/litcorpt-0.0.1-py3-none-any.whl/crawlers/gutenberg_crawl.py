#!/usr/bin/env python3
"""This program dumps books in portuguese from Project Gutenberg"""

#%%
import os
from pathlib import Path

import litcorpt.settings as settings
import litcorpt.crawlers.gutenberg as gutenberg
import litcorpt.utils as utils


#%%
def pick_problems(data):
    """Return a sub dictionary containing only entries that triggered an issue (for testing)"""
    problems = [ '13092', '11299', '14503', '16429', '24824', '25987', '28122',
                 '2837',  '31190', '32174', '33067', '33068', '33588', '34755',
                 '35130', '35131', '35982', '46860', '63664', '65021', '28341', ]
    samples = { key: meta for key, meta in data.items() if key in problems }

    return samples

#%%
def download_all_books(testmode=False):
    """This functions mirrors portuguese books from Gutenberg website"""

    settings.init()
    settings.GUTENBERG_DATAPATH = os.environ.get('GUTENBERG_DATAPATH', '~/data/gutenberg')
    settings.GUTENBERG_DATAPATH = os.path.expanduser(settings.GUTENBERG_DATAPATH)

    Path(settings.GUTENBERG_DATAPATH).mkdir(parents=True, exist_ok=True)
    books = gutenberg.retrieve_booklist(verbose=True)
    if testmode:
        # Problem samples
        books = pick_problems(books)
        # Random samples
        books = utils.dict_random_samples(books, 5)
    books = gutenberg.retrieve_metadata(books, verbose=True)
    books = gutenberg.retrieve_books(books, verbose=True)
    books_sz = gutenberg.dump_data(books, replace=True, verbose=True)
    return books_sz

#%%
if __name__ == '__main__':
    pass
