#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup as bs
from bs4 import Comment
import sys
from urllib.parse import urljoin
import os

URLROOT = "http://www.dominiopublico.gov.br/pesquisa/ResultadoPesquisaObraForm.do?first=2080&skip=0&ds_titulo=&co_autor=&no_autor=&co_categoria=2&pagina=2&select_action=Submit&co_midia=2&co_obra=&co_idioma=1&colunaOrdenar=null&ordem=null"

response = requests.get(URLROOT)

soup = bs(response.text, 'html.parser')
book_table = soup.find('table', { 'class': 'displaytagTable' }).tbody

for tr in book_table.findAll('tr'):
    td = tr.findAll('td')
    book_href = td[1].a['href']
    book_link = urljoin(URLROOT, book_href)
    bookrps = requests.get(book_link)
    
#book_link = "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1982"

    try:
        if bookrps is None:
            bookrps = requests.get(book_link)
    except NameError:
        bookrps = requests.get(book_link)

    booksoup = bs(bookrps.text, 'html.parser')
    comments = booksoup.findAll(string=lambda text: isinstance(text, Comment))
    comment_soup = bs(comments[2], 'html.parser')
    ebookpdf_href = comment_soup.find('a')['href']
    ebookpdf_down = f"{ebookpdf_href}"
    ebookpdf_base = os.path.basename(ebookpdf_down)
    ebookpdf_name = ebookpdf_base.split('.')[0]
    ebookpdf_info = f"{ebookpdf_name}-info.txt"


    detalhe = booksoup.find('td', { 'class': 'detalhe1'})
    tablebib = detalhe.find_parent('table')

    for tr in tablebib.findAll('tr'):
        label = tr.find('td', { 'class': 'detalhe1'}).text.strip().split(':')[0]
        if label == 'Título':
            detalhe2 = tr.findAll('td', {'class': 'detalhe2'})
            title = detalhe2[1].text.strip()
        elif label == 'Autor':
            detalhe2 = tr.findAll('td', {'class': 'detalhe2'})
            author_str = detalhe2[1].text.strip()
            author_lst = author_str.split()
            author_name = ' '.join(author_lst[0:-1])
            author_surname = ""
            if len(author_lst) > 1:
                author_surname = author_lst[-1]


    print(f"Writing {ebookpdf_info}")
    ebookinf_fd = open(ebookpdf_info, 'w')
    ebookinf_str = f"{author_name},{author_surname},{title},None"
    ebookinf_fd.write(ebookinf_str)
    ebookinf_fd.close()

    #detalhe2 = tr.findAll('td', {'class': 'detalhe2'})
    ##value = detalhe2[1].text
    #print(f'{label} --> {len(value)}')








# #     print(f"Crawling  {book_link}")
# 
# #book_link = "http://www.dominiopublico.gov.br/pesquisa/DetalheObraForm.do?select_action=&co_obra=1982"
# 
# #if bookrps is None:
# bookrps = requests.get(book_link)
#     
# booksoup = bs(bookrps.text, 'html.parser')
# comments = booksoup.findAll(string=lambda text: isinstance(text, Comment))
# comment_soup = bs(comments[2], 'html.parser')
# ebookpdf_href = comment_soup.find('a')['href']
# ebookpdf_down = f"/download{ebookpdf_href}"
# ebookpdf_link = urljoin(URLROOT, ebookpdf_down)
# 
# ebookpdf_name = f"teste.pdf"
# ebookpdf_path = os.path.join(writedir, ebookpdf_name)
# 
# print(f"Requesting {ebookpdf_link}")
# ebookpdf_resp = requests.get(ebookpdf_link)
# print(f" Writing to {ebookpdf_path}.", end="")
# ebookpdf_fd = open(ebookpdf_path, 'wb')
# ebookpdf_fd.write(ebookpdf_resp.content)
# ebookpdf_fd.close()
# print(f" Done.")
# #
# #print(book_link)
# #print(ebookpdf_link)
# #
# #ebookinf_name = f"{book_info['ebookno']}-info.txt"
# #     ebooktxt_path = os.path.join(writedir, ebooktxt_name)
# #     ebookinf_path = os.path.join(writedir, ebookinf_name)
# #print(ebookpdf_href, ebookpdf_down, ebookpdf_link)
# 
#     #book_title = td[2].a.text.strip()
# 
# 
# 
# # books = soup.findAll("li", {"class": "pgdbetext"})
# # for book in books:
# #     bookanchor = book.find('a')['href']
# #     booklink = urljoin(URLROOT, bookanchor)
# #     print(f"Crawling  {booklink}")
# #     #URLBOOK = "http://www.gutenberg.org/ebooks/25697"
# #     #if "bookrps" not in locals() or bookrps is None:
# #     #    bookrps = requests.get(URLBOOK)
# #     bookrps = requests.get(booklink)
# # 
# #     booksoup = bs(bookrps.text, 'html.parser')
# # 
# #     filestable = booksoup.find('table', { 'class': 'files'})
# #     bibtable = booksoup.find('table', { 'class': 'bibrec'})
# # 
# #     book_info = { 'authorname': '',
# #                   'authorsurname': '',
# #                   'title': '',
# #                   'ebookno': '',
# #                   'notestring': ''}
# # 
# #     # Process bibliographic information
# #     for tr in bibtable.findAll('tr'):
# #         thead = tr.th
# # 
# #         if thead.text == 'Author':
# #             author_string = tr.td.text.strip()
# #             author_list = author_string.split(',')
# #             if len(author_list) > 2:
# #                 author_surname = author_list[0].strip()
# #                 author_name = author_list[1].strip()
# #                 author_life = author_list[-1].strip()
# #             else:
# #                 author_name = author_list[0]
# #                 author_surname = author_list[0]
# # 
# #             book_info['authorname'] = author_name
# #             book_info['authorsurname'] = author_surname
# # 
# #         if thead.text == 'Title':
# #             title_string = tr.td.text.strip()
# #             book_info['title'] = title_string
# # 
# #         if thead.text == 'EBook-No.':
# #             ebook_string = tr.td.text.strip()
# #             book_info['ebookno'] = ebook_string
# # 
# #         if thead.text == 'Language Note':
# #             note_string = tr.td.text.strip()
# #             book_info['notestring'] = note_string
# #             
# #     # Read ebook and write to disk
# #     ebooktxt_name = f"{book_info['ebookno']}.txt"
# #     ebookinf_name = f"{book_info['ebookno']}-info.txt"
# #     ebooktxt_path = os.path.join(writedir, ebooktxt_name)
# #     ebookinf_path = os.path.join(writedir, ebookinf_name)
# #     if os.path.isfile(ebookinf_path):
# #         print(f"File {ebookinf_path} exists. Skipping.")
# #     else:
# #         ebookinf_fd = open(ebookinf_path, 'w')
# #         ebookinf_str = f'{book_info["authorname"]},{book_info["authorsurname"]},{book_info["title"]},{book_info["notestring"]}'
# #         ebookinf_fd.write(ebookinf_str)
# #         ebookinf_fd.close()
# #         print(f" Done.")
# # 
# #     if os.path.isfile(ebooktxt_path):
# #         print(f"File {ebooktxt_path} exists. Skipping.")
# #     else:
# #         ebooktxt_href = None
# #         for anchor in filestable.findAll('a'):
# #             if 'type' in anchor.attrs:
# #                 if 'text/plain' in anchor.attrs['type']:
# #                     ebooktxt_href = anchor['href']
# # 
# #         if ebooktxt_href is not None:
# #             ebooktxt_link = urljoin(URLBOOK, ebooktxt_href)
# #             print(f"Requesting {ebooktxt_name} from {ebooktxt_link}.", end="")
# #             ebooktxt_resp = requests.get(ebooktxt_link)
# #             print(f" Writing to {ebooktxt_path}.", end="")
# #             ebook_fd = open(ebooktxt_path, 'wb')
# #             ebook_fd.write(ebooktxt_resp.content)
# #             ebook_fd.close()
# #             print(f" Done.")
# #         else:
# #             print(f"Could not find book entry for {booklink}.")
# # 
