import pandas as pd
from conf.configuration import *
import re

def calculate_statistics_for(ontology):
    path_source = get_path_source('ontology-'+ontology)
    path_statistics=get_path_histogram_two_parameters('ontology-'+ontology,'topic','token')
    df_documents=pd.read_csv(path_source,sep=",",encoding="utf-8")
    df_documents['token.count']=df_documents.apply(count_tokens,axis=1)
    del df_documents['text']
    df_documents.to_csv(path_statistics,sep=",",encoding="utf-8")

def count_tokens(row):
    text = row['text']
    text = text.lower()
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", " ", text)
    text = re.sub("[^A-Za-z]+", " ", text).replace("  ", " ")
    tokens =text.split(" ")
    return len(tokens)
def calculate_statistics():
    ontologies= get_topic_ontologies()
    mins=[]
    means=[]
    maxs=[]

    for ontology in ontologies:
        print(ontology)
        calculate_statistics_for(ontology)
        path_statistics=get_path_histogram_two_parameters('ontology-'+ontology,'topic','token')
        df_statistics =pd.read_csv(path_statistics,sep=",",encoding="utf-8")
        min=df_statistics['token.count'].min()
        max=df_statistics['token.count'].max()
        mean=df_statistics['token.count'].mean()
        mins.append(min)
        maxs.append(max)
        means.append(mean)
    df_statistics=pd.DataFrame({'ontology':ontologies,'min':mins,'max':maxs,'mean':means},)
    df_statistics.to_csv('/home/yamenajjour/workspace/research-in-progress/arguana/COLING-20/coling20-topic-ontologies-for-argumentation-data/ontology-tokens-statistics.csv'
                         ,columns=['ontology','min','mean','max'],sep=",",encoding="utf-8")
calculate_statistics()