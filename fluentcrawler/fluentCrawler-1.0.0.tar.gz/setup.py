import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="fluentCrawler",
  version="1.0.0",
  author="szw",
  author_email="1259577135@qq.com",
  description="A decorator crawler",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://gitee.com/szw1259577135/flu-crawler",
  packages=['fluentCrawler'], 
  platforms=["all"],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)