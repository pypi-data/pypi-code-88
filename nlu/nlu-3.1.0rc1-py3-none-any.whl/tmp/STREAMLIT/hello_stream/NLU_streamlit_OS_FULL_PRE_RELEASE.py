import nlu
from nlu.discovery import Discoverer
from nlu.pipe.utils.storage_ref_utils import StorageRefUtils
from typing import List, Tuple, Optional, Dict, Union
import streamlit as st
from nlu.utils.modelhub.modelhub_utils import ModelHubUtils
import numpy as np
import pandas as pd
from nlu.pipe.viz.streamlit_viz.streamlit_utils_OS import StreamlitUtilsOS
from nlu.pipe.viz.streamlit_viz.gen_streamlit_code import get_code_for_viz
from nlu.pipe.viz.streamlit_viz.styles import _set_block_container_style
import random

import numpy as np
import pandas as pd
import streamlit as st
import nlu
from typing import List, Sequence, Tuple, Optional, Dict, Union, Callable
import streamlit as st
import spacy
from spacy.language import Language
from spacy import displacy
from sparknlp.annotator import  *
from nlu.pipe.utils.modelhub_utils import ModelHubUtils
from nlu.utils.modelhub.modelhub_utils import ModelHubUtils

THE_MATRIX_ARCHITECT_SCRIPT = """Neo: Who are you?
The Architect: Hello, Neo.
Neo: Who are you?
Neo: There are only two possible explanations: either no one told me, or no one knows.
The Architect: Precisely. As you are undoubtedly gathering, the anomaly's systemic, creating fluctuations in even the most simplistic equations.The Architect: Hello, Neo.
Neo: Who are you?
Neo: There are only two possible explanations: either no one told me, or no one knows.
The Architect: Precisely. As you are undoubtedly gathering, the anomaly's systemic, creating fluctuations in even the most simplistic equations.
The Architect: Hello, Neo.
Neo: Who are you?
Neo: There are only two possible explanations: either no one told me, or no one knows.
The Architect: Precisely. As you are undoubtedly gathering, the anomaly's systemic, creating fluctuations in even the most simplistic equations.
"""
THE_MATRIX_ARCHITECT_SCRIPT2= """
Neo: There are only two possible explanations: either no one told me, or no one knows.
The Architect: Precisely. As you are undoubtedly gathering, the anomaly's systemic, creating fluctuations in even the most simplistic equations.
Once again, the responses of other Neos appear on the monitors: "You can't control me! Fuck you! I'm going to kill you! You can't make me do anything!
Neo: Choice. The problem is choice.
The scene cuts to Trinity fighting an agent, and then back to the Architect's room
The Architect: The first matrix I designed was quite naturally perfect, it was a work of art, flawless, sublime. A triumph equaled only by its monumental failure. The inevitability of its doom is as apparent to me now as a consequence of the imperfection inherent in every human being, thus I redesigned it based on your history to more accurately reflect the varying grotesqueries of your nature. However, I was again frustrated by failure. I have since come to understand that the answer eluded me because it required a lesser mind, or perhaps a mind less bound by the parameters of perfection. Thus, the answer was stumbled upon by another, an intuitive program, initially created to investigate certain aspects of the human psyche. If I am the father of the matrix, she would undoubtedly be its mother.
Neo: The Oracle.
The Architect: Please. As I was saying, she stumbled upon a solution whereby nearly 99% of all test subjects accepted the program, as long as they were given a choice, even if they were only aware of the choice at a near unconscious level. While this answer functioned, it was obviously fundamentally flawed, thus creating the otherwise contradictory systemic anomaly, that if left unchecked might threaten the system itself. Ergo, those that refused the program, while a minority, if unchecked, would constitute an escalating probability of disaster.
Neo: This is about Zion.
The Architect: You are here because Zion is about to be destroyed. Its every living inhabitant terminated, its entire existence eradicated.
Neo: Bullshit.
The responses of other Neos appear on the monitors: "Bullshit!"
The Architect: Denial is the most predictable of all human responses. But, rest assured, this will be the sixth time we have destroyed it, and we have become exceedingly efficient at it.
Scene cuts to Trinity fighting an agent, and then back to the Architects room.
The Architect: The function of the One is now to return to the source, allowing a temporary dissemination of the code you carry, reinserting the prime program. After which you will be required to select from the matrix 23 individuals, 16 female, 7 male, to rebuild Zion. Failure to comply with this process will result in a cataclysmic system crash killing everyone connected to the matrix, which coupled with the extermination of Zion will ultimately result in the extinction of the entire human race.
Neo: You won't let it happen, you can't. You need human beings to survive.
The Architect: There are levels of survival we are prepared to accept. However, the relevant issue is whether or not you are ready to accept the responsibility for the death of every human being in this world.
The Architect presses a button on a pen that he is holding, and images of people from all over the matrix appear on the monitors
The Architect: It is interesting reading your reactions. Your five predecessors were by design based on a similar predication, a contingent affirmation that was meant to create a profound attachment to the rest of your species, facilitating the function of the one. While the others experienced this in a very general way, your experience is far more specific. Vis-a-vis, love.
Images of Trinity fighting the agent from Neo's dream appear on the monitors
Neo: Trinity.
The Architect: Apropos, she entered the matrix to save your life at the cost of her own.
Neo: No!
The Architect: Which brings us at last to the moment of truth, wherein the fundamental flaw is ultimately expressed, and the anomaly revealed as both beginning, and end. There are two doors. The door to your right leads to the source, and the salvation of Zion. The door to the left leads back to the matrix, to her, and to the end of your species. As you adequately put, the problem is choice. But we already know what you're going to do, don't we? Already I can see the chain reaction, the chemical precursors that signal the onset of emotion, designed specifically to overwhelm logic, and reason. An emotion that is already blinding you from the simple, and obvious truth: she is going to die, and there is nothing that you can do to stop it.
Neo walks to the door on his left
The Architect: Humph. Hope, it is the quintessential human delusion, simultaneously the source of your greatest strength, and your greatest weakness.
Neo: If I were you, I would hope that we don't meet again.
The Architect: We won't.
End Scene
"""

# nlu_streamlit.sh
# TODO NGROK INTEGRATION - 1liner for demo pyngrok
# Split releases
# ask ida for emdium posts
# NER_COLORS = {}
# TODO VIZ 4 dataset
# TODO TIME SERIES VIZ FOR DATASETS
# https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html#sklearn.decomposition.TruncatedSVD
@st.cache(allow_output_mutation=True)
def get_pipe(model='ner'): return nlu.load(model)
def visualize_side_header():
    HTML_logo = """
<div>
  <a href="https://www.johnsnowlabs.com/">
     <img src="https://nlp.johnsnowlabs.com/assets/images/logo.png" width="300"  height="100" >
   </a>
</div>
    """
    st.sidebar.markdown(HTML_logo, unsafe_allow_html=True)
def find_embed_col(df, search_multi=False):
    """Find col that contains embed"""
    if not search_multi:
        for c in df.columns:
            if 'embed'in c : return c
    else:
        e_cols =[]
        for c in df.columns:
            if 'embed'in c : e_cols.append(c)
    return  e_cols
def find_embed_component(p):
    """Find NER component in pipe"""
    for c in p.components :
        if 'embed' in c.info.outputs[0] : return c
    st.warning("No Embed model in pipe")
    return None
def display_model_info(model2viz):
    """Display Links to Modelhub for every NLU Ref loaded"""
    default_modelhub_link = 'https://modelshub.johnsnowlabs.com/'
    nlu_refs = set(model2viz.split(' '))
    for nlu_ref in nlu_refs :
        model_hub_link = ModelHubUtils.get_url_by_nlu_refrence(nlu_ref)
        if model_hub_link is not None :
            st.sidebar.write(f"[Model info for {nlu_ref}]({model_hub_link})")
        else :
            st.sidebar.write(f"[Model info for {nlu_ref}]({default_modelhub_link})")
def extract_name(component_or_pipe):
    name =''
    if hasattr(component_or_pipe.info,'nlu_ref') : name = component_or_pipe.info.nlu_ref
    elif hasattr(component_or_pipe,'storage_ref') : name = component_or_pipe.info.storage_ref
    elif hasattr(component_or_pipe,'nlp_ref') : name = component_or_pipe.info.nlp_ref
    return name
def display_embed_vetor_information(embed_component,embed_mat):
    name = extract_name(embed_component)
    if name =='': name = 'See modelshub for more details'
    exp = st.beta_expander("Vector information")
    exp.code({"Vector Dimension ":embed_mat.shape[1],
              "Num Vectors":embed_mat.shape[0] + embed_mat.shape[0],
              'Vector Name':name})
from sklearn.manifold import TSNE, Isomap, LocallyLinearEmbedding, MDS, SpectralEmbedding
from sklearn.decomposition import TruncatedSVD,DictionaryLearning, FactorAnalysis, FastICA, KernelPCA, PCA
def get_manifold_algo(algo,dim):
    # manifold
    if algo=='TSNE' : return TSNE(n_components=dim)
    if algo=='ISOMAP' : return Isomap(n_components=dim)
    if algo=='LLE' : return LocallyLinearEmbedding(n_components=dim)
    if algo=='Spectral Embedding' : return  SpectralEmbedding(n_components=dim)
    if algo=='MDS' : return MDS(n_components=dim)
    # Matrix Decomposition
    if algo== 'PCA' : return PCA(n_components=dim)
    if algo== 'SVD aka LSA' : return TruncatedSVD(n_components=dim)
    if algo =='DictionaryLearning': return DictionaryLearning(n_components=dim)
    if algo =='FactorAnalysis': return FactorAnalysis(n_components=dim)
    if algo =='FastICA': return FastICA(n_components=dim)
    if algo =='KernelPCA': return KernelPCA(n_components=dim)
    # not applicable because negative values, todo we could just take absolute values of all embeds..
    # if algo =='LatentDirichletAllocation': return LatentDirichletAllocation(n_components=dim)
    # if algo =='NMF': return NMF(n_components=dim)


import numpy as np
import plotly.express as px


def display_low_dim_embed_viz_sentence(
        pipe, # nlu pipe
        default_texts: List[str] = ("Donald Trump likes to party!", "Angela Merkel likes to party!", 'Peter HATES TO PARTTY!!!! :('),
        title: Optional[str] = "Lower dimensional Manifold visualization for Sentence Embeddings",
        sub_title: Optional[str] = "`todo subtileme`",
        write_raw_pandas : bool = False ,
        default_applicable_algos : List[str] = ('TSNE','PCA'),
        applicable_algos : List[str] = ("TSNE", "ISOMAP",'LLE','Spectral Embedding','MDS','PCA','SVD aka LSA','DictionaryLearning','FactorAnalysis','FastICA','KernelPCA',),  # LatentDirichletAllocation 'NMF',
        target_dimensions : List[int] = (1,2,3),
        show_algo_select : bool = True,
        show_color_select: bool = True,
        key : Optional[str] = 'sentence_embed_manifold',
        display_embed_information:bool=True,
):
    # TODO dynamic columns infer for mouse over, sentence/doc level classifier results applicable!!!
    # todo selectable mouseover features
    # todo upload dataset

    if title:st.header(title)
    if sub_title:st.header(title)
    data = st.text_area('Enter N texts, seperated by new lines to visualize embeddings for ','\n'.join(default_texts),key=key)
    data = data.split("\n")
    while '' in data : data.remove('')
    if len(data)<=1:
        st.error("Please enter more than 2 lines of text, seperated by new lines (hit <ENTER>)")
        return

    if show_algo_select:
        exp = st.beta_expander("Select dimension reduction technique to apply")
        algos = exp.multiselect(
            "Reduce embedding dimensionality to something visualizable",
            options=applicable_algos,
            key=key,
            # default=default_applicable_algos,
        default=applicable_algos,
        )
    else : algos = default_applicable_algos
    cols = st.beta_columns(2)
    if show_color_select: feature_to_color_by = cols[0].selectbox('Feature to color plots by ',['sentiment',],0,key=key)

    detect_sentences = cols[1].checkbox("Detect sentences automatically", value=True)
    output_level = 'sentence' if detect_sentences  else 'document'
    text_col = 'sentence'
    predictions =   pipe.predict(data,output_level=output_level).dropna()
    e_col = find_embed_col(predictions)
    e_com = find_embed_component(pipe)
    embedder_name = extract_name(e_com)
    if embedder_name =='': embedder_name = 'See modelshub for more details'

    emb = predictions[e_col]
    mat = np.array([x for x in emb])
    if display_embed_information: display_embed_vetor_information(e_com,mat)
    for algo in algos :
        # calc reduced dimensionality with every algo
        if 1 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,1).fit_transform(mat)
            x = low_dim_data[:,0]
            y = np.zeros(low_dim_data[:,0].shape)
            # tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col], 'sentiment':predictions.sentiment, })
            tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col],  'sentiment' : predictions.sentiment})
            fig = px.scatter(tsne_df, x="x", y="y",color=feature_to_color_by, hover_data=['text','sentiment', ],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig,key=key)
        if 2 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,2).fit_transform(mat)
            x = low_dim_data[:,0]
            y = low_dim_data[:,1]
            tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col],'sentiment':predictions.sentiment, })
            fig = px.scatter(tsne_df, x="x", y="y",color=feature_to_color_by, hover_data=['text','sentiment'],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig,key=key)
        if 3 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,3).fit_transform(mat)
            x = low_dim_data[:,0]
            y = low_dim_data[:,1]
            z = low_dim_data[:,2]
            tsne_df =  pd.DataFrame({'x':x,'y':y,'z':z, 'text':predictions[text_col],  'sentiment':predictions.sentiment, })
            fig = px.scatter_3d(tsne_df, x="x", y="y", z='z',color=feature_to_color_by, hover_data=['text','sentiment'],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig,key=key)



def viz_streamlit(
    text:Union[str, List[str], pd.DataFrame, pd.Series], # text 2 viz
    default_ner_model2viz:Union[str, List[str]] = 'en.ner.onto.electra.base',   # models2viz
    default_sentence_embed_2viz:Union[str, List[str]] = 'en.embed_sentence.electra',
    default_word_embed_2viz:Union[str, List[str]] = 'en.embed.bert.small_L2_128 en.pos en.sentiment',
    extra_classifier_for_sentence_embedding_coloring:Union[str, List[str]] = 'en.sentiment',
    extra_classifier_for_word_embedding_coloring:Union[str, List[str]] = 'en.pos en.sentiment',
    default_manifold_text:List[str]= ('Donald Trump Likes to part', 'Angela Merkel likes to party', 'Peter HATES TO PARTTY!!!! :('),
    show_side_header:bool=True,
    show_word_embed_model_select:bool = True,
    show_sentence_embed_model_select:bool = True,
    )->None:
    """Visualize either individual building blocks for streamlit or a full UI to experiment and explore models with

    """
    st.title('NLU ❤️ Streamlit - Prototype your NLP startup in 0 lines of code')

    if show_side_header :     visualize_side_header()
    if isinstance(default_ner_model2viz, List)       : default_ner_model2viz = ' '.join(default_ner_model2viz)
    if isinstance(default_sentence_embed_2viz, List)       : default_ner_model2viz = ' '.join(default_ner_model2viz)
    word_embed_2viz     = default_word_embed_2viz     +' '  +extra_classifier_for_word_embedding_coloring
    sentence_embed_2viz = default_sentence_embed_2viz +' '  +extra_classifier_for_sentence_embedding_coloring

    text    = st.text_area("Enter text you want to visualize below", text)

    #
    # if show_sentence_embed_model_select  :
    #     sentence_embed_models = nlu.get_components('embed_sentence')
    #     sentence_embed_2viz = st.sidebar.selectbox('Select a Sentence Embedding',sentence_embed_models,index=sentence_embed_models.index(default_sentence_embed_2viz.split(' ')[0]))
    # if show_word_embed_model_select  :
    #     word_embed_models = nlu.get_components('embed.')
    #     word_embed_2viz = st.sidebar.selectbox('Select a Word Embedding',word_embed_models,index=word_embed_models.index(default_word_embed_2viz.split(' ')[0]))
    # word_embed_2viz     = word_embed_2viz + ' ' + extra_classifier_for_word_embedding_coloring
    # sentence_embed_2viz = sentence_embed_2viz + ' ' + extra_classifier_for_sentence_embedding_coloring


    active_visualizers = ['embedding_sentence','embedding_word']

    if 'embedding_word' in active_visualizers :
        word_embed_pipe = get_pipe('ner sentiment pos ') # TODO PARAM pize get pipez
        display_low_dim_embed_viz_token(word_embed_pipe, default_manifold_text, applicable_algos=['TSNE','LLE'])
    # if 'embedding_sentence' in active_visualizers :
    #     sentence_embed_pipe = get_pipe(sentence_embed_2viz)
    #     display_low_dim_embed_viz_sentence(sentence_embed_pipe, default_manifold_text)
# Get a list of all NER models and define default input text
ner_models = nlu.get_components('ner',include_pipes=True)
default_text = "Sundar Pichai is the CEO of Google."


nlu.enable_streamlit_caching()
viz_streamlit(default_text,ner_models, default_manifold_text=THE_MATRIX_ARCHITECT_SCRIPT.split('\n'))



# TODO MULTI-COL-LAYOUT
# TODO Multi embed select and infer



