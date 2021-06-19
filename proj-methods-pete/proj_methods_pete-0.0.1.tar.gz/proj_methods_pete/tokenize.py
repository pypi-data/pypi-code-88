import nltk
nltk.download(['punkt', 'wordnet'])
nltk.download('words')

# import statements
from nltk import sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

def tokenize(text):
    """ Tokenize function to normalise and lemmatize the workds
    Input:
    - Text string

    Output:
    - List of tokens which is cleaned from normalised and lemmatize text and word tokenize
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens