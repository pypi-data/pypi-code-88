from cologer.main import Cologer
from cologer.field import Fore, Back, Style


loger = Cologer()
loger.set_field_fore(time=Fore.CYAN,level=Fore.BLACK)
loger.debug.fields.level.set_back(Back.MAGENTA)
loger.info.fields.level.set_back(Back.BLUE)
loger.success.fields.level.set_back(Back.GREEN)
loger.warning.fields.level.set_back(Back.YELLOW)
loger.error.fields.level.set_back(Back.RED)