from sigur_interact import settings
from socket import socket
from traceback import format_exc


def get_connection(ip, port, test_mode, *args, **kwargs):
    if test_mode:
        from sigure_emulator.main import SigurEmulator
        se = SigurEmulator()
        return se
    try:
        sock = socket()
        sock.connect((ip, port))
        return sock
    except ConnectionRefusedError:
        pass


def new_event_react(data, external_event_func, *args, **kwargs):
    """ Реакция на новое событие по подписке """
    if external_event_func:         # Если задана функция внешнего модуля,
        external_event_func(data)   # вызвать его и передать ему событие


def send_sigur_command(sigur_socket, command):
    """ Отправляет команду в контроллер и возрващает ответ """
    command = get_command_formatted(command)
    send_command(sigur_socket, command)
    response = get_response(sigur_socket, command=command)
    return response


def get_command_formatted(command):
    """ Получает команду, форматирует его необходимый контроллеру вид и возвращает результат """
    masked_command = settings.controller_comands_mask.format(command)
    formatted_command = bytes(masked_command, encoding='utf-8')
    return formatted_command


def get_response(sock, command=None):
    """ Получает ответ от контроллера """
    try:
        return {'command': command, 'status': True, 'info': sock.recv(1024)}
    except AttributeError:
        return {'command': command, 'status': False, 'info': format_exc()}


def send_command(sock, command):
    """ Отправить команду на контролер """
    try:
        sock.send(command)
    except AttributeError:
        return {'status': False, 'info': format_exc()}


def get_sigur_auth_command(version, login, password):
    command = settings.sigur_auth_command.format(version, login, password)
    return command


def auth_connection(sock, login="Administrator", password="", version=1.8):
    """ Отправить команду на авторизацию на контроллере """
    if sock:
        auth_command = get_sigur_auth_command(version, login, password)
        send_result = send_sigur_command(sock, auth_command)
        return send_result

def get_gate_status(sock, gate_num):
    object_status = get_object_status(sock, gate_num)['info']
    status = parse_object_status(object_status)
    return status


def get_object_status(sock, object_num):
    command = settings.get_object_command.format(object_num)
    response = send_sigur_command(sock, command)
    print("RESPONSE:",  response)
    return response


def parse_object_status(object_status):
    """ Парсит ответ от контроллера Sigur на комманду GETAPINFO """
    object_status_str = str(object_status)
    splitted = object_status_str.split(' ')
    for el in splitted:
        if 'ONLINE' in el:
            return el


