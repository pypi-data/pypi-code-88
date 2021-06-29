class SigurEmulator:
    """ Класс, эмулирующий подключение по socket с реальным контроллером СКУД, имеет методы:
    send - для отправки команд, recv - для получения ответа.
    Так-же имеет метод engine, который обрабатывает ответы полученные из send и создает ответы, доступные для recv """
    def __init__(self):
        self.buffer = ''

    def send(self, command, *args, **kwargs):
        print('\nSigurEmulator got command: {}'.format(command))


    def recv(self, *args, **kwargs):
        print("Sigur SKUD testing socket.")
        print("RECIEVING {}".format(args))

    def connect(self, *args, **kwargs):
        print("Sigur SKUD testing socket.")
        print("CONNECTING {}".format(kwargs))