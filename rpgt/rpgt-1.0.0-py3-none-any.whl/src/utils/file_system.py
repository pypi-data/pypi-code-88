"""
File system module.
"""
import os
import shutil


def clear_cwd(cwd: str) -> None:
    """
    Clears current working directory.
    """

    for filename in os.listdir(cwd):
        file_path = os.path.join(cwd, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except IOError as exception:
            print("Failed to delete %s. Reason: %s" % (file_path, exception))
