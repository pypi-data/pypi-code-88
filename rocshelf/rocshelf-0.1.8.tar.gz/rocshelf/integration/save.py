""" Сохранение результата компиляции в кеш """

from rcore import utils
from rcore.rpath import rPath
from rocshelf.config import pcf, rcf
from rocshelf.components import routes, localization, relations

configFileName = 'rocshelf-compiled.json'


def save_processing_config():
    """ Сохранение необходимых полкей из конфигураци """

    templates = {}

    for localizationName in localization.GetLocal.all():
        templates[localizationName] = {}
        relation = relations.Relation(None, localizationName)
        for route in routes.GetRoute.all():
            templates[localizationName][route] = relation.template_path(route)

    compiledConfig = {
        'export': pcf.get(['path', 'export']),
        'templates': templates
    }

    compiledConfig = utils.rRecursion(compiledConfig).path_to_str()

    rPath(configFileName, fromPath='cache').dump(compiledConfig)
