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

        self.N = len(self.fonts)
        self.M = len(self.backgrounds)
        self.R = len(self.ink_colors)

    def upload_source(self, PATH_TO_SOURCE):
        self.source = open(PATH_TO_SOURCE, 'r', encoding='utf-8').read().replace('\u200e','').split('\n')
        self.source = [s for s in self.source if len(s) < 20]
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

    def generate_from_string(self, string, backgroud_type='random'):
        if len(string) < 6:
            return None
        if len(string) > 15:
            return None

        j = random.randint(0, self.R - 1)
        ink_color = self.ink_colors[j]

        if backgroud_type == 'clear':
            img = Image.new('RGB', (256, 64), color=(0, 0, 0))
        if backgroud_type == 'random':
            i = random.randint(0, self.M - 1)
            img = Image.open(self.backgrounds[i])
            if 'dark' in self.backgrounds[i]:
                ink_color = (15, 15, 15)

        font_size = 460 // len(string)

        i = random.randint(0, self.N - 1)
        counter = 0
        while not self.fonts[i].isValid(string):
            i = random.randint(0, self.N - 1)
            counter += 1
            if counter > 10:
              return None
        if font_size < 30:
          font_size = 35
        if font_size > 80:
          font_size = 60
        font_size = int(font_size * self.fonts[i].size_coef)
        font = ImageFont.truetype(self.fonts[i].path, font_size)
        d = ImageDraw.Draw(img)
        d.text((3, 3), string, font=font, fill=ink_color)
        return img