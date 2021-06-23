import pandas as pd
import matplotlib.pyplot as plt

from conf.configuration import *
def drop_no_matches(df_ground_truth_corpora):
    df_ground_truth_corpora=df_ground_truth_corpora[df_ground_truth_corpora['ontology-topic-id']!="-1"]
    df_ground_truth_corpora=df_ground_truth_corpora[df_ground_truth_corpora['ontology-topic-id']!="-2"]
    return df_ground_truth_corpora
def get_ontology_topics_count(ontology):
    path_ontology_topics=get_path_topics(ontology)
    df_ontology_topics=pd.read_csv(path_ontology_topics,sep=",")
    return df_ontology_topics.shape[0]
def show_ontology_topics_distribution(ontology):
    print(ontology)
    all_ontology_topics_count=get_ontology_topics_count("ontology-"+ontology)
    path_ground_truth_corpora=get_path_ground_truth_corpora('topic-inventory',ontology)
    df_ground_truth_corpora=pd.read_csv(path_ground_truth_corpora,sep=",",encoding="utf-8",dtype={'ontology-topic-id':str,'topic-id':str})
    df_ground_truth_corpora['corpus-topic-id']=df_ground_truth_corpora.apply(lambda record:record['corpus']+"-"+record['topic-id'],axis=1)
    print("Count of unique corpora topics:\t %d"%len(df_ground_truth_corpora['corpus-topic-id'].unique()))
    print("Count of no-matches (human):\t %d"%len(df_ground_truth_corpora[df_ground_truth_corpora['ontology-topic-id']=="-1"]))
    print("Count of no-matches (bm25):\t %d"%len(df_ground_truth_corpora[df_ground_truth_corpora['ontology-topic-id']=="-2"]))
    print("Count of annotations:\t %d"%df_ground_truth_corpora.shape[0])
    df_ground_truth_corpora=drop_no_matches(df_ground_truth_corpora)
    ontology_topics_per_corpus_topic=df_ground_truth_corpora['corpus-topic-id'].value_counts().to_frame()
    print("Count of matching annotations: \t %d"%df_ground_truth_corpora.shape[0])
    print("Count of corpora topics with matches: \t %d"%len(df_ground_truth_corpora['corpus-topic-id'].unique()))
    print("Count of all ontology topics:\t %d"%all_ontology_topics_count)
    print("Count of annotated ontology topics:\t %d"%(len(df_ground_truth_corpora['ontology-topic-id'].value_counts())))
    print("Minimum ontology topics count per corpus topic:\t %d "%ontology_topics_per_corpus_topic.min())
    print("Average ontology topics count per corpus topic:\t %.2f "%ontology_topics_per_corpus_topic.mean())
    print("Standard deviation of ontology topics count per corpus topic:\t %.2f "%ontology_topics_per_corpus_topic.std())
    print("Maximum ontology topics count per corpus topic:\t %d "%ontology_topics_per_corpus_topic.max())
    print("\n========================\n")


