import nlu
# TODO
# display_vector_simmilarity()
# display_entity_simmilarity()

# TOO unremovable footers?
# TODO sentence/doc similarity
# TODO auto-detect GPU? If TF avaiable, try to check if TF gpu avaiable?
# TODO XIBIT, YO I HEARD YOU LIKE EMBEDDINGS, SO we made a TOOl to embed you embeddings into 1-D, 2-D, and 3-D
# TODO INSTALL INSTRUCTIONS
# TODO 3D Similarity Matrix/CUBE/HYPER-SPHERE??!?!??!?!
# TODO SLACK LINK 4 COMMUNITY/ NLP DISCUSS FORUM
# TODO default sentiment classifier and no NER?
# TODO SENTENCE SIMILARITY
# TODO trigger ALL model dropdowns via show_model_select
# Todo model_selection for each app? Or just via audo infer?
# Todo extra classifiers, sentiment?
# todo remove XX for translators
# Todo code snippet on left side is wrong and for viz_word_embed aswell
# TODO always display LOGO
# TODO not all pipes listed in pipe param info
# TODO POS SELECTOR # TODO POS MODEL SELECT?
# AR NER BUGGY !
# LANGUAGE DETECT TOGGLE!
# NER.onto.lg BUGGY!
nlu.enable_streamlit_caching() # Optional caching the models, recommended
# Peter is from Berlin and where he loves visting the Charlottenburg Palace
#
data = 'Peter is from Berlin and where he loves visting the Charlottenburg Palace'
# # NER -> onto.sm,  NER-BERT-MINI -> BIGGER NER -> French NER ->
# 1. default text,
# 2. "Hello from john Snow Labs"
# 3. Show Bert
# 4. Wikipedia Math + lang https://fr.wikipedia.org/wiki/Histoire_des_math%C3%A9matiques
# 5 Some extra lang  ru.ner,tr.ner , fr.ner ,  de.ner, it.ner
nlu.load('ner').viz_streamlit(data)

# nlu.load('ner').viz_streamlit_ner(data)
#
# # EMBEDS
# 1. bert elmo glove
# + SIM
# 2.albert electra xlnet
# - sim
# 3. biobert / Covid /  small bert
#
# 2 or 3 metrics
# I love peanutbutter on my bread /// AND jelly!
# You can use 100's of Word embeddings to compare your texts
# I love love looove peanut butter for breakfast !
# and jelly <3
# and calculate similarities for!


# nlu.load('bert').viz_streamlit_word_similarity(['I love love loooove NLU! <3','I also love love looove  Streamlit! <3'], num_cols=3)
#
#
# # TOKEN
# lema, stem, pos, spell ,??
# data = 'You can play around with any of the 1000+ models in this visualization and view features generated'
# nlu.load('spell stem lemma pos').viz_streamlit_token('I liek pentut buttr and jelly !')
#
#
# # DEP TREEE
# nlu.load('dep.typed').viz_streamlit_dep_tree('POS tags define a grammatical label for each token and the Dependency Tree classifies Relations between the tokens')
# # CLASSIFIER
# sentiment, sarcasm, emotion, question, spam,
#
# nlu.load('sentiment').viz_streamlit_classes(['I love NLU and Streamlit!','I love buggy software', 'Sign up now get a chance to win 1000$ !', 'I am afraid of Snakes','Unicorns have been sighted on Mars!','Where is the next bus stop?'],sub_title=sh)

# FULL UI TODO
# # TODO automatically show all embeds and NER?
# ner_models = nlu.get_components('ner',include_pipes=True)
# default_text = "Angela Merkel from Germany and Donald Trump from America dont share many opinions"
# # nlu.load('ner').viz_streamlit(default_text, visualizers=['similarity'])
# #

# nlu.load('ner').viz_streamlit(visualizers=['similarity'])
# nlu.load('ner').viz_streamlit(similarity_texts=['I love love love  NLU !', 'I also love love love LOVE Streamlit'])
# nlu.load('ner').viz_streamlit(visualizers=['similarity','ner', 'dependency_tree'], num_similarity_cols=3)


# TODO dependencies sparknlp_display, sklearn, plotly



# 1. NER :  Peter loves visiting Charlottenburg Palace in Berlin
#   1.1NER -BERT
# 2 DEP:  billy likes to swim on sunny days
# 3 Token :  stem/pos/lemma/ There are 1000s of models to play with //
# 4. Class : Sentiment/Emotion :  I love sunny days, I hate rainy days
# 5. Embeds - Elmo, Bert, Glove, Albert, Electra, Xlnet
#

# nlu.load('ner').viz_streamlit(['I love NLU and Streamlit!','I hate buggy software'])
