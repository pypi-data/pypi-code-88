#encoding=utf-8
from distutils.core import setup
with open(r'README.txt', 'r')as a:
    long_description = a.read()
setup(

    name='XiaoMai_Chaun',  # 对外模块名称
    version = '1.0', # 版本号
    description= '这是第一次对外发布的模块，用于测试哦！',
    url = "http://test.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author= '小心甘', # 发布人姓名
    author_email= '3039486905@qq.com',  #发布人邮箱
    py_modules= ['XiaoMai_Chaun.demo01', 'XiaoMai_Chaun.demo02']  # 对外发布的模块

)
'''构建一个发布文件。通过终端，cd 到模块文件夹 c 下面，再键入命令：
python setup.py sdist'''
'''本地安装模块
将发布安装到你的本地计算机上。仍在 cmd 命令行模式下操作，进 setup.py 所在目
录，键入命令：
python setup.py install
安装成功后，我们进入 python 目录/Lib/site-packages 目录（第三方模块都安装的这
里,python 解释器执行时也会搜索这个路径）'''