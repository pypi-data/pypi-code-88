import re
import io
import requests
import pandas as pd
import spacy
from collections import defaultdict
from math import log
import nltk


def load_dataset(url, sep='\t', decode='utf-8', dtype=None):
    def requests_csv(url, decode='utf-8'):
        return (requests.get(url).content.decode(decode))
    return pd.read_csv(io.StringIO(requests_csv(url, decode)), sep=sep, dtype=dtype)


# words freq file
url_words_by_freq = 'https://raw.githubusercontent.com/alseambusher/columbus/master/words-by-frequency.txt'
response_words_by_freq = requests.get(url_words_by_freq)
    
with open('words-by-frequency.txt', mode='w') as fw:
    fw.write(response_words_by_freq.text)
    
# Build a cost dictionary, assuming Zipf's law and cost = -math.log(probability).
words = open('words-by-frequency.txt').read().split()
wordcost = dict((k, log((i+1)*log(len(words)))) for i,k in enumerate(words))
maxword = max(len(x) for x in words)

# Drop non-english words spacy
sp_nlp = spacy.load('en_core_web_sm')
words_nltk = set(nltk.corpus.words.words())


class PreprocessDataframe():
    def __init__(self, df: pd.core.frame.DataFrame, subset: str = 'text', warn_bad_lines=None):
        self.df = df
        self.subset = subset
        self.warn_bad_lines = warn_bad_lines

    def preprocessing(self,
                      lower_case: bool = True,
                      infer_spaces: bool = True,
                      slang_translator: bool = False,
                      apply_re: bool = True,
                      re_kind=None
                      ):
        """Preprocess the dataframe with multiple techniques.

        Args:
            - lower_case:
            - infer_spaces:
            - apply_re:
            - slang_trranslator:
            - re_kind:
        Returns:
            A full preprocessing pandasa dataframe.

        """

        output_name = 'sentences dataset'

        def _infer_spaces(s: str, verbose=0):  # verbose=1 not currently working
            """Uses dynamic programming to infer the location of spaces in a string
            without spaces.
            """
            if ' ' not in s:
                # Find the best match for the i first characters, assuming cost has
                # been built for the i-1 first characters.
                # Returns a pair (match_cost, match_length).
                def best_match(i):
                    return min((c + wordcost.get(s[i-k-1:i], 9e999), k+1) for k, c in enumerate(reversed(cost[max(0, i-maxword):i])))

                # Build the cost array.
                cost = [0]
                for i in range(1, len(s)+1):
                    c, k = best_match(i)
                    cost.append(c)

                # Backtrack to recover the minimal-cost string.
                out = []
                i = len(s)

                while i > 0:
                    c, k = best_match(i)
                    assert c == cost[i]

                    # Apostrophe and digit handling
                    if verbose == 1:
                        newToken = True

                        if not s[i-k:i] == "'":  # ignore a lone apostrophe
                            if len(out) > 0:
                                # re-attach split 's and split digits
                                # digit followed by digit
                                if out[-1] == "'s" or (s[i-1].isdigit() and out[-1][0].isdigit()):
                                    # combine current token with previous token
                                    out[-1] = s[i-k:i] + out[-1]
                                    newToken = False

                        if newToken:
                            out.append(s[i-k:i])
                    elif verbose == 0:
                        out.append(s[i-k:i])
                    i -= k

                return ' '.join(reversed(out))
            else:
                return s

        def _slang_translator(text: str):
            """Translate slangs
            """
            # slang translator file
            url_my_slangs = 'https://raw.githubusercontent.com/Y4rd13/datasets/main/Slangs%20Abbreviations%20with%20their%20meanings.csv'
            my_slangs_csv = load_dataset(url_my_slangs, sep=',', dtype={'slang': str, 'meaning': str})

            my_slangs_csv['length'] = my_slangs_csv.slang.str.len()
            my_slangs_csv = my_slangs_csv[my_slangs_csv.length <= 5]

            text = text.split()
            c = 0

            for s in text:
                if len(s) <= 5:
                    s = re.sub('[^a-zA-Z0-9-_.]', '', s)
                    for __, row in my_slangs_csv.iterrows():
                        if s.lower() == row[0]:
                            # if match found, replace it with its abbreviation in text
                            text[c] = row[1]
                else:
                    pass

                c += 1

            return ' '.join(text)

        # Lower case
        if lower_case:
            print('Everything to lower case...')
            self.df[self.subset] = self.df[self.subset].str.lower()

        # Infering spaces
        if infer_spaces:
            print('Infering spaces...')
            self.df[self.subset] = self.df[self.subset].apply(
                lambda x: _infer_spaces(s=x, verbose=0))

        # Slang translator
        if slang_translator:
            print('Applying slang translator...')
            self.df[self.subset] = self.df[self.subset].apply(
                lambda x: _slang_translator(text=x))

        if apply_re:
            print(f'Applying Regular Expressions: {re_kind}...')
            # Removing urls
            self.df[self.subset] = self.df[self.subset].apply(
                lambda x: re.sub(r'https://www\.|http:\.|https://|www\.', '', x))
            self.df[self.subset] = self.df[self.subset].apply(lambda x: re.sub(
                r'[\S]+\.(net|com|org|info|edu|gov|uk|de|ca|jp|fr|au|us|ru|ch|it|nel|se|no|es|mil|cl)[\S]*\s?', '', x))

            # Removing special character and numbers
            if re_kind == 'full':
                # removes all special characters
                self.df[self.subset] = self.df[self.subset].apply(lambda x: re.sub(
                    r'(@[A-Za-z0-9]+)|([^0-9A-Za-zÁ-Úá-ú \t])|(\w+:\/\/\S+)|^rt|http.+?%', '', x))
            elif re_kind == 'partial':
                # we stay with dots and commas
                self.df[self.subset] = self.df[self.subset].apply(
                    lambda x: re.sub(r'[^.,a-zA-Z0-9 \n\.]', '', x))
            self.df[self.subset] = self.df[self.subset].apply(
                lambda x: re.sub(r'\d+', '', x))

            if slang_translator:
                print('Applying slang translator...')
                # Slang translator again in case new words appear using re
                self.df[self.subset] = self.df[self.subset].apply(
                    lambda x: _slang_translator(text=x))

        # Removing empty values (just in case)
        print('Removing NaN...')
        nan_value = float('NaN')
        self.df.replace('', nan_value, inplace=True)
        # unclean_df.replace(' ', nan_value, inplace=True)
        self.df.dropna(inplace=True)

        # Stripping spaces in both sides
        print('Stripping spaces in bnoth sides...')
        self.df[self.subset] = self.df[self.subset].str.strip()

        # Re-writting the created file without NaN values
        print('Remaking df...')
        self.df.to_csv('./' + output_name,
                       quotechar='"', encoding='utf-8', index=False)

        # Returning clean csv
        df = pd.read_csv('./' + output_name, encoding='utf-8',
                         warn_bad_lines=self.warn_bad_lines).dropna()

        return df

    def ner_spacy_dropNonEnglish(self, text_ner: str, threshold=.2, verbose=0):
        """Drop non-English words
        """

        text = self.text_ner

        def non_enwords(sentence: str, saved_list):
            return ' '.join(
                [
                    word for word in nltk.wordpunct_tokenize(sentence) if word.lower() in words_nltk
                    or not word.isalpha()
                    or word in saved_list
                ]
            )  # or word in saved_list)

        with sp_nlp.disable_pipes('ner'):
            doc = sp_nlp(text)

        (beams) = sp_nlp.entity.beam_parse(
            [doc], beam_width=16, beam_density=0.0001)

        entity_scores = defaultdict(float)

        for beam in beams:
            for score, ents in sp_nlp.entity.moves.get_beam_parses(beam):
                for start, end, label in ents:
                    entity_scores[(start, end, label)] += score

        saved = []
        for key in entity_scores:
            start, end, label = key
            score = entity_scores[key]
            if verbose == 1:
                print('Label: {}, Text: {}, Score: {}'.format(
                    label, doc[start:end], score))

            if (score > threshold):
                if verbose == 2:
                    print('Label: {}, Text: {}, Score: {}'.format(
                        label, doc[start:end], score))
                saved.append(doc[start:end].text)

        saved_list = (' '.join(saved)).split()
        nonen_words_list = non_enwords(sentence=text, saved_list=saved).split()

        return ' '.join([w for w in text.split() if w in saved_list or w in nonen_words_list])

    def checkFill_nan(self, df: pd.core.frame.DataFrame, fill_value=0):
        """Check and fill NaN values in the dataframe

        Args:
            - df: dataframe
            - fill_value: value used to fill the dataframe. Default: 0.

        Returns:
            The dataframe without NaN values

        """

        check = [i for i in (df.isnull().any()) if i == True]

        try:
            check.index(True)
            df.fillna(value=fill_value, inplace=True)
            print('NaN values successfully filled with {}'.format(fill_value))
        except:
            print('No NaN values found')

    def NLP_options(self,
                    verbose: int,
                    ):
        """Different NLP techniques options.

        Args:
            - df: dataframe.
            - subset: target column.
            - verbose: 0, 1. Verbosity mode. 1 = remove repetitions, 2 = remove stopwords.
        Returns:
            NLP dataframe with technique applied
        """

        if verbose == 0:
            # Removing repetitions (goood ==> good, god ==> god)
            pattern = re.compile(r'(.)\1{2,}', re.DOTALL)
            self.df[self.subset] = self.df[self.subset].str.replace(
                pattern, r'\1')
            pass
        elif verbose == 1:
            url_stopwords = 'https://raw.githubusercontent.com/Y4rd13/datasets/main/IS_STOPWORDS.txt'
            response_stopwords = requests.get(url_stopwords)

            with open('IS_STOPWORDS.txt', mode='w') as fw:
                fw.write(response_words_by_freq.text)
            IS_STOPWORDS = open('IS_STOPWORDS.txt').read().split()

            # Removing stopwords
            self.df[self.subset] = self.df[self.subset].apply(lambda x: ' '.join(
                [i for i in x.split() if i.lower() not in (IS_STOPWORDS)]))    