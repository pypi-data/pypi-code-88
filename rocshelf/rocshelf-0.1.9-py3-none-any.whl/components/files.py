""" Модуль регуляции работы с входными и выходными типами файлов

"""

from rocshelf.config import pcf

STATIC_STYLE_EXPANSIONS = ('.css', '.scss', '.sass')
STATIC_SCRIPT_EXPANSIONS = ('.js', )
HTML_EXPANSIONS = ('.html', )

FILE_TYPES = ('style', 'script', 'html')


class GetFileInfo(object):
    """ Интерфес для получения имен и расширейни файлов исходников """

    htmlExpansions = {
        'style': 'css',
        'script': 'js',
        'html': 'html',
    }

    @staticmethod
    def expansions() -> list[str]:
        return {
            fileType: pcf.setting('expansion', fileType) for fileType in FILE_TYPES
        }

    @staticmethod
    def expansion(fileType: str) -> str:
        return pcf.setting('expansion', fileType)

    @staticmethod
    def html_expansions():
        return GetFileInfo.htmlExpansions

    @staticmethod
    def html_expansion(fileType: str):
        return GetFileInfo.htmlExpansions[fileType]
