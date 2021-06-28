import os
import warnings

import scipy.io

import scipy.misc
import numpy as np
from imageio import imread, volread, imsave, volsave, get_reader


def saveimage(image, pathname):
    """
    Save image at a given pathname
    """
    pathname = os.path.expanduser(pathname)
    if (image.ndim > 3) or (image.ndim == 3 and list(image.shape)[2] > 3):
        if image.ndim == 4 and image.shape[2] < image.shape[3]:
            image = image.transpose((0, 1, 3, 2))
        filename, ext = os.path.splitext(pathname)
        volsave(filename + ".tif", image)
    else:
        imsave(pathname, image)


def loadimage(pathname):
    """
    Load image using pathname
    """
    pathname = os.path.expanduser(pathname)
    _, file_extension = os.path.splitext(pathname)
    if file_extension == ".tif":
        image = volread(pathname)
    else:
        image = imread(pathname)

    return image


def loadmatlab(pathname):
    """
    Load matlab file using pathname
    """
    pathname = os.path.expanduser(pathname)
    if os.path.exists(pathname):
        try:
            matlab_dict = scipy.io.loadmat(pathname)
        except IOError as e:
            raise ValueError("{}: {}".format(pathname, e))

    return matlab_dict


class imageProvider(object):
    """
    Image provider
    """

    def __init__(self, path, ext=None):
        """
        Create list with path to images
        """
        path = os.path.expanduser(path)
        if os.path.isdir(path) is not True:
            raise ValueError("Path {} is not directory".format(path))

        if ext is None:
            ext = ["jpg", "png", "bmp", "tiff", "tif"]

        self._path = path

        self._files = [
            f
            for f in sorted(os.listdir(self._path))
            if f.split(".")[-1] in ext
        ]
        self._num = len(self._files)

        if self.isempty():
            warnings.warn("No image file was found in {}".format(path))

        self._ext = ext
        self._index = 0

    def getimage(self, ind):
        """
        Get image at position "ind"
        """
        if ind < 0 and ind > self._num:
            raise ValueError("Index outside range")

        pathname = os.path.join(self._path, self._files[self._index])
        return np.array(loadimage(pathname=pathname))

    def __getitem__(self, ind):
        """
        Get image at position "ind"
        """
        self._index = ind
        return self.getimage(ind)

    def next(self):
        """
        Get next image
        """
        ind = self._index
        pathname = os.path.join(self._path, self._files[ind])
        im = loadimage(pathname)
        self._index = (ind + 1) % self._num
        return np.array(im)

    def getimagename(self):
        """
        Get current image name
        """
        return self._files[self._index]

    def isempty(self):
        return self._num == 0

    def __len__(self):
        return self._num


class segmentationProvider(object):
    """
    Segmentation dataset provider
    """

    def __init__(
        self, path_images, path_labels, ext_images=None, ext_labels=None
    ):
        self.images = imageProvider(path_images, ext_images)
        self.labels = imageProvider(path_labels, ext_labels)
        self._num = len(self.images)
        assert len(self.labels) == len(
            self.images
        ), "The number of images ({}) should match the number of labels ({})".format(
            len(self.images), len(self.labels)
        )
        self._index = 0

    def getimage(self, ind):
        """
        Get image at position "ind"
        """
        return self.images[ind]

    def getlabel(self, ind):
        """
        Get label at position "ind"
        """
        return self.labels[ind]

    def __getitem__(self, ind):
        """
        Get image at position "ind"
        """
        self._index = ind
        return self.getimage(ind), self.getlabel(ind)

    def next(self):
        """
        Get next image
        """
        ind = self._index
        image, label = self.__getitem__(ind)
        self._index = (ind + 1) % self._num
        return image, label

    def getimagename(self):
        """
        Get current image name
        """
        return self.images.getimagename()

    def getlabelname(self):
        """
        Get current label name
        """
        return self.labels.getimagename()

    def isempty(self):
        return self._num == 0

    def __len__(self):
        return self._num


class matProvider(object):
    def __init__(self, path, ext=None):
        path = os.path.expanduser(path)
        if os.path.isdir(path) is not True:
            raise ValueError("Path {} is not directory".format(path))

        if ext is None:
            ext = ["mat"]

        self._path = path

        self._files = [
            f
            for f in sorted(os.listdir(self._path))
            if f.split(".")[-1] in ext
        ]
        self._num = len(self._files)

        if self.isempty():
            warnings.warn("No matlab file was found in {}".format(path))

        self._ext = ext
        self._index = 0

    def getdata(self, ind):
        """
        Get matlab matrix at position "ind"
        """
        if ind < 0 and ind > self._num:
            raise ValueError("Index outside range")

        pathname = os.path.join(self._path, self._files[self._index])
        return loadmatlab(pathname)

    def __getitem__(self, ind):
        """
        Get data at position "ind"
        """
        self._index = ind
        return self.getdata(ind)

    def next(self):
        """
        Get next data
        """
        ind = self._index
        pathname = os.path.join(self._path, self._files[ind])
        data = loadmatlab(pathname)
        self._index = (ind + 1) % self._num
        return data

    def getfilename(self):
        """
        Get current image name
        """
        return self._files[self._index]

    def isempty(self):
        return self._num == 0

    def __len__(self):
        return self._num
