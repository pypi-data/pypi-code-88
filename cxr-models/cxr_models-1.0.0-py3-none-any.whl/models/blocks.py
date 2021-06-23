# Residual Unit:
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import *

@tf.keras.utils.register_keras_serializable()
class SimpleConvBlock(tf.keras.layers.Layer):
    
    def __init__(self, filters=16, kernel_size = (5,5), strides= (1,1), padding = 'same', activation='relu',
                name=None, **kwargs):
        super(SimpleConvBlock, self).__init__(name=name)
        self.activation  = activation
        self.filters     = filters
        self.kernel_size = kernel_size
        self.strides     = strides
        self.padding     = padding
        
        self.conv = Conv2D(filters=self.filters, kernel_size = self.kernel_size, strides= self.strides,
                           padding = self.padding, activation=None)
        self.bn   = BatchNormalization
        self.act  = Activation
        
    def call(self, input_tensor, **kwargs):
        x = self.conv(input_tensor)
        x = self.bn()(x)
        x = self.act(self.activation)(x)
        return x
    
    def get_config(self):
        config = super(SimpleConvBlock, self).get_config()
        config.update({"filters":self.filters,
                       "kernel_size":self.kernel_size, 
                       "strides":self.strides,
                       "padding":self.padding,
                       "activation":self.activation})
        return config 
    @classmethod
    def from_config(cls, config):
        return cls(**config)
       
@tf.keras.utils.register_keras_serializable()
class ResidualUnit(tf.keras.layers.Layer):
    
    def __init__(self,nb_of_input_channels, max_dilation, number_of_units, activation='relu', name=None, **kwargs):
        super(ResidualUnit, self).__init__(name=name, **kwargs)
        self.nb_of_input_channels = nb_of_input_channels
        self.max_dilation         = max_dilation
        self.number_of_units      = number_of_units
        self.activation           = activation
        self.conv0  = Conv2D(self.nb_of_input_channels*2, kernel_size = (1,1), strides = (1,1), padding='same', 
                        dilation_rate= (1,1), activation=None)
        self.bn     = BatchNormalization
        self.act    = Activation
        self.dcn    = DepthwiseConv2D
        self.cat    = Concatenate
        self.conv1  = Conv2D(self.nb_of_input_channels, kernel_size = (1,1), strides = (1,1), padding='same',
                      dilation_rate= (1,1), activation=None)
        self.add    = Add
        
    
    def call(self, input_tensor, **kwargs):
        for i in range(self.number_of_units):
            x1 = self.conv0(input_tensor)
            x1 = self.bn()(x1)
            x1 = self.act(self.activation)(x1)
            a = []
            for i in range(1, self.max_dilation+1):
                temp = self.dcn( kernel_size=(3,3), dilation_rate = (i,i), padding = 'same',
                                       activation= None)(x1)
                temp = self.bn()(temp)
                temp = self.act(self.activation)(temp)
                a.append(temp)
        x = self.cat(axis= -1)(a)
        x = self.conv1(x)
        x = self.bn()(x)
        x = self.act(self.activation)(x)
        x = self.add()([x, input_tensor])
        input_tensor = x
        return x
    
    def get_config(self):
        config = super(ResidualUnit, self).get_config()
        config.update({"nb_of_input_channels":self.nb_of_input_channels,
                "max_dilation":self.max_dilation,
                "number_of_units":self.number_of_units,
                "activation":self.activation})
        return config 
    @classmethod
    def from_config(cls, config):
        return cls(**config)




# Shifter Unit:

@tf.keras.utils.register_keras_serializable()
class ShifterUnit(tf.keras.layers.Layer):
    
    def __init__(self, nb_of_input_channels, max_dilation, activation='relu', name=None, **kwargs):
        super(ShifterUnit, self).__init__(name=name, **kwargs)
        self.nb_of_input_channels  = nb_of_input_channels
        self.max_dilation          = max_dilation
        self.activation            = activation
        self.conv0  = Conv2D(self.nb_of_input_channels*4, kernel_size = (1,1), strides = (1,1), padding='same', 
                      dilation_rate= (1,1), activation=None)
        self.bn     = BatchNormalization
        self.act    = Activation
        self.dcn    = DepthwiseConv2D
        self.mp     = MaxPool2D
        self.cat    = Concatenate
        self.conv1  = Conv2D(self.nb_of_input_channels*2, kernel_size = (1,1), strides = (1,1), padding='same', 
                      dilation_rate= (1,1), activation=self.activation)
        
    def call(self, input_tensor, **kwargs):
        x1 = self.conv0(input_tensor)
        x1 = self.bn()(x1)
        x1 = self.act(self.activation)(x1)
        a = []
        for i in range(1, self.max_dilation+1):
            temp = self.dcn( kernel_size=(3,3), dilation_rate = (i,i), padding = 'same',
                                   activation= self.activation)(x1)
            temp = self.mp(pool_size=(2,2))(temp)
            temp = self.bn()(temp)
            temp = self.act(self.activation)(temp)
            a.append(temp)
        x = self.cat(axis= -1)(a)
        x = self.conv1(x)
        x = self.bn()(x)
        x = self.act(self.activation)(x)
        return x
    
    def get_config(self):
        config = super(ShifterUnit, self).get_config()
        config.update({"nb_of_input_channels":self.nb_of_input_channels,
                        "max_dilation":self.max_dilation,
                        "activation":self.activation})
        return config 
    @classmethod
    def from_config(cls, config):
        return cls(**config)