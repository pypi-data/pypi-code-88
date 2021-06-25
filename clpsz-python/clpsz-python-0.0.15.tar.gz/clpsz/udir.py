import os


# not include files in subdirectories
def get_files_from_dir(dir_path):
    result = []
    for (_dir, dir_names, filenames) in os.walk(dir_path):
        if not os.path.samefile(_dir, dir_path):
            break
        for filename in filenames:
            result.append(os.path.join(_dir, filename))
    return result
