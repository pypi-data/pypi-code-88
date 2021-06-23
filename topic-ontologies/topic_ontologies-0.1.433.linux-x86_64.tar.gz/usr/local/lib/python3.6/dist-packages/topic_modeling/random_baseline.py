from conf.configuration import *
import pandas as pd
from utils.parts import *
import random
import csv
def log_status(counter,size,debug):
    percentage=(float(counter)/size)*100
    if debug and random.randint(0,1000) %997 ==0:
        logging.warning("finished %2.2f"%percentage)

def produce_random_suggestions(dataset, ontology, k, debug=False):
    path_top_k_results=get_path_top_k_topics_per_document(dataset,ontology,'random',k)
    path_ontology_topics=get_path_topics('ontology-'+ontology)
    df_ontology_topics=pd.read_csv(path_ontology_topics,sep=',',quotechar='"',quoting=csv.QUOTE_ALL,encoding='utf-8',dtype={'id': object})
    df_ontology_topics.rename(columns={'id':'ontology-topic-id'},inplace=True)
    labels=[]

    for df_part in parts_text(dataset):
        counter=0
        for index,document in df_part.iterrows():
            size=df_part.shape[0]
            log_status(counter,size,debug)
            relevant_topics=df_ontology_topics['ontology-topic-id'].sample(k).values
            df_relevant_topics=pd.DataFrame({'ontology-topic-id':relevant_topics})
            df_relevant_topics['id']=document['id']
            labels.append(df_relevant_topics)
    df_labels=pd.concat(labels)
    df_labels.to_csv(path_top_k_results,sep=",",quotechar='"',quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)