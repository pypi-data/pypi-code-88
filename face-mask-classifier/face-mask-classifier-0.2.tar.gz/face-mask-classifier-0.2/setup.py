from distutils.core import setup
import setuptools
setup(
  name = 'face-mask-classifier',         # How you named your package folder (MyLib)
  packages = ['face-mask-classifier'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Detect face mask in an Image',   # Give a short description about your library
  author = 'Baskaran Thulukanam',                   # Type in your name
  author_email = 'baskar.mailbox@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/Baskar-t/face-mask-classifier',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/Baskar-t/face-mask-classifier/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['face-mask', 'classifier', 'SVM-classifier'],   # Keywords that define your package best
  Install_requires=[            # I get to this in a second
          'kears-facenet'
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