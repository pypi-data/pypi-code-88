from topic_modeling.topics import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
def load_corpus_vectors(dataset,topic_ontology,topic_model,is_argument_corpus):

    if is_argument_corpus:
        path_topic_vectors = get_path_argument_vectors(dataset,topic_ontology,topic_model)
    else:
        path_topic_vectors = get_path_document_vectors(dataset,topic_ontology,topic_model)
    vectors_df = pd.read_pickle(path_topic_vectors)
    if is_argument_corpus:
        corpora_vectors = list(vectors_df['argument-vector'])
    else:
        corpora_vectors = list(vectors_df['document-vector'])
    sum=np.zeros(len(corpora_vectors[0]))
    for vector in corpora_vectors:
        sum = sum + vector
    vector_norm = np.sum(sum)
    normalized_vector = sum/vector_norm
    return normalized_vector

def get_top_topics(corpus_vector,num):
    top_ten_threshold = sorted(corpus_vector,)[-num]
    filtered_topic_vector = []
    for topic_weight in corpus_vector:
        if topic_weight< top_ten_threshold:
            filtered_topic_vector.append(0)
        else:
            filtered_topic_vector.append(topic_weight)
    return filtered_topic_vector

def load_corpora_with_vectors_for_visualization(topic_ontology,topic_model):
    argument_corpora= ['args-me','ibm-debater-evidence-sentences','ukp-ukpconvarg-v1','ukp-ukpconvarg-v2','ibm-debater-evidence-quality']
    corpora = load_corpora_list()
    corpora_vectors= []
    for corpus in tqdm(corpora):
        print(corpus)
        if corpus in argument_corpora:
            corpora_vectors.append(load_corpus_vectors(corpus,topic_ontology,topic_model,True))
        else:
            corpora_vectors.append(load_corpus_vectors(corpus,topic_ontology,topic_model,False))

    corpora_vectors_np = np.array(corpora_vectors)
    return corpora,corpora_vectors_np

def load_corpora_with_vectors(topic_ontology,topic_model):
    argument_corpora= ['args-me','ibm-debater-evidence-sentences','ukp-ukpconvarg-v1','ukp-ukpconvarg-v2','ibm-debater-evidence-quality']
    corpora = load_corpora_list()
    topics = load_topics('ontology-'+topic_ontology)
    corpora_vectors= []
    corpora_topic_weights = {}
    for corpus in tqdm.tqdm(corpora):
        if corpus in argument_corpora:
            corpora_vectors.append(load_corpus_vectors(corpus,topic_ontology,topic_model,True))
        else:
            corpora_vectors.append(load_corpus_vectors(corpus,topic_ontology,topic_model,False))

    filtered_corpora_vectors = [get_top_topics(corpus_vector,20) for corpus_vector in corpora_vectors]
    for topic_index,topic in enumerate(topics):
        corpora_topic_weights[topic]=[]
        for corpus_index,corpus in enumerate(corpora):
            corpora_topic_weights[topic].append(filtered_corpora_vectors[corpus_index][topic_index])
    corpora_topic_weights['corpus']=corpora
    return corpora,corpora_topic_weights


def save_corpora_vectors(topic_ontology,topic_model):
    path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s'%(topic_ontology,topic_model))
    corpora,filtered_corpora_vectors= load_corpora_with_vectors(topic_ontology,topic_model)
    df_corpora=pd.DataFrame(filtered_corpora_vectors)
    df_corpora.to_csv(path_histogram,encoding='utf-8',sep=',')


def visualize_horizontal_bar_chart(topic_ontology,topic_model):
    path_horizontal_path_histograms = get_path_figure_histogram_two_parameters('ontology-' + topic_ontology, 'document-count', '%s-%s' % (topic_ontology, topic_model))

    topics = load_topics('ontology-'+topic_ontology)
    corpora,corpora_vectors= load_corpora_with_vectors_for_visualization(topic_ontology,topic_model)

    fig, ax = plt.subplots(figsize=(40, 20))
    ax.set_xticks(np.arange(len(topics)))
    ax.set_yticks(np.arange(len(corpora)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(topics)
    ax.set_yticklabels(corpora)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")


    im = ax.imshow(corpora_vectors,cmap="YlGn",)
    fig.tight_layout()
    fig.savefig(path_horizontal_path_histograms)



visualize_horizontal_bar_chart('strategic-intelligence','esa')