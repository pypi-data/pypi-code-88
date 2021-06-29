from setuptools import setup
from io import open


def read(filename):
    with open(filename, encoding='utf-8') as file:
        return file.read()


setup(
    name='faina_semenovna',
    version='0.1a1',
    packages=['faina_semenovna', 'faina_semenovna.blanks'],
    install_requires=read('requirements.txt').split('\n'),
    url='https://gitlab.com/whiteapfel/FainaSemenovna',
    license='MPL 2.0',
    project_urls={
        "Дока по API от ФНС": "https://npd.nalog.ru/html/sites/www.npd.nalog.ru/pinfexch_0307.docx",
        "Донатик": "https://pfel.cc/donate",
        "Исходнички": "https://gitlab.com/whiteapfel/FainaSemenovna",
        "Тележка для вопросов": "https://t.me/apfel"
    },
    author='WhiteApfel',
    author_email='white@pfel.ru',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    description='Simplifies work with XML-API for self-employed partners in Russia'
)
