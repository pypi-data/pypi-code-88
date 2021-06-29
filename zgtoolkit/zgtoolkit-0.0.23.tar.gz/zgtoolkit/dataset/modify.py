import os
from pathlib import Path
from glob import glob
import numpy as np
from ..utils import track_iter_progress
from .parse import parse_label
import xml.etree.ElementTree as ET


def modify_annocls(anno_path, root, classes, label_suffix, image_format='.jpg'):
    assert '.' in image_format
    assert '.' in label_suffix
    if not isinstance(root, list):
        root = [root]

    label_paths = [glob(os.path.join(x, f'*{label_suffix}')) for x in root]
    label_paths = np.concatenate(label_paths).tolist()
    label_names = ['/'.join(Path(x).parts[-2:]) for x in label_paths]
    with open(anno_path, 'r') as f:
        datas = f.readlines()
        new_datas = []
        for line in track_iter_progress(datas):
            annos = line.split(' ')
            image_path = annos[0]
            if '\\' in image_path:
                image_path = image_path.replace('\\', '/')

            label_path = Path(image_path).with_suffix(label_suffix)
            name = '/'.join(Path(label_path).parts[-2:])
            if name in label_names:
                index = label_names.index(name)
                label_path = label_paths[index]
                objs = parse_label(label_path, label_suffix, classes)
                objs = objs.astype(str)
                annos[1:] = [','.join(x) for x in objs]
            line = ' '.join(annos)
            line += '\n'
            new_datas.append(line)
    with open(anno_path, 'w') as f:
        f.writelines(new_datas)


def modify_annoroot(anno_path, root, image_format='.jpg'):
    assert '.' in image_format
    if not isinstance(root, list):
        root = [root]

    image_paths = [glob(os.path.join(x, f'*{image_format}')) for x in root]
    image_paths = np.concatenate(image_paths).tolist()
    image_names = ['/'.join(Path(x).parts[-2:]) for x in image_paths]
    with open(anno_path, 'r') as f:
        datas = f.readlines()
        new_datas = []
        for line in track_iter_progress(datas):
            annos = line.split(' ')
            image_path = annos[0]
            if '\\' in image_path:
                image_path = image_path.replace('\\', '/')

            image_path = Path(image_path)
            name = '/'.join(Path(image_path).parts[-2:])
            if name in image_names:
                index = image_names.index(name)
                image_path = image_paths[index]
                annos[0] = image_path
            line = ' '.join(annos)
            new_datas.append(line)
    with open(anno_path, 'w') as f:
        f.writelines(new_datas)


def modify_label(root, label_suffix, old_label, new_label):
    assert '.' in label_suffix
    anno_paths = glob(os.path.join(root, f'*{label_suffix}'))

    for anno_path in track_iter_progress(anno_paths):
        if 'xml' in label_suffix:
            datas = ET.parse(str(anno_path))
            for name in datas.iter('name'):
                if name.text == old_label:
                    name.text = new_label
            datas.write(str(anno_path), encoding='utf-8')
