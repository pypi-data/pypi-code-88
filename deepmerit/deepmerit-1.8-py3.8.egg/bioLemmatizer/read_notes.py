#Code
import pandas as pd
import numpy as np
from functools import reduce
import pandas as pd
import numpy as np
from flask import request
from functools import reduce
def capitalize_after_hyphen(x):
    a=list(x)
    a[p.index('-')+1]=a[p.index('-')+1].capitalize()
    x=''.join(a)
    return ''.join(a)

 

# limit - changeable (no.of.records)
# offset - Changeable (start index)
# patients - Changeable (table name)
url1= "https://mimic.vlife.virtusa.com/v1/chart-events?limit=5&offset=0"
url2= "https://mimic.vlife.virtusa.com/v1/lab-events?limit=5&offset=0"

 

urls = [url1,url2]
d={}
for url in urls:
    p = url[(url.index('v1/')+len('v1/')):url.index('?limit')]
    if p=='dx-codes':
        p='dxCode'
    else:

 

        try:
            p=capitalize_after_hyphen(p)
        except:
            pass
        try:
            p=p[:p.index('-')]+p[p.index('-')+1:]
        except:
            pass

 

        try:
            p=capitalize_after_hyphen(p)
        except:
            pass
        try:
            p=p[:p.index('-')]+p[p.index('-')+1:]
        except:
            pass
    d['{}'.format(p)]=pd.DataFrame(requests.get(url).json()['{}'.format(p)])
    d['{}'.format(p)].to_csv('{}.csv'.format(p),encoding='utf-8', index=False)
def capitalize_after_hyphen(x):
    a=list(x)
    a[p.index('-')+1]=a[p.index('-')+1].capitalize()
    x=''.join(a)
    return ''.join(a)

 

# limit - changeable (no.of.records)
# offset - Changeable (start index)
# patients - Changeable (table name)
url1= "https://mimic.vlife.virtusa.com/v1/prescriptions?limit=1000000&offset=0"
#url2= "https://mimic.vlife.virtusa.com/v1/lab-events?limit=5&offset=0"

 

urls = [url1]
d={}
for url in urls:
    p = url[(url.index('v1/')+len('v1/')):url.index('?limit')]
    if p=='dx-codes':
        p='dxCode'
    else:

 

        try:
            p=capitalize_after_hyphen(p)
        except:
            pass
        try:
            p=p[:p.index('-')]+p[p.index('-')+1:]
        except:
            pass

 

        try:
            p=capitalize_after_hyphen(p)
        except:
            pass
        try:
            p=p[:p.index('-')]+p[p.index('-')+1:]
        except:
            pass
    d['{}'.format(p)]=pd.DataFrame(request.get(url).json()['{}'.format(p)])
    d['{}'.format(p)].to_csv('{}.csv'.format(p),encoding='utf-8', index=False)
df_notes = pd.read_csv('noteEvents.csv')
#df_notes =df_notes.sort_values('subject_id')

df_notes = df_notes[["Unnamed: 0","row_id","subject_id","hadm_id","chartdate","charttime","storetime","category","description","text"]]
df_notes =df_notes.sort_values(by=['subject_id'])
df_notes.to_csv('noteEvents_new.csv')
df_proc = pd.read_csv('procedures.csv')
df_diag = pd.read_csv('diagnoses.csv')
from sqlalchemy import create_engine
engine = create_engine("postgresql://postgres:postgres@54.88.151.77:5432/mimic")
df_notes = pd.read_sql_query("select * from noteEvents where category = 'Discharge summary' limit 5 ",con=engine)
x = df_notes.to_csv('noteEvents.csv')
import pandas as pd
import numpy as np

import re


def reformat(code, is_diag):
    """
        Put a period in the right place because the MIMIC-3 data files exclude them.
        Generally, procedure codes have dots after the first two digits, 
        while diagnosis codes have dots after the first three digits.
    """
    code = ''.join(code.split('.'))
    if is_diag:
        if code.startswith('E'):
            if len(code) > 4:
                code = code[:4] + '.' + code[4:]
        else:
            if len(code) > 3:
                code = code[:3] + '.' + code[3:]
    else:
        code = code[:2] + '.' + code[2:]
    return code

def preproc(df):
    """
    Remove '\n' and all text within brackets (and also brackets themselves)
    """
    
    df['text'] = df['text'].apply(lambda x: x.replace('\n', ' '))
    df['text'] = df['text'].apply(lambda x: re.sub("[\[].*?[\]]", "", x))
    
    return df
df_diag['ABS_CODE'] = df_diag.apply(lambda row: str(reformat(str(row[1]), True)), axis=1)
df_proc['ABS_CODE'] = df_proc.apply(lambda row: str(reformat(str(row[1]), False)), axis=1)
df_codes = pd.concat([df_diag, df_proc])
df_notes = df_notes.dropna(subset=['hadm_id'])
df_notes['subject_id'] = df_notes['subject_id'].apply(lambda x: int(x))
df_notes['hadm_id'] = df_notes['hadm_id'].apply(lambda x: int(x))

df_codes['subject_id'] = df_codes['subject_id'].apply(lambda x: int(x))
df_codes['hadm_id'] = df_codes['hadm_id'].apply(lambda x: int(x))
df_notes = preproc(df_notes)
df_notes_grouped = df_notes.groupby(by=['hadm_id','subject_id'], as_index=False).agg({'text': lambda x: ' '.join(x)})
merged = pd.merge(df_notes_grouped, df_codes, on='hadm_id', how='left')
merged = merged.dropna(subset=['ABS_CODE'])
merged.to_csv('merged.csv')
grouped = merged.groupby(by=['hadm_id', 'subject_id_x'], as_index=False).agg({'ABS_CODE': lambda x: list(x),'text': 'first'})
grouped = grouped.sort_values(['subject_id_x', 'hadm_id'])
grouped = grouped.rename(columns={'ABS_CODE': 'labels', 'subject_id_x':'subject_id'})
grouped = grouped[['subject_id', 'hadm_id', 'text', 'labels']]
grouped = grouped.reset_index(drop=True)
grouped['labels'] = grouped['labels'].apply(lambda x: ';'.join(x))
import pandas as pd
grouped = pd.read_csv("grouped.csv")
grouped = grouped[['subject_id','hadm_id','text','labels']]
remove = ['admission date:', 'discharge date:', 'date of birth:', 'service:', 'chief complaint:', 'HISTORY OF PRESENT ILLNESS:',
          'PAST MEDICAL HISTORY:', 'admission diagnosis:', 'history of the present illness:', 'attending:', 'cc:']
remove = [r.lower() for r in remove]
import re
grouped['text'] = grouped['text'].apply(lambda x: re.sub(r'|'.join(map(re.escape, remove)), '', x.lower()))
grouped['text'] = grouped['text'].apply(lambda x: x.lstrip())
grouped.to_pickle('dataframes/df_data.pkl')
df = pd.read_pickle('dataframes/df_data.pkl')
remove = ['admission date:', 'discharge date:', 'date of birth:', 'service:', 'chief complaint:', 'HISTORY OF PRESENT ILLNESS:',
          'PAST MEDICAL HISTORY:', 'admission diagnosis:', 'history of the present illness:', 'attending:', 'cc:']
import re

df['text'] = df['text'].apply(lambda x: re.sub(r'|'.join(map(re.escape, remove)), '', x.lower()))
df['text'] = df['text'].apply(lambda x: x.lstrip())
df.to_pickle('dataframes/df_v2.pkl')

def clean_text(text):
    df1=text.lower()
    import re
    result1=re.sub(r'\d+','',df1)
    import string
    result2=result1.translate(str.maketrans('', '', string.punctuation))
    result3=result2.strip()
    import nltk
    from nltk.corpus import stopwords
    stop_words=set(stopwords.words('english'))
    from nltk.tokenize import word_tokenize
    tokens=word_tokenize(result3)
    result4=[i for i in tokens if not i in stop_words]
    result5=' '.join(result4)
    import re
    result6=re.sub(r'\b\w{1,3}\b','',result5)
    return result6