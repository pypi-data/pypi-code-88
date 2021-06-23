import pandas as pd
from conf.configuration import *
import csv
from sklearn.metrics import f1_score,recall_score,precision_score
import logging
from datetime import datetime
import random
from numpy import mean
from mylogging.mylogging import *
def produce_judgements(experiment,debug=False):
    dataset=get_path_source_part(experiment,'dataset')
    ontology=get_path_source_part(experiment,'ontology')
    path_document_topics=get_path_document_topic_ontology(dataset,ontology)
    path_judgements=get_path_judgement(experiment)
    df_document_topics=pd.read_csv(path_document_topics,sep=",",encoding="utf-8",quotechar='"',dtype={'ontology-topic-id':str})
    df_document_topics=df_document_topics[~df_document_topics['ontology-topic-id'].isin(['-1','-2'])]
    df_document_topics.to_csv(path_judgements,sep=",",encoding="utf-8",quotechar='"',index=False)





def load_labels(df_document_topics):
    df_document_topics.sort_values('id',inplace=True)
    df_document_topics_agg=df_document_topics.groupby('id').agg({'ontology-topic-id':list}).reset_index()

    document_ids = df_document_topics_agg['id'].values
    topic_ids = df_document_topics_agg['ontology-topic-id'].values

    document_with_topics=list(zip(document_ids,topic_ids))

    return document_with_topics

def load_judgements(experiment):
    path_judgements=get_path_judgement(experiment)
    df_document_topics=pd.read_csv(path_judgements,sep=",",encoding="utf-8",quotechar='"',dtype={'ontology-topic-id':str})
    labels = load_labels(df_document_topics)
    return labels


def drop_documents_not_in_judgements(df_suggestions, documents_with_topics):
    df_suggestions=df_suggestions[df_suggestions['id'].isin(documents_with_topics)]
    return df_suggestions


def load_predicted_topics_top_k(dataset,ontology,model,k,documents_with_topics):

    path_top_k_results=get_path_top_k_topics_per_document(dataset,ontology,model,k)
    df_suggestions=pd.read_csv(path_top_k_results,sep=",",encoding="utf-8",quotechar='"',dtype={'ontology-topic-id':str})
    df_suggestions=drop_documents_not_in_judgements(df_suggestions,documents_with_topics)
    labels =load_labels(df_suggestions)
    return labels
def load_ontology_topics(ontology):
    path_ontology_topics=get_path_topics('ontology-'+ontology)
    df_ontology_topics=pd.read_csv(path_ontology_topics,sep=',',quotechar='"',encoding='utf-8',dtype={'id': object})
    return df_ontology_topics['id'].values


def load_predicted_topics_threshold(dataset, ontology, model, threshold, documents_with_topics):
    path_top_k_results=get_path_topics_per_document_threshold(dataset,ontology,model,threshold)
    df_suggestions=pd.read_csv(path_top_k_results,sep=",",encoding="utf-8",quotechar='"',dtype={'ontology-topic-id':str})
    df_suggestions=drop_documents_not_in_judgements(df_suggestions,documents_with_topics)
    labels =load_labels(df_suggestions)
    return labels


def run_experiment(experiment,model,configuration,configuration_value,debug):
    dataset=get_path_source_part(experiment,'dataset')
    ontology=get_path_source_part(experiment,'ontology')
    ontology_topics=load_ontology_topics(ontology)
    documents_with_true_topics=load_judgements(experiment)
    documents_with_topics=[document_topics[0] for document_topics in documents_with_true_topics]
    if configuration=="top-k":
        documents_with_predicted_topics=load_predicted_topics_top_k(dataset,ontology,model,configuration_value,documents_with_topics)
    else:
        documents_with_predicted_topics=load_predicted_topics_threshold(dataset,ontology,model,configuration_value,documents_with_topics)
    effectiveness=evaluate(documents_with_true_topics,documents_with_predicted_topics,ontology_topics,debug)
    return effectiveness

def evaluate_threshold(experiment,model,threshold,debug=False):
    dataset=get_path_source_part(experiment,'dataset')
    ontology=get_path_source_part(experiment,'ontology')
    ontology_topics=load_ontology_topics(ontology)
    documents_with_true_topics=load_judgements(experiment)
    documents_with_topics=[document_topics[0] for document_topics in documents_with_true_topics]
    documents_with_predicted_topics=load_predicted_topics_top_k(dataset,ontology,model,k,documents_with_topics)
    effectiveness=evaluate(documents_with_true_topics,documents_with_predicted_topics,ontology_topics,debug)
    return effectiveness

def generate_labels(relevant_topics,ontology_topics):
    labels=[]
    for topic in ontology_topics:
        if topic in relevant_topics:
            labels.append(True)
        else:
            labels.append(False)
    return labels

def evaluate_sklearn(relevant_topics, predicted_topics, ontology_topics,debug=False):
    all_relevant_precisions=[]
    all_relevant_recalls=[]
    all_relevant_f1s=[]

    all_unrelevant_precisions=[]
    all_unrelevant_recalls=[]
    all_unrelevant_f1s=[]

    all_precisions=[]
    all_recalls=[]
    all_f1s=[]

    for i,document_topics in enumerate(relevant_topics):

        true_labels=generate_labels(document_topics[1],ontology_topics)
        predicted_labels=generate_labels(predicted_topics[i][1],ontology_topics)
        f1=f1_score(true_labels,predicted_labels,average='macro')
        recall=recall_score(true_labels,predicted_labels,average='macro')
        precision=precision_score(true_labels,predicted_labels,average='macro')
        relevant_f1= f1_score(true_labels,predicted_labels,average="binary",pos_label=True)
        relevant_recall=recall_score(true_labels,predicted_labels,average="binary",pos_label=True)
        relevant_precision=precision_score(true_labels,predicted_labels,average="binary",pos_label=True)

        unrelevant_f1= f1_score(true_labels,predicted_labels,average="binary",pos_label=False)
        unrelevant_recall=recall_score(true_labels,predicted_labels,average="binary",pos_label=False)
        unrelevant_precision=precision_score(true_labels,predicted_labels,average="binary",pos_label=False)

        all_recalls.append(recall)
        all_precisions.append(precision)
        all_f1s.append(f1)

        all_relevant_precisions.append(relevant_precision)
        all_relevant_recalls.append(relevant_recall)
        all_relevant_f1s.append(relevant_f1)

        all_unrelevant_precisions.append(unrelevant_precision)
        all_unrelevant_recalls.append(unrelevant_recall)
        all_unrelevant_f1s.append(unrelevant_f1)

    overall_f1=mean(all_f1s)
    overall_recall=mean(all_recalls)
    overall_precision=mean(all_precisions)

    overall_relevant_f1=mean(all_relevant_f1s)
    overall_relevant_precision=mean(all_relevant_precisions)
    overall_relevant_recall=mean(all_relevant_recalls)

    overall_unrelevant_f1=mean(all_unrelevant_f1s)
    overall_unrelevant_precision=mean(all_unrelevant_precisions)
    overall_unrelevant_recall=mean(all_unrelevant_recalls)

    return {'f1':overall_f1,'recall':overall_recall,'precision':overall_precision,
            'relevant-f1':overall_relevant_f1,'relevant-recall':overall_relevant_recall,'relevant-precision':overall_relevant_precision,
            'unrelevant-recall':overall_unrelevant_recall,'unrelevant-precision':overall_unrelevant_precision,'unrelevant-f1':overall_unrelevant_f1
            }

def evaluate(relevant_topics, predicted_topics, ontology_topics,debug=False):
    #true_labels=[(1,[1,2,3,4]),(2,[4,5,6,3]),...,]
    #predicted_labels=[(1,[
    ontology_topics_set=set(ontology_topics)

    all_relevant_precisions=[]
    all_relevant_recalls=[]
    all_relevant_f1s=[]

    all_unrelevant_precisions=[]
    all_unrelevant_recalls=[]
    all_unrelevant_f1s=[]

    all_precisions=[]
    all_recalls=[]
    all_f1s=[]
    size=len(list(relevant_topics))

    for i,document_topics in enumerate(relevant_topics):
        log_status(i,size,debug)
        relevant_topics_set=set(document_topics[1])
        unrelevant_topics_set=ontology_topics_set.difference(relevant_topics_set)
        predicted_topics_set=set(predicted_topics[i][1])
        unpredicted_topics_set=ontology_topics_set.difference(predicted_topics_set)
        if document_topics[0]!=predicted_topics[i][0]:
            raise ValueError("mismtach")

        true_positives = relevant_topics_set.intersection(predicted_topics_set)
        true_negatives = unrelevant_topics_set.intersection(unpredicted_topics_set)
        if len(predicted_topics_set)==0:
            relevant_precision=0
        else:
            relevant_precision= len(true_positives)/float(len(predicted_topics_set))
        if len(relevant_topics_set)==0:
            relevant_recall=0
        else:
            relevant_recall= len(true_positives)/float(len(relevant_topics_set))

        if relevant_recall==0 and relevant_precision ==0:
            relevant_f1=0
        else:
            relevant_f1=2*relevant_precision*relevant_recall/(relevant_precision+relevant_recall)


        unrelevant_precision=len(true_negatives)/float(len(unpredicted_topics_set))
        unrelevant_recall=len(true_negatives)/float(len(unrelevant_topics_set))
        unrelevant_f1=2*unrelevant_precision*unrelevant_recall/(unrelevant_precision+unrelevant_recall)

        f1=(relevant_f1+unrelevant_f1)/2.0
        recall=(relevant_recall+unrelevant_recall)/2.0
        precision=(relevant_precision+unrelevant_precision)/2.0

        all_recalls.append(recall)
        all_precisions.append(precision)
        all_f1s.append(f1)

        all_relevant_precisions.append(relevant_precision)
        all_relevant_recalls.append(relevant_recall)
        all_relevant_f1s.append(relevant_f1)

        all_unrelevant_precisions.append(unrelevant_precision)
        all_unrelevant_recalls.append(unrelevant_recall)
        all_unrelevant_f1s.append(unrelevant_f1)

    overall_f1=mean(all_f1s)
    overall_recall=mean(all_recalls)
    overall_precision=mean(all_precisions)

    overall_relevant_f1=mean(all_relevant_f1s)
    overall_relevant_precision=mean(all_relevant_precisions)
    overall_relevant_recall=mean(all_relevant_recalls)

    overall_unrelevant_f1=mean(all_unrelevant_f1s)
    overall_unrelevant_precision=mean(all_unrelevant_precisions)
    overall_unrelevant_recall=mean(all_unrelevant_recalls)

    return {'f1':overall_f1,'recall':overall_recall,'precision':overall_precision,
            'relevant-f1':overall_relevant_f1,'relevant-recall':overall_relevant_recall,'relevant-precision':overall_relevant_precision,
            'unrelevant-recall':overall_unrelevant_recall,'unrelevant-precision':overall_unrelevant_precision,'unrelevant-f1':overall_unrelevant_f1
            }

def run_experiments(experiment,model,k_s,thresholds,debug=False):
    # code logging
    path_evalaution=get_path_evaluation_model(experiment,model)
    precisions=[]
    recalls=[]
    f1_scores=[]
    true_precisions=[]
    true_recalls=[]
    true_f1_scores=[]
    false_precisions=[]
    false_recalls=[]
    false_f1_scores=[]
    for k in k_s:
        log("running %s for top-%d"%(experiment,k))
        effectiveness=run_experiment(experiment,model,'top-k',k,debug)
        precisions.append(effectiveness['precision'])
        recalls.append(effectiveness['recall'])
        f1_scores.append(effectiveness['f1'])
        true_precisions.append(effectiveness['relevant-precision'])
        true_recalls.append(effectiveness['relevant-recall'])
        true_f1_scores.append(effectiveness['relevant-f1'])
        false_recalls.append(effectiveness['unrelevant-recall'])
        false_precisions.append(effectiveness['unrelevant-precision'])
        false_f1_scores.append(effectiveness['unrelevant-f1'])
    for threshold in thresholds:
        log("running %s for threshold %2.2f}"%(experiment,threshold))
        effectiveness=evaluate_threshold(experiment,model,'threshold',threshold,debug)
        precisions.append(effectiveness['precision'])
        recalls.append(effectiveness['recall'])
        f1_scores.append(effectiveness['f1'])
        true_precisions.append(effectiveness['relevant-precision'])
        true_recalls.append(effectiveness['relevant-recall'])
        true_f1_scores.append(effectiveness['relevant-f1'])
        false_recalls.append(effectiveness['unrelevant-recall'])
        false_precisions.append(effectiveness['unrelevant-precision'])
        false_f1_scores.append(effectiveness['unrelevant-f1'])

    configurations= ["top-k-%d"%k for k in k_s]
    configurations.extend(["threshold-%f"%threshold for threshold in thresholds])

    df_evaluation=pd.DataFrame({'configuration':configurations,'precision':precisions,'recall':recalls,'f1':f1_scores,'relevant-precision':true_precisions,'relevant-recall':true_recalls,'relevant-f1':true_f1_scores
                                ,'unrelevant-precision':false_precisions,'unrelevant-recall':false_recalls,'unrelevant-f1':false_f1_scores
                                })
    df_evaluation.to_csv(path_evalaution,sep=",",encoding="utf-8",columns=['k','precision','recall','f1','relevant-precision','relevant-recall','relevant-f1',
                                                                           'unrelevant-precision','unrelevant-recall','unrelevant-f1'
                                                                           ],index=False)

