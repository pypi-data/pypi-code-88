from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models import Word2Vec
from tqdm.auto import tqdm
from time import time
import numpy as np
import pickle
import pathlib
import os

from zarebin_brain.NLP.Normalizer import Normalizer
from zarebin_brain.NLP.Tokenizer.Tokenizer import Tokenize
from zarebin_brain.NLP.NER_parsbert import NER3

STOP_WORD_PATH = os.path.join(pathlib.Path(__file__).parent.absolute(), "data/external/stop_words.txt")
PARAM_FILE_NAME = "params.txt"
WORD2VEC_MODEL_FILENAME = "word2vec.h5"
WORDS_ID_FILENAME = "words_idf.pkl"


class Query2Vec:
    """
    ‫این کلاس یک مدل query2vec با استفاده از word2vec و idf کلمات میسازد
    """
    normalizer = Normalizer()
    tokenizer = Tokenize()
    ner = NER3.NER()
    persian_stop_words = None
    words_idf = dict()
    w2v_model = None
    ner_tags_weights = {'pers': 1, 'loc': 1, 'org': 1, 'fac': 1, 'event': 1, 'pro': 1}
    document_count = 0
    training_params = dict()

    my_tokenizer = tokenizer.space_tokenize
    my_normalizer = normalizer.normalizeText

    def __init__(self, vector_size=100, min_count=5, window=5):
        self.training_params["vector_size"] = vector_size
        self.training_params["min_count"] = min_count
        self.training_params["window"] = window

        self.__load_persian_stop_words()

    def __load_persian_stop_words(self):
        """
        ‫از فایل stop word ها را میخواند
        """
        persian_stop_words_raw = open(STOP_WORD_PATH, 'r', encoding="utf8").read().split('\n')
        self.persian_stop_words = [self.my_normalizer(text) for text in persian_stop_words_raw]
        return

    def __remove_stop_words(self, token_list):
        """
        ‫از لیست توکنهای یک جمله یا کوئری، stop word ها را حذف میکند
        Args:
            token_list: iterable of strings
            list of tokens from a sentence or query
        Returns: list of strings
            list of tokens after stop word removal

        """
        return list(filter(lambda x: (x not in self.persian_stop_words), token_list))

    def __save_words_idf(self, address):
        """
        ‫دیکشنری استخراج شده از کلمات و idf انها در دیتای آموزش را در قالب pickle ذخیره میکند
        Args:
            address: string
            path to file, for saving word idf dictionary

        """
        with open(address, 'wb') as f:
            pickle.dump(self.words_idf, f)

    @staticmethod
    def __load_words_idf(address):
        """
        ‫دیکشنری کلمات و idf انها را، از یک فایل به فرمت pickle میخواند
        Args:
            address: string
            path to file for reading word idf dictionary

        Returns: dict(string, float)
        word: idf dictionary

        """
        with open(address, 'rb') as f:
            words_idf = pickle.load(f)
        return words_idf

    def __normalize_sentences(self, sentences):
        """
        ‫لیستی از جمله ها را یکسان سازی میکند
        Args:
            sentences: iterable of strings

        Returns: iterable of strings
        normalized sentences

        """
        normalized_sentences = []
        for sent in tqdm(sentences):
            normalized_sentences.append(self.my_normalizer(sent))
        return normalized_sentences

    def __preprocess_sentences(self, sentences):
        """
        ‫لیستی از جمله ها را tokenize میکند و stop word ها را حذف میکند
        Args:
            sentences: iterable of strings

        Returns: iterable of iterables
        ‫ هر لیست شامل توکنهای یک جمله است

        """
        tokenized_sentences = []
        for sent in tqdm(sentences):
            tokens = self.my_tokenizer(sent)
            tokens = self.__remove_stop_words(tokens)
            tokenized_sentences.append(tokens)
        return tokenized_sentences

    def __train_word2vec_model(self, sentences, update=False, workers=3, epochs=5):
        """
        ‫مدل word2vec را آموزش میدهد یا مدل آموزش داده شده را fine-tune میکند
        Args:
            sentences: iterable of iterables
            ‫هر جمله به صورت لیستی از توکنهاست
            update: boolean
            ‫مشخص میکند که آیا مدل fine-tune شود یا مدل جدیدی آموزش داده شود
            workers: int
            ‫تعداد thread ها برای استفاده در آموزش مدل
            epochs: int
            ‫تعداد epoch برای آموزش مدل

        """

        vector_size = self.training_params["vector_size"]
        min_count = self.training_params["min_count"]
        window = self.training_params["window"]

        if not update:
            self.w2v_model = Word2Vec(min_count=min_count, window=window, workers=workers, vector_size=vector_size)

        t = time()

        if update:
            self.w2v_model.build_vocab(sentences, progress_per=10000, update=True)
        else:
            self.w2v_model.build_vocab(sentences, progress_per=10000)

        print('Time to build vocab: {} mins'.format(round((time() - t) / 60, 2)))

        t = time()

        self.w2v_model.train(sentences, total_examples=self.w2v_model.corpus_count,
                             epochs=epochs, report_delay=1)

        print('Time to train the model: {} mins'.format(round((time() - t) / 60, 2)))

    def __save_word2vec(self, address):
        """
        ‫مدل word2vec را در ادرس داده شده ذخیره میکند
        Args:
            address: string
            path to file for saving model

        """
        self.w2v_model.save(address)

    @staticmethod
    def __load_word2vec(address):
        """
        ‫مدل word2vec را از روی فایل میخواند
        Args:
            address: string
            path to file for loading model

        Returns: Word2Vec model

        """
        w2v_model = Word2Vec.load(address)
        return w2v_model

    def __save_params(self, address):
        """
        ‫پارامترهای مدل را در یک فایل در قالب pickle ذخیره میکند
        Args:
            address: string
            path to file for saving model params

        """
        with open(address, "wb") as file:
            pickle.dump(self.training_params, file)

    @staticmethod
    def __load_params(address):
        """
        ‫پارامترهای مدل را از یک فایل به فرمت pickle میخواند
        Args:
            address: string
            path to file

        Returns: dict(string, value)
        dictionary contains value for model params

        """
        with open(address, "rb") as file:
            training_params = pickle.load(file)
        return training_params

    def set_ner_tags_weights(self, weights):
        """
        ‫برای هر یک از تگهای ner ای که در وزن دهی تاثیر دارند، وزن را تعیین میکند
        Args:
            weights: iterable of floats

        """
        if len(self.ner_tags_weights) != len(weights):
            print("dimension mismatch")
            return
        self.ner_tags_weights = dict(zip(self.ner_tags_weights.keys(), weights))
        return

    def query_to_vec(self, query, tf_idf_enable=True, ner_enable=False):
        """
        ‫برای یک کوئری، با مدل آموزش دیده شده، یک بردار تولید میکند
        Args:
            query: string
            tf_idf_enable: boolean
            use tf_idf for weighting tokens or not
            ner_enable: boolean
            use ner for weighting tokens or not

        Returns: np array of size vector_size

        """
        if ner_enable:
            query_ner = dict(self.ner.parsbert_ner([query])[0])

        weights_sum = 0
        query_vector = np.zeros(self.training_params["vector_size"])
        words = self.my_tokenizer(self.my_normalizer(query))
        for word in words:
            weight = 1
            if word in self.w2v_model.wv.key_to_index:
                if tf_idf_enable and (word in self.words_idf):
                    weight *= self.words_idf[word]
                if ner_enable and (word in query_ner) and (query_ner[word] in self.ner_tags_weights):
                    weight *= self.ner_tags_weights[query_ner[word]]
                query_vector += weight * self.w2v_model.wv.get_vector(word, norm=True)
                weights_sum += weight

        if weights_sum:
            return query_vector / weights_sum
        else:
            return query_vector

    def __compute_words_idf(self, sentences, update=False):
        """
        ‫با استفاده از لیستی از جملات، idf کلمات را میسازد یا مدل ساخته شده را بروز میکند
        Args:
            sentences: list of strings
            update: boolean
            update current model or create new model from scratch

        """
        document_count = len(sentences)
        vectorizer = TfidfVectorizer(tokenizer=self.my_tokenizer, stop_words=self.persian_stop_words)
        vectorizer.fit(sentences)
        idfs = dict(zip(vectorizer.get_feature_names(), vectorizer.idf_))

        if update:
            self.words_idf, self.document_count = self.__merge_idf_dicts(self.document_count,
                                                                         document_count,
                                                                         self.words_idf,
                                                                         idfs)
        else:
            self.words_idf = idfs
            self.document_count = document_count

    def __merge_idf(self, n1, n2, idf1, idf2):
        """
        ‫برای یک کلمه،‌ idf آن در 2 پیکره متنی را داریم و idf کل را محاسبه میکنیم.
        Args:
            n1: int
            number of documents in first corpus
            n2: int
            number of documents in second corpus
            idf1: float
            idf of word in first corpus
            idf2: float
            idf of word in second corpus

        Returns: float
            idf of word in total

        TODO : this function will be called for each word in vocab, check if it's a bottleneck in update model process
        """
        df1 = np.round(((n1 + 1) / np.exp(idf1 - 1)) - 1)
        df2 = np.round(((n2 + 1) / np.exp(idf2 - 1)) - 1)
        idf_t = np.log((n1 + n2 + 1) / (df1 + df2 + 1)) + 1
        return idf_t

    def __merge_idf_dicts(self, n1, n2, dict1, dict2):
        """
        ‫برای دو پیکره متنی، که برای هر یک idf کلمات را داریم، idf کلمات در در مجموع دو پیکره حساب میکند
        Args:
            n1: int
            number of documents in first corpus
            n2: int
            number of documents in second corpus
            dict1: dict(string, float)
            words idf dictionary in first corpus
            dict2: dict(string, float)
            words idf dictionary in second corpus

        Returns: dict(string, float), int
            words idf in total corpus
            number of documents in total

        """
        dict_t = {k: self.__merge_idf(n1, n2, dict1.get(k, np.log(n1 + 1) + 1), dict2.get(k, np.log(n2 + 1) + 1))
                  for k in set(dict1) | set(dict2)}
        return dict_t, n1 + n2

    def get_word_idf(self, word):
        """
        ‫برای کلمه ورودی، idf آن کلمه را خروجی میدهد
        Args:
            word: string

        Returns: float
        idf of word

        """
        return self.words_idf.get(word)

    def train_model(self, sentences, update=False, workers=3, epochs=5):
        """
        ‫کل مدل را با پیکره متنی ورودی آموزش میدهد
        Args:
            sentences: iterable of strings
            update: boolean
            update current model or build a new model
            workers: int
            number of threads to use for training word2vec
            epochs: int
            number of epochs to train word2vec

        """
        normalized_sentences = self.__normalize_sentences(sentences)
        processed_sentences = self.__preprocess_sentences(normalized_sentences)

        self.__train_word2vec_model(processed_sentences, update=update, workers=workers, epochs=epochs)
        self.__compute_words_idf(normalized_sentences, update=update)

    def save_model(self, path):
        """
        ‫مدل آموزش دیده را در یک پوشه ذخیره میکند
        Args:
            path: string
            path to folder for saving model files

        """
        if os.path.exists(path):
            print("path already exists, please change the path or delete existing path\nsaving model failed")
            return
        os.mkdir(path)
        self.__save_word2vec(os.path.join(path, WORD2VEC_MODEL_FILENAME))
        self.__save_words_idf(os.path.join(path, WORDS_ID_FILENAME))
        self.__save_params(os.path.join(path, PARAM_FILE_NAME))
        return

    @classmethod
    def load(cls, path):
        """
        ‫مدل را از مسیر ورودی میخواند
        Args:
            path: string
            path to model folder

        Returns: Query2Vec
        instance of class

        """
        if not os.path.exists(path) or not os.path.isdir(path):
            raise Exception("directory doesn't exists")

        training_params = cls.__load_params(os.path.join(path, PARAM_FILE_NAME))
        word2vec_model = cls.__load_word2vec(os.path.join(path, WORD2VEC_MODEL_FILENAME))
        words_ifs = cls.__load_words_idf(os.path.join(path, WORDS_ID_FILENAME))

        model = cls(vector_size=training_params["vector_size"],
                    min_count=training_params["min_count"],
                    window=training_params["window"])
        model.w2v_model = word2vec_model
        model.words_idf = words_ifs

        return model
