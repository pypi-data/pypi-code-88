import rlogging
from rocshelf.compile import meta, routes, tracebacks, utils, params

logger = rlogging.get_logger('mainLogger')


@tracebacks.stage_run
def run():
    """ Полная компиляция исходников опираясь на конфигурацию приложения """

    logger.info('Запуск компиляции')

    utils.backuping_last_compilation()
    utils.delete_dist()

    routes.run()
    meta.run()
