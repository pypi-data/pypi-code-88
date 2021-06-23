import pandas as pd
from conf.configuration import *

def produce_topic_coverage_unit(dataset, ontology):
    path_topics=get_path_topics('ontology-'+ontology)
    path_topic_coverage_document=get_path_topic_coverage_document(dataset,ontology)
    path_best_topics=get_path_best_topics_per_document(dataset,ontology)
    path_hashmap = get_path_hashmap('argument-inventory','document-id','id')
    df_topics=pd.read_csv(path_topics,sep=",",encoding='utf-8',dtype={'id':str})
    df_topics.rename(columns={'name':'topic','id':'topic.id'},inplace=True)


    df_argument_inventory_hash= pd.read_csv(path_hashmap,sep=",",encoding="utf-8",quotechar='"')
    df_corpora_size=df_argument_inventory_hash.groupby('corpus').agg({'document-id':'count'}).reset_index()
    df_corpora_size.rename(columns={'document-id':'corpus-size'},inplace=True)
    df_best_topics=pd.read_csv(path_best_topics,sep=",",encoding="utf-8",dtype={'topic.id':str})

    df_best_topics.rename(columns={'document.id':'id'},inplace=True)

    df_best_topics=df_best_topics.merge(df_argument_inventory_hash,on='id')
    all_frames=[]
    for corpus, documents_per_corpus in df_best_topics.groupby('corpus'):
        df_corpus_coverage=documents_per_corpus.groupby('topic.id').agg({'id':'count'}).reset_index()
        df_corpus_coverage['corpus']=corpus
        all_frames.append(df_corpus_coverage)

    df_corpora_coverage=pd.concat(all_frames)
    df_corpora_coverage.rename(columns={'id':'matched-topics'},inplace=True)
    df_corpora_coverage=df_corpora_coverage.merge(df_corpora_size,on='corpus')
    df_corpora_coverage['matched-topics-relative']=df_corpora_coverage.apply(lambda topic_record:topic_record['matched-topics']/float(topic_record['corpus-size']),axis=1)

    df_corpora_coverage=df_corpora_coverage.merge(df_topics,on='topic.id')
    df_corpora_coverage.to_csv(path_topic_coverage_document,sep=",",encoding='utf-8',index=False,columns=['corpus','topic','matched-topics','matched-topics-relative'])


def produce_topic_coverage_corpus_label(dataset, ontology):
    path_topics=get_path_topics('ontology-'+ontology)
    path_topic_coverage_corpus_label=get_path_topic_coverage_corpus_topic(dataset,ontology)
    path_ground_truth_corpora=get_path_ground_truth_corpora(dataset,ontology)

    df_topics=pd.read_csv(path_topics,sep=",",encoding='utf-8',dtype={'id':str})
    df_topics.rename(columns={'name':'topic','id':'ontology-topic-id'},inplace=True)
    df_ground_truth_topics=pd.read_csv(path_ground_truth_corpora,sep=",",encoding="utf-8",dtype={'ontology-topic-id':str})


    df_corpora_size=df_ground_truth_topics.groupby('corpus').agg({'topic-id':'nunique'}).reset_index()
    df_corpora_size.rename(columns={'topic-id':'corpus-size'},inplace=True)
    df_corpora_size.to_csv('/home/yamenajjour/Dropbox/tasks/daily-tasks/01-02-2021/corpora-size.csv',sep=",",encoding="utf-8")



    all_frames=[]
    for corpus, topic_per_corpus in df_ground_truth_topics.groupby('corpus'):
        df_corpus_coverage=topic_per_corpus.groupby('ontology-topic-id').agg({'topic-id':'nunique'}).reset_index()
        df_corpus_coverage['corpus']=corpus
        all_frames.append(df_corpus_coverage)

    df_corpora_coverage=pd.concat(all_frames)
    df_corpora_coverage.rename(columns={'topic-id':'matched-topics'},inplace=True)
    df_corpora_coverage=df_corpora_coverage.merge(df_corpora_size,on='corpus')
    df_corpora_coverage['matched-topics-relative']=df_corpora_coverage.apply(lambda topic_record:topic_record['matched-topics']/float(topic_record['corpus-size']),axis=1)

    df_corpora_coverage=df_corpora_coverage.merge(df_topics,on='ontology-topic-id')
    df_corpora_coverage.to_csv(path_topic_coverage_corpus_label,sep=",",encoding='utf-8',index=False,columns=['corpus','topic','matched-topics','matched-topics-relative'])


