from setuptools import setup, find_packages
setup(
    name='QConnectionQuery',  # '库的名称,一般写成文件夹的名字就可以了，也有的人不写成文件夹的名字，那么pip install和具体的import使用时候就不一样了，用起来会十分蛋疼，有一些包就是这样的。比如一个包，安装时候是pip install  xxx,但当你要使用时候要import yyy
    version="0.1.2",                  # 版本，每次发版本都不能重复，每次发版必须改这个地方
    description='内部使用',
    long_description="内部使用",    # 这是详细的，一般是交别人怎么用，很多包没写，那么在官网就造成没有使用介绍了
    long_description_content_type="text/markdown",
    author='lwt',       # 作者
    author_email='1447914988@qq.com',
    maintainer='lwt',     # 主要的工作人员
    maintainer_email='1447914988@qq.com',
    license='MIT License',
    # packages=['douban'], # 发布的包名
    packages=find_packages(),
    platforms=["all"],
    url='https://gitee.com/lwtyhm/qconnection-query.git',   # 这个是连接，一般写github就可以了，会从pypi跳转到这里去
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # License
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # 支持python版本
    install_requires=[              # 这里是依赖列表，表示运行这个包的运行某些功能还需要你安装其他的包
        'pyzmq',"pandas"
    ]
)