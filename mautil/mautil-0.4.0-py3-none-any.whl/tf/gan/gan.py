import os, logging
from collections import OrderedDict
import tensorflow as tf

from mautil.tf.models import TFModel, CFG
from mautil.basic_models import InputFeature
import mautil as mu

logger = logging.getLogger(__name__)

class GAN(TFModel):
    """ A basic jointly training gan
    """
    cfg = TFModel.cfg.copy()
    cfg.noise_dim = 128
    cfg.sample_num = 16
    cfg.save_sample = False
    cfg.gen_weight = 1.0

    def __init__(self, name='GAN', cfg={}):
        super(GAN, self).__init__(name, cfg)
        self._samples = self.get_samples()

    def get_samples(self):
        samples = tf.random.normal([self.cfg.sample_num, self.cfg.noise_dim], seed=self.cfg.seed)
        return samples

    def get_input_features(self):
        input_features = super(GAN, self).get_input_features()
        input_features['img'] = InputFeature('img', [28, 28, 1], tf.float32)
        input_features['noise'] = InputFeature('noise', [self.cfg.noise_dim], tf.float32)
        #input_features['dis_real_targets'] = InputFeature('dis_real_targets', [], tf.float32)
        #input_features['dis_fake_targets'] = InputFeature('dis_fake_targets', [], tf.float32)
        #input_features['gen_targets'] = InputFeature('gen_targets', [], tf.float32)
        return input_features

    def main_nn(self, inputs):
        imgs = inputs['img']
        noise = inputs['noise']
        #noise = tf.random.normal([self.cfg.batch_size, self.cfg.noise_dim])
        gen_outputs = self.generator(noise)
        real_outputs = self.discrimator(imgs)
        fake_outputs = self.discrimator(gen_outputs)
        return fake_outputs, real_outputs, fake_outputs

    def create_keras_model(self, inputs):
        self.generator = self.create_generator()
        self.discrimator = self.create_discrimator()
        return super(GAN, self).create_keras_model(inputs, compile=False)

    def create_generator(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Dense(7 * 7 * 256, use_bias=False, input_shape=(self.cfg.noise_dim,)))
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.LeakyReLU())

        model.add(tf.keras.layers.Reshape((7, 7, 256)))
        assert model.output_shape == (None, 7, 7, 256)

        model.add(tf.keras.layers.Conv2DTranspose(128, (5, 5), strides=(1, 1), padding='same', use_bias=False))
        assert model.output_shape == (None, 7, 7, 128)
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.LeakyReLU())

        model.add(tf.keras.layers.Conv2DTranspose(64, (5, 5), strides=(2, 2), padding='same', use_bias=False))
        assert model.output_shape == (None, 14, 14, 64)
        model.add(tf.keras.layers.BatchNormalization())
        model.add(tf.keras.layers.LeakyReLU())

        model.add(tf.keras.layers.Conv2DTranspose(1, (5, 5), strides=(2, 2), padding='same', use_bias=False, activation='tanh'))
        assert model.output_shape == (None, 28, 28, 1)

        return model

    def create_discrimator(self):
        model = tf.keras.Sequential()
        model.add(tf.keras.layers.Conv2D(64, (5, 5), strides=(2, 2), padding='same',
                                         input_shape=[28, 28, 1]))
        model.add(tf.keras.layers.LeakyReLU())
        model.add(tf.keras.layers.Dropout(0.3))

        model.add(tf.keras.layers.Conv2D(128, (5, 5), strides=(2, 2), padding='same'))
        model.add(tf.keras.layers.LeakyReLU())
        model.add(tf.keras.layers.Dropout(0.3))

        model.add(tf.keras.layers.Flatten())
        model.add(tf.keras.layers.Dense(1))

        return model

    def calc_loss(self, outputs, targets):
        gen_outputs, real_outputs, fake_outputs = outputs
        #gen_targets, real_targets, fake_targets = targets
        gen_targets, real_targets, fake_targets = tf.ones_like(gen_outputs), tf.ones_like(real_outputs), tf.zeros_like(fake_outputs)
        losses = OrderedDict()
        losses['gen_loss'] = self.cfg.gen_weight * tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(gen_targets, gen_outputs))
        real_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(real_targets, real_outputs))
        fake_loss = tf.reduce_mean(tf.nn.sigmoid_cross_entropy_with_logits(fake_targets, fake_outputs))
        dis_loss = real_loss + fake_loss
        losses['real_loss'] = real_loss
        losses['fake_loss'] = fake_loss
        losses['dis_loss'] = dis_loss

        losses['loss'] = losses['gen_loss'] + losses['dis_loss']
        return losses

    def save_sample(self, epoch):
        fpath = self.gen_fname('sample_output', 'sample_{:04d}.dump'.format(epoch))
        gen_outputs = self.generator(self._samples)
        mu.dump(gen_outputs, fpath)
        logger.info('sample saved to %s', fpath)

    def load_sample(self, epochs=None):
        if epochs is None:
            epochs = self.cfg.epochs
        epoch_outputs = []
        for i in range(epochs):
            fpath = self.gen_fname('sample_output', 'sample_{:04d}.dump'.format(i))
            if os.path.exists(fpath):
                epoch_outputs.append(mu.load_dump(fpath))
            else:
                logger.error('sample outputs of epoch:%s does not exists:%s', i, fpath)
        return epoch_outputs

    def fit_epoch(self, ds, epoch, step, opt, callbacks, **kwargs):
        rst = super(GAN, self).fit_epoch(ds, epoch, step, opt, callbacks, **kwargs)
        if self.cfg.save_sample:
            self.save_sample(epoch)
        return rst

    def _get_train_vars(self):
        """
        must keep same order as grads calculated in fit_batch
        :return:
        """
        gen_vars = self.generator.trainable_variables
        dis_vars = self.discrimator.trainable_variables
        return gen_vars + dis_vars

    def fit_batch(self, inputs, targets=None):
        gen_vars = self.generator.trainable_variables
        dis_vars = self.discrimator.trainable_variables
        with tf.GradientTape() as gen_tape, tf.GradientTape() as dis_tape:
            outputs = self._model(inputs, training=True)
            losses = self.calc_loss(outputs, targets)
        gen_grads = self.calc_grads(gen_tape, gen_vars, losses['gen_loss'])
        dis_grads = self.calc_grads(dis_tape, dis_vars, losses['dis_loss'])
        grads = gen_grads + dis_grads
        self.apply_grads(gen_vars+dis_vars, grads)
        #opt.apply_gradients(zip(grads, gen_vars+dis_vars))
        return grads, losses


class ConstraintGANTrainer(object):
    def calc_loss(self, outputs, targets):
        losses = super(ConstraintGANTrainer, self).calc_loss(outputs, targets)
        if losses['fake_loss'] < self.cfg.min_fake_loss:
            losses['dis_loss'] = 0.0

        if losses['gen_loss'] < self.cfg.min_gen_loss:
            losses['gen_loss'] = 0.0
        return losses

if __name__ == "__main__":
    import logging
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s', datefmt='%m/%d/%Y %H:%M:%S',
                        level=logging.INFO)
    import numpy as np
    def map_func(x):
        dis_real_targets = np.ones([x.numpy().shape[0]], np.float32)
        dis_fake_targets = 1-dis_real_targets
        gen_targets = dis_real_targets
        return x, (gen_targets, dis_real_targets, dis_fake_targets)

    ds1 = tf.data.Dataset.from_tensor_slices(np.random.rand(101, 128))
    ds2 = tf.data.Dataset.from_tensor_slices(np.random.rand(101, 28, 28, 1))
    ds = tf.data.Dataset.zip((ds1, ds2))
    ds = ds.map(lambda noise, img: {'img': img, 'noise':noise}).batch(5)

    cfg = GAN.cfg.copy()
    cfg.epochs = 3
    cfg.batch_size = 5
    cfg.accumulated_batch_size = 2
    cfg.run_eagerly = True
    model = GAN(cfg=cfg.__dict__)
    model.tffit(ds)




