from __future__ import print_function
from PIL import Image
import time

from tesserocr import PyTessBaseAPI, RIL, iterate_level
image = Image.open("/Users/mohamedmentis/Dropbox/My Mac (MacBook-Pro.local)/Documents/Mentis/Development/Python/pdf2text/pdfs/images/saram_FRFFGGlobalFlexSustAccR2.png")

with PyTessBaseAPI() as api:
    t=time.time()
    api.SetImage(image)
    print(api.GetUTF8Text())
    print('TOME:', time.time()-t)
#    print(api.AllWordConfidences())
