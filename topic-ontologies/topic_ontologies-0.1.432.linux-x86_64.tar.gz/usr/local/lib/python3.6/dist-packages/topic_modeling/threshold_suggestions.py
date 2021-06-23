from conf.configuration import *
import pandas as pd
from utils.parts import *
import random
import csv
import numpy as np
from topic_modeling.topics import *
from mylogging.mylogging import *
def produce_threshold_suggestions(dataset,ontology,model,threshold,debug=False):
    path_topic_path_threshold = get_path_topics_per_document_threshold(dataset,ontology,model,threshold)
    topics,topic_ids = load_topics_with_ids('ontology-'+ontology)
    top_document_dict={}
    top_document_dict['id']=[]
    top_document_dict['topic-id']=[]

    for document_vectors_ids in parts_vectors(dataset,ontology,model):
        for document_vector_id in document_vectors_ids:
            document_vector= np.array(document_vector_id[0])
            document_id=document_vector_id[1]
            if isinstance(document_vector,list):
                topics_indexes = np.where(document_vector>=threshold)[0]
                scores = document_vector[topics_indexes]
            else:
                topics_indexes = np.where(document_vector>=threshold)[0]
                scores = document_vector[topics_indexes]

            top_topic_ids = [topic_ids[topic_index] for topic_index in topics_indexes]
            top_document_dict['topic-id'].extend(top_topic_ids)
            top_document_dict['id'].extend([document_id for _ in top_topic_ids])
    df_threshold_topic=pd.DataFrame(top_document_dict)
    log_size("threshold-topics",df_threshold_topic.shape[0])
    df_threshold_topic.to_csv(path_topic_path_threshold,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)


