from typing import Tuple, Union

import pandas as pd
import tensorflow as tf

from sui.toolbox.preprocessing import one_hot, standardization
from sui.dl.initializers import get_init
from sui.dl.optimizers import get_opti


class FM:
    def __init__(self, categorical_feats: Union[list, tuple] = None, numerical_feats: Union[list, tuple] = None,
            learning_rate: float = 0.1, is_one_hot: bool = True, is_standardization: bool = True,
            loss: str = 'sigmoid', optimizer='ftrl',
            vector_size: int = 30, initializer='glorotuniform', bias: float = 0.0):
        super().__init__()
        self.categorical_feats = categorical_feats
        self.numerical_feats = numerical_feats
        self.learning_rate = learning_rate
        self.is_one_hot = is_one_hot
        self.is_standardization = is_standardization
        self.loss = loss
        self.optimizer = get_opti(optimizer)(learning_rate=self.learning_rate, )
        self.vector_size = vector_size
        self.initializer = get_init(initializer)

        self.fields = None
        self.bias = tf.Variable(initial_value=bias, dtype=tf.float32)
        self.linear_weight = None
        self.weight_matrix = None

    def train(self, X_, y, epochs: int = 50, is_preprocess: bool = True, init_gauss: Tuple[float] = (0, 0.2),
            shuffle=10000):
        X_ = self.preprocess(X_).to_numpy() if is_preprocess else X_
        # initialize the weight of the model
        if self.linear_weight is None or self.weight_matrix is None:
            self._init_weights(X_=X_, init_gauss=init_gauss)

        for epoch in range(epochs):
            train_set = tf.data.Dataset.from_tensor_slices((X_, y)).shuffle(shuffle)
            epoch_loss = 0.0
            for train_sample in train_set:
                x_sample = tf.cast(train_sample[0], tf.float32)
                y_sample = tf.cast(train_sample[1], tf.float32)

                # 1-order
                first_order_sum = tf.einsum('f,f->', self.linear_weight, x_sample)

                # 2-order
                sum_of_all_interaction = tf.einsum('fk,f->k', self.weight_matrix, x_sample)
                sum_of_all_interaction = sum_of_all_interaction ** 2

                weight_square = tf.einsum('fk,fk->fk', self.weight_matrix, self.weight_matrix)
                x_square = tf.einsum('f,f->f', x_sample, x_sample)
                overlapped_interaction = tf.einsum('fk,f->k', weight_square, x_square)

                second_order_sum = 0.5 * tf.einsum('k->', sum_of_all_interaction - overlapped_interaction)

                # predict the y_hat
                y_hat = self.bias + first_order_sum + second_order_sum
                print('y_sample:', y_sample)
                print('y_hat:', y_hat)
                # batch_loss = get_loss(self.loss)(label=y_sample, logits=y_hat)
                batch_loss = tf.keras.optimizers.Ftrl(label=y_sample, logits=y_hat)
                if batch_loss < 0:
                    print('Batch Loss:', batch_loss)
                    print('Learning Speed:', self.learning_rate * batch_loss * y_sample)
                print('Original loss:', batch_loss)
                self._update_weight(x_sample=x_sample, loss=self.learning_rate * tf.reduce_mean(batch_loss))
                epoch_loss += batch_loss
                # print(epoch_loss)
            mean_loss = tf.keras.metrics.Mean(name='train_loss')
            print('epoch: {} ==> loss: {}'.format(epoch + 1, mean_loss(epoch_loss)))
            break

    def preprocess(self, X_):
        self._check_feats(X_)

        X_ = standardization(X_, self.numerical_feats) if self.is_standardization else X_
        X_ = one_hot(X_, categorical_feats=self.categorical_feats) if self.is_one_hot else X_

        self.fields = self.categorical_feats
        self.categorical_feats = X_.columns.difference(self.numerical_feats)

        return X_

    def _check_feats(self, X_):
        self.categorical_feats = list(X_.columns) if self.categorical_feats is None else self.categorical_feats
        self.numerical_feats = list(
            X_.columns.difference(self.categorical_feats)) if self.numerical_feats is None else self.numerical_feats

    def _init_weights(self, X_, init_gauss: Tuple[float] = (0, 0.2)):
        self._check_feats(X_)
        cols = len(self.categorical_feats) + len(self.numerical_feats)
        # self.linear_weight = np.array([gauss(init_gauss[0], init_gauss[1]) for _ in range(cols)])
        # self.weight_matrix = np.array(
        #     [[gauss(init_gauss[0], init_gauss[1]) for _ in range(self.vector_size)] for _ in range(cols)])
        self.linear_weight = tf.Variable(self.initializer(shape=(cols,)))
        self.weight_matrix = tf.Variable(self.initializer(shape=(cols, self.vector_size)))

    def _update_weight(self, x_sample, loss):
        print('loss:', loss)
        self.bias = self.bias - loss
        for sample in x_sample:
            for feat_idx, feature in enumerate(sample):
                if feature != 0:
                    print(feature, feat_idx)
            print('sample:')
            print(sample)
            break
        # self.weight_matrix = self.weight_matrix - loss
        # print(self.weight_matrix)

    def predict(self, X, training=False):
        # 1-order
        first_order_sum = self.bias + tf.einsum('i,i->', self.linear_weight, x)

        # 2-order
        second_order_sum = 0.0
        if training:
            # for each dimension in a latent vector
            for l in range(self.vector_size):
                sum_of_all_interaction = 0.0
                overlapped_interaction = 0.0
                # weight matrix = [[1, 2, 3, 1, 5], [2, 1, 3, 2, 1], [3, 5, 2, 4, 4]]
                # weight[i][l] = 1, 2, 3, 1, 5
                # x[i] = 0, 1, 2

                for i, x_i in enumerate(x):
                    sum_of_all_interaction += self.weight_matrix[i][l] * x_i
                    overlapped_interaction += self.weight_matrix[i][l] ** 2 * x_i ** 2
                sum_of_all_interaction = sum_of_all_interaction ** 2

                second_order_sum += sum_of_all_interaction - overlapped_interaction
        second_order_sum = second_order_sum * 0.5
        y_hat = self.bias + first_order_sum + second_order_sum

        return y_hat


if __name__ == '__main__':
    df = pd.read_csv('../../../data/titanic.csv')
    X, y = df[df.columns.difference(['Survived'])], df['Survived']
    X = X[['Age', 'Pclass', 'Fare', 'Sex']]
    X = X.fillna(X.mean())
    fm = FM(categorical_feats=['Pclass', 'Sex'])
    fm.train(X_=X, y=y, epochs=500)
