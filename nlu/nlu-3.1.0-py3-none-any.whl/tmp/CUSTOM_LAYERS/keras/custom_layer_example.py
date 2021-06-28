import nlu

b = nlu.load('bert')
data  = 'I love KERAS + NLU <3'
df = b.predict(data)
# CKL mat means th
np_bert_CKL_mat = df['word_embeddings@small_bert_L2_128_embeddings'].values
"""
 Tensor Docs https://www.tensorflow.org/guide/tensor 
 Ragged Tensor https://www.tensorflow.org/guide/tensor#ragged_tensors 
 Sparse Tensor https://www.tensorflow.org/guide/tensor#sparse_tensors

Righ now NLU returns NP arrays. One sucy thing is, if you take a column of Word Vectors in 


"""

from keras import backend as K
from keras.layers import Layer
import tensorflow as tf
import tensorflow as tf
import pandas as pd

def deduct_vector_dim(pipe, vec_col='word_embeddings@small_bert_L2_128_embeddings'):


class WordEmbeddingsLayer(tf.keras.layers.Layer):
    """ Tokenized and embed UNTOKENIZED RAW TEXT
    This layer has 2 modes
    1. If a Tensor with 1 String is input, the String will be tokenized and a tensor one vector per word is returned
    2. If a Tensor with more than 1 String is input (dim=S>1), then the layer will view this as a vector of independent Strings.
       Each String will the tokenized and embedded and a Matrix of  shape SxD will be returned
       where S is num Strings and D is dim of embedding"""
    def __init__(self, n_units=8):
        super().__init__()
        self.n_units = n_units
    def build(self, input_shape):
        self.nlu_model = nlu.load('bert')
        self.embed_key = 'word_embeddings@small_bert_L2_128_embeddings'

    def call(self, inputs, training=False):
        """
        Input Options, W=Words, N=Num Rows aka Documents
        AUTO-DETECT-TOKEN-MODE --- WORD EMBEDDINGS
        1. Input 1 Document per Tensor, 1xW --> Tensor Shape[0] = 1
        2. Input N Document per Tensor, NxW --> Tensor Shape[0] >1
        """
        pd_series       = pd.Series(tensor_of_strings.numpy())
        pd_embed_series = self.nlu_model.predict(pd_series, output_level='document')[self.embed_key].values

        # return tf.ones(1)
        return tf.matmul(inputs,inputs)


tensor_of_strings = tf.constant(["Gray wolf","Quick brown fox","Lazy dog"])
ragged_tensor  = tf.strings.split(tensor_of_strings)
layer = DoubleLinearLayer()
# x = tf.ones((3, 100))
# res = layer(x)

# TF->NP->PDS->SDF
pd_series = pd.Series(tensor_of_strings.numpy())
res = layer(tensor_of_strings)



print('yp',res)
print('yp',res)
print('yp',res)
print('yp',res)
data = 'yo'