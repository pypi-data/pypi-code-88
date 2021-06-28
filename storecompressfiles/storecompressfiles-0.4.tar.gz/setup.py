from distutils.core import setup
from storecompressfiles.class1 import encode
setup(
  name = 'storecompressfiles',      
  packages = ['storecompressfiles'],  
  version = '0.4',     
  license='MIT',       
  description = 'Package can be used to store text files in compressed format i.e. allocating less space in the memory',   
  author = 'Ramandeep Singh',                   
  author_email = 'raman77768@gmail.com',      
  url = 'https://github.com/raman77768/storecompressfiles', 
  download_url = 'https://github.com/raman77768/storecompressfiles/archive/refs/tags/v_0.4.tar.gz',    
  keywords = ['compress', 'small size', 'memory', 'encode', 'encryption'],   
  install_requires=['pandas'],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
