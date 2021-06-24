from cv2 import imread, cvtColor, COLOR_BGR2RGB
from sklearn.cluster import KMeans
from numpy import bincount, where

def importimage(filename):
    return imread(filename)

def processimage(image):
    ##Convert image into the RGB space
    img = cvtColor(image, COLOR_BGR2RGB)

    ##Resize into x by 3
    img = img.reshape((img.shape[0] * img.shape[1],3)) 

    return img

def findcolour(image, clusters):
    ##Create KMeans model with desired clusters.
    ##Number of clusters should be equal to the expected number of colours within the image.
    km = KMeans(n_clusters=clusters)
    model = km.fit(image)

    ##Calculate count of each label in the immage
    count = bincount(model.labels_)

    ##Return label used to define most dominate cluster (RGB value)
    return model.cluster_centers_[where(count == count.max())[0]][0]

def distance(c1, c2):

    distance = 0

    ##Standard Euclidean Distance
    for i in range(3):
        distance += ((c1[i] - c2[i])**2)

    return distance**(1/2)


def checkcolour(rgb, comparison):
    
    if comparison == {}:
    ##Define comparison base colours if none is passed.
    ##Expected benchmark RGB values should be passed/tuned to ensure accuracy.
        comparison = {
            "blue": [0,0,225],
            "red": [255,0,0],
            "green" : [0,128,0],
            "yellow": [255,255,0],
            "purple": [128,0,128],
            "white": [255,255,255],
            "black": [0,0,0],
            "orange": [255,165,0]
            }

    ##Calculate distance between rgb value and baseline. The smaller the value the closer the colours are in RGB space (the more likely they are to be the "same")
    for c in comparison:
        comparison[c] = distance(rgb, comparison[c])

    return comparison

def colourpick(filename, clusters, comparison={}):
    img = processimage(importimage(filename))
    col = findcolour(img, clusters)
    return checkcolour(col, comparison)