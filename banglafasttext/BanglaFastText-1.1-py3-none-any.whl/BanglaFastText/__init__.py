import gdown
import zipfile
import pickle
import numpy as np
import os
import logging
from gensim.models.fasttext import FastText
from tqdm.auto import tqdm
from sklearn.metrics.pairwise import cosine_similarity



class BanglaFasttext:
    def __init__(self, model_path=None, method='cbow', Save_path = ''):
        if model_path == None:
            print(' - Downloading Bangla FastText model...')
            if method == 'cbow':
                url='https://storage.googleapis.com/kaggle-data-sets/1410402/2360821/compressed/Bangla_FastText_cbow/Bangla_FastText_cbow.pickle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210622%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210622T182940Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=7823f961ab9198791ffe3ce25ca974ac9dd17571014d41c365d6db68fce6ac59e40ac466aecba59db57600f6a1e3dddbdf7fd602524fc8edaa7ec02a2265a0ec6f7862c6d1b049fb0931da3ea3d4ce3c465ef2912435df7130f028e0d5e03ab78d9280d09a9a3327dc79453733303cc22333f8bff4d2dc1b721d199c4e3b53f5efd82002f23c8101ef9b3b6214a3aab190ef4f48201713363efa60d271ad687a5e5baa96dc269160b3da430a9305ec4e90d9a6124f955d7c987fefed9b5b1643d18af545c03d8e35ab2122af80e2f1bc61b38465392eba6099e5f234500806f890d022e3aa09d950b5e52204142ee6b2d857f2f55beab0ba637ea9108991d3a8'
            else:

                url='https://storage.googleapis.com/kaggle-data-sets/1410402/2360821/compressed/Bangla_FastText_skipgram/Bangla_FastText_skipgram.pickle.zip?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=gcp-kaggle-com%40kaggle-161607.iam.gserviceaccount.com%2F20210622%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20210622T183114Z&X-Goog-Expires=259199&X-Goog-SignedHeaders=host&X-Goog-Signature=16935d84ceddd171d9e2ad46d43d8b8daf26119b5582bbf9da880dbdcea77239e612b7b344b055169099676ef2bce7c8e7b82f22b53978a5a35c77c9746c3ee7022c0b60b8f472bff7db2e264e506d9c35e31936c7b3bc6cf1d77c74a8cf894becab729c59c8a3457c49208362ed9e4821266d071c114fe3944d4fd57375df392956a1c1844758fbfe4e316332164077042e62cc9509107650b1c9eda0a7bddc02614c5240dab0bb41b276bdafa93754c1db716a0fc85073f8215aa55074669199c9ca39ff761caebe53cf58158df1bb7592283e9b5622a5e29baeb61d8147e865ada41ecc53338c18e8e914be99e0d750f883a8a04a11d4a182c53391e916f2'

            gdown.download(
                url=url,
                output= Save_path+'BanglaFastTextModel.zip',
                quiet=True
            )
            print(' - Model preparation ...')
  
            with zipfile.ZipFile( Save_path+'BanglaFastTextModel.zip', 'r') as zip_ref:
                zip_ref.extractall( Save_path)
            try:
                with open( Save_path+'Bangla_FastText_cbow.pickle', 'rb') as handle:
                    model = pickle.load(handle)
            except:
                with open( Save_path+'Bangla_FastText_skipgram.pickle', 'rb') as handle:
                    model = pickle.load(handle)

            
            self.modelwv =model.wv
            self.model=model
                               
        else:
            print(' - Model preparation ...')

            try:
                model = FastText.load(model_path)
            except:
                with open(model_path, 'rb') as handle:
                    model = pickle.load(handle)  
            self.modelwv =model.wv
            self.model=model              

    def model_load(self):
        return self.modelwv

        
    def div_norm(self, x):
        
        norm_value = np.sqrt(np.sum(x**2))

        if norm_value > 0:
            return x * ( 1.0 / norm_value)
        else:
            return x


    def sent_embd(self,corpus):
        emd_corpus=[]
        for sent in tqdm(corpus):
            try:
                embd = [self.div_norm(self.modelwv[i]) for i in sent.split()]
                emd_corpus.append(list(np.mean(embd, axis=0)))
            except:
                emd_corpus.append(self.div_norm(self.modelwv['unknown']))
        return np.asarray(emd_corpus)


    def word_similarity(self, word1, word2):
        return cosine_similarity(self.modelwv[word1].reshape(1, -1), self.modelwv[word2].reshape(1, -1))[0]
    def sent_similarity(self, sent1, sent2):
        sent1=self.sent_embd(sent1)
        sent2=self.sent_embd(sent2)

        return cosine_similarity(self.modelwv[sent1].reshape(1, -1), self.modelwv[sent2].reshape(1, -1))[0]


    def fine_tuning(self,corpus, epochs=5):
        sent=[]
        for k in corpus:
            sent.append(k.split())
        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        self.model.build_vocab(corpus_iterable=sent, update=True)
        self.model.train(corpus_iterable=sent, total_examples = len(sent), epochs=epochs)
        self.modelwv = self.model.wv
        return self.model
