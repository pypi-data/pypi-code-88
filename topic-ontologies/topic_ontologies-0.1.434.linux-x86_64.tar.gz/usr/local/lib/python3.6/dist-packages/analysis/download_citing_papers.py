from conf.configuration import *
import pandas as pd
import urllib.request
import logging
import time
import random
import os.path
from datetime import datetime
#import pdftotext
import re
def filter_downloadable():
    corpora=['ukp-argument-annotated-essays-v2']
    #corpora = load_corpora_list()
    websites={
              'arxiv':'https://arxiv.org',
              'acm':'https://dl.acm.org',
              'acl':'https://www.aclweb.org'
              }

    patterns={
        'arxiv':lambda url:url.replace('abs','pdf'),
        'acm':lambda url: url.split('?')[0]+'.pdf' if '?' in url  else (url.replace("abs","pdf") if "abs" in url else url+".pdf"),
        'acl':lambda url: url[:-1]+".pdf"
    }

    for corpus in corpora:
        print(corpus)
        path_citing_papers_links=get_path_citing_papers_links(corpus)
        if path_citing_papers_links!=None:
            df_citing_papers_links = pd.read_csv(path_citing_papers_links,sep=",",encoding="utf-8",quotechar="\"")
            df_citing_papers_links['ArticleURL']=df_citing_papers_links['ArticleURL'].astype(str)
            df_citing_papers_links['pdf']=df_citing_papers_links.apply(lambda row: row['ArticleURL'].endswith('pdf'),axis=1)
            df_citing_papers_links['url']=""
            df_non_pdf_files=df_citing_papers_links[~df_citing_papers_links.pdf]
            for website in websites:
                head=websites[website]
                df_citing_papers_links[website]=df_non_pdf_files.apply(lambda row: row['ArticleURL'].startswith(head),axis=1)

            for index, row in df_citing_papers_links.iterrows():
                if row.pdf:
                    df_citing_papers_links.loc[index,'url']=row['ArticleURL']
                else:
                    for website in websites:
                        pattern=patterns[website]
                        if row[website]:
                            df_citing_papers_links.loc[index,'url']=pattern(row['ArticleURL'])
            df_citing_papers_links['id']=range(0,df_citing_papers_links.shape[0])
            df_citing_papers_links.to_csv(path_citing_papers_links,sep=",",encoding="utf-8",quotechar="\"",index=False)

def setup_mozilla():
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)

def download_files(check_existence=False):
    logging.basicConfig(format="%(message)s",filename="../logs/download-citing-papers.log")
    corpora=['ukp-argument-annotated-essays-v2']
    logging.warning(datetime.now())
    #corpora = load_corpora_list()
    #corpora=['upotsdam-arg-microtexts-v2']
    for corpus in corpora:
        logging.warning("download citing papers of %s"%corpus)
        path_citing_papers_links=get_path_citing_papers_links(corpus)
        path_citing_papers=get_path_citing_papers(corpus)
        if path_citing_papers_links!=None:
            df_citing_papers_links = pd.read_csv(path_citing_papers_links,sep=",",encoding="utf-8",quotechar="\"")
            df_citing_papers_links=df_citing_papers_links.loc[df_citing_papers_links['url'].dropna().index]
            for index,paper in df_citing_papers_links.iterrows():
                id=paper['id']
                url=paper['url']

                path=path_citing_papers+"/"+str(id)+".pdf"
                #print(url,path)
                try:
                    setup_mozilla()
                    if check_existence:
                        if not os.path.exists(path):
                            logging.warning("downloading %s"%url)
                            urllib.request.urlretrieve(url,path)
                    else:
                            logging.warning("downloading %s"%url)
                            urllib.request.urlretrieve(url,path)

                except Exception as error:
                    logging.warning(error)
                    logging.warning("could not download %s" %url)

                time.sleep(random.randint(1,20))

def parse_files():
    #logging.basicConfig(format="%(message)s",filename="../logs/parsing-papers.log")
    corpora=load_corpora_list()
    for corpus in corpora:
        logging.warning("parsing papers of %s"%corpus)
        path_citing_papers_links=get_path_citing_papers_links(corpus)
        path_citing_papers_texts=get_path_citing_papers_text(corpus)
        if path_citing_papers_links!=None and os.path.exists(path_citing_papers_links):
            path_citing_papers=get_path_citing_papers(corpus)
            df_citing_papers=pd.read_csv(path_citing_papers_links,sep=",",encoding="utf-8",quotechar="\"")
            df_citing_papers['text']=""
            for index,citing_paper in df_citing_papers.iterrows():
                paper_id=citing_paper['id']
                path_citing_paper = path_citing_papers+"/"+str(paper_id)+".pdf"
                if os.path.exists(path_citing_paper):
                    logging.warning("found %s %s"%(corpus,paper_id))
                    text=""
                    try:
                        with open(path_citing_paper,'rb') as f:
                            paper_pdf = pdftotext.PDF(f)
                            for page in paper_pdf:
                                text=text+page
                    except Exception as error:
                        logging.warning(error)
                    text=text.replace("\t"," ").replace("\n"," ")
                    text=re.sub(r"\s+"," ",text)
                    df_citing_papers.loc[index,'text']=text
            df_citing_papers=df_citing_papers[['id','Abstract','Cites','Title','text']]
            df_citing_papers.to_csv(path_citing_papers_texts,sep=",",encoding="utf-8",quotechar="\"")

def count_citing_papers():
    corpora = load_corpora_list()
    all_count_of_citing_papers=0
    for corpus in corpora:
        print(corpus)
        path_citing_papers_links=get_path_citing_papers_links(corpus)
        if path_citing_papers_links!=None:
            df_citing_papers=pd.read_csv(path_citing_papers_links,sep=",",encoding="utf-8",quotechar="\"")
            count_of_citing_papers=df_citing_papers.shape[0]
            print(count_of_citing_papers)
            all_count_of_citing_papers= all_count_of_citing_papers+ count_of_citing_papers
    print(all_count_of_citing_papers)

def count_downloaded_papers():
    corpora = load_corpora_list()
    all_count_of_downloaded_papers=0
    for corpus in corpora:
        print(corpus)
        path_downloaded_papers=get_path_citing_papers(corpus)
        downloaded_papers=os.listdir(path_downloaded_papers)
        count_downloaded_papers=len(downloaded_papers)
        all_count_of_downloaded_papers=all_count_of_downloaded_papers+count_downloaded_papers
    print(all_count_of_downloaded_papers)



