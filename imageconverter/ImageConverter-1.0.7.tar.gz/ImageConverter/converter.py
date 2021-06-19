from glob import glob
from os.path import isfile, realpath, dirname
from PIL import Image

class Converter:
    
    def __init__(self,files):
        self.files = files
    
    def toPng(self,savePath=None):
        convertFiles = self.files
        for images in convertFiles:
            image = Image.open(images)
            temp = images.split('\\')
            temp1 = temp[-1]
            temp2 = temp1.split('.')
            temp3 = temp2[0]
            if(savePath==None):
                image.save(temp3+".png")
            else:
                if savePath[-1]=='/':
                    image.save(savePath+temp3+".png")
                else:
                    image.save(savePath+"/"+temp3+".png")