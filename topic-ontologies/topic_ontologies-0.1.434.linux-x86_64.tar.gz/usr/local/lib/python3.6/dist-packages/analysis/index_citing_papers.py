import pandas as pd
from whoosh import index
from whoosh import fields
from whoosh import qparser
from  conf.configuration import *
from whoosh.analysis import StandardAnalyzer
from pathlib import Path
from whoosh.qparser import OrGroup
import logging
from datetime import datetime
import shutil
logging.basicConfig(format="%(message)s",filename="../logs/citing-paper-indexing.log",level=logging.DEBUG)

def create_schema():
    st_ana = StandardAnalyzer()# StandardAnalyzer skips stop words, tokenize by spacy, and lower
    schema = fields.Schema(id=fields.STORED,
                           text=fields.TEXT(analyzer=st_ana, stored=True),
                           )
    return  schema

def index_papers():
    logging.warning(datetime.now())

    corpora = load_corpora_list()
    schema=create_schema()
    for corpus in corpora:
        logging.warning("indexing %s"%corpus)
        path_citing_papers_text = get_path_citing_papers_text(corpus)
        path_corpus_index = get_path_citing_papers_index(corpus)
        if path_corpus_index!=None and path_citing_papers_text!=None:
            df_citing_papers_text = pd.read_csv(path_citing_papers_text,sep=",",encoding="utf-8",quotechar="\"")
            df_citing_papers_text=df_citing_papers_text.dropna(subset=['text'])
            index_path=Path(path_corpus_index)
            ix = index.create_in(index_path, schema)
            writer = ix.writer()
            for i,citing_paper in df_citing_papers_text.iterrows():
                id=citing_paper['id']
                logging.warning("indexing paper %d"%id)
                text=citing_paper['text']
                if text!=None:
                    writer.add_document(id=id,text=text)
            writer.commit()

def find_experiment_papers():

    df_corpora_queries=pd.read_csv("/mnt/ceph/storage/data-in-progress/topic-ontologies/citing-papers/corpora-queries-no-citations.csv",sep=",",encoding="utf-8")
    df_corpora_queries=df_corpora_queries.melt('corpus',value_name='query')

    df_corpora_queries=df_corpora_queries.dropna(subset=['query'])
    df_corpora_queries['query']=df_corpora_queries['query'].astype(str)
    for corpus in load_corpora_list():
        path_corpus_index = get_path_citing_papers_index(corpus)
        path_corpus_papers= get_path_citing_papers(corpus)
        path_experiment_papers=get_path_experiment_papers(corpus)
        print(corpus,path_experiment_papers)
        if path_corpus_papers!=None and path_corpus_index!=None:
            ix = index.open_dir(path_corpus_index)
            with ix.searcher() as searcher:
                corpus_queries=df_corpora_queries[df_corpora_queries['corpus']==corpus]

                for ind, corpus_query in corpus_queries.iterrows():
                    query=corpus_query['query']
                    logging.warning(query)
                    if query!=None:
                        qp = qparser.QueryParser("text", schema=ix.schema,)
                        q= qp.parse(corpus_query['query'])
                        results = searcher.search(q,limit=300)
                        rank =0
                        for res in results:
                            rank=rank+1
                            paper_id= str(res['id'])
                            from_path=path_corpus_papers+"/"+paper_id+".pdf"

                            to_path=path_experiment_papers+"/"+paper_id+".pdf"
                            try:
                                shutil.copy(from_path,to_path)
                            except Exception as error:
                                logging.warning(error)
