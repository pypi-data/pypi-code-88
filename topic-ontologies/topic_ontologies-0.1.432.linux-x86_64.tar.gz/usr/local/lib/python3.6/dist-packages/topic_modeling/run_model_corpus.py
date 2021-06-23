from topic_modeling.model_corpora import *
import sys


ontology = sys.argv[1]
model = sys.argv[2]
corpus = sys.argv[3]

model_corpus(corpus,ontology,model)


