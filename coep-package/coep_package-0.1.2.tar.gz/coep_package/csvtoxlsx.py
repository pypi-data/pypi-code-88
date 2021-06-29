import os
import glob
import csv
import sys
import pandas as pd
import numpy as np

def preprocessor(array):
    colnames = [
        'Question Type',
        'Answer Type',
        'Topic Number',
        'Variation',
        'Question (Text Only)',
        'Correct Answer 1',
        'Correct Answer 2',
        'Correct Answer 3',
        'Correct Answer 4',
        'Wrong Answer 1',
        'Wrong Answer 2',
        'Wrong Answer 3',
        'Time in seconds',
        'Difficulty Level',
        'Question (Image/ Audio/ Video)',
        'Contributor\'s Registered mailId',
        'Solution (Text only)',
        'Solution (Image/ Audio/ Video)'
    ]
    for path in array:
        print(path)
        df = pd.read_csv(path,header=1,names=colnames)
        df['Variation Number'] = df['Variation'].copy()
        del df['Variation']

        vc = str(df['Variation Number'].unique()[0])
        df['Variation Number'] = '0'+ vc if (vc[0] != 0 and int(vc)<10 ) else vc

        tv = str(df['Topic Number'].unique()[0])
        df['Topic Number'] = '0'+ tv if tv[0] != 0 else tv
        df.insert(0, "Sr. No", [str(i+1) for i in range(0,len(df))], True)
        df2 = pd.DataFrame([['****',None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None]], columns=df.columns)
        df = pd.concat([df, df2],ignore_index=True)
        df_empty = pd.DataFrame()
        filename = path.split('\\')[-1].split('.')[0]
        with pd.ExcelWriter(filename+'.xlsx') as writer:  
            df_empty.to_excel(writer, sheet_name='Sheet1',index=False)
            df.to_excel(writer, sheet_name=filename,index=False)
    return

def converter(fileargs=None):
    if(fileargs):
        #print(sys.argv[1:],len(sys.argv))
        #print(fileargs)
        array = [fileargs]
    else:
        #print('null')
        array = glob.glob(os.path.join('.', '*.csv'))
    preprocessor(array)
    for i in array:
        os.remove(i)

#converter()
