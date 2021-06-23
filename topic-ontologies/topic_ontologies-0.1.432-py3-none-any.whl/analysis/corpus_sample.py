import pandas as pd
from conf.configuration import *
import csv
def load_dataset(dataset,level='document'):
    if level=='argument':
        path = get_path_preprocessed_arguments(dataset)
        df_arguments = pd.read_csv(path,quotechar='"',sep="|",quoting=csv.QUOTE_ALL,encoding='utf-8')
        return df_arguments
    else:
        path = get_path_preprocessed_documents(dataset)
        df_documents = pd.read_csv(path,quotechar='"',sep="|",quoting=csv.QUOTE_ALL,encoding='utf-8')
        return df_documents

def sample_dataset(dataset,level,n):
    df_dataset = load_dataset(dataset,level)
    sampled_df = df_dataset.sample(n=n)
    return sampled_df



def create_sample_of_all_corpora(path,n):

    corpora = load_corpora_list('left-sample-corpora')
    samples= []
    corpora_sample=None
    for corpus in corpora:
        granularity= get_granularity(corpus)
        if granularity =='document':
            sampled= sample_dataset(corpus,'document',n)
            print(corpus)
        else:
            print(corpus)
            sampled = sample_dataset(corpus,'argument',n)
            sampled['document']=sampled['argument']
            sampled['document-id']=sampled['argument-id']
            del sampled['argument']
            del sampled['argument-id']
        sampled['corpus'] = [corpus for i in range(n)]
        samples.append(sampled)
    corpora_sample = pd.concat(samples)
    corpora_sample.to_csv(path,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding='utf-8',index=False)

#path=get_source_subset_path('sample','left')
#create_sample_of_all_corpora(path,5)

path_sample_change_my_view = get_path_source_part('sample', 'cornell-change-my-view')
create_sample_of_all_corpora(path_sample_change_my_view,5)
def concatenate_with_left():
    path_sample_left = get_path_source_part('sample', 'left')
    path_sample_original= get_path_source_part('sample', 'original')
    df_left= pd.read_csv(path_sample_left,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding='utf-8')
    df_sample_original =pd.read_csv(path_sample_original,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding='utf-8')
    df_all=pd.concat([df_left, df_sample_original])
    path_new = get_path_source('sample')
    df_all.to_csv(path_new,quotechar='"',sep=",",quoting=csv.QUOTE_ALL,encoding='utf-8',index=False)

#concatenate_with_left()
