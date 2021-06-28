SPARK_NLP_LICENSE =  "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2NDIyNzM5ODksImlhdCI6MTYxMDczNzk4OSwidW5pcXVlX2lkIjoiYjQyZTc3ODgtNTc2NS0xMWViLTgyMDgtNzIyM2RkN2MyNzY0In0.vXrrwHdBssA7X1D7yfved7nKzvpxvKAOOKViNBS19S_DBoPRyBX1AwoQaisi-3Wp3MFnHZNKl6EVPLb3xt4UXLDjWs_5Nr6l32DAx1VuEZCAvtGqAJZeJsV7cgrRrf3Gh8WM2XutZRgsqQn21pNNGDcmxLH_-4LfPOqzrL5nNbZ2RXT_U3mD6umK38nD6gHaOCDn_zbZsum3SSZ0yUybA8OaCFTE8nPv-fdREBYHmM3mKYwmHguJxJcQTkSEfayMDnqx2G6k90ZOo4LcblC9wHPigF3WtsRpsRd1s2DEDu8r9rqmqK2Uxl1bHl38KgIQBhE0Z26qUTW8Hg031QUFOA"
AWS_ACCESS_KEY_ID =  "AKIASRWSDKBGNTFDKLUV"
AWS_SECRET_ACCESS_KEY =  "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"
OCR_LICENSE                 = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJleHAiOjE2MzQyMjY4NDgsImlhdCI6MTYwMjYwNDQ0OCwidW5pcXVlX2lkIjoiNTQwYjU4ZDItMGQ2Yy0xMWViLWE0ZTAtNDJiYmNmMGU5Y2UyIn0.c-hgzBKdimyj7GtgDHQ3UjgNwSYWWdmKHlln3PFiu5b_b0wnodG2MJJ9rL1BXvBp2abW-6teQxA5j-7ZoB7Jl90xOMaoBtviUSvXdJMXQm7RN8y4zMFON2OnNDsfkt7kyyff5EI_7hD2M3pyDxtgr9DPaToXUR111o0MJq79_w_PG7GULNFZnNz73qXDw2fZpRG_aW0Akk6e8tJ2nkMP_YawUpLXSJHpGXMK6eBQ0qlBgk0y3ga__NqD062P6wyXXolrHQX40qXhA9vOnABUNz9PYzPMoGBdjmwrXMCbaSW8bX-dI5lLUOLQBcJSi4dQ7Jli_hhnHsdG4bIzZIVl9Q'
JSL_SECRET                  = '3.0.2-08d4231c2d0b95eaf306cf06e79d94f6567defe5'
# TODO TIME-SERIES-TOPIC-CHART -> TIME SERIES NER COUNT, LINE PLOT of HOW OFTEN EACH TOPIC OCCURS
# TODO VISUALIZE_STREAMLIT(HC=False) Visualized FULL UI with/withouth HC stuff  and code gen!
# TODO dropdown with ALL NLU REFS!
# TODO if RESOLUTION or RELATION PICEDK, make 2nd dropdown appear and make user pick NER model
# TODO, why not just make every viz applicable?
# TODO VECTOR SIMMILARITY
# TODO TOKEN ATTRIBUTES == JUST TABLE ---> BUT WITH TEXT AS HEADING!
import streamlit as st
import nlu
# TODO HYPERLINK OF MODELS TO MODELHUB!
# TODO MAKE MODEL SELECTION FOR ANY MODEL A MULTI SELECT!!
# TODO LATER FUNKY PLOTS
# Wind vector map! https://vega.github.io/vega-lite/examples/
# http://docs.bokeh.org/en/0.12.5/docs/reference/charts.html
# https://vega.github.io/vega-lite/examples/point_angle_windvector.html
nlu.auth(SPARK_NLP_LICENSE,AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,JSL_SECRET)
# Cache Pipe! # https://docs.streamlit.io/en/stable/caching.html#the-hash-funcs-parameter

st.title('NLU ❤️ Streamlit - Prototype your NLP startup in 0 lines of code')

sample_data = {
'ner' : 'Donald Trump from America and Angela Merkel from Germany love John Snow Labs software!',
'med_ner' : 'Peter has no cancer!',
'dependency' : 'Billy likes to go to the mall',
'relation' : 'MRI demonstrated infarction in the upper brain stem , left cerebellum and  right basil ganglia',
'assertion' : '''The human KCNJ9 (Kir 3.3, GIRK3) is a member of the G-protein-activated inwardly rectifying potassium (GIRK) channel family.', 'Here we describe the genomicorganization of the KCNJ9 locus on chromosome 1q21-23 as a candidate gene forType II diabetes mellitus in the Pima Indian population.', 'The gene spansapproximately 7.6 kb and contains one noncoding and two coding exons separated byapproximately 2.2 and approximately 2.6 kb introns, respectively.', 'We identified14 single nucleotide polymorphisms (SNPs), including one that predicts aVal366Ala substitution, and an 8 base-pair', '(bp) insertion/deletion.', 'Ourexpression studies revealed the presence of the transcript in various humantissues including pancreas, and two major insulin-responsive tissues: fat andskeletal muscle.', 'The characterization of the KCNJ9 gene should facilitate furtherstudies on the function of the KCNJ9 protein and allow evaluation of thepotential role of the locus in Type II diabetes.''',
'resolution':'''The patient is a 5-month-old infant who presented initially on Monday with a cold, cough, and runny nose for 2 days. Mom states she had no fever. Her appetite was good but she was spitting up a lot. She had no difficulty breathing and her cough was described as dry and hacky. At that time, physical exam showed a right TM, which was red. Left TM was okay. She was fairly congested but looked happy and playful. She was started on Amoxil and Aldex and we told to recheck in 2 weeks to recheck her ear. Mom returned to clinic again today because she got much worse overnight. She was having difficulty breathing. She was much more congested and her appetite had decreased significantly today. She also spiked a temperature yesterday of 102.6 and always having trouble sleeping secondary to congestion.'''

}

def get_list_of_model_type(m_type='', licensed=True, get_all= False):
    nlu_refs_of_type = []
    model_universe = nlu.Spellbook.pretrained_models_references
    for lang, models in model_universe.items():
        for nlu_ref, nlp_ref in model_universe[lang].items():
            if m_type in nlu_ref or get_all: nlu_refs_of_type.append(nlu_ref)
    if licensed:
        model_universe = nlu.Spellbook.pretrained_healthcare_model_references
        for lang, models in model_universe.items():
            for nlu_ref, nlp_ref in model_universe[lang].items():
                if m_type in nlu_ref or get_all: nlu_refs_of_type.append(nlu_ref)
    return nlu_refs_of_type

@st.cache(allow_output_mutation=True)
def get_pipe(model='ner'): return nlu.load(model)
def viz_HTML_dep(text,model2viz='dep.typed',return_pandas=False):
    """Just VIZ the svg"""
    if not return_pandas: get_pipe(model2viz).viz(text, write_to_streamlit=True)
    else :
        df = get_pipe(model2viz).predict(text, output_level='token')
        st.write(df)
def viz_HTML_ner(text,model2viz,return_pandas=False):
    """Split the CSS and HTML and viz them seperatly or it wont render properly"""
    if not return_pandas: get_pipe(model2viz).viz(text, write_to_streamlit=True)
    else :
        df = get_pipe(model2viz).predict(text, output_level='chunk')
        st.write(df)
def viz_HTML_assertion(text,model2viz='en.med_ner.clinical en.assert',return_pandas=False):
    """Viz resolution"""
    if not return_pandas: get_pipe(model2viz).viz(text, write_to_streamlit=True)
    else :
        df = get_pipe(model2viz).predict(text, output_level='chunk')
        st.write(df)
def viz_HTML_resolution(text,model2viz='med_ner.jsl.wip.clinical en.resolve_chunk.cpt_clinical',return_pandas=False):
    """Viz resolution"""
    if not return_pandas: get_pipe(model2viz).viz(text, write_to_streamlit=True)
    # if not return_pandas:
    #     HTML = get_pipe(model2viz).viz(text, return_html=True)
    #     CSS,HTML = HTML.split('</style>')
    #     CSS = CSS + '</style>'
    #     HTML = f'<div> {HTML} '
    #     st.markdown(CSS, unsafe_allow_html=True)
    #     st.markdown(HTML, unsafe_allow_html=True)
    else :
        output_level = 'chunk' if 'chunk' in model2viz else 'sentence'
        df = get_pipe(model2viz).predict(text, output_level=output_level)
        st.write(df)
def viz_HTML_relation(text, model2viz='en.med_ner.jsl.wip.clinical.greedy en.relation',return_pandas=False):
    """Viz resolution"""
    # if not return_pandas:
    #     HTML = get_pipe(model2viz).viz(text, return_html=True)
    #     st.markdown(HTML, unsafe_allow_html=True)
    if not return_pandas: get_pipe(model2viz).viz(text, write_to_streamlit=True)
    else:
        df = get_pipe(model2viz).predict(text, output_level='relation')
        st.write(df)
def viz_HTML_any_model_raw(text, model2viz='emotion'):
    """Viz resolution"""
    df = get_pipe(model2viz).predict(text)
    st.write(df)

def make_base_UI():
    # Model Selection UI
    #
    ner_models         = get_list_of_model_type('ner')
    resolve_models     = get_list_of_model_type('resolve')
    assert_models      = get_list_of_model_type('assert')
    relation_models    = get_list_of_model_type('relation')
    max_text_display_len = 35
    text_for_model     = st.text_area("Enter text you want to visualize and process below", 'Billy loves Berlin')
    text_for_model_to_draw = text_for_model if len(text_for_model)< 100 else f"{text_for_model[:max_text_display_len]}..."
    actions  = ['Visualize a model','Run any NLU ref and view pandas','Run custom NLU ref and view pandas','T-SNE']
    selected_action = st.sidebar.selectbox('Select an action',(actions))

    def draw_custom_NLU_ref_UI():
        st.sidebar.write('Define any combination of nlu_references and run')
                                                                                                                                                                                                                                                                                                                                        custom_NLU2viz      = st.sidebar.text_input('Define a custom NLU reference to pass to nlu.load() and view RAW pandas','emotion sentiment')
        run = st.sidebar.button('Run model')
        if run :
            code =f"""#Running NLU command:\n import nlu \nimport streamlit as st \ndf=nlu.load('{custom_NLU2viz}').predict('{text_for_model_to_draw}')\nst.write(df)"""
            st.code(code, language='python')
            viz_HTML_any_model_raw(text_for_model,custom_NLU2viz)
    def draw_any_NLU_ref_UI():
        all_models          = get_list_of_model_type(get_all=True)
        any_model_2viz  = st.sidebar.selectbox('Pick any model to run',(all_models))
        run = st.sidebar.button('Run model')
        if run :
            code =f"""#Running NLU command:\n import nlu \nimport streamlit as st \nnlu.load('{any_model_2viz}').predict('{text_for_model_to_draw}')\nst.write(df)"""
            st.code(code, language='python')
            viz_HTML_any_model_raw(text_for_model,any_model_2viz)
    def draw_viz_ui():
        ner_model2viz      = st.sidebar.selectbox('Pick a Named Entity Recognizer (NER) model',(ner_models))
        resolve_model2viz  = st.sidebar.selectbox('Pick a Resolver model',(resolve_models))
        assert_model2viz   = st.sidebar.selectbox('Pick a Assertion model',(assert_models))
        relation_model2viz = st.sidebar.selectbox('Pick a Relation extractor model',(relation_models))
        models_types_to_run = ['Named Entity Recognizer (NER)','Dependency Tree and Part of Speech Tags','Resolution', 'Relation','Assertion']
        model_type2viz = st.sidebar.selectbox('Select a mode type to run and visualize. ',(models_types_to_run))
        st.sidebar.write('Assertion, Relation and Resolver models will receive input from currently selected NER model.')
        return_pandas = st.sidebar.checkbox('Return RAW pandas from NLU')
        if return_pandas: st.sidebar.write('Visualization disabled')
        run = st.sidebar.button('Run model')
        if run :
            if model_type2viz in ['ner','med_ner','Named Entity Recognizer (NER)']:
                if not return_pandas : code =f"""#Running NLU command:\nimport nlu \nnlu.load('{ner_model2viz}').viz('{text_for_model_to_draw}',write_to_streamlit=True)"""
                else :   code =f"""#Running NLU command:\nimport nlu\nimport streamlit as st \ndf=nlu.load('{ner_model2viz}').predict('{text_for_model_to_draw})\nst.write(df)"""

                st.code(code, language='python')
                viz_HTML_ner(text_for_model,ner_model2viz,return_pandas)
            if model_type2viz == 'Dependency Tree and Part of Speech Tags':
                code =f"""#Running NLU command:\nimport nlu \nnlu.load('dep.typed').viz('{text_for_model_to_draw},write_to_streamlit=True')"""
                st.code(code, language='python')
                viz_HTML_dep(text_for_model,'dep.typed',return_pandas) # there is only 1 dep
            # models below require NER input
            if model_type2viz == 'Resolution':
                code =f"""#Running NLU command:\nimport nlu \nnlu.load('{ner_model2viz + ' ' + resolve_model2viz}').viz('{text_for_model_to_draw},write_to_streamlit=True')"""
                st.code(code, language='python')
                viz_HTML_resolution(text_for_model,ner_model2viz + ' ' + resolve_model2viz,return_pandas)
            if model_type2viz == 'Assertion':
                code =f"""#Running NLU command:\nimport nlu \nnlu.load('{ner_model2viz + ' ' + assert_model2viz}').viz('{text_for_model_to_draw},write_to_streamlit=True')"""
                st.code(code, language='python')
                viz_HTML_assertion(text_for_model,ner_model2viz + ' ' +  assert_model2viz,return_pandas)
            if model_type2viz == 'Relation':
                code =f"""#Running NLU command:\nimport nlu \nnlu.load('{ner_model2viz + ' ' + relation_model2viz}').viz('{text_for_model_to_draw}, write_to_streamlit=True')"""
                st.code(code, language='python')
                viz_HTML_relation(text_for_model,ner_model2viz + ' ' +  relation_model2viz,return_pandas)
    def draw_T_SNE_UI():
        embed_models         = get_list_of_model_type('embed')
        #1. Get dataset?
        #2  Get label col for hue
        embed_model2viz      = st.sidebar.selectbox('Select an Embedding',(embed_models))
        pipe = get_pipe(embed_model2viz)
        def deduct_embed_col(): pass
        def deduct_embed_dimension(): pass
        def get_T_SNE_low_dim_data(start_dim, target_dim=2 ): pass

    if selected_action ==   'Visualize a model':                         draw_viz_ui()
    elif selected_action == 'Run any NLU ref and view pandas':   draw_any_NLU_ref_UI()
    elif selected_action == 'Run custom NLU ref and view pandas':draw_custom_NLU_ref_UI()
    elif selected_action == 'T-SNE':draw_T_SNE_UI()
make_base_UI()

def show_ui_ner(): pass
def hide_ui_ner(): pass
def show_ui_dep(): pass
def hide_ui_dep(): pass
def show_ui_resolution(): pass
def hide_ui_resolution(): pass
def show_ui_relation(): pass
def hide_ui_relation(): pass
# TODO, each model has UI with tunable params/ filters, etc.
# if model2viz == 'ner' : show_ui_ner()# TODO
# if model2viz == 'dep.typed' : show_ui_dep()# TODO
# if model2viz == 'resolution' : show_ui_resolution()# TODO
# if model2viz == 'relation' : show_ui_relation()# TODO
# if model2viz == 'dep.typed' : show_ui_dep()# TODO












# import pandas as pd
# import numpy as np
#
# chart_data = pd.DataFrame(
#     np.random.randn(20, 3),
#     columns=['a', 'b', 'c'])
#
# st.line_chart(chart_data)
#
# map_data = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])
#
# st.map(map_data)
# options = st.multiselect(
#     'What are your favorite colors',
#     ['Green', 'Yellow', 'Red', 'Blue'],
#     ['Yellow', 'Red'])
#
# st.write('You selected:', options)

