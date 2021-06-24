import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="fluentCrawler",
  version="1.0.1",
  author="szw",
  author_email="1259577135@qq.com",
  description="A decorator crawler",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://gitee.com/szw1259577135/flu-crawler",
  packages=['fluentCrawler'],
  install_requires=[
    "Django >= 1.1.1",
    "caldav == 0.1.4",
    "retrying==1.3.3",
    "w3lib==1.22.0",
    "requests==2.25.1",
    "lxml==4.6.3",
    "urllib3==1.26.4",
    "gne==0.2.6",
    "gerapy_auto_extractor==0.1.2"
  ],
  platforms=["all"],
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)