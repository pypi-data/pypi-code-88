import requests
import zipfile
import os
from os import walk
import numpy as np
import csv
from skimage.io import imread, imsave
from tqdm import tqdm
from multiprocessing import Pool
from functools import partial

def remove_background(path):
    im = imread(path)
    # im[im == [[[76,105,113,0]]]] = 0
    if len(im.shape)>2 and im.shape[2] == 4:
        mask = im[:,:,3:]==0
        im[np.repeat(mask, 4, 2)] = 0
        tokens = path.split('.')
        path = ".".join(tokens[:-1] + ['jpg'])
        imsave(path, im[:,:,:3])
    return path

# list
def list_available():
    return [
        dict(folder='dataofficial', 
             category=[
             'Pop-Up Stickers',
             'Big stickers',
             'BROWN & FRIENDS',
             'Animated Stickers',
             'Humor and Entertainment',
             'Anime',
             'Games',
             'With Voice or Sound',
             'Kids Cartoons',
             'Horoscope',
             'Music sticker',
             'TV Stars',
             'Cartoons',
             'Love and Romance',
             'Manga',
             "Official Creators' Stickers",
             'Disney',
             'Sanrio',
             'Characters',
             'Custom stickers'],
             total=2948,
             count={
             'Animated Stickers': 967,
             'With Voice or Sound': 613,
             'Music sticker': 43,
             'Sanrio': 65,
             'Cartoons': 90,
             'Humor and Entertainment': 66,
             'Horoscope': 1,
             'TV Stars': 90,
             'Manga': 142,
             'Pop-Up Stickers': 149,
             'BROWN & FRIENDS': 68,
             'Characters': 241,
             "Official Creators' Stickers": 3,
             'Disney': 145,
             'Big stickers': 12,
             'Games': 36,
             'Kids Cartoons': 54,
             'Anime': 76,
             'Custom stickers': 46,
             'Love and Romance': 41
             }), 
        dict(folder='dataofficial-th', 
             category=[
             'ครีเอเตอร์ทางการ',
             'BROWN&FRIENDS',
             'มาสคอต',
             'สติกเกอร์แอนิเมชัน',
             'ความรักและโรแมนติก',
             'สติกเกอร์เติมคำ',
             'การ์ตูนเด็ก',
             'ดารา & คนดัง',
             'ดิสนีย์',
             'อนิเมะ',
             'สติกเกอร์มีเสียง',
             'ดวงชะตาราศี',
             'เกม',
             'สติกเกอร์ป๊อปอัพ',
             'บิ๊กสติกเกอร์',
             'ตลกขบขัน',
             'ซานริโอ้',
             'มังงะ',
             'การ์ตูน',
             'มิวสิคสติกเกอร์'],
            total=2922,
            count={'บิ๊กสติกเกอร์': 11, 'ความรักและโรแมนติก': 41, 'ดารา & คนดัง': 85, 'ครีเอเตอร์ทางการ': 3, 'ตลกขบขัน': 66, 'สติกเกอร์เติมคำ': 41, 'การ์ตูน': 88, 'สติกเกอร์แอนิเมชัน': 962, 'BROWN&FRIENDS': 68, 'ดิสนีย์': 144, 'สติกเกอร์มีเสียง': 611, 'ดวงชะตาราศี': 1, 'ซานริโอ้': 65, 'มังงะ': 140, 'อนิเมะ': 73, 'การ์ตูนเด็ก': 54, 'มิวสิคสติกเกอร์': 43, 'เกม': 36, 'มาสคอต': 241, 'สติกเกอร์ป๊อปอัพ': 149}), 
        dict(folder='data', 
             taste=[
             'Polite Language',
             'Seasonal',
             'Gorgeous',
             'Dialects & Slang',
             'Speech Balloons',
             'Humorous',
             'Greetings',
             'Warm & Fuzzy',
             'Cute',
             'Cool',
             'Wacky'], 
             character=[
             'Female Characters',
             'Rabbits',
             'Male Characters',
             'Pandas',
             'Birds',
             'Bears',
             'Weird',
             'Families & Couples',
             'Seals',
             'Names',
             'Dogs',
             'Cats',
             'Food',
             'Other'],
            total=357361,
            count={'Gorgeous': 28127, 'Food': 23821, 'Names': 54413, 'Dogs': 24892, 'Other': 50951, 'Rabbits': 23737, 'Female Characters': 38145, 'Families & Couples': 29035, 'Male Characters': 37325, 'Cats': 30389, 'Pandas': 7705, 'Birds': 17307, 'Seals': 2515, 'Bears': 17126, 'Greetings': 28684, 'Weird': 44552, 'Polite Language': 16073, 'Humorous': 47116, 'Cool': 23471, 'Dialects & Slang': 27144, 'Cute': 58422, 'Seasonal': 13303, 'Speech Balloons': 14157, 'Warm & Fuzzy': 56312}), 
        dict(folder='data-th', 
             taste=[
             'ตลก',
             'เทศกาล',
             'ทักทาย',
             'ภาษาท้องถิ่น, สแลง',
             'น่ารัก',
             'เท่',
             'บอลลูนข้อความ',
             'สวยเริ่ด',
             'อบอุ่น',
             'แปลก',
             'ภาษาสุภาพ'], 
             character=[
             'หมี',
             'ชื่อ',
             'สุนัข',
             'หญิง',
             'นก',
             'อาหาร',
             'แมว',
             'ครอบครัว, คู่รัก',
             'แมวน้ำ',
             'แพนด้า',
             'กระต่าย',
             'อื่นๆ',
             'ชาย'],
             total=245513,
             count={'ทักทาย': 28692, 'แพนด้า': 6525, 'นก': 14179, 'สุนัข': 20362, 'กระต่าย': 16865, 'หมี': 14256, 'อาหาร': 17295, 'อื่นๆ': 31848, 'ครอบครัว, คู่รัก': 23555, 'หญิง': 24756, 'แมวน้ำ': 1868, 'แมว': 18781, 'ชาย': 25202, 'ชื่อ': 30021, 'น่ารัก': 59032, 'เท่': 23624, 'เทศกาล': 13552, 'ตลก': 47172, 'อบอุ่น': 57357, 'สวยเริ่ด': 16084}
            ), 
    ]

def _process(line, location='./tmp', key=False):
    fileName = line.split('/')[-1]
    productId = fileName.split('.')[0]
    imagePaths = []

    try:
      zipFilePath = os.path.join(location, fileName)
      if not os.path.exists(zipFilePath):
          zipFile = requests.get('http://dl.stickershop.line.naver.jp/products/0/0/1/{}/android/stickers.zip'.format(productId), timeout=10)
          with open(zipFilePath, 'wb') as f:
              f.write(zipFile.content)
      extractLocation = os.path.join(location, productId)
      if not os.path.exists(extractLocation):
          with zipfile.ZipFile(zipFilePath, 'r') as zip_ref:
              zip_ref.extractall(extractLocation)
      for (dirpath, dirnames, filenames) in walk(extractLocation):
          if key == True:
            imagePathsA = [os.path.join(dirpath,f) for f in filenames if '_key.png' in f]
          else:
            imagePathsA = [os.path.join(dirpath,f) for f in filenames if 'png' in f and '_key.png' not in f]
          paths = []
          for path in imagePathsA:
             try:
                 p = remove_background(path)
                 paths.append(p)
             except:
                 print('error saving image', path)
          imagePaths.extend(paths)
          break
    except:
        print('error processing image', line)
    return imagePaths

def get_image_paths(folder='dataofficial', taste=None, character=None, category=None, n=1, location='./tmp', num_workers=1, seed=None):
    os.makedirs(location, exist_ok=True)
    listPath = os.path.join(location, '{}_list.txt'.format(folder))
    if not os.path.exists(listPath):
        mylist = requests.get('https://s3.peer-ai.com/{}/list.txt'.format(folder))
        with open(listPath, 'wb') as f:
            f.write(mylist.content)
    with open(listPath, 'r') as f:
        lines = f.read()
    allLines = [l for l in lines.split('\n') if len(l) > 0]
    if category is not None:
        allLines = [l for l in allLines if category in l]
    if taste is not None:
        allLines = [l for l in allLines if taste in l]
    if character is not None:
        allLines = [l for l in allLines if character in l]
    if n >= 1:
        np.random.seed(seed)
        lines = np.random.choice(allLines, n)
    else:
        lines = allLines
    imagePaths = []
    if num_workers == 1:
        for line in tqdm(lines):
            imagePaths.extend(_process(line, location=location))
    else:
        with Pool(num_workers) as p:
            for imagePathsA in tqdm(p.imap(partial(_process, location=location), lines), total=len(lines)):
                imagePaths.extend(imagePathsA)
    # for line in tqdm(lines): # parallel for here
    #   imagePaths.extend(_process(location, line))
    return imagePaths

