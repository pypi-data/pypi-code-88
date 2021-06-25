import nlu

b = nlu.load('bert')
data  = 'I love PYOTRCH + NLU <3'
df = b.predict(data)
# CKL mat means th
np_bert_CKL_mat = df['word_embeddings@small_bert_L2_128_embeddings'].values()
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

class DoubleLinearLayer(tf.keras.layers.Layer):
    def __init__(self, n_units=8):
        super().__init__()
        self.n_units = n_units

    def build(self, input_shape):
        self.weights1 = self.add_weight(
            "weights1",
            shape=(int(input_shape[-1]), self.n_units),
            initializer=tf.keras.initializers.RandomNormal(),
        )
        self.weights2 = self.add_weight(
            "weights2",
            shape=(self.n_units, self.n_units),
            initializer=tf.keras.initializers.RandomNormal(),
        )

    def call(self, inputs):
        x = tf.matmul(inputs, self.weights1)
        return tf.matmul(x, self.weights2)

layer = DoubleLinearLayer()
x = tf.ones((3, 100))
layer(x)


print('yp')
print('yp')
print('yp')
print('yp')
data = 'yo'