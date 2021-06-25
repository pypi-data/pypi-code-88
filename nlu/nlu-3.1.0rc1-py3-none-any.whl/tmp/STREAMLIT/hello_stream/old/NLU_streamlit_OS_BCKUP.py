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
import modelhub_utils
from nlu.pipe.utils.modelhub_utils import ModelHubUtils

THE_MATRIX_ARCHITECT_SCRIPT = """
The Architect: Hello, Neo.
Neo: Who are you?
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




# TODO sentence/doc similarity
# display_vector_simmilarity()
# display_entity_simmilarity()
# display_pipe_information()
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


def find_ner_model(p):
    """Find NER component in pipe"""
    for c in p.components :
        if isinstance(c.model,(NerDLModel,NerCrfModel)):return c.model
    st.warning("No NER model in pipe")
    return None
def get_NER_tags_in_pipe(p):
    """Get NER tags in pipe, used for showing visualizable tags"""
    n = find_ner_model(p)
    if n is None : return []
    classes_predicted_by_ner_model = n.getClasses()
    split_iob_tags = lambda s : s.split('-')[1] if '-' in s else ''
    classes_predicted_by_ner_model = list(map(split_iob_tags,classes_predicted_by_ner_model))
    while '' in classes_predicted_by_ner_model : classes_predicted_by_ner_model.remove('')
    classes_predicted_by_ner_model = list(set(classes_predicted_by_ner_model))
    return classes_predicted_by_ner_model
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

def display_ner(
        pipe, # Nlu pipe
        text:str,
        ner_tags: Optional[List[str]] = None,
        show_label_select: bool = True,
        show_table: bool = True,
        title: Optional[str] = "Named Entities",
        colors: Dict[str, str] = {},
        show_color_selector: bool = False,
):
    if not show_color_selector :
        if title: st.header(title)
        if ner_tags is None: ner_tags = get_NER_tags_in_pipe(pipe)
        if show_label_select:
            exp = st.beta_expander("Select entity labels to highlight")
            label_select = exp.multiselect(
                "These labels are predicted by the NER model. Select which ones you want to display",
                options=ner_tags,default=list(ner_tags),)
        pipe.viz(text,write_to_streamlit=True, viz_type='ner',labels_to_viz=label_select,viz_colors=colors)
    else : # TODO WIP color select
        cols = st.beta_columns(3)
        exp = cols[0].beta_expander("Select entity labels to display")
        color = st.color_picker('Pick A Color', '#00f900')
        color = cols[2].color_picker('Pick A Color for a specific entity label', '#00f900')
        tag2color = cols[1].selectbox('Pick a ner tag to color', ner_tags)
        colors[tag2color]=color
def extract_name(component_or_pipe):
    name =''
    if hasattr(component_or_pipe.info,'nlu_ref') : name = component_or_pipe.info.nlu_ref
    elif hasattr(component_or_pipe,'storage_ref') : name = component_or_pipe.info.storage_ref
    elif hasattr(component_or_pipe,'nlp_ref') : name = component_or_pipe.info.nlp_ref
    return name
def display_dep_tree(
        pipe, #nlu pipe
        text,
        title: Optional[str] = "Dependency Parse & Part-of-speech tags",
    ):
    if title:st.header(title)
    pipe.viz(text,write_to_streamlit=True,viz_type='dep')

def visualize_tokens_and_class(
        pipe, # nlu pipe
        text,
        title: Optional[str] = "Token attributes & Classification results ",
        show_feature_select:bool =True,
        features:Optional[List[str]] = None,
        full_metadata: bool = True,
        output_level:str = 'token'
) -> None:
    """Visualizer for token attributes."""
    if title:st.header(title)
    df = pipe.predict(text, output_level=output_level, metadata=full_metadata)
    if not features : features = df.columns
    if show_feature_select :
        exp = st.beta_expander("Select token and classification attributes")
        features = exp.multiselect(
            "Token attributes",
            options=list(df.columns),
            default=list(df.columns),
        )
    st.dataframe(df[features])

def display_embed_vetor_information(embed_component,embed_mat):
    name = extract_name(embed_component)
    if name =='': name = 'See modelshub for more details'
    exp = st.beta_expander("Vector information")
    exp.code({"Vector Dimension ":embed_mat.shape[1],
              "Num Vectors":embed_mat.shape[0] + embed_mat.shape[0],
              'Vector Name':name})
def display_word_simmilarity(
        pipe, #nlu pipe
        default_texts: Tuple[str, str] = ("Donald Trump likes to party!", "Angela Merkel likes to party!"),
        threshold: float = 0.5,
        title: Optional[str] = "Vectors & Scalar Similarity & Vector Similarity & Embedding Visualizations  ",
        write_raw_pandas : bool = False ,
        display_embed_information:bool = True,
):

    """We visualize the following cases :
    1. Simmilarity between 2 words - > sim (word_emb1, word_emb2)
    2. Simmilarity between 2 sentences -> let weTW stand word word_emb of token T and sentence S
        2.1. Raw token level with merged embeddings -> sim([we11,we21,weT1], [we12,we22,weT2])
        2.2  Autogenerate sentemb, basically does 2.1 in the Spark NLP backend
        2.3 Already using sentence_embedder model -> sim(se1,se2)
    3. Simmilarity between token and sentence -> sim([we11,w21,wT1], se2)
    4. Mirrored 3
     """
    # https://scikit-learn.org/stable/modules/classes.html#module-sklearn.metrics.pairwise
    from sklearn.metrics.pairwise import distance_metrics
    if title:st.header(title)
    dist_metric_algos =distance_metrics()
    dist_algos = list(dist_metric_algos.keys())
    # TODO NORMALIZE DISTANCES TO [0,1] for non cosine
    if 'haversine'   in dist_algos    : dist_algos.remove('haversine') # not applicable in >2D
    if 'precomputed' in dist_algos  : dist_algos.remove('precomputed') # Not a dist
    exp = st.beta_expander("Select distance metric to compare vectors with")
    dist_algo_selection = exp.multiselect("Applicable distance metrics",options=dist_algos,default=['cosine'],)

    cols = st.beta_columns(2)
    text1 = cols[0].text_input("Text or word1",default_texts[0])
    text2 = cols[1].text_input("Text or word2",default_texts[1])
    data1 = pipe.predict(text1,output_level='token')
    data2 = pipe.predict(text2,output_level='token')
    e_col = find_embed_col(data1)
    e_com = find_embed_component(pipe)
    # get tokens for making indexes later
    tok1 = data1['token']
    tok2 = data2['token']
    emb2 = data2[e_col]
    emb1 = data1[e_col]
    embed_mat1 = np.array([x for x in emb1])
    embed_mat2 = np.array([x for x in emb2])
    if display_embed_information: display_embed_vetor_information(e_com,embed_mat1)


    def calc_sim(embed_mat1,embed_mat2,metric=''):
        # sim_mat = cosine_similarity(embed_mat1,embed_mat2)
        # sim_mat = chi2_kernel(embed_mat1,embed_mat2)
        sim_mat = dist_metric_algos[metric](embed_mat1,embed_mat2)
        return sim_mat
    for dist_algo in dist_algo_selection:
        sim_score = calc_sim(embed_mat1,embed_mat2,dist_algo)
        sim_score = pd.DataFrame(sim_score)
        sim_score.index   = tok1.values
        sim_score.columns = tok2.values
        if write_raw_pandas :st.write(sim_score)
        if sim_score.shape == (1,1) :
            sim_score = sim_score.iloc[0][0]
            if sim_score > threshold:
                st.success(sim_score)
                st.success(f'Scalar Similarity={sim_score} for distance metric={dist_algo}')
                st.error('No similarity matrix for only 2 tokens. Try entering at least 1 sentences in a field')
            else:
                st.error(f'Scalar Similarity={sim_score} for distance metric={dist_algo}')
        else :
            # todo try error plotly import
            import plotly.express as px
            # for tok emb, sum rows and norm by rows, then sum cols and norm by cols to generate a scalar from matrix
            scalar_sim_score  = np.sum((np.sum(sim_score,axis=0) / sim_score.shape[0])) / sim_score.shape[1]
            if scalar_sim_score > threshold:
                st.success(f'Scalar Similarity :{scalar_sim_score} for distance metric={dist_algo}')
            else:
                st.error(f'Scalar Similarity :{scalar_sim_score} for distance metric={dist_algo}')
            fig = px.imshow(sim_score, title=f'Simmilarity Matrix for distance metric={dist_algo}')
            st.write(fig)
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

def display_low_dim_embed_viz_token(
        pipe, # nlu pipe
        default_texts: List[str] = ("Donald Trump likes to party!", "Angela Merkel likes to party!", 'Peter HATES TO PARTTY!!!! :('),
        title: Optional[str] = "Lower dimensional Manifold visualization for word embeddings",
        write_raw_pandas : bool = False ,
        default_applicable_algos : List[str] = ('TSNE','PCA',),
        applicable_algos : List[str] = ("TSNE", "ISOMAP",'LLE','Spectral Embedding','MDS','PCA','SVD aka LSA','DictionaryLearning','FactorAnalysis','FastICA','KernelPCA',),  # LatentDirichletAllocation 'NMF',
        target_dimensions : List[int] = (1,2,3),
        show_algo_select : bool = True,
        show_color_select: bool = True,
        MAX_DISPLAY_NUM:int=100,
        display_embed_information:bool=True,
):
    # TODO dynamic columns infer for mouse over
    # NIOT CRASH [1], [a b], [ab]
    # todo dynamic deduct Tok vs Sent vs Doc vs Chunk embeds
    # todo selectable color features
    # todo selectable mouseover features
    # todo upload dataset
    if len(default_texts) > MAX_DISPLAY_NUM : default_texts = default_texts[:MAX_DISPLAY_NUM]
    if title:st.header(title)
    data = st.text_area('Enter N texts, seperated by new lines to visualize embeddings for ','\n'.join(default_texts))
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
            default=applicable_algos,
            # default=default_applicable_algos,
        )
    else : algos = default_applicable_algos
    if show_color_select: feature_to_color_by =  st.selectbox('Feature to color plots by ',['pos','sentiment',],0)
    text_col = 'token'
    predictions =   pipe.predict(data,output_level='token').dropna()
    e_col = find_embed_col(predictions)
    e_com = find_embed_component(pipe)
    embedder_name = extract_name(e_com)
    emb = predictions[e_col]
    mat = np.array([x for x in emb])
    if display_embed_information: display_embed_vetor_information(e_com,mat)
    for algo in algos :
        if len(mat.shape)>2 : mat =mat.reshape(len(emb),mat.shape[-1])
        # calc reduced dimensionality with every algo
        if 1 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,1).fit_transform(mat)
            x = low_dim_data[:,0]
            y = np.zeros(low_dim_data[:,0].shape)
            # tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col], 'sentiment':predictions.sentiment, })
            tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col], 'pos':predictions.pos, 'sentiment' : predictions.sentiment})
            fig = px.scatter(tsne_df, x="x", y="y",color=feature_to_color_by, hover_data=['text','sentiment', 'pos'],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig)
        if 2 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,2).fit_transform(mat)
            x = low_dim_data[:,0]
            y = low_dim_data[:,1]
            tsne_df =  pd.DataFrame({'x':x,'y':y, 'text':predictions[text_col], 'pos':predictions.pos, 'sentiment':predictions.sentiment, })
            fig = px.scatter(tsne_df, x="x", y="y",color=feature_to_color_by, hover_data=['text'],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig)
        if 3 in target_dimensions:
            low_dim_data = get_manifold_algo(algo,3).fit_transform(mat)
            x = low_dim_data[:,0]
            y = low_dim_data[:,1]
            z = low_dim_data[:,2]
            tsne_df =  pd.DataFrame({'x':x,'y':y,'z':z, 'text':predictions[text_col], 'pos':predictions.pos, 'sentiment':predictions.sentiment, })
            fig = px.scatter_3d(tsne_df, x="x", y="y", z='z',color=feature_to_color_by, hover_data=['text'],title=f'3D manifold with {algo} via {embedder_name}')
            st.write(fig)

def display_low_dim_embed_viz_sentence(
        pipe, # nlu pipe
        default_texts: List[str] = ("Donald Trump likes to party!", "Angela Merkel likes to party!", 'Peter HATES TO PARTTY!!!! :('),
        title: Optional[str] = "Lower dimensional Manifold visualization for Sentence Embeddings",
        write_raw_pandas : bool = False ,
        default_applicable_algos : List[str] = ('TSNE','PCA'),
        applicable_algos : List[str] = ("TSNE", "ISOMAP",'LLE','Spectral Embedding','MDS','PCA','SVD aka LSA','DictionaryLearning','FactorAnalysis','FastICA','KernelPCA',),  # LatentDirichletAllocation 'NMF',
        target_dimensions : List[int] = (1,2,3),
        show_algo_select : bool = True,
        show_color_select: bool = True,
        key : Optional[str] = 'sentence_embed_manifold',
        display_embed_information:bool=True,

):
    # TODO dynamic columns infer for mouse over
    # todo selectable mouseover features
    # todo upload dataset

    if title:st.header(title)
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
    model_selection:List[str],
    default_similarty_text:Tuple[str,str]= ('Donald Trump Likes to part', 'Angela Merkel likes to party'),
    default_ner_model2viz:Union[str, List[str]] = 'en.ner.onto.electra.base',   # models2viz
    default_sentence_embed_2viz:Union[str, List[str]] = 'en.embed_sentence.electra',
    default_word_embed_2viz:Union[str, List[str]] = 'en.embed.bert.small_L2_128 en.pos en.sentiment',
    extra_classifier_for_sentence_embedding_coloring:Union[str, List[str]] = 'en.sentiment',
    extra_classifier_for_word_embedding_coloring:Union[str, List[str]] = 'en.pos en.sentiment',

    default_manifold_text:List[str]= ('Donald Trump Likes to part', 'Angela Merkel likes to party', 'Peter HATES TO PARTTY!!!! :('),
    visualizers:List[str] = ( "dependency_tree", "ner",  "similarity_scalar", 'similarity_matrix' "token", "embedding_word",'classification','embedding_sentence'), #viz2apply(#
    show_side_header:bool=True,
    show_models_info:bool = True,
    # Side model selection params
    show_model_select:bool = True,
    show_ner_model_select:bool = True,
    show_word_embed_model_select:bool = True,
    show_sentence_embed_model_select:bool = True,
    show_classifier_model_select:bool = True,
    show_viz_selection:bool = True,
    )->None:
    """Visualize either individual building blocks for streamlit or a full UI to experiment and explore models with

    """
    st.title('NLU ❤️ Streamlit - Prototype your NLP startup in 0 lines of code')

    if show_side_header :     visualize_side_header()
    if isinstance(default_ner_model2viz, List)       : default_ner_model2viz = ' '.join(default_ner_model2viz)
    if isinstance(default_sentence_embed_2viz, List)       : default_ner_model2viz = ' '.join(default_ner_model2viz)
    ner_model_2_viz     = default_ner_model2viz
    word_embed_2viz     = default_word_embed_2viz     +' '  +extra_classifier_for_word_embedding_coloring
    sentence_embed_2viz = default_sentence_embed_2viz +' '  +extra_classifier_for_sentence_embedding_coloring

    text    = st.text_area("Enter text you want to visualize below", text)

    if show_model_select :
        st.sidebar.checkbox('Show generated code samples')
        if show_ner_model_select  :
            ner_model_2_viz = st.sidebar.selectbox("Select a NER model",model_selection,index=model_selection.index(default_ner_model2viz.split(' ')[0]),)
        if show_classifier_model_select  :
            classifier_models = list(set(nlu.get_components('classify') + nlu.get_components('sentiment', include_pipes=True) +  nlu.get_components('pos')))
            classifier_2viz = st.sidebar.selectbox('Select a classifier',classifier_models,index=classifier_models.index(extra_classifier_for_word_embedding_coloring.split(' ')[-1]))

        if show_sentence_embed_model_select  :
            sentence_embed_models = nlu.get_components('embed_sentence')
            sentence_embed_2viz = st.sidebar.selectbox('Select a Sentence Embedding',sentence_embed_models,index=sentence_embed_models.index(default_sentence_embed_2viz.split(' ')[0]))
        if show_word_embed_model_select  :
            word_embed_models = nlu.get_components('embed.')
            word_embed_2viz = st.sidebar.selectbox('Select a Word Embedding',word_embed_models,index=word_embed_models.index(default_word_embed_2viz.split(' ')[0]))
            submit    = st.sidebar.button('Run model on input')
    active_visualizers = visualizers
    if show_viz_selection: active_visualizers = st.sidebar.multiselect("Visualizers",options=visualizers,default=visualizers)
    word_embed_2viz     = word_embed_2viz + ' ' + extra_classifier_for_word_embedding_coloring
    sentence_embed_2viz = sentence_embed_2viz + ' ' + extra_classifier_for_sentence_embedding_coloring


    all_models = ner_model_2_viz + ' en.dep.typed '  + word_embed_2viz +' ' +sentence_embed_2viz
    if show_models_info : display_model_info(all_models)



    if 'embedding_sentence' in active_visualizers :
        sentence_embed_pipe = get_pipe(sentence_embed_2viz)
        display_low_dim_embed_viz_sentence(sentence_embed_pipe, default_manifold_text)
    if 'embedding_word' in active_visualizers :
        word_embed_pipe = get_pipe(word_embed_2viz)
        display_low_dim_embed_viz_token(word_embed_pipe, default_manifold_text)




def visualize_IU():
    """Viz NLU UI"""
    # Get a list of all NER models and define default input text
    ner_models = nlu.get_components('ner',include_pipes=True)
    default_text = "Sundar Pichai is the CEO of Google."
    viz_streamlit(default_text,ner_models, default_manifold_text=THE_MATRIX_ARCHITECT_SCRIPT.split('\n'))
# nlu_streamlit.sh
# TODO NGROK INTEGRATION - 1liner for demo pyngrok
# Split releases
# ask ida for emdium posts
# NER_COLORS = {}
# TODO VIZ 4 dataset
# TODO TIME SERIES VIZ FOR DATASETS

"""
nlu.load(<M>).viz_streamlit(default_text,ner_models, default_manifold_text=THE_MATRIX_ARCHITECT_SCRIPT.split('\n'))
nlu.load('ner').viz(write_to_streamlit=True)  
nlu.lod().v
"""
visualize_IU()









# all_models = nlu.get_components('',get_all=True)
# ner_model_selection = st.sidebar.selectbox(
#     "ALL Model",
#     all_models,
#     # index=ner_models.index('en.ner.onto'),
# )
# embed_model = st.sidebar.selectbox(
#     "Model",
#     model_names,
#     index=default_model_index,
#     key=f"{key}_visualize_models",
#     format_func=format_func,
# )
#
# classifier_model = st.sidebar.selectbox(
#     "Model",
#     model_names,
#     index=default_model_index,
#     key=f"{key}_visualize_models",
#     format_func=format_func,
# )
#
# simm_algo = st.sidebar.selectbox(
#     "Model",
#     model_names,
#     index=default_model_index,
#     key=f"{key}_visualize_models",
#     format_func=format_func,
# )
#
# dim_reduce_algo = st.sidebar.selectbox(
#     "Model",
#     model_names,
#     index=default_model_index,
#     key=f"{key}_visualize_models",
#     format_func=format_func,
# )
