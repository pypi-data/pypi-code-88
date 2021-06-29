from setuptools import setup, find_packages
import shutil


try:
    shutil.rmtree("build")
    shutil.rmtree("dist")
except:
    pass


setup(name='script_client',
      version='1.5.0',
      author='TDC',
      author_email='tiandachun@meicai.cn',
      description="script client",
      long_description='''script client''',
      install_requires=['JPype1>=0.7.4',
                        "loguru>=0.3.2",
                        "requests>=2.22.0",
                        "tornado>=6.1",
                        "APScheduler>=3.7.0",
                        "psutil>=5.8.0",
                        ],
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      data_files=[
          ('script_client/static', ['script_client/static/layui.js']),
          ('script_client/static/js', ['script_client/static/js/ace.js', 'script_client/static/js/ext-language_tools.js',
                                    'script_client/static/js/mode-python.js','script_client/static/js/theme-eclipse.js']),
          ('script_client/static/js/snippets', ['script_client/static/js/snippets/python.js']),
          ('script_client/static/font',['script_client/static/font/iconfont.eot','script_client/static/font/iconfont.svg',
                                        'script_client/static/font/iconfont.ttf','script_client/static/font/iconfont.woff',
                                        'script_client/static/font/iconfont.woff2']),
          ('script_client/static/css', ['script_client/static/css/layui.css']),
          ('script_client/static/css/modules', ['script_client/static/css/modules/code.css']),
          ('script_client/static/css/modules/laydate/default', ['script_client/static/css/modules/laydate/default/laydate.css']),
          ('script_client/static/css/modules/layer/default', ['script_client/static/css/modules/layer/default/icon.png',
                                                              'script_client/static/css/modules/layer/default/icon-ext.png',
                                                              'script_client/static/css/modules/layer/default/layer.css',
                                                              'script_client/static/css/modules/layer/default/loading-0.gif',
                                                              ]),
          ('script_client/templates', ['script_client/templates/base.html','script_client/templates/file_manage.html',
                                       'script_client/templates/sys_manage.html']),
      ]
      )
