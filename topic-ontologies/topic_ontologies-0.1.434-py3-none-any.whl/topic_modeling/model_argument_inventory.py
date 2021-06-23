import sys
sys.path.insert(0,"/home/yamenajjour/git/topic-ontologies/")

from pyspark.sql import SparkSession
import argument_esa_model.esa_all_terms
import argument_esa_model.esa_top_n_terms
from conf.configuration import *
def get_vocab_size(model):
    if '-' in model:
        vocab_size=int(model.split("-")[-1])
    else:
        vocab_size=10
    return vocab_size

def dict_to_list(dictionary):
    vector  = []
    for key in sorted(dictionary):
        vector.append(dictionary[key])
    return vector



spark = SparkSession.builder.appName('topic-ontologies').config('master','yarn').getOrCreate()

spark_context= spark.sparkContext
URI = spark_context._gateway.jvm.java.net.URI
Path = spark_context._gateway.jvm.org.apache.hadoop.fs.Path
FileSystem = spark_context._gateway.jvm.org.apache.hadoop.fs.FileSystem
FsPermission = spark_context._gateway.jvm.org.apache.hadoop.fs.permission.FsPermission
fs = FileSystem.get(URI("hdfs://nn.hdfs.webis.de:8020"), spark_context._jsc.hadoopConfiguration())
fs.listStatus(Path('/user/befi8957'))
log4jLogger = spark_context._gateway.jvm.org.apache.log4j
LOGGER = log4jLogger.LogManager.getLogger(__name__)
set_cluster_mode()
def project_arguments(topic_ontology,model,dataset,is_testing):

    vocab_size=get_vocab_size(model)
    def project(argument):
        if is_testing:
            return dict_to_list({"a":0.3,"b":0.3,"c":0.4})
        set_cluster_mode()
        path_word2vec_model = get_path_topic_model('word2vec','word2vec')
        path_word2vec_vocab = get_path_vocab('word2vec')
        if model == 'esa':
            path_topic_model = get_path_topic_model('ontology-'+topic_ontology,model)
            vector = argument_esa_model.esa_all_terms.model_topic(path_topic_model,path_word2vec_model,path_word2vec_vocab,'cos',argument)
            return dict_to_list(vector)
        else:
            import nltk
            nltk.data.path.append('/mnt/ceph/storage/data-in-progress/topic-ontologies/nltk/')
            set_cluster_mode()
            path_corpus = get_path_source("ontology-"+topic_ontology)
            path_word2vec_model = get_path_topic_model('word2vec','word2vec')
            path_word2vec_vocab = get_path_vocab('word2vec')
            vector = argument_esa_model.esa_top_n_terms.model_topic(path_corpus,path_word2vec_model,path_word2vec_vocab,argument,vocab_size)
            return dict_to_list(vector)



    part_count=get_part_count(dataset)
    for part in range(0,part_count):
        LOGGER.info("Current corpus:"+str(part))
        LOGGER.warn("Current corpus:"+str(part))
        path_documents=get_path_preprocessed_documents_version(dataset,str(part))
        path_document_vectors = get_path_document_vectors_part(dataset,topic_ontology,model,part)
        documents_df  = spark.read.format("csv").option("header", "true").option("delimiter", ",", ).option('quote', '"').load(path_documents).na.drop()
        documents = documents_df.select("document").rdd.map(lambda r: r[0]).repartition(1000)
        ids = (documents_df.select("id").rdd.map(lambda r: r[0])).repartition(1000)
        vectors = documents.map(lambda document:project(document))
        ids_with_vectors=vectors.zip(ids)
        FileSystem.mkdirs(fs,Path(path_document_vectors),FsPermission(77777))
        LOGGER.warn("Lok: saving to"+str(path_document_vectors))
        ids_with_vectors.saveAsPickleFile(path_document_vectors)

model = sys.argv[2]
ontology = sys.argv[1]
dataset= sys.argv[3]

LOGGER.warn("Lok: processing %s %s %s"%(model,ontology,dataset))
project_arguments(ontology,model,dataset,False)