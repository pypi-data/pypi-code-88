import pandas as pd
from difflib import SequenceMatcher
def similar(a,b):
    return SequenceMatcher(None,a,b).ratio()

def fuzzy_merge_topic_ids(df_documents,df_topics,):
    df_documents['topic-id']=-1
    for d_i,d_row in df_documents.iterrows():
        best_similarity=0
        for topic_i,topic_row in df_topics.iterrows():
            similarity=similar(d_row['topic'],topic_row['topic'])
            if similarity>best_similarity :
                topic_id= topic_row['topic-id']
                df_documents.loc[d_i,'topic-id']=topic_id
                best_similarity=similarity
    return df_documents

def drop_separator(text,sep):
    return text.replace(sep,"")