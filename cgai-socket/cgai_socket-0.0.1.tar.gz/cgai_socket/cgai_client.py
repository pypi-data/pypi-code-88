# -*- coding:utf-8 -*-


import socket


class Client(object):
    def __init__(self,HOST,PORT,BUFFER,timeout=0.55):
        super(Client, self).__init__()
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(timeout)
        self.HOST = HOST
        self.PORT = PORT
        self.BUFFER = BUFFER

    def send(self,msg):
        """
        发送信息
        :param msg:
        :return:
        """
        result = None
        try:
            self.client.connect((self.HOST, self.PORT))
            self.client.send(str(msg).encode('utf8'))
            all_backs = b''
            while True:
                back = self.client.recv(self.BUFFER)
                if not back:
                    break
                all_backs += back

        except Exception as request_from_222_ERR:
            print(str(request_from_222_ERR))
        finally:
            data = eval(all_backs.decode('utf8'))
            result = data.get('back',None)

            self.client.close()
        return result



