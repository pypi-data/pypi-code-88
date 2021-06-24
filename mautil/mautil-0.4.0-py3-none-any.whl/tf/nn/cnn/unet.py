import logging
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dropout, Cropping2D, Conv2DTranspose, UpSampling2D
import tensorflow as tf

from mautil.tf.nn import NN

logger = logging.getLogger(__name__)

def calc_cropping_2d(shape, target_shape):
    dh = shape[0] - target_shape[0]
    dw = shape[1] - target_shape[1]
    crop_top, crop_left = dh//2,  dw//2
    crop_bottom, crop_right = dh-crop_top, dw-crop_left
    return crop_top, crop_bottom, crop_left, crop_right


class DownBlock(NN):
    def __init__(self, name, filters, kernel_size, width=2, strides=(1, 1), dropout=0.1, padding='same', activation='relu',
                 use_batch_norm=True, **kwargs):
        super(DownBlock, self).__init__(name=name)
        self.filters = filters
        self.kernel_size = kernel_size
        self.width = width
        self.strides = strides
        self.dropout = dropout
        self.padding=padding
        self.activation = activation
        self.use_batch_norm = use_batch_norm
        self.kwargs = kwargs

        self.block_layers = self.create_layers()

    def create_layers(self):
        layers = []; strides = self.strides
        for i in range(self.width):
            if i!=0:
                strides = (1,1)
            layers.append(Conv2D(self.filters, self.kernel_size, padding=self.padding, strides=strides, **self.kwargs))
            if self.use_batch_norm:
                layers.append(tf.keras.layers.BatchNormalization())
            if self.dropout>0:
                logger.info('%s use dropout %s', self.name, self.dropout)
                layers.append(Dropout(self.dropout))
            layers.append(tf.keras.layers.Activation(self.activation))
        return layers

    def call(self, inputs, training=None, mask=None):
        for layer in self.block_layers:
            inputs = layer(inputs, training=training)
        return inputs


class UpBlock(DownBlock):
    def create_layers(self):
        layers = []
        for i in range(self.width+1):
            layer = tf.keras.Sequential()
            if i==0:
                layer.add( Conv2DTranspose(self.filters, self.kernel_size, strides=self.strides, padding=self.padding,
                                    **self.kwargs))
            else:
                layer.add(Conv2D(self.filters, self.kernel_size, padding=self.padding, **self.kwargs))
            if self.use_batch_norm:
                layer.add(tf.keras.layers.BatchNormalization())
            if self.dropout > 0:
                logger.info('%s use dropout %s', self.name, self.dropout)
                layer.add(Dropout(self.dropout))
            layer.add(tf.keras.layers.Activation(self.activation))
            layers.append(layer)
        return layers

    def call(self, inputs, skip, training=None, mask=None):
        inputs = self.block_layers[0](inputs, training=training)
        if self.padding == 'same':
            crop_top, crop_bottom, crop_left, crop_right = calc_cropping_2d(inputs.shape[1:], skip.shape[1:])
            if crop_top!=0 or crop_bottom != 0 or crop_left !=0 or crop_right !=0:
            #if 1==1:
                logger.info('cropped inputs shape %s to skip shape %s', tf.shape(inputs), tf.shape(skip))
                inputs = Cropping2D(cropping=((crop_top, crop_bottom), (crop_left, crop_right)))(inputs, training=training)
        elif self.padding =='valid':
            crop_top, crop_bottom, crop_left, crop_right = calc_cropping_2d(skip.shape[1:], inputs.shape[1:])
            skip = Cropping2D(cropping=((crop_top, crop_bottom), (crop_left, crop_right)))(skip, training=training)

        inputs = tf.concat([skip, inputs], -1)
        for layer in self.block_layers[1:]:
            inputs = layer(inputs, training=training)
        return inputs


class Stack(NN):
    def __init__(self, name, blocks, **kwargs):
        super(Stack, self).__init__(name=name, **kwargs)
        self.blocks = blocks

    def call(self, inputs, skips=None, training=None, mask=None):
        outputs = []
        for i, block in enumerate(self.blocks):
            if skips is not None:
                inputs = block(inputs, skip=skips[i], training=training, mask=mask)
            else:
                inputs = block(inputs, training=training, mask=mask)
            outputs.append(inputs)
        return outputs


class Unet(NN):
    def __init__(self, name='unet', filters=64, kernel_size=3, depth=5, width=2, up_dropout=0.1, strides=(2,2), padding='same',
                 activation='relu', down_cls=DownBlock, up_cls=UpBlock, down_dropout=0.1, **kwargs):
        """
        :param name:
        :param filters:
        :param kernel_size:
        :param depth: num of downsample plus one
        :param width: num of conv layer exclude up/down sample layer
        :param dropout:
        :param pool_size:
        :param padding:
        :param activation:
        :param kwargs:
        """

        super(Unet, self).__init__(name=name)
        self.return_last = kwargs.pop('return_last', False)
        self.filters = []
        if not isinstance(filters, list):
            for i in range(depth):
                self.filters.append(filters*(2**i))
        else:
            self.filters = filters

        self.up_dropout = up_dropout
        self.down_dropout = down_dropout
        if not isinstance(up_dropout, list):
            self.up_dropout = [up_dropout for i in range(depth)]
        if not isinstance(down_dropout, list):
            self.down_dropout = [down_dropout for i in range(depth)]
        self.strides = strides
        if not isinstance(strides, list):
            self.strides = [tuple(strides) for i in range(depth)]



        down_blocks = []
        name = 'down_block_{}'
        for i in range(depth):
            strides= self.strides[i]
            use_batch_norm = False if i==0 else True
            down_blocks.append(down_cls(name.format(i), self.filters[i], kernel_size, width, strides, self.down_dropout[i],
                                        padding, activation, use_batch_norm=use_batch_norm, **kwargs))
        self.down_stack = Stack('down_stack', down_blocks)

        up_blocks = []
        name = 'up_block_{}'
        for i in range(depth-2, -1, -1):
            up_blocks.append(up_cls(name.format(i), self.filters[i], kernel_size, width, self.strides[i+1], self.up_dropout[i],
                                    padding, activation, **kwargs))
        self.up_stack = Stack('up_stack', up_blocks)

    def call(self, inputs, training=None, mask=None):
        down_outputs = self.down_stack(inputs, training=training, mask=mask)
        x = down_outputs[-1]
        skips = down_outputs[:-1][::-1]
        up_outputs = self.up_stack(x, skips, training=training, mask=mask)
        outputs = [x] + up_outputs
        if self.return_last:
            outputs = outputs[-1]
        return outputs


if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s -   %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S', level=logging.DEBUG)
    import numpy as np
    depth = 3
    filters = 2
    kernel_size = 3
    strides = [(1,1), (2,2), (2,2)]
    inputs = np.random.rand(2, 48, 51, 3).astype(np.float32)

    unet = Unet(filters=filters, kernel_size=kernel_size, depth=depth, strides=strides, padding='same')
    outputs = unet(inputs)
    assert outputs[-1].shape == list(inputs.shape[:3]) + [filters], outputs[-1].shape

    unet = Unet(filters=filters, kernel_size=kernel_size, depth=depth, strides=strides, padding='valid')
    outputs = unet(inputs)
    assert outputs[-1].shape == (2, 8, 8, filters), outputs[-1].shape

    print('^_^')



