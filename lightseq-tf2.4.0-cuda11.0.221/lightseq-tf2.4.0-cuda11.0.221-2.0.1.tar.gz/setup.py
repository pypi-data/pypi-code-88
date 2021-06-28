from setuptools import find_packages, setup
from setuptools.dist import Distribution

class BinaryDistribution(Distribution):
  def is_pure(self):
    return False
  def has_ext_modules(self):
    return True

from setuptools.command.install import install
class InstallPlatlib(install):
    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib=self.install_platlib

setup(
  name='lightseq-tf2.4.0-cuda11.0.221',
  version='2.0.1',
  author='Xiaohui Wang, Ying Xiong, Xian Qian, Yang Wei',
  author_email='wangxiaohui.neo@bytedance.com, xiongying.taka@bytedance.com, qian.xian@bytedance.com, weiyang.god@bytedance.com',
  description='LightSeq is a high performance training library '
  'for sequence processing and generation implemented in CUDA',
  url='https://github.com/bytedance/lightseq2',
  classifiers=[
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: Apache Software License',
      'Operating System :: POSIX :: Linux',
  ],
  distclass=BinaryDistribution,
  cmdclass={'install': InstallPlatlib},
  packages=find_packages(),
  package_data={
    'lightseq':['liblightseq_op.so', '__init__.py'],
  },
  include_package_data=True,
)
