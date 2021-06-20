# ---------- requirements ----------
from datetime import datetime, timedelta
import os


# ---------- preprocess functions ----------

def map_save_path_routine(file_path):
    """
    Format the path to where the files outputed by the functions
    in maps will be saved.

    :param file_path: the file_path argument given by the user when calling
        the function. Default is '~/Desktop/vizcovidfr_files/'.
    :type file_path: str

    :return: the given file path appended with /vizcovidfr_files
    :rtype: str
    """
    if (file_path == '~/Desktop/vizcovidfr_files/'):
        A = os.path.expanduser("~")
        B = "Desktop"
        file_path = os.path.join(A, B)

    if not os.path.exists(os.path.join(file_path, "vizcovidfr_files")):
        os.mkdir(os.path.join(file_path, "vizcovidfr_files"))

    file_path = os.path.join(file_path, "vizcovidfr_files")
    return file_path
