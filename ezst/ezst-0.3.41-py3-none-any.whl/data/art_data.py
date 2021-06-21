import os
import zipfile
import requests

base_dir = 'art'


def load():
  save_path = './art.zip'
  url = 'https://easy-server.s3.ap-northeast-2.amazonaws.com/ezst/art.zip'
  r = requests.get(url, stream=True)
  with open(save_path, 'wb') as fd:
      for chunk in r.iter_content(chunk_size=128):
          fd.write(chunk)

  local_zip = 'art.zip'

  zip_ref = zipfile.ZipFile(local_zip, 'r')

  zip_ref.extractall('./')
  zip_ref.close()
  
  os.remove("art.zip")