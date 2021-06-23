import pandas as pd
import matplotlib.pyplot as plt
from docutils.nodes import thead

from conf.configuration import *
import numpy as np
import csv
from topic_modeling.topics import *
import sys

def get_top_topics_for(dataset, topic_ontology, topic_model, threshold=None):
    granularity = get_granularity(dataset)
    if threshold!=None:

        if granularity =='document':
            path_top_k_topic_path = get_path_topics_per_document_threshold(dataset,topic_ontology,topic_model,threshold)
        else:
            path_top_k_topic_path = get_path_topics_per_argument_threshold(dataset,topic_ontology,topic_model,threshold)

        df_topics = pd.read_csv(path_top_k_topic_path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",dtype={'topic.id':object})
    else:
        if granularity =='document':
            path_top_k_topic_path = get_path_top_k_topics_per_document(dataset,topic_ontology,topic_model,1)
        else:
            path_top_k_topic_path = get_path_top_k_topics_per_argument(dataset,topic_ontology,topic_model,1)
        df_topics = pd.read_csv(path_top_k_topic_path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding="utf-8",dtype={'topic.id':object})

    #TODO possible bug of counting documents. Probabliy document ids are not unique
    df_topic_per_document= df_topics.groupby('topic.id').agg({'document.id':pd.Series.nunique}).rename(columns={'document.id':"document.count"}).reset_index()




    topics =list(df_topic_per_document['topic.id'])
    documents_count=list(df_topic_per_document['document.count'])
    return {topic_id:documents_count[index]for index,topic_id in enumerate(topics)}

def get_top_topics_for_all_corpora(topic_ontology,topic_model,threshold=None):

    corpora = load_corpora_list()

    corpora_entries=[]
    topics=[]
    document_counts=[]

    ontology_topics,ontology_topic_ids= load_topics_with_ids('ontology-'+topic_ontology)
    for corpus in corpora:
        print(corpus)
        try:
            topics_with_document_count= get_top_topics_for(corpus, topic_ontology, topic_model, threshold)
            for topic_id in ontology_topic_ids:
                topics.append(topic_id)
                if topic_id in topics_with_document_count:
                    document_counts.append(topics_with_document_count[topic_id])
                else:
                    document_counts.append(0.0)
                corpora_entries.append(corpus)

        except Exception as error:
            print( error)
            print("%s Nope!" %corpus)

    return corpora_entries,topics,document_counts


def save_top_topics_with_document_counts(topic_ontology, topic_model,threshold=None):
    if threshold!=None:

        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-threshold'%(topic_ontology,topic_model))
        corpora,topic_ids,document_counts= get_top_topics_for_all_corpora(topic_ontology,topic_model,threshold)
    else:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s'%(topic_ontology,topic_model))
        corpora,topic_ids,document_counts= get_top_topics_for_all_corpora(topic_ontology,topic_model)

    df_corpora=pd.DataFrame({'corpus':corpora,"topic.id":topic_ids,"document.count":document_counts})
    df_corpora.to_csv(path_histogram,encoding='utf-8',sep=',')

def load_top_topics_with_document_counts(topic_ontology, topic_model,threshold=None):
    if threshold!=None:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-threshold'%(topic_ontology,topic_model))
        df_top_topics_with_document_counts = pd.read_csv(path_histogram,encoding='utf-8',sep=',',dtype={'topic.id':str})
    else:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s'%(topic_ontology,topic_model))
        df_top_topics_with_document_counts = pd.read_csv(path_histogram,encoding='utf-8',sep=',',dtype={'topic.id':str})
    return df_top_topics_with_document_counts

def load_topic_map(ontology):
    topic_map={}
    topics,topic_ids= load_topics_with_ids('ontology-'+ontology)

    for topic_id,topic in zip(topic_ids,topics):
        topic_map[str(topic_id)]=topic
    return topic_map

def visualize_top_topics_bar_diagram(topic_ontology, topic_model,threshold=None):
    df_top_topics_with_document_counts= load_top_topics_with_document_counts(topic_ontology,topic_model,threshold)
    df_top_topics_with_document_counts=df_top_topics_with_document_counts.groupby('topic.id').agg({'document.count':sum}).reset_index()
    topic_map=load_topic_map(topic_ontology)
    df_top_topics_with_document_counts=df_top_topics_with_document_counts.sort_values('document.count',ascending=False)
    #df_top_topics_with_document_counts=df_top_topics_with_document_counts[df_top_topics_with_document_counts['document.count']>100 ]
    topics = [topic_map[topic_id] for topic_id in list(df_top_topics_with_document_counts['topic.id'])]
    document_counts = df_top_topics_with_document_counts['document.count'].astype(int).values
    if threshold!=None:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-threshold-agg-by-topic'%(topic_ontology,topic_model))
    else:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-agg-by-topic'%(topic_ontology,topic_model))
    print(topics)
    print(document_counts)
    df_documents_over_topics_all_corpora=pd.DataFrame({'topic.id':df_top_topics_with_document_counts['topic.id'],'topic':topics,'document.count':document_counts})
    df_documents_over_topics_all_corpora.to_csv(path_histogram,sep=",",encoding='utf-8')
    if threshold!=None:
        path_figure_histogram = get_path_figure_histogram_two_parameters('ontology-' + topic_ontology, 'document-count', '%s-%s-threshold-agg-by-topic' % (topic_ontology, topic_model))
    else:
        path_figure_histogram = get_path_figure_histogram_two_parameters('ontology-' + topic_ontology, 'document-count', '%s-%s-agg-by-topic' % (topic_ontology, topic_model))
    fig, ax = plt.subplots(figsize=(120, 20))
    plt.xticks(rotation=90)
    plt.bar(topics,document_counts)
    fig.savefig(path_figure_histogram)

def visualize_top_topics_plot(topic_ontology, topic_model,threshold):
    df_top_topics_with_document_counts= load_top_topics_with_document_counts(topic_ontology,topic_model,threshold)
    df_top_topics_with_document_counts=df_top_topics_with_document_counts.groupby('topic.id').agg({'document.count':sum}).reset_index()
    topic_map=load_topic_map(topic_ontology)
    df_top_topics_with_document_counts=df_top_topics_with_document_counts.sort_values('document.count',ascending=False)
    #df_top_topics_with_document_counts=df_top_topics_with_document_counts[df_top_topics_with_document_counts['document.count']>100 ]
    topics = [topic_map[topic_id] for topic_id in list(df_top_topics_with_document_counts['topic.id'])]
    document_counts = df_top_topics_with_document_counts['document.count'].astype(int).values
    if threshold!=None:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-threshold-agg-by-topic'%(topic_ontology,topic_model))
    else:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-agg-by-topic'%(topic_ontology,topic_model))
    print(topics)
    print(document_counts)
    df_documents_over_topics_all_corpora=pd.DataFrame({'topic.id':df_top_topics_with_document_counts['topic.id'],'topic':topics,'document.count':document_counts})
    df_documents_over_topics_all_corpora.to_csv(path_histogram,sep=",",encoding='utf-8')
    if threshold!=None:
        path_figure_plot = get_path_figure_plot_two_parameters('ontology-' + topic_ontology, 'document-count', '%s-%s-threshold-agg-by-topic' % (topic_ontology, topic_model))
    else:
        path_figure_plot = get_path_figure_plot_two_parameters('ontology-' + topic_ontology, 'document-count', '%s-%s-agg-by-topic' % (topic_ontology, topic_model))


    fig, ax = plt.subplots(figsize=(40, 20))
    plt.xticks(rotation=90)
    plt.plot(topics,document_counts)
    fig.savefig(path_figure_plot)


def visualize_interactive_heat_map_threshold(topic_ontology, topic_model, threshold):
    #Dataframe <-read.csv("/mnt/ceph/storage/data-in-progress/topic-ontologies/topic-ontologies/ontoglies/wikipedia/document-over-wikipedia-esa-threshold-hisotgram.csvspread")
    # rownames(dataframe) <- dataframe$corpus
    #heatmaply(dataframe,color = c("white","black"),file="/home/yamenajjour/overleaf/coling20-topic-ontologies-for-argumentation/coling20-topic-ontologies-for-argumentation-data/heatmap.html")
    if threshold!=None:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s-threshold'%(topic_ontology,topic_model))
    else:
        path_histogram = get_path_histogram_two_parameters('ontology-'+topic_ontology,'document-count','%s-%s'%(topic_ontology,topic_model))

    df = pd.read_csv(path_histogram,encoding='utf-8',sep=',',dtype={'topic.id':object})
    def load_topic_map(ontology):
        topic_map={}
        topics,topic_ids= load_topics_with_ids('ontology-'+ontology)

        for topic_id,topic in zip(topic_ids,topics):
            topic_map[str(topic_id)]=topic
        return topic_map
    df = df.pivot(index='corpus',columns='topic.id',values='document.count')
    df=df.reset_index()
    topic_map=load_topic_map('debatepedia')
    print(df.info())
    df=df.set_index('corpus')
    df.rename(columns=topic_map,inplace=True)
    df_sum=df.sum(axis=1)
    df_normalized=df.div(df_sum,axis=0)
    df_normalized=df_normalized.mul(100)
    df_normalized.to_csv(path_histogram+"spread",sep=",",encoding="utf-8")

#save_top_topics_with_document_counts('debatepedia', 'esa')
#save_top_topics_with_document_counts('strategic-intelligence', 'esa')
#save_top_topics_with_document_counts('wikipedia', 'esa')

#visualize_top_topics_bar_diagram('strategic-intelligence','esa')
#visualize_top_topics_bar_diagram('debatepedia','esa')
#visualize_top_topics_bar_diagram('wikipedia','esa')

ontology = sys.argv[1]
model = sys.argv[2]
threshold= float(sys.argv[3])

save_top_topics_with_document_counts(ontology, model,threshold)
visualize_top_topics_bar_diagram(ontology,model,threshold)
visualize_top_topics_plot(ontology,model,threshold)

