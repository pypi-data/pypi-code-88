# -*- coding: utf-8 -*-

"""
@date: 2021/6/9 上午10:13
@file: main.py
@author: zj
@description: 
"""

import torch

from efficientnet import EfficientNet

if __name__ == '__main__':
    model = EfficientNet.from_pretrained('efficientnet-b0').to(device=torch.device('cpu'))
    print(model)

    torch.manual_seed(10)
    data = torch.randn(1, 3, 224, 224)
    print(data)

    res = model(data)
    print(res)
