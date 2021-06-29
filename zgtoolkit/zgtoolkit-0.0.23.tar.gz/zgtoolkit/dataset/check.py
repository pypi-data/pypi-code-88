import xml.etree.ElementTree as ET
from glob import glob
import os
import numpy as np
from pathlib import Path

from ..utils import track_iter_progress
from .parse import parse_label


def print_label(root, label_suffix):
    assert '.' in label_suffix
    anno_paths = glob(os.path.join(root, f'*{label_suffix}'))

    labels = []
    for anno_path in track_iter_progress(anno_paths):
        if 'xml' in label_suffix:
            datas = ET.parse(str(anno_path))
            for name in datas.iter('name'):
                labels.append(name.text)

    print(set(labels))
    return set(labels)


def check_bboxlabel(root, label_suffix, area_limit, cls_limit):
    assert '.' in label_suffix
    anno_paths = glob(os.path.join(root, f'*{label_suffix}'))

    label_cls = print_label(root, label_suffix)
    if set(label_cls) != set(cls_limit):
        raise ValueError('label not match')
    for anno_path in track_iter_progress(anno_paths):
        objs = parse_label(anno_path, label_suffix, cls_limit)
        bboxes = objs[:, 0:4]
        whs = bboxes[:, 2:] - bboxes[:, 0:2]
        areas = whs[:, 0] * whs[:, 1]

        if np.any(areas < area_limit):
            print(f'{Path(anno_path).name} has abnormal bbox')
    print('check completed!')
