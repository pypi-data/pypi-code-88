import os
import json
import shutil
import time
from .image_utils import create_thumbnail


def filter_images(method, root):
    if method == 'PHash':
        from imagededup.methods import PHash as Hash
    elif method == 'AHash':
        from imagededup.methods import AHash as Hash
    elif method == 'DHash':
        from imagededup.methods import DHash as Hash
    elif method == 'WHash':
        from imagededup.methods import WHash as Hash
    else:
        from imagededup.methods import PHash as Hash
    print('hash = %s, image_dir = %s' % (method, root))
    dedup(method, Hash(), root)


def dedup(_method, _hash, _root):
    dedup_dir = os.path.join(_root, _method.lower())
    dedup_json = os.path.join(dedup_dir, 'dedup.json')
    filter_json = os.path.join(dedup_dir, 'filter.json')
    print('dedup_dir = %s' % dedup_dir)
    print('dedup_json = %s' % dedup_json)
    print('filter_json = %s' % filter_json)

    if not os.path.exists(dedup_dir):
        os.mkdir(dedup_dir)

    if os.path.exists(dedup_json):
        os.remove(dedup_json)

    if os.path.exists(filter_json):
        os.remove(filter_json)

    encodings = _hash.encode_images(image_dir=_root)

    duplicates = _hash.find_duplicates(encoding_map=encodings, outfile=dedup_json)

    print('duplicates = %s' % len(duplicates))

    cp = duplicates.copy()
    for k, v in duplicates.items():
        if len(v) != 0:
            if cp.__contains__(k):
                for i in v:
                    if cp.__contains__(i):
                        cp.pop(i)
        else:
            cp.pop(k)

    lis = list()
    for k, v in cp.items():
        d = dict(img=k, dedup=v)
        lis.append(d)

    print('result = %s' % len(lis))

    with open(filter_json, 'w') as f:
        json.dump(lis, f, indent=4)

    readme = os.path.join(dedup_dir, 'readme.txt')

    with open(readme, 'w') as f:
        f.write('hash = %s\n\n' % _method)
        f.write('image_dir = %s\n\n' % _root)
        f.write('dedup_dir = %s\n\n' % dedup_dir)
        f.write('dedup_json = %s\n\n' % dedup_json)
        f.write('filter_json = %s\n\n' % filter_json)
        f.write('duplicates = %s\n\n' % len(duplicates))
        f.write('result = %s\n\n' % len(lis))
        f.flush()

    print('start => ', time.strftime('%Y-%m-%d %H:%M:%S'))
    for k, v in cp.items():
        images = [k] + v
        for img in images:
            infile = os.path.join(_root, img)
            outfile = create_thumbnail(infile, size=(300, 300))
            print(outfile)
    print('end => ', time.strftime('%Y-%m-%d %H:%M:%S'))


def filter_dedup(root, alg):
    file = os.path.join(root, alg, 'filter.json')
    with open(file, 'r') as f:
        filter_list = json.load(f)
    dedup_dir = os.path.join(root, 'dedup')
    if not os.path.exists(dedup_dir):
        return filter_list
    dedup_list = os.listdir(dedup_dir)
    if len(dedup_list) == 0:
        return filter_list
    _filter = []
    for item in filter_list:
        _img = item['img']
        _dedup = item['dedup']
        lis = []
        for img in _dedup:
            if not dedup_list.__contains__(img):
                lis.append(img)
        if len(lis) != 0:
            _filter.append(dict(img=_img, dedup=lis))
    return _filter


def move_to_dedup(root, img):
    _dedup = os.path.join(root, 'dedup')
    if not os.path.exists(_dedup):
        os.mkdir(_dedup)
    file = os.path.join(root, img)
    shutil.move(file, _dedup)
    return True


def del_from_dedup(root, img):
    return dict(root=root, img=img)
