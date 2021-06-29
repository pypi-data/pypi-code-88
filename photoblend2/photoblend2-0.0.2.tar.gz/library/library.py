from PIL import Image
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
import numpy as np
import ctypes

def call_blend(image1_name, image2_name, blend_type):

    # Loads the shared object created by the Makefile
    _lib = ctypes.CDLL('./library/blendlib.so')


    # Sets argument and return types for C functions
    _lib.AdditionBlend.argtypes = [
        ctypes.c_int,
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C'),
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C'),
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C')
    ]
    _lib.AdditionBlend.restype = None


    _lib.SubtractionBlend.argtypes = [
        ctypes.c_int,
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C'),
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C'),
        np.ctypeslib.ndpointer(dtype=np.uint8, ndim=1, flags='C')
    ]
    _lib.SubtractionBlend.restype = None


    # Functions to bridge Python to C functions
    def addition_blend(size, image1, image2, result):
        _lib.AdditionBlend(ctypes.c_int(width1 * height1 * 3), image1, image2, result)


    def subtraction_blend(size, image1, image2, result):
        _lib.SubtractionBlend(ctypes.c_int(width1 * height1 * 3), image1, image2, result)


    # Open images/get dimensions
    try:
        img1 = Image.open(str(image1_name))
        width1, height1 = img1.size
    except FileNotFoundError as error:
        print('File ' + str(image1_name)  + ' not found.')
        return
    except:
        print('Error other than file not found.')
        return

    try:
        img2 = Image.open(str(image2_name))
        width2, height2 = img2.size
    except FileNotFoundError as error:
        print('File ' + str(image2_name) + ' not found.')
        return
    except:
        print('Error other than file not found.')
        return

    # Create blank image object with same dimensions
    img3 = Image.new(mode="RGB", size=(width1, height1))

    # Convert the images to a 1-D numpy array
    image1 = np.asarray(img1).flatten()
    image2 = np.asarray(img2).flatten()
    image3 = np.asarray(img3).flatten()

    size = image1.size

    # Image details
    print("Flat image Details:")
    print("-------------------")
    print(f"Dimensions: {image1.ndim}")
    print(f"Shape: {image1.shape}")
    print(f"Data Type: {image1.dtype}")
    print(f"Object type: {type(image1)}")
    print(f"CTypes: {image1.ctypes}\n")

    # call to C
    if blend_type == "add":
        addition_blend(size, image1, image2, image3)
    elif blend_type == "subtract":
        subtraction_blend(size, image1, image2, image3)
    else:
        print('Selected mode not currently supported.')
        return

    # Change resulting image back to 3-D array
    new_image = np.reshape(image3, (width1, height1, 3))
    result = Image.fromarray(new_image, 'RGB')
    result.save('test_image.jpg', 'JPEG')

    myImage = QLabel().setPixmap(QPixmap("test_image.jpg"))
    return myImage

    print("New image loaded.")
