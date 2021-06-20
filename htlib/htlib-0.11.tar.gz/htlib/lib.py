from serial import Serial
from time import sleep
from threading import Thread
from requests import post
from smtplib import SMTP

class BSerial(Serial):
    """
    This class have some methods to ease the use of pyserial

    Args:
        Serial (of module pyserial): extends from Serial
    """
    def __init__(self,**kargs):
        """
        **kargs: init from Serial, more information in https://pyserial.readthedocs.io/en/latest/pyserial_api.html
        example:
            port: Device name
            baudrate(int): baud rate such as 9600 or 115200 
        """
        super().__init__(**kargs)

        self.separator="-"

    def write_string_port(self,value):
        """
        method to send some value to serial port

        Args:
            value (anytype): this value will convert to string to send it to serial port
        """
        self.write((str(value)+'\n').encode())

    def start_read_string_port(self,command):
        """
        method to start to receive values
        Args:
            command (function): create in this "function" the actions to the value received
        """
        self.start_thread = True
        self.thread = Thread(target=self.__Thread_read_port,args=(command,))
        self.thread.start()

    def stop_read_string_port(self):
        """
        method to stop receiving values
        """
        self.start_thread = False
        self.thread.join()
        del(self.start_thread)
        del(self.thread)

    def __Thread_read_port(self,command):
        """
        private method

        Args:
            command (function): this method read values from serial port
        """
        while self.start_thread:
            if self.in_waiting > 0:
                value = self.readline().decode().replace("\n","")
                command(value.split(self.separator))

class Ubidot_Client:

    def __init__(self,token,device):
        """ Constructor for client 

            token([str]): CREDENTIALS UBIDOT
            device([str]): Device Label

        """
        self.token = token
        self.label_device = device

        self.HEADERS = {'X-Auth-Token':token}

    def __send_value(self, data, variable_label):
        """this method is executing in thread
        """
        link = f"https://things.ubidots.com/api/v1.6/devices/{self.label_device}/{variable_label}/values"
        try:

            self.r = post(link,headers=self.HEADERS,json=data)
            print("[OK]: DATA HAS BEEN SENDED SUCCESFUL")
        except Exception as e: 
            print(f"[ERROR]: {str(e)}")

    def send_value(self, variable_label, inthread=False,  **data):
        """Send value to Ubidot
        Args:
            data ([keywords]): data to send,example label_variable=value,label_variable2=value2,...
        """
        
        if inthread:
            Thread(target=self.__send_value, args=(data, variable_label)).start()
        else:
            self.__send_value(data, variable_label)

    def close(self):
        self.r.close()

class Email:

    def __init__(self,email,password):
        """init class Email

        Args:
            email ([str]): [your email]
            password ([str]): [your password]
        """

        self.email = email
        self.password = password

    def send_email(self,dest,message="email from python",server="smtp.live.com",port=587):
        """send an email in a second thread

        Args:
            dest (list): [destination email]
            message (str, optional): [message of the email]. Defaults to "email from python".
            server (str, optional): [server from the domain]. Defaults to "smtp.live.com".
            port (int, optional): [port from the domain]. Defaults to 587.
        """
        t = Thread(target=self.__thread_send_email,args=(dest,message,server,port))
        t.start()

    def __thread_send_email(self,dest,message,server,port):
        message = '\n'+message
        try:
            with SMTP(server,port) as server:
                server.ehlo() 
                server.starttls() 
                server.login(self.email,self.password)
                server.sendmail(self.email,dest,message)
                server.quit()
        except Exception as e:
            print(f"[RROR] = {str(e)}")


if __name__ == '__main__':#example

    def action_read(value):
        print(value)

    s = BSerial(port='COM1',baudrate=9600)
    s.start_read_string_port(action_read)

    while True:
        valor = input("Ingrese un valor - x para terminar")
        if valor == "x":break
        s.write_string_port(valor)
        sleep(1)#only for sthetic, i you wish try like comment
    s.stop_read_string_port()
    s.close()

        