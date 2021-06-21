from tensorflow import keras
from tensorflow.python.keras.engine.keras_tensor import KerasTensor

from uberlimb.parameters import ModelArchitecture


def perceptron(x: KerasTensor,
               depth: int, width: int,
               initializer: keras.initializers.Initializer,
               activation: str):
    for _ in range(depth):
        x = keras.layers.Dense(width,
                               kernel_initializer=initializer,
                               activation=activation)(x)
    return x


def densenet(x,
             depth,
             width,
             initializer,
             activation):
    for _ in range(depth):
        y = keras.layers.Dense(width,
                               kernel_initializer=initializer,
                               activation=activation)(x)
        x = keras.layers.Concatenate()([x, y])
    return x


def resnet(x: KerasTensor,
           depth: int, width: int,
           initializer: keras.initializers.Initializer,
           activation: str):
    y = keras.layers.Dense(width,
                           kernel_initializer=initializer,
                           activation=activation)(x)
    for i in range(depth - 1):
        x = keras.layers.Dense(width,
                               kernel_initializer=initializer,
                               activation=activation)(x)
        x = keras.layers.Add()([x, y])
        x = keras.layers.Activation(activation)(x)
        y = x
    return x


def resnet_concat(x: KerasTensor,
                  depth: int, width: int,
                  initializer: keras.initializers.Initializer,
                  activation: str):
    y = keras.layers.Dense(width,
                           kernel_initializer=initializer,
                           activation=activation)(x)
    for i in range(depth - 1):
        x = keras.layers.Dense(width,
                               kernel_initializer=initializer,
                               activation=activation)(x)
        x = keras.layers.Concatenate()([x, y])
        y = x
    return x


def chain(x: KerasTensor,
          depth: int, width: int,
          initializer: keras.initializers.Initializer,
          activation: str):
    for i in range(depth):
        if i % 3 == 0:
            x = keras.layers.Dense(width,
                                   kernel_initializer=initializer,
                                   activation=activation)(x)
        else:
            x_1 = keras.layers.Dense(width,
                                     kernel_initializer=initializer,
                                     activation=activation)(x)
            x_2 = keras.layers.Dense(width,
                                     kernel_initializer=initializer,
                                     activation=activation)(x)
            x = keras.layers.Add()([x_1, x_2])
            x = keras.layers.Activation('tanh')(x)
    return x


def plexus(x: KerasTensor,
           depth: int, width: int,
           initializer: keras.initializers.Initializer,
           activation: str):
    for i in range(depth):
        if i % 3 == 0:
            x = keras.layers.Dense(width,
                                   kernel_initializer=initializer,
                                   activation=activation)(x)
            x_1 = x
            x_2 = x
            x_3 = x
        else:
            x_1 = keras.layers.Dense(width,
                                     kernel_initializer=initializer,
                                     activation=activation)(x_23)
            x_2 = keras.layers.Dense(width,
                                     kernel_initializer=initializer,
                                     activation=activation)(x_13)
            x_3 = keras.layers.Dense(width,
                                     kernel_initializer=initializer,
                                     activation=activation)(x_12)
        x_12 = keras.layers.Concatenate()([x_1, x_2])
        x_13 = keras.layers.Concatenate()([x_1, x_3])
        x_23 = keras.layers.Concatenate()([x_2, x_3])
    x = keras.layers.Concatenate()([x_1, x_2, x_3])
    return x


architecture_lookup = {
    ModelArchitecture.PERCEPTRON: perceptron,
    ModelArchitecture.DENSENET: densenet,
    ModelArchitecture.RESNET: resnet,
    ModelArchitecture.RESNET_CONCAT: resnet_concat,
    ModelArchitecture.CHAIN: chain,
    ModelArchitecture.PLEXUS: plexus,
}
