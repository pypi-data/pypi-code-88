from time import sleep


def unsubscribe_ce(sock):
    '''Отписка от событий контроллера класса CE'''
    sleep(1)
    sock.send(b'"UNSUBSCRIBE" CE\r\n')


def unsubscribe_us(sock):
    '''Отписка от обычный событий контроллера'''
    sleep(1)
    sock.send(b'"UNSUBSCRIBE"\r\n')


def subscribe_ce(sock):
    sleep(1)
    sock.send(b'"SUBSCRIBE" CE\r\n')


def subscribe_us(sock):
    sleep(1)
    sock.send(b'"SUBSCRIBE"\r\n')


def resubscribe(sock):
    print('\nПереподписка')
    unsubscribe_ce(sock)
    subscribe_ce(sock)


def unsubscribe_us2(sock):
    '''Отписка без получения ответа'''
    sleep(1)
    sock.send(b'"UNSUBSCRIBE"\r\n')


def get_point_status(data):
    point = data[4]
    status = data[3]
    return point, status


def send_open_gate_command(sock, gate_num):
    set_status_unlocked(sock, gate_num)


def send_close_gate_command(sock, gate_num):
    set_status_locked(sock, gate_num)


def set_status_unlocked(sock, point_num):
    set_status(sock, point_num, 'UNLOCKED')


def set_status_locked(sock, point_num):
    set_status(sock, point_num, 'LOCKED')


def set_status_normal(sock, point_num):
    set_status(sock, point_num, 'NORMAL')


def set_status(sock, point_num, state):
    msg = 'SETAPMODE {} {}\r\n'.format(state, point_num)
    sock.send(bytes(msg, encoding='utf-8'))


def send_auth_connection(sock):
    try:
        sock.send(b'"LOGIN" 1.8 "Administrator" ""\r\n')
        return sock
    except AttributeError:
        pass
