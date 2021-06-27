from PIL import Image, ImageDraw, ImageFont
from .font import *
import random
import os

dirname = os.path.dirname(__file__)

class Generator:
    def __init__(self):
        self.fonts = f
        path = os.path.join(dirname, 'content')
        self.backgrounds = backgrounds = [ os.path.join(path,f) for f in os.listdir(path) if f[-2:] == 'ng']
        self.ink_colors = [(0, 0, 0), (32, 29, 137), (92, 69, 237), (42, 129, 197), (32, 29, 237)]
        self.source = []
        self.len2font_size = { 4 : 90 , 5 : 90 , 6 : 80 , 7 : 75 , 8 : 75 , 9 : 85 , 10 : 85 , 11 : 68 , 12 : 65, 13 : 65, 14 : 65 }

        self.N = len(self.fonts)
        self.M = len(self.backgrounds)
        self.R = len(self.ink_colors)

    def upload_source(self, PATH_TO_SOURCE):
        self.source = open(PATH_TO_SOURCE, 'r', encoding='utf-8').read().replace('\u200e','').split('\n')
        self.source = [s for s in self.source if len(s) < 14]
        print(len(self.source), 'expressions have been udploaded')

    def generate_batch(self, batch_size):
        assert len(self.source) > 0, 'Source is empty. Use upload() method to upload text'
        batch = []
        for i in range(batch_size):
            exp = random.choice(self.source)
            item = (self.generate_from_string(exp), exp)
            while item[0] == None:
              exp = random.choice(self.source)
              item = (self.generate_from_string(exp), exp)
          
            batch.append(item)
        return batch

    def select_background(self,string):
        exp = False
        long_letters = ['р','в','д','б','з','ф','у']
        for ll in long_letters:
          if ll in string:
            exp= True

        i = random.randint(0, self.M - 1)
        if exp == True:
          while 'exp' not in self.backgrounds[i]:
            i = random.randint(0, self.M - 1)
        else:
          while 'exp' in self.backgrounds[i]:
            i = random.randint(0, self.M - 1)

        img = Image.open(self.backgrounds[i])
        return img


    def generate_from_string(self, string, FONT_PATH=None):
        if len(string) < 4:
          return None
        if len(string) > 14:
          return None
        j = random.randint(0, self.R - 1)
        ink_color = self.ink_colors[j]
        img = self.select_background(string)
        L = len(string)

        font_size = self.len2font_size[L]


        if FONT_PATH != None:
          font = ImageFont.truetype(FONT_PATH, int(font_size))
        else:
          i = random.randint(0, self.N - 1)
          counter = 0
          while not self.fonts[i].isValid(string):
              i = random.randint(0, self.N - 1)
              counter += 1
              if counter > 10:
                return None
          font_size = int(font_size*self.fonts[i].size_coef)
          try:
            font = ImageFont.truetype(self.fonts[i].path, font_size)
          except:
            i = random.randint(0, self.N - 1)
            font = ImageFont.truetype(self.fonts[i].path, font_size)
        d = ImageDraw.Draw(img)
        d.text((10, 1), string, font=font, fill=ink_color)
        return img