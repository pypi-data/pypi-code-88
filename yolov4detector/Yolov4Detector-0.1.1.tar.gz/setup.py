import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Yolov4Detector",
    version="0.1.1",
    author="GoatWang",
    author_email="jeremy4555@yahoo.com.tw",
    description="Yolov4Detector",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GoatWang/Yolov4Detector",
    packages=setuptools.find_packages(),
    package_data={'Yolov4Detector': ['cfgs/*/*', 'samples/*']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
      install_requires=[
        'numpy >= 1.17',
        'opencv-python >= 4.1',
        'matplotlib',
        'pillow',
      ]
)

# 0.0.2 add get_params in io (cfg_fp, weights_fp, names_fp, img_size)
# 0.0.3 add name conversion function when inference
# 0.0.4 mod road names to Dxx
# 0.0.5 no box bug fixed
# 0.0.6 no box bug fixed
# 0.0.7 change to darknet yolov4
# 0.0.8 DEBUG NMS threshold input
# 0.0.9 add predict batch function
# 0.1.0 change to have coco pretrained weight as default
# 0.1.1 change README


# sudo python3 setup.py sdist bdist_wheel
# twine upload dist/Yolov4Detector-0.1.1*
    

