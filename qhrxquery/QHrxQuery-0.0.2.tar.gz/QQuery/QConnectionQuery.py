import zmq
import pandas as pd

class QConnectionQuery:
    def __init__(self,address,port):
        self.address = address
        self.port = port

    def __deal(self,msg):
        msglist = msg.split(";")
        name = msglist[0].split(",")
        msglist.pop(0)
        typelist = msglist[0].split(",")
        msglist.pop(0)
        list = []
        for row in msglist:
            data = row.split(",")
            field = []
            index = 0
            for type in typelist:
                if type =="float":
                    field.append(float(data[index]))
                elif type =="int":
                    field.append(int(data[index]))
                else:
                    field.append(data[index])
                index+=1
            list.append(field)
        return pd.DataFrame(list, columns=name)

    def __connect(self):
        self.context = zmq.Context()
        self.socket = self.context.socket(zmq.REQ)
        self.socket.connect("tcp://" + self.address + ":" + str(self.port))
        self.socket.setsockopt(zmq.RCVTIMEO, 8000)
        self.socket.setsockopt(zmq.SNDTIMEO, 1)
        self.socket.setsockopt(zmq.LINGER, 0)

    ## type数据类型
    #       share->成分股(可使用数字0代替) ,
    #       option->成分期权(可使用数字1代替),
    #       minute->分钟数据(可使用数字2代替),
    #       day->日线数据(可使用数字3代替)
    def query(self,type,code,field = "",begin_time = "",end_time = ""):
        try:
            self.__connect()
            msg = str(type)+":"+code+":"+field+":"+begin_time+":"+end_time
            self.socket.send(bytes(msg, encoding='utf-8'))
            msg = self.socket.recv().decode('utf-8')
            if len(msg) == 0:
                return pd.DataFrame([], columns=[])
            self.socket.close()
            return self.__deal(msg)
        except Exception as e:
            self.socket.close()
            return pd.DataFrame([], columns=[])
