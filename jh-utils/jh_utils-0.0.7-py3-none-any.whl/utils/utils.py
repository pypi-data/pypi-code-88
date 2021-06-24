import os

def get_files(folder, contains = 'INMET_SE_ES_'):
    folder = './{folder}'.format(folder = year)
    return list(filter(lambda k: str(contains) in k, os.listdir(folder)))