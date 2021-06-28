# https://towardsdatascience.com/synonyms-and-antonyms-in-python-a865a5e14ce8
# https://spacytextblob.netlify.app/docs/example
import nltk
import spacy
from nltk.corpus import wordnet
from spacytextblob.spacytextblob import SpacyTextBlob
import en_core_web_sm


nltk.download('wordnet')

nlp = en_core_web_sm.load()
nlp.add_pipe("spacytextblob")


def nlpFunc(text):
  
    synonyms = []
    
    # NLP analysis of single-line text
    doc = nlp(text)

    # print(doc._.assessments)

    if len(text) != 0:
        
        # list comphresion to get the emotional words
        words = list(zip(*doc._.assessments))
        
        # for index in range(0, len(words)):
        if(len(words) != 0):
            word = list(zip(*words[0]))
            print(word)
            word3 = list(zip(*word))

            for index in range(0, len(word3)):
                # print(index, "-", *word3[index])

                # Word Cloud
                # looks for synonym(s) of the emotional word(s)
                for syn in wordnet.synsets(*word3[index]):
                    # returns the synonyms of the emotional word(s)
                    for lm in syn.lemmas():
                        # adds the snonym(s) to the synonyms list
                        synonyms.append(lm.name())
                # prints the synonym(s) of the emotional word(s)
                print(set(synonyms))

            # Input multiple lines of text
            docs = list(nlp.pipe([text]))
        else:
            synonyms = ["no synonyms found"]

        # for doc in docs:
            # print('Assessments:', doc._.assessments)
    else:
        synonyms = ["Please enter text"]
        
    return synonyms
