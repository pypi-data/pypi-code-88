from mautil.tf.gan import GAN
from mautil.tf.nn import NN


class BigGANBlock(NN):
    def __init__(self, name='BigGANBlock' ):
        pass

    def call(self, inputs, training=None, mask=None):
        pass


class BigGAN(GAN):
    cfg = GAN.cfg.copy()
