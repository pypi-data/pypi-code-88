#Version: 1.0, Copyright: EliServices

class processGame:                                                                                    #The name that your target process is supposed to have. Can be replaced later.
    def __init__(self):
        global os, time, log
        import os, time

        self.path = os.path.abspath(".")                                                              #Make path available
        log = open(self.path + "/processnamer.log", "a")

        self.pid = (os.getpid())                                                                      #Make the current pid available
        vars = self.getName(self.pid).split(" ")
        self.script = vars[1]                                                                         #Make script name available
        self.prcname = vars[0]                                                                        #Make the name of the current process available

        log.write(time.ctime().split()[3] + ": " + self.prcname + "\n")
        log.flush()

    def nameStart(self,id, script):                                                                   #By default, th process that calles this is started
        global stream
        stream = os.popen("bash -c \"exec -a " + str(id) + " python " + str(script) + "&\"")          #Start process via bash
        log.write(time.ctime().split()[3] + ": " + self.prcname + ": Started new script: " + script + ", ProcessName: " + id + "\n")
        log.flush()
        return

    def nameStop(self,id,sig="SIGKILL"):
        sig = sig.upper()
        if sig == "SIGKILL":
            sig = " -KILL"
        elif sig == "SIGINT":
           sig = " -INT"
        elif sig == "SIGTERM":
            sig = " -TERM"
        elif sig == "SIGSTOP":
            sig = " -STOP"
        else:
            sig = ""

        global stream
        stream = os.popen("pkill" + sig + " -e -f " + id)                                             #bash command to kill process with id "id"
        output = stream.read()
        return output

    def getName(self,pid):
        global stream
        stream = os.popen("ps -o cmd= {}".format(pid))                                                #Bash command
        processname = stream.read().split("\n")[0]
        return processname

    def close(self):
        log.write(time.ctime().split()[3] + ": " + self.prcname + ": Exiting.\n")
        log.flush()
        log.close()                                                                                   #Close logfile

        try:
            stream.close()                                                                            #Close os.popen()
        except:
            pass

        return
