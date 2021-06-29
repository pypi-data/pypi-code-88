from sigur_interact import functions
from sigur_interact.tests import settings_test


print('Создание подключения')
sigur_socket = functions.get_connection(settings_test.contr_ip, settings_test.contr_port)
print('Авторизация')
auth_result = functions.auth_connection(sigur_socket)
print("Результат:", auth_result)