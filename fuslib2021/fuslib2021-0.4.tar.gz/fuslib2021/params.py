import numpy as np


#PARMAS ESTARFM


w = 25  # set the half window size, if 25, the window size is 25*2+1=51 fine pixels
num_class = 4.0  # set the estimated number of classes, please set a larger value if blending images with very few bands
num_similar_pixel = 20   # set number of similar pixels, a smaller value is faster but accuracy may be lower
DN_min = 0.0  # set the range of DN value of the image,If byte, 0 and 255
DN_max = 10000.0
background = -9999   # set the value of background pixels. 0 means that pixels will be considered as background if one of its bands= 0
patch_long = 1000   # set the size of each block, if process whole ETM scene, set 500-1000

#500 de normal para el patch long




#PARMAS STARFM


# Set the size of the moving window in which the search for similar pixels 
# is performed
windowSize = 31

# Set the path where the results should be stored
#pathst = 'STARFM_demo/'

# Set to True if you want to decrease the sensitivity to the spectral distance
logWeight = False

# If more than one training pairs are used, set to True
tempst = False

# The spatial impact factor is a constant defining the relative importance of 
# spatial distance (in meters)
# Take a smaller value of the spatial impact factor for heterogeneous regions 
# (e.g. A = 150 m)
spatImp = 150 

# increasing the number of classes limits the number of similar pixels
numberClass = 4 

# Set the uncertainty value for the fine resolution sensor
# https://earth.esa.int/web/sentinel/technical-guides/sentinel-2-msi/performance 
uncertaintyFineRes = 0.03

# Set the uncertainty value for the coarse resolution sensor
# https://sentinels.copernicus.eu/web/sentinel/technical-guides/sentinel-3-olci/validation
uncertaintyCoarseRes = 0.03

# Other global variables
mid_idx = (windowSize**2)//2
specUncertainty = np.sqrt(uncertaintyFineRes**2 + uncertaintyCoarseRes**2)
tempUncertainty = np.sqrt(2*uncertaintyCoarseRes**2)

# Set the size of the slices in which to divide the image
# This number should be multiple of the image height and not bigger than it
# Use bigger size for small images
sizeSlices = 50













