import nlu
import streamlit as st
from sparknlp.annotator import NerConverter,DependencyParserModel
from typing import List, Tuple, Optional, Dict, Union
import streamlit as st
from nlu.utils.modelhub.modelhub_utils import ModelHubUtils
import numpy as np
import pandas as pd
from sparknlp.annotator import *
from nlu.pipe.viz.streamlit_viz.streamlit_utils_OS import StreamlitUtilsOS
from nlu.pipe.viz.streamlit_viz.gen_streamlit_code import get_code_for_viz
from nlu.discovery import Discoverer
def visualize_classes(
        pipe, # nlu pipe
        text:Union[str,list,pd.DataFrame, pd.Series]='I love NLU and Streamlit and sunny days!',
        output_level:Optional[str]='document',
        title: Optional[str] = "Text Classification",
        metadata : bool = False,
        positions : bool = False,
        set_wide_layout_CSS:bool=True,
        generate_code_sample:bool = False,
        key = "NLU_streamlit"
)->None:

    if title:st.header(title)
    if generate_code_sample: st.code(get_code_for_viz('CLASSES',StreamlitUtilsOS.extract_name(pipe),text))
    classifier_pipes = [pipe]
    classifier_components_usable = [e for e in Discoverer.get_components('classify',True, include_aliases=True)]
    classifier_components = StreamlitUtilsOS.find_all_classifier_components(pipe)
    loaded_classifier_nlu_refs = [c.info.nlu_ref for c in classifier_components]
    # VizUtilsStreamlitOS.classifiers =

    for l in loaded_classifier_nlu_refs:
        if 'converter' in l :
            loaded_classifier_nlu_refs.remove(l)
            continue
        if l not in classifier_components_usable : classifier_components_usable.append(l)

    classifier_components_selection   = st.sidebar.multiselect("Pick additional Classifiers",options=classifier_components_usable,default=loaded_classifier_nlu_refs,key = key)
    classifier_algos_to_load = list(set(classifier_components_selection) - set(loaded_classifier_nlu_refs))
    for embedder in classifier_algos_to_load:classifier_pipes.append(nlu.load(embedder))
    dfs = []
    all_classifier_cols=[]
    for p in classifier_pipes :
        df = p.predict(text, output_level=output_level, metadata=metadata, positions=positions)
        classifier_cols = StreamlitUtilsOS.get_classifier_cols(p)
        for c in classifier_cols :
            if c not in df.columns : classifier_cols.remove(c)

        if 'text' in df.columns: classifier_cols += ['text']
        elif 'document' in df.columns: classifier_cols += ['document']
        all_classifier_cols+= classifier_cols
        dfs.append(df)
    df = pd.concat(dfs, axis=1)
    df = df.loc[:,~df.columns.duplicated()]
    for c in all_classifier_cols :
        if c not in df.columns : all_classifier_cols.remove(c)
    all_classifier_cols = list(set(all_classifier_cols))

    if len(all_classifier_cols) == 0: st.warning('No classes detected')
    else :st.write(df[all_classifier_cols],key=key)


nlu.enable_streamlit_caching()
st.sidebar.write('lol') # elmo albert en.embed.bert.base_cased electra xlnet ar.embed.cbow biobert
visualize_classes(nlu.load('ner '),'hell oworld wahs tis up Peter Licks to FUCK pepeonle')