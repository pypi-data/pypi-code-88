import pathlib
from distutils.core import setup
from setuptools import find_packages
HERE=pathlib.Path(__file__).parent
README=(HERE/"README.md").read_text()

setup(
  name = 'face-mask-classifier',         # How you named your package folder (MyLib)
  packages = find_packages(include=['face-mask-classifier','face-mask-classifier.detect_mask','face-mask-classifier.train']),
  include_package_data=True,
  version = '1.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Detect face mask in an Image',# Give a short description about your library
  long_description=README,
  long_description_content_type="text/markdown",  
  author = 'Baskaran Thulukanam',                   # Type in your name
  author_email = 'baskar.mailbox@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Baskar-t/face-mask-classifier',   # Provide either the link to your github or to your website
  #download_url='https://github.com/Baskar-t/face-mask-classifier/archive/refs/tags/0.4.tar.gz',
  keywords = ['face-mask-classifer', 'SVM-classifier'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'Keras==2.4.3',
          'keras-facenet==0.3.2',
          'tensorflow==2.5.0',
          'scikit-learn==0.24.2',
          'mtcnn==0.1.0',
          'numpy==1.19.5'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)