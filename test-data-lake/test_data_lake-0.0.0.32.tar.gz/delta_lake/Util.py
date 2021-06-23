from notebookutils import mssparkutils


class Util:

    def __init__(self):
        pass

    def list_folder_delta_lake(self, dir):
        """
        method to list the folders in the data lake
        :param dir: directory to list
        :return: the directories and files in an array
        """
        return mssparkutils.fs.ls(dir)

    def delete_file_delta_lake(self, path):
        """
        remove files from data lake
        :param path: directory to delete
        """
        mssparkutils.fs.rm(path, True)
