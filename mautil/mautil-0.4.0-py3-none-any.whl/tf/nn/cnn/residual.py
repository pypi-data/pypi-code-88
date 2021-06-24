import tensorflow as tf
from tensorflow.keras.layers import Conv2D, Conv2DTranspose

from mautil.tf import NN

class Block(NN):
    def __init__(self, name='Block', filters=64, kernel_size=3, strides=(1,1), activation='relu', padding='same', batch_norm=True,
                 transpose=False, **kwargs):
        super(ResidualBlock, self).__init__(name=name, **kwargs)
        self.net = tf.keras.Sequential()
        if batch_norm:
            self.net.add(tf.keras.layers.BatchNormalization())
        self.net.add(tf.keras.layers.Activation(activation))
        if transpose:
            self.net.add(Conv2DTranspose(filters, kernel_size, strides=strides, activation=activation, padding=padding))
        else:
            self.net.add(Conv2D(filters, kernel_size, strides=strides, activation=activation, padding=padding))

    def call(self, inputs, training=None, mask=None):
        return self.net(inputs, training=training, mask=mask)


class ResidualBlock(NN):
    def __init__(self, name='ResidualBlock', filters=64, kernel_size=3, activation='relu', padding='same', reduction_factor=4,
                 downsample=True, upsample=False, strides=(2,2), batch_norm=True, **kwargs):
        """
        conv0 for skip connection
        :param name:
        :param filters:
        :param kernel_size:
        :param activation:
        :param padding:
        :param reduction_factor:
        :param downsample:
        :param upsample:
        :param strides:
        :param batch_norm:
        :param kwargs:
        """
        super(ResidualBlock, self).__init__(name=name, **kwargs)

        self._downsample = downsample
        self._upsample = upsample

        self.conv1 = Block(filters//reduction_factor,(1,1), (1,1), activation=activation, batch_norm=batch_norm, padding=padding)
        if upsample:
            self.conv2 = Block(filters // reduction_factor, (kernel_size, kernel_size), strides=strides, activation=activation, batch_norm=batch_norm, padding=padding, transpose=True)
            self.conv0 =Block(filters, (kernel_size, kernel_size), strides=strides, activation=None, batch_norm=False, padding=padding, transpose=True)
        else:
            self.conv2 = Block(filters//reduction_factor,(kernel_size, kernel_size), (1,1), activation=activation, batch_norm=batch_norm, padding=padding)
        self.conv3 = Block(filters//reduction_factor,(kernel_size, kernel_size), (1,1), activation=activation, batch_norm=batch_norm, padding=padding)
        if downsample:
            self.conv4 = Block(filters, (1,1), strides=strides, activation=activation, batch_norm=batch_norm)
            self.conv0 = Block(filters, (kernel_size, kernel_size), strides=strides, activation=None, batch_norm=False)
        else:
            self.conv4 = Block(filters, (1,1), strides=(1,1), activation=activation, batch_norm=batch_norm)

    def call(self, inputs, training=None, mask=None):
        out1 = self.conv1(inputs, training=training, mask=mask)
        out2 = self.conv1(out1, training=training, mask=mask)
        out3 = self.conv1(out2, training=training, mask=mask)
        out4 = self.conv1(out3, training=training, mask=mask)
        if self._downsample:
            iniputs = self.conv0(inputs, training, mask=mask)
        out = inputs + out4
        return out






