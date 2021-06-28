import nlu
default_text = ('What is love?', 'Baby dont hurt me')
nlu.load('ner').viz_streamlit(default_text, visualizers=['embedding_sentence'])
nlu.load('ner').viz_streamlit(default_text, visualizers=['embedding_words'])
