import setuptools

setuptools.setup(name='fg-proto',
      version='0.0.23',
      author='Michal Plebanski',
      author_email='m@example.com',
      install_requires=["protobuf"],
      py_modules=["fg_proto"],             # Name of the python package
      package_dir={'':'fg_proto/src'}, 
)