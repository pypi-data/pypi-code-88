import PIL
import numpy as np
from PIL import Image
from PIL import ImageOps

def ascii_convert(path: str, store: str):
    """
    You need to give the path to image to be converted and the 
    name of text file where you would like to save the ascii art.
    """
    # try:
    img = Image.open(path)
    #convert image to grayscale
    img = ImageOps.grayscale(img)
    arr = np.array(img)
    #resizing image based on aspect ratio
    aspect = len(arr)/len(arr[0])
    img = img.resize((100,int(100*aspect*0.6)))
    arr = np.array(img)
    
    #ascii set
    ascii_set = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    arr =np.reshape(arr,(1,-1))
    
    #generating new ascii art
    new_art = [ascii_set[int(point/25)] for point in arr[0]]
    new_art = np.reshape(new_art,(-1,100))
    #saving to text file
    with open(store,'w') as f:
        for j in range(len(new_art)):
            for i in range(len(new_art[j])):
                f.write(new_art[j][i])
            f.write('\n')
    print("Generated ascii art at the desired location")

    # except:
    #     print("Unscriptable Image")