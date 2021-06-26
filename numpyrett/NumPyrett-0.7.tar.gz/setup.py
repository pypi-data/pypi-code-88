from distutils.core import setup
import os

def read(fname):
    """Read the README.MD file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
  name = 'NumPyrett',        
  packages = ['NumPyrett'],   
  version = '0.7',     
  license='MIT',        
  description = 'Prettyprint NumPy polynomials, matrices and arrays using LaTeX',
  long_description=read('README.md'),
  long_description_content_type='text/markdown' ,
  author = 'Rahul Gupta',                  
  author_email = 'rahul.gupta@gmconsultants.com',    
  url = 'https://github.com/argoopjmc/NumPyrett',  
  download_url = 'https://github.com/argoopjmc/NumPyrett/archive/refs/tags/v_07.tar.gz',
  keywords = ['NumPy', 'Education', 'Latex'],
  install_requires=[            
          'numpy'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',   
    'Intended Audience :: Science/Research',
    'Intended Audience :: Education',
    'Topic :: Scientific/Engineering',
    'Topic :: Text Processing :: Markup :: LaTeX',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3.6',      
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8'
  ],
)