import tensorflow as tf
import numpy as np
from .blocks import ResidualUnit, ShifterUnit, SimpleConvBlock

class CovXNet(tf.keras.Model):
    
    def __init__(self, depth, activation='relu', **kwargs):
        super(CovXNet, self).__init__(**kwargs)
        self.depth       = depth
        self.activation  = activation
        
        self.conv0 = SimpleConvBlock(filters=16, kernel_size = (5,5), strides= (1,1), padding = 'same', activation=self.activation,
                              name='conv_block_0')
        self.conv1 = SimpleConvBlock(filters=32, kernel_size = (3,3), strides= (2,2), padding = 'same', activation=self.activation,
                              name='conv_block_1')
        
        self.ru0 = ResidualUnit(nb_of_input_channels=32, max_dilation=5, number_of_units=self.depth, name='ru_c32_d5',
                                activation=self.activation)
        self.su0 = ShifterUnit(nb_of_input_channels=32, max_dilation=5, name='su_c32_d5',activation=self.activation)
        
        self.ru1 = ResidualUnit(nb_of_input_channels=64, max_dilation=4, number_of_units=self.depth, name='ru_c64_d4',
                                activation=self.activation)
        self.su1 = ShifterUnit(nb_of_input_channels=64, max_dilation=4, name='su_c64_d4',activation=self.activation)
        
        self.ru2 = ResidualUnit(nb_of_input_channels=128, max_dilation=3, number_of_units=self.depth, name='ru_c128_d3',
                                activation=self.activation)
        self.su2 = ShifterUnit(nb_of_input_channels=128, max_dilation=3, name='su_c128_d3',activation=self.activation)
        
        self.ru3 = ResidualUnit(nb_of_input_channels=256, max_dilation=2, number_of_units=self.depth, name='ru_c256_d2',
                                activation=self.activation)
        
        self.gap = tf.keras.layers.GlobalAveragePooling2D()
        
        self.cls = tf.keras.layers.Dense(units=1000, activation='softmax')

    def call(self, input_shape, name='covxnet-128', **kwargs):
        input_shape = np.array(input_shape)
        xin = tf.keras.layers.Input(shape= input_shape)

        x = self.conv0(xin)
        x = self.conv1(x)

    # Max Dilation rate will be vary in the range (1,5). 

    # Max Dilation rate is 5 for tensor (64x64x32)
        x = self.ru0(x)
        x = self.su0(x)

    # Max Dilation rate is 4 for (32x32x64)
        x = self.ru1(x)
        x = self.su1(x)

    # Max Dilation rate is 3 for (16x16x128)
        x = self.ru2(x)
        x = self.su2(x)

    # Max Dilation rate is 2 for (8x8x256)
        x = self.ru3(x)

        x = self.gap(x)
        
        x = self.cls(x)

        model = tf.keras.models.Model(xin, x, name=name)

        return model
    
    def get_config(self):
        config = super(CovXNet, self).get_config()
        config.update({"depth":self.depth, 
                      "activation":self.activation,
               })
        return config 

    @classmethod
    def from_config(cls, config):
        return cls(**config)