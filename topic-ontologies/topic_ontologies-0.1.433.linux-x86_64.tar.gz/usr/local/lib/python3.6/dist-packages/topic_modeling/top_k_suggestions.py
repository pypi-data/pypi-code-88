from conf.configuration import *
import pandas as pd
from utils.parts import *
import random
import csv
import numpy as np
from topic_modeling.topics import *
def produce_top_k_suggestions(dataset,ontology,model,k,debug=False):
    path_top_k_topic_path = get_path_top_k_topics_per_document(dataset,ontology,model,k)
    topics,topic_ids = load_topics_with_ids('ontology-'+ontology)
    top_k_document_dict={}
    top_k_document_dict['id']=[]
    top_k_document_dict['topic-id']=[]

    for document_vectors_ids in parts_vectors(dataset,ontology,model):
        for document_vector_id in document_vectors_ids:
            document_vector = document_vector_id[0].copy()
            document_id=document_vector_id[1]
            for i in range(k):
                top_topic_index = np.argmax(document_vector)
                top_topic= topics[top_topic_index]
                top_topic_weight= document_vector[top_topic_index]
                top_topic_id=topic_ids[top_topic_index]
                document_vector[top_topic_index]=0
                top_k_document_dict['id'].append(document_id)
                top_k_document_dict['topic-id'].append(top_topic_id)

    df_top_k_topic=pd.DataFrame(top_k_document_dict)
    log_size("top-k-topics",df_top_k_topic.shape[0])
    df_top_k_topic.to_csv(path_top_k_topic_path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)




