import setuptools

setuptools.setup(
    name='any_face',
    version='2.3.7',
    author='Serene',
    author_email='serenetech90@gmail.com',
    description='Anonymize human faces with Multi-Cascaded CNN',
    # package_dir='app',
    py_modules= ['anony_face'],
    packages=setuptools.find_packages(),
    install_requires=['mtcnn', 'opencv-python', 'matplotlib', 'Click'],
    entry_points='''
        [console_scripts]
        anony_face=anony_face:main
    ''',
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)