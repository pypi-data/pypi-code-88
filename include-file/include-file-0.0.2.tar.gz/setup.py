from setuptools import find_packages, setup


def readme():
  with open('README.md') as f:
    return f.read()


setup(name='include-file',
      version='0.0.2',
      description="Replace {% include 'file.txt' %} with actual file contents",
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='https://github.com/seanhwangg/incluce_file',
      author='Sean Hwang',
      author_email='rbtmd1010@gmail.com',
      packages=find_packages(),
      python_requires='>=3.8',
      install_requires=[
          'pypandoc>=1.5',
          'panflute>=2.1',
      ],
      license='MIT')
