from distutils.core import setup
setup(
    name="GrandyuStudio",          # 对外我们要发布的模块名字
    version="1.0",                 # 版本号
    description="这是关于测试的模块", # 描述
    author="侯宴春",
    author_email="houyanchun1017@icloud.com",
    py_modules=["GrandyuStudio.module01",  # 要发布的模块
                "GrandyuStudio.module02"]  # 要发布的模块
)