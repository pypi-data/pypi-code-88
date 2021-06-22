import setuptools

setuptools.setup(
    name="ECAUGT",
    version="0.0.7",
    author="Yixin Chen & XiaoXiao Nong & Haiyang Bian",
    author_email="chenyx19@mails.tsinghua.edu.cn",
    maintainer='Minsheng Hao',
    maintainer_email="hmsh653@gmail.com",
    description="ECA Client",
#     long_description=long_description,
#     long_description_content_type="text/markdown",
#     url="https://github.com/kenblikylee/imgkernel",
    packages=setuptools.find_packages(),
    package_data={
        # 引入任何包下面的 *.txt、*.rst 文件
        "": ["*.csv"],
    },
    install_requires=[
        'tablestore',
        'numpy',
        'pandas'
        ],
    liciense='GPL',
    keywords=["Client", "ECA"],
    python_requires='>=3',
)
