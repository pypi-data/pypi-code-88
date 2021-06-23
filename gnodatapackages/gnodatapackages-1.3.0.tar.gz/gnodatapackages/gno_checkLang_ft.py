#!/usr/bin/env python
# coding: utf-8


'''
lid.176.ftz, which is the compressed version of the model, with a file size of 917kB.

'''

import os
import fasttext

def test():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print(__file__)
    return ("hello am here at langcheck")


def gno_predictLang(mytext):
'''
input needs to be string
returns the last 2 char --> 'en', 'zh' to represent the language
'''
    dir_path = os.path.dirname(os.path.realpath(__file__))
    PRETRAINED_MODEL_PATH = os.path.join(dir_path, 'lid.176.ftz')
    model = fasttext.load_model(PRETRAINED_MODEL_PATH)

    return model.predict(mytext.splitlines())[0][0][0][-2:]

