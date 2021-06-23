import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
   long_description = fh.read()
setuptools.setup(    
    name="SteveChessboardSmith23",    
    version="0.0.1",    
    author="steve",    
    author_email="s.smith200712@gmail.com",    
    description="It is a chess board",    
    long_description=long_description,    
    long_description_content_type="text/markdown",    
    url="https://github.com/STEVE-al/ChessBoardGame",    
    packages=setuptools.find_packages(),    
    classifiers=[        "Programming Language :: Python :: 3",        
                 "License :: OSI Approved :: MIT License",        
                 "Operating System :: OS Independent",    
                 ],   
    python_requires='>=3.6',)