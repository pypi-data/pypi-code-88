import os.path as osp
import sys
import argparse

import numpy as np
import pandas as pd
from skimage.io import imread
from skimage.measure import regionprops_table
import tifffile as tifff


# number of images
NUM_IMAGES = 195

def load_image(idx: int, PATH):
    """
    Freely inspired from napari tutorial: https://napari.org/tutorials/applications/cell_tracking.html
    Load result of manual tracking as an image. 

    Parameters
    ----------
    idx : int
        Index of the image to load.

    PATH : str
        Path to image folder

    Returns
    -------
    image : np.ndarray
       The image specified by the index, idx
    """
    filename = osp.join(PATH, '01_GT/TRA', f'man_track{idx:0>3}.tif')
    return imread(filename)


def regionprops_plus_time(idx, stack):
    """
    Freely inspired from napari tutorial: https://napari.org/tutorials/applications/cell_tracking.html
    Return the unique track label, centroid and time for each track vertex.

    Parameters
    ----------
    idx : int
        Index of the image to calculate the centroids and track labels.
    stack : numpy.ndarray
        stack of images containing the results of manual tracking


    Returns
    -------
    data_df : pd.DataFrame
       The dataframe of track data for one time step (specified by idx).
    """

    props = regionprops_table(stack[idx, ...], properties=('label', 'centroid'))
    props['frame'] = np.full(props['label'].shape, idx)
    return pd.DataFrame(props)


def parse_args(args=None):
    """
    Parse arguments for main()
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('data_dir',
                        help='path of the data directory')
    
    parser.add_argument('-i', '--no_image',
                        action="store_true",
                        default=False,
                        help='do not extract image')

    parser.add_argument('-p', '--positions',
                        action="store_true",
                        default=False,
                        help='extract positions')

    parsed_args = parser.parse_args(args)

    return parsed_args


def main(args=None):
    """ 
    Main function to extract images from dataset and save it as a tiff stack
    Freely inspired from napari tutorial: https://napari.org/tutorials/applications/cell_tracking.html
    """

    # load and check argument
    args = sys.argv[1:] if args is None else args
    parsed_args = parse_args(args)

    data_dir = osp.realpath(parsed_args.data_dir)
    dont_get_image = parsed_args.no_image
    get_positions = parsed_args.positions

    # check data_dir
    if not osp.exists(data_dir):
        raise Exception("ERROR: the passed data directory does not exist. Aborting...")

    if not osp.isdir(data_dir):
        raise Exception("ERROR: the passed data directory is not a directory. Aborting...")

    if not dont_get_image:
        print("extracting images...")
        # extract images
        stack = np.asarray([imread(osp.join(data_dir, '01', f't{i:0>3}.tif')) for i in range(NUM_IMAGES)])

        #save_image
        tifff.imsave(osp.join(data_dir,'stack.tif'), stack)

    if get_positions:
        print("extracting positions...")
        stack = np.asarray([load_image(i,data_dir) for i in range(NUM_IMAGES)])
        data_list = []
        for idx in range(NUM_IMAGES): 
            sys.stdout.write("\033[K")
            print('image {}/{}'.format(idx + 1,NUM_IMAGES), end ='\r', flush = True)
            data_list.append(regionprops_plus_time(idx,stack))
        data_df_raw = pd.concat(data_list).reset_index(drop=True)

        # sort the data lexicographically by track_id and time
        data_df = data_df_raw.sort_values(['label', 'frame'], ignore_index=True)

        # create the final data array: track_id, T, Z, Y, X
        data = data_df.loc[:, ['label', 'frame', 'centroid-0', 'centroid-1', 'centroid-2']]

        # rename columns
        data.columns = ['track', 'frame', 'z', 'y', 'x']

        # save
        data.to_csv(osp.join(data_dir,'positions.csv'), index=False)


if __name__ == '__main__':
    main()


