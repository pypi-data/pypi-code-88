import numpy as np
from topic_modeling.topics import *
import csv
import logging
import pickle
import pyarrow
import sys
def load_corpus(dataset,topic_ontology,topic_model):
    granularity = get_granularity(dataset)
    if granularity =='document':
        part_count=get_part_count(dataset)
        document_ids=[]
        document_vectors=[]
        if part_count!=None:
            for part_num in range(part_count):

                path_document_vectors_part=get_path_document_vectors_part(dataset,topic_ontology,topic_model,part_num)
                logging.warning("reading argument vectors from %s"%path_document_vectors_part)
                vectors_df = pd.read_pickle(path_document_vectors_part)
                document_ids.extend(list(vectors_df['document-id']))
                document_vectors.extend(list(vectors_df['document-vector']))
        else:

            path_topic_vectors = get_path_document_vectors(dataset,topic_ontology,topic_model)
            vectors_df = pd.read_pickle(path_topic_vectors)
            logging.warning("reading document vectors from %s"%path_topic_vectors)
            document_ids = list(vectors_df['document-id'])
            document_vectors = list(vectors_df['document-vector'])
        return document_ids,document_vectors
    else:
        path_topic_vectors = get_path_argument_vectors(dataset,topic_ontology,topic_model)
        logging.warning("reading argument vectors from %s"%path_topic_vectors)
        try:
            vectors_df = pd.read_pickle(path_topic_vectors)
        except Exception as error:
            vectors_df = pd.read_parquet(path_topic_vectors)

        argument_ids = list(vectors_df['argument-id'])
        argument_vectors = list(vectors_df['argument-vector'])
        return argument_ids,argument_vectors

def load_corpus_part(dataset,topic_ontology,topic_model,part_num):
    granularity = get_granularity(dataset)
    if granularity =='document':
        path_document_vectors_part=get_path_document_vectors_part(dataset,topic_ontology,topic_model,part_num)
        logging.warning("reading argument vectors from %s"%path_document_vectors_part)
        vectors_df = pd.read_pickle(path_document_vectors_part)
        document_ids=list(vectors_df['document-id'])
        document_vectors=list(vectors_df['document-vector'])
        return document_ids, document_vectors



def get_top_topics(corpus_vector,k):
    top_ten_threshold = sorted(corpus_vector,)[-num]
    filtered_topic_vector = []
    for topic_weight in corpus_vector:
        if topic_weight< top_ten_threshold:
            filtered_topic_vector.append(0)
        else:
            filtered_topic_vector.append(topic_weight)
    return filtered_topic_vector


    corpora_vectors= [load_corpus_vectors(corpus,topic_ontology,topic_model) for corpus in corpora]
    filtered_corpora_vectors = [get_top_topics(corpus_vector,10) for corpus_vector in corpora_vectors]
    filtered_corpora_vectors_np = np.array(filtered_corpora_vectors)
    return corpora,filtered_corpora_vectors_np



def save_top_topics_threshold(dataset,topic_ontology,topic_model,threshold):
    logging.warning('producing top topics threshold for %s %s %s' %(topic_ontology,topic_model,dataset))
    granularity = get_granularity(dataset)
    if granularity =='document':
        path_top_topics_path_threshold = get_path_topics_per_document_threshold(dataset,topic_ontology,topic_model,threshold)
    else:
        path_top_topics_path_threshold = get_path_topics_per_argument_threshold(dataset,topic_ontology,topic_model,threshold)
    part_count=get_part_count(dataset)

    topics,topic_ids = load_topics_with_ids('ontology-'+topic_ontology)
    top_document_dict={}
    top_document_dict['document.id']=[]
    top_document_dict['topic.id']=[]
    top_document_dict['score']=[]
    if part_count!=None:
        for part_num in range(part_count):
            logging.warning("processing part %d"%part_num)
            document_ids, document_vectors=load_corpus_part(dataset,topic_ontology,topic_model,part_num)
            logging.warning("loaded %d document vectors"%len(document_vectors))
            for i, document_id in enumerate(document_ids):
                if isinstance(document_vectors[i],list):
                    document_vector= np.array(document_vectors[i])
                    topics_indexes = np.where(document_vector>=threshold)[0]
                    scores = document_vector[topics_indexes]
                else:
                    topics_indexes = np.where(document_vectors[i]>=threshold)[0]
                    scores = document_vectors[i][topics_indexes]
                top_topic_ids = [topic_ids[topic_index] for topic_index in topics_indexes]
                top_document_dict['topic.id'].extend(top_topic_ids)
                top_document_dict['document.id'].extend([document_id for _ in top_topic_ids])
                top_document_dict['score'].extend(scores)
    else:
        document_ids, document_vectors = load_corpus(dataset,topic_ontology,topic_model)
        logging.warning("loaded %d document vectors"%len(document_vectors))
        for i, document_id in enumerate(document_ids):
            if isinstance(document_vectors[i],list):
                document_vector= np.array(document_vectors[i])
                topics_indexes = np.where(document_vector>threshold)[0]
                scores = document_vector[topics_indexes]
            else:
                topics_indexes = np.where(document_vectors[i]>threshold)[0]
                scores = document_vectors[i][topics_indexes]
            top_topic_ids = [topic_ids[topic_index] for topic_index in topics_indexes]
            top_document_dict['topic.id'].extend(top_topic_ids)
            top_document_dict['document.id'].extend([document_id for _ in top_topic_ids])
            top_document_dict['score'].extend(scores)

    df_top_topics_threshold=pd.DataFrame(top_document_dict)
    logging.warning("saving top topics for corpus %s, topic ontology %s, topic model %s into %s"%(dataset,topic_ontology,topic_model,path_top_topics_path_threshold))
    df_top_topics_threshold.to_csv(path_top_topics_path_threshold,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)

def save_top_k_topics_per_doucment(dataset,topic_ontology,topic_model,k):
    logging.warning('preprocessing %s %s' %(topic_ontology,topic_model))

    granularity = get_granularity(dataset)
    if granularity =='document':
        path_top_k_topic_path = get_path_top_k_topics_per_document(dataset,topic_ontology,topic_model,k)
    else:
        path_top_k_topic_path = get_path_top_k_topics_per_argument(dataset,topic_ontology,topic_model,k)

    topics,topic_ids = load_topics_with_ids('ontology-'+topic_ontology)
    topic_label_template="top-%d-topic"
    topic_weight_label_tempate="top-%d-topic-weight"
    #initializing columns
    top_k_document_dict={}
    top_k_document_dict['document.id']=[]
    top_k_document_dict['topic.id']=[]
    top_k_document_dict['score']=[]

    document_ids, document_vectors = load_corpus(dataset,topic_ontology,topic_model)
    logging.warning("loaded %d document vectors"%len(document_vectors))

    for i,document_id in enumerate(document_ids):
        document_vector = document_vectors[i].copy()
        for i in range(k):
            top_topic_index = np.argmax(document_vector)
            top_topic= topics[top_topic_index]
            top_topic_weight= document_vector[top_topic_index]
            top_topic_id=topic_ids[top_topic_index]
            document_vector[top_topic_index]=0
            top_k_document_dict['document.id'].append(document_id)
            top_k_document_dict['topic.id'].append(top_topic_id)
            top_k_document_dict['score'].append(top_topic_weight)
    df_top_k_topic=pd.DataFrame(top_k_document_dict)
    logging.warning("saving top topics for corpus %s, topic ontology %s, topic model %s into %s"%(dataset,topic_ontology,topic_model,path_top_k_topic_path))
    df_top_k_topic.to_csv(path_top_k_topic_path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)

def generate_top_topics_sample():
     argument_esa_model.esa_all_terms.initialize_mode()
     save_top_k_topics_per_doucment('sample','debatepedia','esa',10)
     argument_esa_model.esa_all_terms.initialize_mode()
     save_top_k_topics_per_doucment('sample','wikipedia','esa',10)
     argument_esa_model.esa_all_terms.initialize_mode()
     save_top_k_topics_per_doucment('sample','strategic-intelligence','esa',10)
     #
     argument_esa_model.esa_all_terms.initialize_mode()
     save_top_k_topics_per_doucment('sample','strategic-intelligence-sub-topics','esa',10)
     #
     argument_esa_model.esa_all_terms.initialize_mode()
     save_top_k_topics_per_doucment('sample','wikipedia-categories','esa',10)
     topic_ontologies= get_topic_ontologies()
     models = ['word2vec-esa-100']
     for topic_ontology in topic_ontologies:
         logging.warning("reading up %s vectors"%topic_ontology)
         for model in models:
            logging.warning("reading up %s vectors"%model)
            save_top_k_topics_per_doucment('sample-cmv',topic_ontology,model,10)

    # save_top_k_topics_per_doucment('sample','debatepedia','word2vec-esa-100',10)
    # save_top_k_topics_per_doucment('sample','strategic-intelligence','word2vec-esa-100',10)
    # save_top_k_topics_per_doucment('sample','wikipedia','word2vec-esa-100',10)
    # save_top_k_topics_per_doucment('sample','wikipedia-categories','word2vec-esa-100',10)
    # save_top_k_topics_per_doucment('sample','strategic-intelligence-sub-topics','word2vec-esa-100',10)
    # save_top_k_topics_per_doucment('sample','debatepedia','word2vec-esa-10',10)
    # save_top_k_topics_per_doucment('sample','strategic-intelligence','word2vec-esa-10',10)
    #save_top_k_topics_per_doucment('sample','wikipedia','word2vec-esa-10',10)
    # save_top_k_topics_per_doucment('sample','wikipedia-categories','word2vec-esa-10',10)
    # save_top_k_topics_per_doucment('sample','strategic-intelligence-sub-topics','word2vec-esa-10',10)

def save_all_topics_per_doucment(dataset,topic_ontology,topic_model):
    logging.warning('preprocessing %s %s' %(topic_ontology,topic_model))

    granularity = get_granularity(dataset)
    document_ids, document_vectors = load_corpus(dataset,topic_ontology,topic_model)
    logging.warning("loaded %d document vectors"%len(document_vectors))
    topics,topic_ids = load_topics_with_ids('ontology-'+topic_ontology)
    k=len(topics)
    if granularity =='document':
        path_top_k_topic_path = get_path_top_k_topics_per_document(dataset,topic_ontology,topic_model,k)
    else:
        path_top_k_topic_path = get_path_top_k_topics_per_argument(dataset,topic_ontology,topic_model,k)

    topic_label_template="top-%d-topic"
    topic_weight_label_tempate="top-%d-topic-weight"
    #initializing columns
    top_k_document_dict={}
    top_k_document_dict['document.id']=[]
    top_k_document_dict['topic.id']=[]
    top_k_document_dict['score']=[]
    for i,document_id in enumerate(document_ids):
        document_vector = document_vectors[i].copy()
        for i in range(k) :
            top_topic_index = np.argmax(document_vector)
            top_topic= topics[top_topic_index]
            top_topic_weight= document_vector[top_topic_index]
            top_topic_id=topic_ids[top_topic_index]
            document_vector[top_topic_index]=0
            top_k_document_dict['document.id'].append(document_id)
            top_k_document_dict['topic.id'].append(top_topic_id)
            top_k_document_dict['score'].append(top_topic_weight)

    df_top_k_topic=pd.DataFrame(top_k_document_dict)
    logging.warning("saving top topics for corpus %s, topic ontology %s, topic model %s into %s"%(dataset,topic_ontology,topic_model,path_top_k_topic_path))
    df_top_k_topic.to_csv(path_top_k_topic_path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",index=False)


def generate_all_top_topics_sample():
    topic_ontologies= get_topic_ontologies()
    models = ['word2vec-esa-100']
    for topic_ontology in topic_ontologies:
        logging.warning("reading up %s vectors"%topic_ontology)
        for model in models:
            logging.warning("reading up %s vectors"%model)
            save_all_topics_per_doucment('sample',topic_ontology,model)

def generate_top_topics_for_corpora_threshold(topic_ontology,topic_model,threshold):
    logging.basicConfig(filename='../logs/top_topics_corpora_threshold.log',level=logging.DEBUG)
    corpora= load_corpora_list()
    for corpus in corpora:
        if corpus=='cornell-change-my-view':
            save_top_topics_threshold(corpus,topic_ontology,topic_model,threshold)


def generate_top_topics_for_corpora(topic_ontology,topic_model,k):
    logging.basicConfig(filename='../logs/top_topics_corpora.log',level=logging.DEBUG)
    corpora= load_corpora_list()
    logging.warning("Generating topics for %s"%topic_ontology)
    logging.warning("+++++++++++++++++++++++++++++++++++++++++++++++")
    for corpus in corpora:
        logging.warning("preprocessing corpus %s, "%corpus)
        try:
            save_top_k_topics_per_doucment(corpus,topic_ontology,topic_model,k)
        except Exception as error:
            logging.warning(error)
            print(error)
            print("no vectors for %s, %s fexists!"%(topic_ontology,corpus))
            logging.warning("no vectors for %s exists!"%corpus)
        logging.warning("===============================================")

ontology = sys.argv[1]
model = sys.argv[2]
threshold= float(sys.argv[3])
#generate_top_topics_sample()
#generate_all_top_topics_sample()

generate_top_topics_for_corpora_threshold(ontology,model,threshold)