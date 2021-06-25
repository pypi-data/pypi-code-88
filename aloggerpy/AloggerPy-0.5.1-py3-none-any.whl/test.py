from Alogger import Alogger

logger = Alogger.Alogger(log_level=Alogger.LogLevel.ALL)
logger.fatal("fatal")
logger.error("error")
logger.warning("warning")
logger.info("info")
logger.debug("debug")
logger.trace("trace")
logger.test("test")
# https://barisariburnu.github.io/blog/2015/08/17/pypi-paketi-olusturma.html


def deneme():
    logger.fatal("fatal")
    logger.error("error")
    logger.warning("warning")
    logger.info("info")
    logger.debug("debug")
    logger.trace("trace")
    logger.test("test")


deneme()
