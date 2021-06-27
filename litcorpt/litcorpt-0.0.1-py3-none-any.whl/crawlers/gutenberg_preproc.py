#!/usr/bin/env python
"""This program preprocess data stored in gutenberg crawled directory"""

import os
import copy

import litcorpt.settings as settings
import litcorpt.crawlers.gutenberg as gutenberg

#%%
def stopline(line):
    """Verify is a line contains a invalid string"""
    badstrings = [ "gallica.bnf.fr", "luizgusmao@bol.com.br", "prepared by",
                   "produced by", "project by", "proofreading", "this etext is",
                   "was produced", "www.pgdp.net", "available by", "produced from",
                   "google print", "google book", "nacional de lisboa.", "de lisboa.",
                   "provided by", "bnd.bn.pt", "the online distributed",
                   "library of portugal", "edited by", "nacional de portugal",
                   "the original version", "project gutenberg", "a partir da digitaliza",
                   "this file was", "scanned images of", "print project",
                   "diponibilizadas pela biblioteca digital", "distributed proofreaders",
                   "this book was", "blogspot.com", "imagens de obras em dom",
                   "biblioteca digital", "book search", "by cornell university", "search)",
                   "digital collections", "internet archive", "disponibilizada pela bibria",
                   "purl.pt", "created from images", "library.utoronto.ca",
                   "file which includes", "www.gutenberg.org", "-h.htm", "of public domain",
                   "thanks to", "dicionario-aberto.net", "de material em dom",
                   "da universidade do minho", "portugal).)", "project.)", "heritage library",
                   "coimbra university", "almamater.uc.pt", "digital do alentejo",
                   "free literature", "free sources for", "made available", "bodleian library",
                   "educational materials", "online soon", "bibliotheca nacional digital",
                   "acervo digital", "images from",
                 ]
    for bad in badstrings:
        if bad in line.lower():
            return True

    return False

#%%
def content_remove_header(content):
    """Clean up Project Gutenberg ebook headers (and footers)"""
    in_recording_mode = False
    inside_header = False
    lines = []
    scontent = content.split('\n')

    for line in scontent:
        if not in_recording_mode:
            if (line.startswith('*** START OF') or
                line.startswith('***START OF') or
                line.startswith('*END THE SMALL')):
                inside_header = True
            if inside_header and len(line.strip()) == 0:
                inside_header, in_recording_mode = False, True
        elif (line.startswith('*** END OF') or
              line.startswith('***END OF') or
              line.startswith('End of the Project') or
              line.startswith('End of Project') or
              line.startswith('THE FULL PROJECT')):
            in_recording_mode = False
        else:
            if not stopline(line):
                lines.append(line)

    # Remove leftout headers
    content_pp = '\n'.join(lines)
    return content_pp



def preprocess():
    """Execute Preprocessing

    TODO (Igor): Should I pass src_datapath and dst_datapath instead hardcode the datapaths?
                 Probably yes. But not now.
    """

    settings.init()
    settings.GUTENBERG_DATAPATH = os.environ.get('GUTENBERG_DATAPATH',
                                                 '~/data/litcorpt_crawl/gutenberg.org/')
    settings.GUTENBERG_DATAPATH = os.path.expanduser(settings.GUTENBERG_DATAPATH)

    #%% Load books
    print(f"Reading data from {settings.GUTENBERG_DATAPATH}")
    books = gutenberg.load()

    #%% Make in memory copy (not needed, just for now)
    ppbooks = copy.deepcopy(books)

    #%% Filter headers
    print("Preprocessing books in memory...")
    for bookid, _ in books.items():
        print(f"{bookid}\t", end="", flush=True)
        ppcontent = content_remove_header(books[bookid]['contents'][0])
        ppbooks[bookid]['contents'][0] = ppcontent
        # Add gutenberg key as a element of meta data
        ppbooks[bookid]['sourcekey'] = bookid
        # Add gutenberg as reference in datasource
        ppbooks[bookid]['datasource'] = "gutenberg"
    print()

    #%% Write to data dir
    # Need to change datapath to write in other location
    # TODO(Igor): This is TOOOOOO hardcoded. BAD BAD.
    settings.GUTENBERG_DATAPATH = os.path.expanduser('~/data/litcorpt_data/gutenberg_org/')
    books_sz = gutenberg.dump_data(ppbooks, replace=True, verbose=True)

    return books_sz

if __name__ == '__main__':
    pass
