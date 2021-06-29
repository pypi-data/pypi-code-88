import tensorflow as tf
from pydantic import validate_arguments
from tensorflow import keras
from tensorflow.python.keras.engine.keras_tensor import KerasTensor

from uberlimb.model.models_impl import architecture_lookup
from uberlimb.parameters import ModelParams, ModelArchitecture


class LimbModel:
    @classmethod
    @validate_arguments
    def build_model(cls, params: ModelParams) -> tf.keras.Model:
        tf.random.set_seed(params.seed)
        initializer = keras.initializers.VarianceScaling(scale=params.variance,
                                                         mode='fan_in',
                                                         distribution='normal',
                                                         seed=params.seed)
        # number of parameters in input grid [x, y, z, alpha, beta, f]
        inputs = keras.Input(shape=(6,))
        model_body = cls._build_model_body(params.architecture,
                                           inputs,
                                           params.depth,
                                           params.width,
                                           initializer,
                                           params.activation.value)
        bottleneck_initializer = keras.initializers.GlorotNormal(params.seed)
        bottleneck = keras.layers.Dense(
            3,
            activation=params.out_activation.value,
            kernel_initializer=bottleneck_initializer)(model_body)
        model: tf.keras.Model = keras.Model(inputs=inputs, outputs=bottleneck)
        model.trainable = False
        return model

    @staticmethod
    def _build_model_body(architecture: ModelArchitecture,
                          x: KerasTensor,
                          depth: int, width: int,
                          initializer: keras.initializers.Initializer,
                          activation: str):
        """This method is a proxy which enforces the arguments we're
        passing to the method inside `architecture_lookup`."""
        model_builder = architecture_lookup[architecture]
        model_body = model_builder(x,
                                   depth,
                                   width,
                                   initializer,
                                   activation)
        return model_body
