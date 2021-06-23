import pandas as pd
from conf.configuration import *
import logging
import sparkpickle
import os
from mylogging.mylogging import *
def parts_text(dataset, separator=","):
    part_count_dateset= get_part_count(dataset)
    log("iterating over the parts of %s"%dataset)
    for part in range(part_count_dateset):
        path=get_path_preprocessed_documents_version(dataset,str(part))
        df_part=pd.read_csv(path,sep=separator,quotechar='"',encoding="utf-8")
        log("text part %d is read"%part)
        yield df_part

def parse_pickle(path,debug=False):
    with open(path,'rb') as file:
        log("reading %s"%path)
        document_ids= sparkpickle.load(file)
        return document_ids

def parts_vectors(dataset,ontology,model,debug=False):
    part_count_dateset= get_part_count(dataset)
    log("iterating over the parts of %s"%dataset)
    for part in range(part_count_dateset):
        part_path=get_path_document_vectors_part(dataset,ontology,model,part)
        files = os.listdir(part_path)
        for file in files:
            if file.startswith('part'):
                file_path = os.path.join(part_path,file)
                document_ids=parse_pickle(file_path,debug)
                log("vectors part %d is read with size %d"%(part,len(document_ids)))
                yield document_ids


