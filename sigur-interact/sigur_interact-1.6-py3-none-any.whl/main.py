from sigur_interact import commands
from sigur_interact import functions
from sigur_interact import settings
from threading import Thread


class SigurSDK:
    def __init__(self, ip, port, entry_gate_num, entry_ph_num, exit_gate_num, exit_ph_num, external_module=None,
                 version=1.8, login="Administrator", password="", test_mode=False, *args, **kwargs):
        self.entry_gate_num = entry_gate_num
        self.entry_ph_num = entry_ph_num
        self.exit_gate_num = exit_gate_num
        self.exit_ph_num = exit_ph_num
        self.all_elements = [self.entry_gate_num, self.entry_ph_num, self.exit_gate_num, self.exit_ph_num]
        self.sock = functions.get_connection(ip, port, test_mode)
        self.auth_status = functions.auth_connection(self.sock, login, password, version)
        self.external_sys = external_module      # Внешний модуль, функции которого могут вызываться из этого класса
        self.external_event_react_func = None    # Внешняя функция, которая будет вызываться по факту нового события
        self.listen_stream = []                  # В этом списке будут храниться все события с контроллера

    def open_entry_gate(self):
        commands.send_open_gate_command(self.sock, self.entry_gate_num)

    def close_entry_gate(self):
        commands.send_close_gate_command(self.sock, self.entry_gate_num)

    def open_exit_gate(self):
        commands.send_open_gate_command(self.sock, self.exit_gate_num)

    def close_exit_gate(self):
        commands.send_close_gate_command(self.sock, self.exit_gate_num)

    def set_point_state(self, point_num, state):
        commands.set_status(self.sock, point_num, state)

    def set_point_locked(self, point_num):
        commands.set_status_locked(self.sock, point_num)

    def set_point_unlocked(self, point_num):
        commands.set_status_unlocked(self.sock, point_num)

    def set_point_normal(self, point_num):
        commands.set_status_normal(self.sock, point_num)

    def subscribe_ce(self):
        commands.subscribe_ce(self.sock)

    def unsubscribe_ce(self):
        commands.unsubscribe_ce(self.sock)

    def subscribe_us(self):
        commands.subscribe_us(self.sock)

    def unsubscribe_us(self):
        commands.unsubscribe_us(self.sock)

    def start_listen_thread(self):
        """ Запустить поток параллельный поток сохранения всех событий в спсиок """
        Thread(target=self.start_listen_stream, args=()).start()

    def set_external_react_function(self, function):
        """ Установить функцию внешнего модуля, который будет вызываться при получении нового события скуд.
        Ему будет передаваться само событие"""
        self.external_event_react_func = function

    def start_listen_stream(self):
        """ Функция сохранения всех событий в список data """
        while True:
            data = self.sock.recv(1024)
            self.listen_stream.append(data)
            functions.new_event_react(data=data, external_event_func=self.external_event_react_func)

    def get_elements_status(self):
        all_el_status = {}
        for el in self.all_elements:
            status = functions.get_gate_status(self.sock, el)
            all_el_status[el] = status
        return all_el_status

    def get_point_status_parsed(self, point_num):
        return functions.get_object_status_parsed(self.sock, point_num)

    def get_gate_status(self, object_num):
        status = functions.get_gate_status(self.sock, object_num)
        return status

    def get_point_status(self, point_num):
        return functions.get_object_status(self.sock, point_num)

    def get_auth_status(self):
        return self.auth_status

    def get_gates_status(self):
        pass




