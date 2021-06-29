#!/usr/bin/python
# encoding: utf-8


import numpy as np
from PIL import Image


class ResizeNormalize(object):

    def __init__(self, size, interpolation=Image.BILINEAR):
        self.size = size
        self.interpolation = interpolation

    def __call__(self, img):

        size = self.size
        img_w, img_h = size
        scale = img.size[1] * 1.0 / img_h
        w = img.size[0] / scale
        w = int(w)
        img = img.resize((w, img_h), self.interpolation)
        w, h = img.size
        if w <= img_w:
            newImage = np.zeros((img_h, img_w), dtype='uint8')
            newImage[:] = 255
            newImage[:, :w] = np.array(img)
            img = Image.fromarray(newImage)
        else:
            img = img.resize((img_w, img_h), self.interpolation)

        img = np.array(img, dtype=np.float32)

        img -= 127.5
        img /= 127.5

        img = img.reshape([*img.shape, 1])

        return img


class StrLabelConverter(object):

    def __init__(self, alphabet):
        self.alphabet = alphabet + 'ç'  # for `-1` index
        self.dict = {}
        for i, char in enumerate(alphabet):
            # NOTE: 0 is reserved for 'blank' required by wrap_ctc
            self.dict[char] = i + 1

    def decode(self, t, length, raw=False):
        t = t[:length]
        if raw:
            return ''.join([self.alphabet[i - 1] for i in t])
        else:
            char_list = []
            for i in range(length):

                if t[i] != 0 and (not (i > 0 and t[i - 1] == t[i])):
                    char_list.append(self.alphabet[t[i] - 1])
            return ''.join(char_list)


class Averager(object):

    def __init__(self):
        self.sum = 0
        self.n_count = 0

    def add(self, v):
        self.n_count += v.data.numel()
        # NOTE: not `+= v.sum()`, which will add a node in the compute graph,
        # which lead to memory leak
        self.sum += v.data.sum()

    def reset(self):
        pass

    def val(self):
        res = 0
        if self.n_count != 0:
            res = self.sum / float(self.n_count)
        return res
