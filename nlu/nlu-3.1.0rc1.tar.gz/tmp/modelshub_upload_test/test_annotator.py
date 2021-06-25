

"""
Test Any open source annotator class with this module.
you just need to call verify_uploaded_model_is_is_correct()
Param Info for verify_uploaded_model_is_is_correct():
ONLY USE either nlu_referenced_requirements OR nlp_referenced_requirements please.
model_path : str
    Path to where the component to load is. Either path to Pipeline or Model
nlu_referenced_requirements : List[str]
    a List of requirements. Should either be NLU or Spark NLP references to specific models, i.e. BIOBERT embeddings
nlp_referenced_requirements : List[Tuple[str,str]]
    A list of Tuples, where first element is SparkNLP Model reference and second Element is Language.



See
test_load_and_verify_pipeline()
test_load_and_verify_model_with_requirements_nlu_based()
test_load_and_verify_model_with_requirements_spark_based()
test_load_and_verify_model_with_no_storage_ref_requirement()
for example usage
"""
import nlu.pipe.component_resolution

""" Map SparkNLP Annotator Classes to load methods which will return corrosponding models when called with parameter
This map is actually not used because of the eval() call!
"""
# from sparknlp.annotator import *
# d = {
#     MultiClassifierDLModel : MultiClassifierDLModel.load ,
#     PerceptronModel : PerceptronModel.load,
#     ClassifierDLModel : ClassifierDLModel.load,
#     BertEmbeddings : BertEmbeddings.load,
#     AlbertEmbeddings : AlbertEmbeddings.load,
#     XlnetEmbeddings : XlnetEmbeddings.load,
#     WordEmbeddingsModel : WordEmbeddingsModel.load,
#     ElmoEmbeddings : ElmoEmbeddings.load,
#     BertSentenceEmbeddings : BertSentenceEmbeddings.load,
#     UniversalSentenceEncoder : UniversalSentenceEncoder.load,
#     TokenizerModel : TokenizerModel.load,
#     DocumentAssembler : DocumentAssembler.load,
#     SentenceDetectorDLModel : SentenceDetectorDLModel.load,
#     SentenceDetector : SentenceDetector.load,
#     ContextSpellCheckerModel : ContextSpellCheckerModel.load,
#     SymmetricDeleteModel : SymmetricDeleteModel.load,
#     NorvigSweetingModel : NorvigSweetingModel.load,
#     LemmatizerModel : LemmatizerModel.load,
#     NormalizerModel : NormalizerModel.load,
#     Stemmer : Stemmer.load,
#     NerDLModel : NerDLModel.load,
#     NerCrfModel : NerCrfModel.load,
#     LanguageDetectorDL : LanguageDetectorDL.load,
#     DependencyParserModel : DependencyParserModel.load,
#     TypedDependencyParserModel : TypedDependencyParserModel.load,
#     SentimentDLModel : SentimentDLModel.load,
#     SentimentDetectorModel : SentimentDetectorModel.load,
#     ViveknSentimentModel : ViveknSentimentModel.load,
#     Chunker : Chunker.load,
#     NGramGenerator : NGramGenerator.load,
#     ChunkEmbeddings : ChunkEmbeddings.load,
#     StopWordsCleaner : StopWordsCleaner.load,
#     TextMatcherModel : TextMatcherModel.load,
#     RegexMatcherModel : RegexMatcherModel.load,
#     DateMatcher : DateMatcher.load,
#     MultiDateMatcher : MultiDateMatcher.load,
#     T5Transformer : T5Transformer.load,
#     MarianTransformer : MarianTransformer.load,
#     PretrainedPipeline : PipelineModel.load,

## NEED MODEL VERSION OF THESE saved ( LICENSED!)
# ContextualParserModel
# - AssertionDLApproach
# - ChunkEntityResolverApproach
# - SentenceEntityResolverApproach
# - DeIdentification
# - RelationExtractionApproach  (NO DL VERSION!!)
# - GenericClassifierApproach  x?
# }

import json
from nlu.pipe.pipe_logic import PipelineQueryVerifier
from nlu.pipe.pipeline import  *
import os
from nlu.pipe.pipe_components import SparkNLUComponent
from pyspark.ml import PipelineModel
def NLP_ref_to_NLU_ref(nlp_ref,lang) :
    """Resolve a Spark NLP reference to a NLU reference"""
    nlu_namespaces_to_check = [nlu.Spellbook.pretrained_pipe_references, nlu.Spellbook.pretrained_models_references]
    for dict_ in nlu_namespaces_to_check:
        if lang in dict_.keys():
            for reference in dict_[lang]:
                if dict_[lang][reference] == nlp_ref:
                    return reference

def check_is_pipeline(path):
    # Folder should contain Stages
    if 'stages' in os.listdir(path) : return True
    return False
def check_is_model(path):
    # Folder should contain Metadata
    if 'metadata' in os.listdir(path) : return True
    return False
def verify_uploaded_model_is_is_correct(model_path:str,nlu_referenced_requirements = [], nlp_referenced_requirements = []):
    """ Use a Annotator Class and a list of either NLU or NLP requirement references to automatically build a Pipeline.
    ONLY USE either nlu_referenced_requirements OR nlp_referenced_requirements please.
    model_path : str
        Path to where the component to load is. Either path to Pipeline or Model
    nlu_referenced_requirements : List[str]
        a List of requirements. Should either be NLU or Spark NLP references to specific models, i.e. BIOBERT embeddings
    nlp_referenced_requirements : List[Tuple[str,str]]
        A list of Tuples, where first element is SparkNLP Model reference and second Element is Language.


    # 1. Build NLU_component class, CANNOT use nrmal builders, need special construction. REQUIRE INFOS FOR build_and_fix_pie process!
    # 2. Build dependency classes i.e. embeddings NLU_components via nlu.load() sub_emthod and get the resolved comonent
    # 3.
    # 2. Build Pipeline with trained anno + requiredments and run "Fix_urself()" magic call
    # 3. Build a Spark DF and RUn pipe, GG
    # 4. pythonfiy>?
    """
    if check_is_pipeline(model_path):
        return verify_pipeline(model_path)
    elif check_is_model(model_path):
            return verify_model(model_path,nlu_referenced_requirements, nlp_referenced_requirements)
    else:
        print("Neither STAGES or METADATA folder detected in unzipped folder. Make sure you include these folders")
        return False

def verify_pipeline(model_path:str,test_data = 'Hello world from John Snow Labs'):
    """
     Build pyspark Pipeline and transform data. No NLU usage
    """
    spark = sparknlp.start()
    df = spark.createDataFrame(pd.DataFrame({'text': test_data}, index=[0]))
    pipe = PipelineModel.load(model_path)
    res = pipe.transform(df)
    res.show()
    return res
def verify_model(model_path:str,nlu_referenced_requirements = [], nlp_referenced_requirements = [],test_data='Hello world from John Snow Labs '):
    """
     Build model with requirements
     Figures out class name by checking metadata json file
     assumes metadatra is always called part-00000
    """
    with open(model_path+'/metadata/'+'part-00000') as json_f:
        class_name = json.load(json_f)['class'].split('.')[-1]
        # The last element in the Class name can be used to just load the model from disk!
        # Just call eval on it, which will give you the actual Python class reference which should have a .load() method
        m = eval(class_name).load(model_path)
    component_type,nlu_anno_class, = resolve_annotator_class_to_nlu_component_info(class_name)
    # Wrap model with NLU Custom Model class so the NLU pipeline Logic knows what to do with it
    c = CustomModel(annotator_class=nlu_anno_class, component_type=component_type, model=m)
    pipe = NLUPipeline()
    pipe.add(c)

    # get requirements
    if len(nlu_referenced_requirements)==0 and len(nlp_referenced_requirements) == 0 :
        pipe = PipelineQueryVerifier.check_and_fix_nlu_pipeline(pipe)
        res = pipe.predict(test_data)
        print(res)
        return res
    elif len(nlu_referenced_requirements) >0:
        for r in nlu_referenced_requirements:
            pipe.add(nlu.pipe.component_resolution.nlu_ref_to_component(r))
    elif len(nlp_referenced_requirements) > 0:
        for r in nlu_referenced_requirements:
            # map back to NLU ref
            pipe.add(nlu.pipe.component_resolution.nlu_ref_to_component(NLP_ref_to_NLU_ref(r)))
    # run pipe with dependencies
    pipe = PipelineQueryVerifier.check_and_fix_nlu_pipeline(pipe)
    res = pipe.predict(test_data)
    print(res)
    return res
def resolve_annotator_class_to_nlu_component_info(anno_class ='LemmatizerModel'):
    """
    SparkNLUComponent.__init__(self, annotator_class, component_type)
    RECURISIVELY SEARCH through NLU COMPONENTS FOLDER for each class for a given <CLASSS>
    Find the file, which called <CLASS>.pretrained or just <CLASS> !!!
    In the folder containing that found file there will be the component_json info we need!]\
    """
    p = nlu.nlu_package_location+'components/'
    anno_class = anno_class+'.'

    import os
    for dirpath, dirs, files in os.walk(p):
        # search for folder that has the component info for that anno_class
        for filename in files:
            if '.py' not in filename or '.pyc' in filename : continue
            fname = os.path.join(dirpath,filename)
            if test_check_if_string_in_file(fname, anno_class):
                parts = dirpath.split('/')
                component_type = parts[-2]
                nlu_anno_class = parts[-1]
                component_type = component_type[:-1]
                return component_type,nlu_anno_class,
    print("COULD NOT FIND COMPONENT INFO FOR ANNO_CLASS", anno_class)
    return False

def test_check_if_string_in_file(file_name, string_to_search):
    """ Check if any line in the file contains given string """
    # Open the file in read only mode
    # print('reading ', file_name)
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False

class CustomModel(SparkNLUComponent):
    """ Builds a NLU Components with component info"""
    def __init__(self, annotator_class='sentiment_dl',  component_type='classifier', model = None):
        self.model = model
        SparkNLUComponent.__init__(self, annotator_class, component_type)
        # Make sure input/output cols match up with NLU defaukts
        if len(self.info.spark_input_column_names) == 1 :
            model.setInputCols(self.info.spark_input_column_names[0])
        else :
            model.setInputCols(self.info.spark_input_column_names)

        if len(self.info.spark_output_column_names) == 1 :
            model.setOutputCol(self.info.spark_output_column_names[0])
        else :
            model.setOutputCol(self.info.spark_output_column_names)

def test_load_and_verify_pipeline(): # OK
    # nlu.load('ner.onto') # Load a pipe to ~/cache_pretrained folder
    pipe_path='/home/loan/cache_pretrained/onto_recognize_entities_sm_en_2.4.0_2.4_1579730599257'
    res = verify_uploaded_model_is_is_correct(pipe_path)
    print(res.columns)
    res.show()
    if res is None :  return False # MODEL CAUSE A CRASH!
    else :  return True

def test_load_and_verify_model_with_requirements_nlu_based(): # OK
    # nlu.load('en.sentiment.twitter.use') # Load a model with storage ref requriements to your ~/cache_pretraiend folder
    model_path = '/home/loan/cache_pretrained/analyze_sentimentdl_use_twitter_en_2.7.1_2.4_1610993470852/stages/2_SentimentDLModel_eca587b575f7' #   Sentiment DL with USE requirements
    # requirements = ['use']
    # NLU can auto-resolve some storage_refs, but it will not work every time! Better be safe and pass actual reference to requirements
    res = verify_uploaded_model_is_is_correct(model_path)#,requirements)
    print(res.columns)
    print(res)
    if res is None :  return False # MODEL CAUSED A CRASH!
    else :  return True

def test_load_and_verify_model_with_no_storage_ref_requirement(): # OK
    # nlu.load('lemma') # Load a model with no storage ref to ~/cache_pretrained folder
    model_path = '/home/loan/cache_pretrained/lemma_bh_2.7.0_2.4_1610989221391' # Sample lemmatizer
    res = verify_uploaded_model_is_is_correct(model_path)
    print(res.columns)
    print(res)
    if res is None :  return False # MODEL CAUSED A CRASH!
    else :  return True

def test_load_and_verify_model_with_requirements_spark_based(): # OK
    # nlu.load('en.sentiment.twitter.use') # Load a model with storage ref requriements to your ~/cache_pretraiend folder
    model_path = '/home/loan/cache_pretrained/analyze_sentimentdl_use_twitter_en_2.7.1_2.4_1610993470852/stages/2_SentimentDLModel_eca587b575f7' #   Sentiment DL with USE requirements
    requirements = ['tfhub_use','en']
    # NLU can auto-resolve some storage_refs, but it will not work every time! Better be safe and pass actual reference to requirements
    res = verify_uploaded_model_is_is_correct(model_path,nlp_referenced_requirements=requirements)#,requirements)
    print(res.columns)
    print(res)
    if res is None :  return False # MODEL CAUSED A CRASH!
    else :  return True

# Test every verification method. Only Open Source annotators and dependencies will work.
test_load_and_verify_model_with_requirements_spark_based()

test_load_and_verify_pipeline()
test_load_and_verify_model_with_requirements_nlu_based()
test_load_and_verify_model_with_no_storage_ref_requirement()




































