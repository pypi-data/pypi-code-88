import xml.etree.ElementTree as ET
import numpy as np
from pathlib import Path


def parse_label(path, label_suffix, classes=None):
    if 'xml' in label_suffix:
        datas = ET.parse(str(path))
        objs = []
        for obj in datas.findall('object'):
            try:
                cls = classes.index(obj.find('name').text.lower()) if classes is not None else 0
            except:
                cls = 0
                print(f'{Path(path).name} not in {classes}')
            bndbox = obj.find('bndbox')
            bbox = [int(x.text) for x in bndbox] + [cls]
            objs.append(bbox)
        objs = np.array(objs, dtype=int)

    return objs


def parse_txt(path):
    results = []
    with open(path, 'r', encoding='utf-8') as f:
        datas = f.readlines()

        for line in datas:
            image_path = line.split(' ')[0]
            annos = line.strip().split(' ')[1:]
            annos = [x.split(',') for x in annos]
            results.append(dict(
                image_path=image_path,
                annos=np.array(annos, dtype=int)
            ))
    return results
