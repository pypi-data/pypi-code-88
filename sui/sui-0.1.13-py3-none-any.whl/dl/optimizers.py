import tensorflow as tf


class SuiOptimizersError(ValueError):
    pass


def get_opti(opti_name: str):
    if opti_name == 'adam':
        return tf.keras.optimizers.Adam
    elif opti_name == 'ftrl':
        return tf.keras.optimizers.Ftrl
    else:
        raise SuiOptimizersError
