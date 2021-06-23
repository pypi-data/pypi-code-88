#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import ftfy


# In[2]:


# cleans/standardize the column names - helps with things like CoName, Co_Name, coName
# remove gibberish and covert back to correct data  in selected column data 
# remove leading and trailing punc in selected column data 

def load_files(File, *argv):       
	
    File_fd = open(File, "r", encoding = "utf8", errors = 'ignore')

    File_pd = pd.read_csv(File_fd, sep = ",", skipinitialspace = True, keep_default_na = False ,header="infer") 
    
    File_pd.columns = ["".join(e for e in x if e.isalnum()).upper() for x in File_pd.columns]
    argv = ["".join(e for e in x if e.isalnum()).upper() for x in argv]  #have to standardize as the line abv, else cant find

#   not entirely sure if the normalization and encoding / decoding is required. leaving it for now
    for arg in argv :
        arg_adj = arg + "_adj"
        File_pd[arg_adj] = File_pd[arg].copy()

        File_pd[arg_adj].apply(ftfy.fix_text).str.normalize('NFKC').str.encode('ascii',errors='ignore').str.decode("utf-8")
        File_pd[arg_adj] = File_pd[arg_adj].str.upper()
        File_pd[arg_adj] = File_pd[arg_adj].str.split().str.join(" ") #removes additional spaces/whitespaces between words 
        File_pd[arg_adj] = File_pd[arg_adj].apply(lambda x : "".join(e for e in x if (e.isalnum() or e.isspace())))  # removes all punc in the entire data and only keeps alphanumeric and space
    File_fd.close()
    
    return File_pd
