import pandas as pd
import string
import numpy as np
import pkg_resources
import seaborn as sns
from PIL import Image
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pdfminer.high_level import extract_text
from tqdm import tqdm
import os

class wording:
    
    def __init__(self):
        self.resource_package = __name__
        self.file = '/'.join(('config', 'lematizer.csv'))
        self.file_path = pkg_resources.resource_filename(self.resource_package, self.file)
        self.df_lema = self.load_lema()
        
        self.file = '/'.join(('config', 'stopwords.csv'))
        self.file_path = pkg_resources.resource_filename(self.resource_package, self.file)
        self.df_stopwords = self.load_stopwords()
        
        self.file = '/'.join(('config', 'positive.csv'))
        self.file_path = pkg_resources.resource_filename(self.resource_package, self.file)
        self.positive_words = self.load_positive_words()
        
        self.file = '/'.join(('config', 'negative.csv'))
        self.file_path = pkg_resources.resource_filename(self.resource_package, self.file)
        self.negative_words = self.load_negative_words()

        self.file_cw = '/'.join(('config', 'class_words.csv'))
        self.file_path_cw = pkg_resources.resource_filename(self.resource_package, self.file_cw)
        self.df_wc = self.load_class_words()

        self.file_nomes = '/'.join(('config', 'nomes.csv'))
        self.file_path_nomes = pkg_resources.resource_filename(self.resource_package, self.file_nomes)
        self.nomes_pessoas = self.load_nomes()

        self.file_cidades = '/'.join(('config', 'cidades.csv'))
        self.file_path_cidades = pkg_resources.resource_filename(self.resource_package, self.file_cidades)
        self.cidades = self.load_cidades()

        self.file_estados = '/'.join(('config', 'estados.csv'))
        self.file_path_estados = pkg_resources.resource_filename(self.resource_package, self.file_estados)
        self.estados = self.load_estados()
        
        self.tfidf = pd.DataFrame()
        self.colection = pd.DataFrame()
        
    def load_file(self, file='none', type='txt', header=False, sep=',', column='None'):
        if file == 'none':
            raise ValueError('No Filename was provided, need one')
        
        if type == 'excel':
            df = pd.read_excel(file)
            if column != 'None':
                df = df[column]
                df.rename(column={column: 'word'}, inplace=True)
            else:
                raise TypeError("An xlsx file column was not selected")

        if type == 'csv':
            if header:
                header=0
            else:
                header=None
            df = pd.read_csv(file, header=header, sep=sep)
            if column != 'None':
                df = pd.DataFrame({'word': df[column]})
            else:
                raise TypeError("An csv file column was not selected")
           
        if type == 'txt':
            f = open(file, "r", encoding='utf8', errors='ignore')
            df = f.read()
            df = pd.DataFrame(df.split('\n'))
            df.columns = ['word']
        
        if type == 'pdf'    :
            df = self.load_pdf(file)
            df = pd.DataFrame([df])
            df.columns = ['word']
        
        self.colection = df.copy()
        
    def load_lema(self):
        df_lema = pd.read_csv(self.file_path, sep=',')
        df_lema.columns = ['word','lema']
        return(df_lema)

    def load_positive_words(self):
        df_pw = pd.read_csv(self.file_path)
        df_pw.columns = ['word']
        return(df_pw)

    def load_negative_words(self):
        df_pw = pd.read_csv(self.file_path)
        df_pw.columns = ['word']
        return(df_pw)
    
    def load_stopwords(self):
        df_sw = pd.read_csv(self.file_path, sep=';', header=None)
        df_sw.columns = ['stopword']
        return(df_sw)
    
    def load_nomes(self):
        df_nome = pd.read_csv(self.file_path_nomes, sep=';')
        return(df_nome)
    
    def load_cidades(self):
        df_cidades = pd.read_csv(self.file_path_cidades, sep=';')
        return(df_cidades)    
    
    def load_estados(self):
        df_estados = pd.read_csv(self.file_path_estados, sep=';')
        return(df_estados)
    
    def del_stopwords(self, text, stopwords=True):
        output = list()
        text = self.del_punck(text)
        text = text.lower()
        for word in text.split(' '):
            if stopwords:
                if len(word) > 3:
                    result = ''.join([str(x) for x in self.df_stopwords[self.df_stopwords['stopword'] == word]['stopword']])
                    if len(result) == 0:
                        output.append(word)
            else:
                output.append(word)
        return(output)
    
    def del_punck(self, text):
        punck = ",.;/<>:?[]{}+_)(*&$#@!)1234567890\n\t\r"
        for c in punck:
            text = text.replace(c,'')
        text = text.replace('&quot', '')
        return(text)
    
    def get_lema(self, text, lemmatizer=True):
        output = list()
        for word in text:
            if lemmatizer:
                w_lema = ''.join([self.df_lema[self.df_lema['lema'] == word]['word'].unique()][0])
                if len(w_lema) == 0:
                    output.append(word)
                else:
                    output.append(w_lema)
            else:
                output.append(word)
        return(output)
    
    def build_tf(self, df, stopwords=True, lemmatizer=True, silence=False):
        frame_tfidf = pd.DataFrame()
        if silence:
            for i in range(df.shape[0]):
                frame_aux = pd.DataFrame()
                line = ''.join(df.loc[i])
                text = self.del_stopwords(line, stopwords=stopwords)
                text = self.get_lema(text, lemmatizer=lemmatizer)
                frame_aux['word'] = text
                frame_aux['doc'] = 'doc-' + str(i)
                frame_tfidf = frame_tfidf.append(frame_aux)
        else:
            for i in tqdm(range(df.shape[0])):
                frame_aux = pd.DataFrame()
                line = ''.join(df.loc[i])
                text = self.del_stopwords(line, stopwords=stopwords)
                text = self.get_lema(text, lemmatizer=lemmatizer)
                frame_aux['word'] = text
                frame_aux['doc'] = 'doc-' + str(i)
                frame_tfidf = frame_tfidf.append(frame_aux)
        frame_tfidf['count'] = 1
        return(frame_tfidf[['doc','word','count']])    

    def build_tf_idf(self, stopwords=True, lemmatizer=True, silence=False):
        df = self.colection.copy()
        f = self.build_tf(df, stopwords=stopwords, lemmatizer=lemmatizer, silence=silence)
        n = df.shape[0]
        f = f.groupby(by=['doc','word']).count().reset_index()
        f.rename(columns={'count':'f'},inplace=True)
        f['tf'] = 1+ np.log2(f['f'])
        f['idf'] = 0    
        idf = f.groupby(by=['word']).count().reset_index()[['word','tf']]
        idf.rename(columns={'tf':'idf'}, inplace=True)    
        idf['log'] = np.log2(1+ (n/idf['idf']))
        if silence:
            for i in range(f.shape[0]):
                w = ''.join(f.loc[i:i,'word'])
                f.loc[i:i,'idf'] = float(idf[idf['word'] == w]['log'])    
        else:
            for i in tqdm(range(f.shape[0])):
                w = ''.join(f.loc[i:i,'word'])
                f.loc[i:i,'idf'] = float(idf[idf['word'] == w]['log'])    
        f['tf_idf'] = f['tf'] * f['idf']
        self.tfidf = f.copy()
        self.set_sign()

    def set_sign(self):
        self.tfidf['sign'] = ''
        for i in range(self.tfidf.shape[0]):
            word = self.tfidf.loc[i,'word']
            p = self.positive_words[self.positive_words['word'] == word]
            n = self.negative_words[self.negative_words['word'] == word]
            if len(p) == 0 and len(n) > 0:
                self.tfidf.loc[i,'sign'] = 'negative'
            elif len(p) == 0 and len(n) == 0:
                self.tfidf.loc[i,'sign'] = 'neutral'
            elif len(p) > 0 and len(n) == 0:
                self.tfidf.loc[i,'sign'] = 'positive'
            elif len(p) > 0 and len(n) > 0:
                self.tfidf.loc[i,'sign'] = 'ambiguous'  
                
    def sentimental_graf(self, rotate=False):
        bar = pd.DataFrame(self.tfidf['sign'].value_counts()).reset_index()
        bar.columns = ['Sentimental','frequency']
        if rotate:
            img = sns.barplot(y='Sentimental', x='frequency', data=bar)
        else:
            img = sns.barplot(x='Sentimental', y='frequency', data=bar)
        return(img)
    
    def sentimental_table(self):
        bar = pd.DataFrame(self.tfidf['sign'].value_counts()).reset_index()
        bar.columns = ['Sentimental','frequency']
        return(bar)
        
    def word_cloud(self, picture='none'):
        resource_package = __name__
        file = '/'.join(('config', 'cloud.jpeg'))
        file_path = pkg_resources.resource_filename(resource_package, file)
        if picture == 'none':
            mask = np.array(Image.open(file_path))
        else:
            mask = np.array(Image.open(picture))
        tuples = [tuple(x) for x in self.tfidf[['word','tf_idf']].values]
        wc = WordCloud(background_color="white", max_words=1000, mask=mask).generate_from_frequencies(frequencies=dict(tuples))
        plt.figure(figsize=(15,15))
        plt.imshow(wc, interpolation="bilinear")
        plt.axis("off")
        return(plt)
        
    def look2word(self, wsearch):
        output = pd.DataFrame({'index': [],'word': []})
        for i in range(self.colection.shape[0]):
            line = self.del_punck(self.colection.loc[i,'word'])
            for word in line.split(' '):
                if word == wsearch:
                    output = output.append(pd.DataFrame({'index':[int(i)],'word':[line]}))
                    break
        output['index'] = output['index'].apply(lambda x: int(x))
        output = output.set_index('index')        
        return(output)
    
    def load_class_words(self):
        df_lema = pd.read_csv(self.file_path_cw, sep=';')
        return(df_lema)
        
    def set_class(self, word='none', wclass='none', force=False):
        word = word.lower()
        wclass = wclass.lower()
        exist = ''.join(self.df_wc[self.df_wc['word'] == word]['class'])
        save = False
        if exist == '-':
            self.df_wc.loc[self.df_wc['word'] == word,'class'] = wclass
            save = True
        elif force:
            self.df_wc.loc[self.df_wc['word'] == word,'class'] = wclass
            save = True
        else:
            print('Word ' + word + ' has a class named ' + wclass + ' you must use force=True to change the class')
        if save:
            self.df_wc.to_csv(self.file_path_cw, sep=';', index=False)

        
    def get_class(self, word='none'):
        word = word.lower()
        return(''.join(self.df_wc[self.df_wc['word'] == word]['class']))

    def load_pdf(self, file, silence=False):
        if not silence:
            print('Reading PDF file ' + file)
        text = extract_text(file)
        text_line = text.split('\n')
        doc = ''
        if silence:
            for line in text_line:
                if len(line) > 0:
                    doc = doc + line + ' '
        else:
            for line in tqdm(text_line):
                if len(line) > 0:
                    doc = doc + line + ' '
        return(doc)
    
    def find_cities(self, city):
        result = int(self.colection['word'].str.find(city))
        return('Substring ' + city + ' found at index: ' + str(result))
    
    def load_colection(self, dir, type='pdf', silence=False):
        files =  [x for x in os.listdir(dir) if x.endswith("." + type)]
        if len(files) == 0:
            raise TypeError("File type " + type + " not found")
        if silence:
            for file in files:
                if type == 'pdf':
                    df = self.load_pdf(os.path.join(dir, file),silence=silence)
                elif type == 'txt':
                        f = open(file, "r")
                        df = f.read()
                        df = pd.DataFrame(df.split('\n'))
                        df.columns = ['word']
                        f.close()
                else:
                    raise TypeError("File type " + type + " not permited")
                df = pd.DataFrame([df])
                df.columns = ['word']
                self.colection = self.colection.append(df)
        else:
            for file in tqdm(files):
                if type == 'pdf':
                    df = self.load_pdf(os.path.join(dir, file),silence=silence)
                elif type == 'txt':
                        f = open(file, "r")
                        df = f.read()
                        df = pd.DataFrame(df.split('\n'))
                        df.columns = ['word']
                        f.close()
                else:
                    raise TypeError("File type " + type + " not permited")
                df = pd.DataFrame([df])
                df.columns = ['word']
                self.colection = self.colection.append(df)

    def load_class_colection(self, dir='none', silence=False):
        if dir == 'none':
            raise TypeError("Directory not valid")
            
        classes =  [x for x in os.listdir(dir)]
        if len(classes) == 0:
            raise TypeError("Directory of classes is empty")

        self.colection = pd.DataFrame()
        if silence:
            for name_class in classes:
                files =  [x for x in os.listdir(dir + name_class)]
                if len(files) == 0:
                    raise TypeError("Directory of classes is empty")
                for name_file in files:
                    f = open(dir + name_class + '/' + name_file, "r", encoding='utf8', errors='ignore')
                    text = f.read()
                    f.close()                                        
                    self.colection = self.colection.append(pd.DataFrame({'doc': [name_file],
                                                                        'word': [text],
                                                                        'class': [name_class]}))
        else:
            for name_class in tqdm(classes):
                files =  [x for x in os.listdir(dir + name_class)]
                if len(files) == 0:
                    raise TypeError("Directory of classes is empty")
                for name_file in files:
                    f = open(dir + name_class + '/' + name_file, "r", encoding='utf8', errors='ignore')
                    text = f.read()
                    f.close()                                        
                    self.colection = self.colection.append(pd.DataFrame({'doc': [name_file],
                                                                        'word': [text],
                                                                        'class': [name_class]}))
                    
            