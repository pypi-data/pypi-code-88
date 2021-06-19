import pandas as pd
import os
from pathlib import Path
import zipfile
import requests
from glob import glob
from apng import APNG
from skimage.io import imread, imsave
from tqdm import tqdm
import numpy as np

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))

def get_animation(productId, location='./_tmp'):
    productId = str(productId)
    location = Path(location)
    location.mkdir(exist_ok=True)
    dataLocation = location / "data"
    dataLocation.mkdir(exist_ok=True)
    zipFilePath = location / f'{productId}.zip'
    if not zipFilePath.exists():
        zipFile = requests.get(f'http://dl.stickershop.line.naver.jp/products/0/0/1/{productId}/iphone/stickerpack@2x.zip', timeout=10)
        with open(zipFilePath, 'wb') as f:
            f.write(zipFile.content)
    extractLocation = location / productId
    if not extractLocation.exists():
        with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
            zip_ref.extractall(extractLocation)
    extractLocation /= "animation@2x"

    
    dataset = []
    for file in glob(str(extractLocation / "*.png")):
        im = APNG.open(file)
        animations = []
        mainpng, maincontrol = im.frames[0]
        for i, (png, control) in enumerate(im.frames):
            path = dataLocation / f"{productId}_{Path(file).name.split('.')[0]}_{i}.png"
            if control.width == 1:
                continue
            if not path.exists():
                png.save(path)
                img = imread(path)
                if img.shape[2]==3:
                    newimg = np.ones(img.shape[:2]+(4,))
                    newimg[:,:,:3] = img
                    img = newimg
                nim = np.zeros([mainpng.height,mainpng.width,4]).astype(np.uint8)
                nim[control.y_offset:control.y_offset+control.height, control.x_offset:control.x_offset+control.width, :] = img
                imsave(path, nim)
            animations.append(str(path))
        dataset.append(animations)
    return dataset

from multiprocessing import Pool

def get_animation_data(num_set, num_workers=0):
    """ total 7107 """
    df = pd.read_csv( dir_path / f'linesticker_animation.csv')
    print("total # set", len(df))
    if num_workers > 0:
        with Pool(num_workers) as p:
            pids = [row['productId'] for i,row in df.iterrows() if i < num_set]
            dataset = [datum for datum in tqdm(p.imap_unordered(get_animation, pids))]
        return dataset
    else:
        dataset = []
        for i, row in tqdm(df.iterrows()):
            if i >= num_set:
                break
            data = get_animation(row['productId'])
            dataset.extend(data)
        return dataset