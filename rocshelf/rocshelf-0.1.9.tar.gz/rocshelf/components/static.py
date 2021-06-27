
import rlogging
from rcore.rpath import rPath
from rocshelf.config import pcf

logger = rlogging.get_logger('mainLogger')


class StaticFile(object):

    staticFileName: str
    staticFilePath: rPath

    def __init__(self, staticFileName: str) -> None:
        self.staticFileName = staticFileName
        self.staticFilePath = pcf.path('import', 'static').merge(staticFileName)

    def move_to_dist(self, targetStaticFileName: str):
        """ Копирование файла статики в папку экспорта

        Args:
            targetStaticFileName (str): Имя файла, которое будет у файла после копирования

        """

        exportFolderPath = pcf.path('export', 'static')
        targetStaticFilepath = exportFolderPath.merge(targetStaticFileName)

        logger.debug('Копирование медиа файла "{0}" в "{1}"'.format(
            self.staticFilePath,
            targetStaticFilepath
        ))
        self.staticFilePath.copy_file(targetStaticFilepath)
