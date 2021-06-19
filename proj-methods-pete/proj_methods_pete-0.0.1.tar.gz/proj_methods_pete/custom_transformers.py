import pandas as pd
import nltk
nltk.download(['punkt', 'wordnet'])
nltk.download('words')
nltk.download('vader_lexicon')

# import statements
from nltk import sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.base import BaseEstimator, TransformerMixin

class HelpWordExtractor(BaseEstimator, TransformerMixin):
    """ Transformer to extract out the word "help" and returns 1 or 0 to support help response classifications
    Input:
    - Sentence list for analysis and prediction

    Output:
    - DataFrame Series of 1 or 0s nothing whether there is the word "help" in message or not
    """
    # To identify specific words for help and label them appropriately
    def contains_help(self, text):
        # Breakdown to each sentence for tokenization
        sentence_list = nltk.sent_tokenize(text)

        # Loop through the list to extract each string
        for sentence in sentence_list:
            # Return 1 if there is word "help" and 0 if not
            if 'help' in sentence:
                return 1
            else:
                return 0
        # Return 0 if sentence is empty or so
        return 0

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        # Apply the contains_help function to the inputted data and transform it as noted
        X_tagged = pd.Series(X).apply(self.contains_help)
        return pd.DataFrame(X_tagged)

    
class WordLengthExtractor(BaseEstimator, TransformerMixin):
    """ Transformer to output the list of word length of the message 
    This is to further add information regarding the inputted message whether there is a relationship between wordlength and the model

    Input:
    - Sentence list for analysis and prediction

    Output:
    - DataFrame Series of message length
    """
    # To see word length whether longer message have more distress in them or not
    def word_length(self, text):
        return len(text)

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        # Apply the word_length function to the inputted data and transform it as noted
        X_tagged = pd.Series(X).apply(self.word_length)
        return pd.DataFrame(X_tagged)
    
class SentimentSentenceExtractor(BaseEstimator, TransformerMixin):
    """ Transformer to output the compound sentiment score of the sentence
    Sentiment is a measure of whether the sentence has a positive or negative words in it.
    This is done through using the SentimentIntensityAnalyzer from nltk.sentiment

    Input:
    - Sentence list for analysis and prediction

    Output:
    - DataFrame Series of compound scores
    """    
    # To see word length whether longer message have more distress in them or not
    def sentiment_analyser(self, text):
        return SentimentIntensityAnalyzer().polarity_scores(text)['compound']

    def fit(self, x, y=None):
        return self

    def transform(self, X):
        # Apply the sentiment_analyser function to the inputted data and transform it as noted
        X_tagged = pd.Series(X).apply(self.sentiment_analyser)
        return pd.DataFrame(X_tagged)

