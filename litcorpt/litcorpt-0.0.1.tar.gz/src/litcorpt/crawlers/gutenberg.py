#!/usr/bin/env python3
"""This provides functions to be able to download, store, load and preprocess
   ebooks from a given url related to Gutenberg Project.

   It stores the book in the path set by settings.GUTENBERG_DATAPATH environment variable
   or from ${HOME}/data/gutenberg if the variable do not exists.

   TODO(Igor):
     - Handle EDITOR if AUTHOR is missing in book table
     - Paralellize book and metadata retrieval
     - (MAYBE) Ebook content header cleanup should occur only when accessing
                book contents, not when storing it on disk.
     - (PROBABLY): Add 'bookid' as a book metadata value as
                   "bookid": "<THEBOOKID>".
                   Surely this duplicates a small data, but reduces the
                   amount of parameters in many functions
     - (MAYBE) In retrieve_book_metadata retrieve only missing data
     - (MAYBE) In retrieve_books retrieve only missing contents
     - (MAYBE) Zip file contents on disk
"""

#%%
import os
import pickle
from urllib.parse import urljoin
from pathlib import Path

import requests
from bs4 import BeautifulSoup as bs

import litcorpt.settings as settings

#%%
def retrieve_booklist(verbose=False):
    """ Retrieve the book list from settings.GUTENBERG_URL
    Input:
        None
    Output:
        books (dict): A dicionary with keys as book id and values
                      with bookpaths to online metadata
    """
    if verbose:
        print(f"Connecting to {settings.GUTENBERG_URL}")

    response = requests.get(settings.GUTENBERG_URL)

    if verbose:
        print("Building book list")

    # Find all book entries
    soup = bs(response.text, 'html.parser')
    books_group = soup.find('div', {'class': 'pgdbbylanguage'})
    books_list = books_group.findAll('li', {'class': 'pgdbetext'})

    # Process entries into a dictionary
    books = {}
    for book_entry in books_list:
        book_link = book_entry.find('a')
        book_href = book_link['href']
        book_title = book_link.get_text()
        book_id = book_href.split('/')[-1]
        books[book_id] = { 'title': book_title, 'href': book_href }

    if verbose:
        if len(books) > 0:
            print(f"{len(books)} books found")
        else:
            print("No books found")

    return books

#%%
def retrieve_book_tables(bookpath):
    """Retrieve the Gutenberg book table for a given bookurl

    Input:
        bookpath (str): A ebookid path for example: /ebooks/123456

    Output:
        booktable (dict): A dicionary containing the contents of ebook
                          metadata as in gutenberg site
    """
    book_url = urljoin(settings.GUTENBERG_URL, bookpath)
    book_req = requests.get(book_url)
    book_soup = bs(book_req.text, 'html.parser')

    # Retrieve bibliographic metadata table
    bibtable = book_soup.find('table', { 'class': 'bibrec'})
    bibtable_list = []
    for row in bibtable.findAll('tr'):
        for td in row.findAll('td'):
            header = row.find('th')
            header = header.text
            content = td.text
            content = content.replace('\r', ': ')
            content = content.strip()
            bibtable_list.append((header, content))

    # Convert metadata list to dict. Merging equal headers in a list
    bibtable_dict = {}
    for key, val in bibtable_list:
        if key not in bibtable_dict:
            bibtable_dict[key] = [val]
        else:
            bibtable_dict[key].append(val)

    # Find anchors to gutenberg ebook files and add to metadata
    filestable = book_soup.find('table', { 'class': 'files'})
    document_anchors = [anchor['href']
                        for anchor in filestable.findAll('a')
                        if 'type' in anchor.attrs
                        if 'text/plain' in anchor.attrs['type']]
    bibtable_dict['files'] = document_anchors

    return bibtable_dict

#%%
def retrieve_book_metadata(bookid, bookmeta, verbose=False):
    """ Retrieve metadata for given bookid and metadata

    TODO: Handle EDITOR if Author is missing

    Input:
        bookid (str): A gutenberg bookid
        metadata (dict): A dictionary containing a book metadata
                         must contain at least 'href' key filled.


    Output:
        bookmeta (dict): A book dict with pre-preocessed metadata.
    """

    if verbose:
        print(f"{bookid}: retrieving metadata {bookmeta['href']}")

    booktable = retrieve_book_tables(bookmeta['href'])

    # Process Author
    if ('Author' in booktable and len(booktable['Author']) > 0):
        # We are handling multiple authors in same title
        author_list = []
        for author in booktable['Author']:

            author_entry = [entry.strip() for entry in author.split(',')]

            # Default author entries
            author_lastname = author_entry[0]
            author_firstname = ''
            author_life = ''

            # Format LastName, First Name, Period
            if len(author_entry) > 2:
                author_firstname = author_entry[1]
                author_life = author_entry[-1]

            # Format LastName, First Name
            elif len(author_entry) == 2:
                author_firstname = author_entry[1]

            author_dict = {'lastname': author_lastname,
                           'firstname': author_firstname,
                           'life': author_life}

            author_list.append(author_dict)

        bookmeta['authors'] = author_list

    if ('Editor' in booktable and len(booktable['Editor']) > 0):
        # We are handling multiple authors in same title
        editor_list = []
        for editor in booktable['Editor']:
            editor_entry = [entry.strip() for entry in editor.split(',')]
            # Default editor entries
            editor_lastname = editor_entry[0]
            editor_firstname = ''
            editor_life = ''
            # Format LastName, First Name, Period
            if len(editor_entry) > 2:
                editor_firstname = editor_entry[1]
                editor_life = editor_entry[-1]
            # Format LastName, First Name
            elif len(editor_entry) == 2:
                editor_firstname = editor_entry[1]

            editor_dict = {'lastname': editor_lastname,
                           'firstname': editor_firstname,
                           'life': editor_life}
            editor_list.append(editor_dict)

        bookmeta['editors'] = editor_list

    # Process Title
    if 'Title' in booktable and len(booktable['Title']) > 0:
        if len(booktable['Title']) > 1:
            print(f'Book {bookid} has more than one title, check closely')
        bookmeta['title'] = booktable['Title'][0]

    # Process Language notes
    if 'Language Note' in booktable and len(booktable['Language Note']) > 0:
        bookmeta['note'] = booktable['Language Note']

    # Process Language
    if 'Language' in booktable and len(booktable['Language']) > 0:
        bookmeta['language'] = [ l.lower() for l in  booktable['Language']]

    # Better treatment for Subjects
    if 'Subject' in booktable and len(booktable['Subject']) > 0:
        subjects = set()
        for subject_entry in booktable['Subject']:
            for subject in subject_entry.split(' -- '):
                subjects.add(subject.strip().lower())

        bookmeta['subject'] = list(subjects)

    # Process Category
    if 'Category' in booktable and len(booktable['Category']) > 0:
        bookmeta['category'] = [ c.lower() for c in booktable['Category']]

    # Better treatment to Library of Congress Classes
    if 'LoC Class' in booktable and len(booktable['LoC Class']) > 0:
        bookmeta['loc'] = booktable['LoC Class']

    if 'files'  in booktable and len(booktable['files']) > 0:
        bookmeta['files'] = booktable['files']

    return bookmeta

#%%
def retrieve_metadata(books, verbose=False):
    """ Retrieve "all"  metadata, from a gutenberg book list.

    TODO (Igor): Write a function to retrieve a single metadata.
                 Iterate this function from here.

    Input:
        books (dict): A dict with books. key is the book id, val is a dict of metadata. The metadata
                      must contain at least 'href' key, pointing to gutenberg.org ebook page.

    Returns:
        books (dict): The books dictionary filled with existent metadata
    """

    for bookid, bookmeta in books.items():
        # Verify if entry is sane
        if 'href' in bookmeta and len(bookmeta['href']) > 0:
            books[bookid] = retrieve_book_metadata(bookid, bookmeta, verbose=verbose)
        else:
            if verbose:
                print(f"{bookid}: href is invalid. Skipping.")
            continue


    return books

#%%
def retrieve_book (bookid, bookmeta, verbose=False):
    """ Retrieve ebook content for a given bookid

    Input:
        bookid (str): The book id
        bookmeta (dict): A dicionary with bookmeta data. Need non-empty
                         'files' key.

    Output:
        contents: A list containing ebooks content.
                  Each element of list is a single ebook as string
    """
    contents = []
    for filepath in bookmeta['files']:
        ebook_url = urljoin(settings.GUTENBERG_URL, filepath)
        if verbose:
            print(f"{bookid}: Requesting content from {ebook_url}.")
        ebooktxt_resp = requests.get(ebook_url)
        ebooktxt_content = ebooktxt_resp.content
        ebooktxt_content = str(ebooktxt_content, 'utf-8')
        contents.append(ebooktxt_content)

    return contents

#%%
def retrieve_books(books, verbose=False):
    """ Retrieve ebook contents for all books listed in metadata
    Input:
        books (dict) a dict containing books and its metadata

    Return:
        books (dict) same dict with file data. In 'contents' metadata key.
    """
    for bookid, bookmeta in books.items():
        if 'files' in bookmeta:
            contents = retrieve_book (bookid, bookmeta, verbose=verbose)
        else:
            if verbose:
                print(f"{bookid}: Do not contain files.")
            continue
        books[bookid]['contents'] = contents

    return books

#%%
def dump_entry(bookid, metadata, replace=False, verbose=False):
    """Write a single book entry in settings.GUTENBERG_DATAPATH for later use.
    Input:
        bookid (str): Book id
        metadata (dict): Book metadata
        replace (bool): If content exists, overwrite. Default behavior is to skip
         verbose (bool): Be verbose
    Output:
        Written (bool): True if written, False if skips
    """
    book_path = os.path.join(settings.GUTENBERG_DATAPATH, bookid)
    Path(book_path).mkdir(parents=True, exist_ok=True)

    book_info_filename = f'{bookid}-info.txt'
    book_pickle_filename = f'{bookid}.p'
    book_content_filename = f'{bookid}.txt'
    book_info_filepath = os.path.join(book_path, book_info_filename)
    book_pickle_filepath = os.path.join(book_path, book_pickle_filename)
    book_content_filepath = os.path.join(book_path, book_content_filename)

    if (os.path.exists(book_info_filepath) or
        os.path.exists(book_pickle_filepath) or
        os.path.exists(book_content_filepath)) and replace is False:
        if verbose:
            print(f"{bookid}: Data path {book_path} isn't empty and replace is False. Skipping.")
        return False


    # INFO (Igor): Info file do not contains all information available in pickle.
    with open(book_info_filepath, 'w') as book_info_fd:
        info_values = []
        info_values.append(bookid)
        info_values.append(metadata.get('title', ''))
        authors = metadata.get('authors', [{}])
        author = authors[0]
        info_values.append(author.get('lastname', ''))
        info_values.append(author.get('firstname', ''))
        editors = metadata.get('editors', [{}])
        editor = editors[0]
        info_values.append(editor.get('lastname', ''))
        info_values.append(editor.get('firstname', ''))
        info_values.append(';'.join(metadata.get('language', [])))
        info_values.append(';'.join(metadata.get('subject', [])))
        info_values.append(';'.join(metadata.get('category', [])))
        info_values.append(' '.join(metadata.get('note', [])))
        info_values_str = ','.join(info_values)
        info_values_str += '\n'
        book_info_fd.write(info_values_str)

    # Only the first file content right now...
    if len(metadata.get('contents', '')) > 0:
        with open(book_content_filepath, 'w') as book_content_fd:
            book_content_fd.write(metadata['contents'][0])

    with open(book_pickle_filepath, 'wb') as book_pickle_fd:
        meta = metadata.copy()
        meta.pop('contents', '')
        pickle.dump(meta, book_pickle_fd)


    return True

#%%
def dump_data(books, replace=False, verbose=False):
    """Write books dictionary in settings.GUTENBERG_DATAPATH for later use

    Input:
        books (dict): A dicionary containing all books

    Output:
        Number (int): Number of success dumps.
    """
    print(f"Writting data to {settings.GUTENBERG_DATAPATH}")
    success_count = 0
    for bookid, metadata in books.items():
        if verbose:
            print(f"{bookid}\t", end="")
        if dump_entry(bookid, metadata, replace=replace, verbose=verbose):
            success_count += 1

    print()
    return success_count

#%%
def load_book(bookid, book_path):
    """ Load book given bookpaths

    TODO: Handle if files are missing. Right now it will break.

    Input:
        bookid (str):  A book id
        bookpath (str): A path to book data

    Output:
        book (dict): A book entry
    """

    book_pickle_filename = f'{bookid}.p'
    book_pickle_filepath = os.path.join(book_path, book_pickle_filename)

    book_content_filename = f'{bookid}.txt'
    book_content_filepath = os.path.join(book_path, book_content_filename)


    # Build bookmeta dict with empty contents
    with open(book_pickle_filepath, 'rb') as book_pickle_fd:
        bookmeta = pickle.load(book_pickle_fd)
        bookmeta['contents'] = []

    # Read file contents (only a single file right now)
    with open(book_content_filepath, 'rb') as book_content_fd:
        contents = book_content_fd.read()
        contents = str(contents, 'utf-8')
        bookmeta['contents'].append(contents)

    return bookmeta

#%%
def load(verbose=False):
    """ Load all portuguese gutenberg books.

    TODO (Igor): Handle if part of information is missing. Right now it will break.

    Input:
        verbose (bool): Display helpful messages

    Output:
        books (dict): A dictionary containing the whole dataset and metadata.

    The books (dict) format entry is the following:

    { BOOKID(str): { 'title': (str) Book title,
                     'href': (str) url path to book metadata,
                     'authors': (list) list of authors and editors,
                     'note': (list) addicional information about the book,
                     'language': (list) document language,
                     'subject': (list) document subjects, as: politics, art, math, etc.,
                     'category': (list) document genre, as drama, poetry, etc,
                     'loc': (list) library of congress catalog entry,
                     'files': (list) url path to book contents (txt file),
                     'contents': (list) contents related to each reference in 'files'.
                   }

    BOOKID is string reference to gutenberg ebook id as '123456' (yes, a string, deal with it).
    """


    bookdirs = [x
                for x in os.listdir(settings.GUTENBERG_DATAPATH)
                if os.path.isdir(os.path.join(settings.GUTENBERG_DATAPATH, x))]

    books = {}
    for bookdir in bookdirs:
        bookid = bookdir
        if verbose:
            print(f"{bookid}\t", end="")
        bookpath = os.path.join(settings.GUTENBERG_DATAPATH, bookdir)
        bookmeta = load_book(bookid, bookpath)
        books[bookid] = bookmeta

    print()
    return books

#%%
if __name__ == '__main__':
    pass
