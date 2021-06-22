import sys
import cartils.enums as enums
import os
import colorama

FAILURE_BASE = '[FAILURE]'
SUCCESS_BASE = '[SUCCESS]'
ERROR_BASE = '[ERROR]'
WARN_BASE = '[WARN]'
INFO_BASE = '[INFO]'
DEBUG_BASE = '[DEBUG]'
TRACE_BASE = '[TRACE]'

FAILURE_PREFIX = f'{enums.Colors.BOLD.value}{enums.Colors.RED.value}{FAILURE_BASE}{enums.Colors.RESET.value} '
SUCCESS_PREFIX = f'{enums.Colors.BOLD.value}{enums.Colors.GREEN.value}{SUCCESS_BASE}{enums.Colors.RESET.value} '
ERROR_PREFIX   = f'{enums.Colors.RED.value}{ERROR_BASE}{enums.Colors.RESET.value} '
WARN_PREFIX    = f'{enums.Colors.YELLOW.value}{WARN_BASE}{enums.Colors.RESET.value} '
INFO_PREFIX    = f'{enums.Colors.BLUE.value}{INFO_BASE}{enums.Colors.RESET.value} '
DEBUG_PREFIX   = f'{enums.Colors.CYAN.value}{DEBUG_BASE}{enums.Colors.RESET.value} '
TRACE_PREFIX   = f'{enums.Colors.MAGENTA.value}{TRACE_BASE}{enums.Colors.RESET.value} '

class Logger:
    def __init__(self, log_level, html=False, html_element='p'):
        if html:
            global FAILURE_PREFIX, SUCCESS_PREFIX, ERROR_PREFIX, WARN_PREFIX, INFO_PREFIX, DEBUG_PREFIX, TRACE_PREFIX
            FAILURE_PREFIX = f'<{html_element} style="color:{enums.Html.RED.value}"><b>{FAILURE_BASE}</b></{html_element}> '
            SUCCESS_PREFIX = f'<{html_element} style="color:{enums.Html.GREEN.value}"><b>{SUCCESS_BASE}</b></{html_element}> '
            ERROR_PREFIX   = f'<{html_element} style="color:{enums.Html.RED.value}">{ERROR_BASE}</{html_element}> '
            WARN_PREFIX    = f'<{html_element} style="color:{enums.Html.YELLOW.value}">{WARN_BASE}</{html_element}> '
            INFO_PREFIX    = f'<{html_element} style="color:{enums.Html.BLUE.value}">{INFO_BASE}</{html_element}> '
            DEBUG_PREFIX   = f'<{html_element} style="color:{enums.Html.CYAN.value}">{DEBUG_BASE}</{html_element}> '
            TRACE_PREFIX   = f'<{html_element} style="color:{enums.Html.MAGENTA.value}">{TRACE_BASE}</{html_element}> '
        colorama.init()
        if log_level == 'NONE':
            self.LOG_LEVEL = enums.LogLevel.NONE.value
        elif log_level == 'FAILURE':
            self.LOG_LEVEL = enums.LogLevel.SUCCESS.value
        elif log_level == 'SUCCESS':
            self.LOG_LEVEL = enums.LogLevel.SUCCESS.value
        elif log_level == 'ERROR':
            self.LOG_LEVEL = enums.LogLevel.ERROR.value
        elif log_level == 'INFO':
            self.LOG_LEVEL = enums.LogLevel.INFO.value
        elif log_level == 'WARN':
            self.LOG_LEVEL = enums.LogLevel.WARN.value
        elif log_level == 'DEBUG':
            self.LOG_LEVEL = enums.LogLevel.DEBUG.value
        elif log_level == 'TRACE':
            self.LOG_LEVEL = enums.LogLevel.TRACE.value        

    def FAILURE(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.FAILURE.value:
            print('{}{}'.format(FAILURE_PREFIX, message))

    def FAILUREs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.FAILURE.value:
            return '{}{}'.format(FAILURE_PREFIX, message)

    def SUCCESS(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.SUCCESS.value:
            print('{}{}'.format(SUCCESS_PREFIX, message))

    def SUCCESSs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.SUCCESS.value:
            return '{}{}'.format(SUCCESS_PREFIX, message)

    def ERROR(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.ERROR.value:
            print('{}{}'.format(ERROR_PREFIX, message))

    def ERRORs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.ERROR.value:
            return '{}{}'.format(ERROR_PREFIX, message)

    def WARN(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.WARN.value:
            print('{}{}'.format(WARN_PREFIX, message))

    def WARNs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.WARN.value:
            return '{}{}'.format(WARN_PREFIX, message)

    def INFO(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.INFO.value:
            print('{}{}'.format(INFO_PREFIX, message))

    def INFOs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.INFO.value:
            return '{}{}'.format(INFO_PREFIX, message)

    def DEBUG(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.DEBUG.value:
            print('{}{}'.format(DEBUG_PREFIX, message))

    def DEBUGs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.DEBUG.value:
            return '{}{}'.format(DEBUG_PREFIX, message)
    
    def TRACE(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.TRACE.value:
            print('{}{}'.format(TRACE_PREFIX, message))

    def TRACEs(self, message):
        if self.LOG_LEVEL >= enums.LogLevel.TRACE.value:
            return '{}{}'.format(TRACE_PREFIX, message)

    

if __name__ == '__main__':
    logger = Logger('TRACE')
    logger.FAILURE("failure test")
    logger.SUCCESS("success test")
    logger.ERROR("error test")
    logger.WARN("warn test")
    logger.INFO("info test")
    logger.DEBUG("debug test")
    logger.TRACE("trace test")

    logger = Logger('TRACE', html=True, html_element="h1")
    logger.FAILURE("failure test")
    logger.SUCCESS("success test")
    logger.ERROR("error test")
    logger.WARN("warn test")
    logger.INFO("info test")
    logger.DEBUG("debug test")
    logger.TRACE("trace test")

    logger = Logger('TRACE', html=True, html_element="h1")
    print(logger.FAILUREs("failure test"))
    print(logger.SUCCESSs("success test"))
    print(logger.ERRORs("error test"))
    print(logger.WARNs("warn test"))
    print(logger.INFOs("info test"))
    print(logger.DEBUGs("debug test"))
    print(logger.TRACEs("trace test"))