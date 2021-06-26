from socket import socket, AF_INET, SOCK_DGRAM
from threading import Lock

# @brief An implementation to allow syslog messages to be generated. 

class FACILITY:
  KERN=0
  USER=1
  MAIL=2
  DAEMON=3
  AUTH=4
  SYSLOG=5
  LPR=6
  NEWS=7
  UUCP=8
  CRON=9
  AUTHPRIV=10
  FTP=11
  LOCAL0=16
  LOCAL1=17
  LOCAL2=18
  LOCAL3=19
  LOCAL4=20
  LOCAL5=21
  LOCAL6=22
  LOCAL7=23
 
class PRIORITY:
  EMERG=0
  ALERT=1
  CRIT=2
  ERROR=3
  WARNING=4
  NOTICE=5
  INFO=6
  DEBUG=7

syslogSocket=None
lock = Lock()
  
def syslog(priority, message, facility=FACILITY.LOCAL0, host='localhost', port=514):
    """
	  @brief Send a syslog message.
      @param priority The syslog priority level.
      @param message The text message to be sent.
      @param facility The syslog facility 
      @param host The host address for the systlog server.
      @param port The syslog port.
	"""
    global lock, timer, syslogSocket
	
    try:
        lock.acquire()
        if not syslogSocket:
            syslogSocket = socket(AF_INET, SOCK_DGRAM)

        smsg = '<%05d>%s' % ( (priority + facility*8), message )
        syslogSocket.sendto(smsg, (host, port))

    finally:
        lock.release()


