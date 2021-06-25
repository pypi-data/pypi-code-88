import pandas as pd
import nlu
from typing import List, Sequence, Tuple, Optional, Dict, Union, Callable
import streamlit as st
def get_pipe(model='ner'): return nlu.load(model)
def display_side_ui(): pass

def viz_streamlit(
    # Base Params
    default_text:Union[str, List[str], pd.DataFrame, pd.Series],
    model_selection:List[str],
    # NER PARAMS
    default_ner_model2viz:Union[str, List[str]] = 'en.ner.onto.electra.base',

    # SIMILARITY PARAMS
    similarity_texts:Tuple[str,str]= ('Donald Trump Likes to part', 'Angela Merkel likes to party'),
    title:str = 'NLU ❤️ Streamlit - Prototype your NLP startup in 0 lines of code' ,
    # UI PARAMS
    visualizers:List[str] = ( "dependency_tree", "ner",  "similarity", "token_information", "embedding_word",'classification','embedding_sentence'), #viz2apply(#
    show_models_info:bool = True,
    show_model_select:bool = True,
    show_viz_selection:bool = True,
    show_logo:bool=True,
    show_code_snippets:bool=False,
    )->None:
    """Visualize either individual building blocks for streamlit or a full UI to experiment and explore models with"""
    from nlu.pipe.viz.streamlit_viz.streamlit_viz_tracker import StreamlitVizTracker

    if title: st.title(title)
    if show_logo :StreamlitVizTracker.show_logo()
    # Join list of NLU refs to str
    if isinstance(default_ner_model2viz, List)       : default_ner_model2viz = ' '.join(default_ner_model2viz)
    ner_model_2_viz     = default_ner_model2viz
    default_text    = st.text_area("Enter text you want to visualize below", default_text)
    if show_model_select :
        st.sidebar.checkbox('Show generated code samples')
        ner_model_2_viz = st.sidebar.selectbox("Select a NER model",model_selection,index=model_selection.index(default_ner_model2viz.split(' ')[0]),)
    active_visualizers = visualizers
    if show_viz_selection: active_visualizers = st.sidebar.multiselect("Visualizers",options=visualizers,default=visualizers)

    all_models = ner_model_2_viz + ' en.dep.typed '
    if show_models_info : StreamlitVizTracker.display_model_info(all_models)

    if 'dependency_tree' in active_visualizers :
        tree_pipe = get_pipe('en.dep.typed')
        StreamlitVizTracker.visualize_dep_tree(tree_pipe, default_text)
    if 'ner' in active_visualizers :
        ner_pipe = get_pipe(ner_model_2_viz)
        StreamlitVizTracker.visualize_ner(ner_pipe, default_text)
    if 'token_information' in active_visualizers:
        ner_pipe = get_pipe(ner_model_2_viz)
        StreamlitVizTracker.visualize_tokens_information(ner_pipe, default_text)
    if 'classification' in active_visualizers:
        ner_pipe = get_pipe(ner_model_2_viz+' sentiment')
        StreamlitVizTracker.visualize_classes(ner_pipe, default_text)
    if 'similarity' in active_visualizers:
        ner_pipe = get_pipe(ner_model_2_viz)
        StreamlitVizTracker.display_word_similarity(ner_pipe, similarity_texts)




def visualize_IU():
    """Viz NLU UI"""
    # Get a list of all NER models and define default input text
    ner_models = nlu.get_components('ner',include_pipes=True)
    default_text = "Sundar Pichai is the CEO of Google."
    viz_streamlit(default_text,ner_models)
visualize_IU()









