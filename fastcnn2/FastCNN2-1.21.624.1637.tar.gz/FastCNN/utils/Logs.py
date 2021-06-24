import threading

class ProcessLog:
    pass

class TrainLog:
    lock = threading.Lock()
    
    def getInputValue(value):
        val = "{}".format(value[0])
        for i in range(1,len(value)):
            val += ",{}".format(value[i])
        rtn = val + "\n"
        return rtn
    
    def add(self,path,logrow):
        self.lock.acquire()
        try:
            fs = open(path,"a+")
            
            fs.write(TrainLog.getInputValue(logrow))
            fs.close()
        except Exception as err:
            print(err)
        finally:
            self.lock.release()
        pass
    
    def get(self,path):
        self.lock.acquire()
        rtn = []
        try:
            fs = open(path,"r")
            
            rs = fs.readlines()
            
            for r in rs:
                r = r[:-1]
                rtn.append(r.split(','))
            
            fs.close()
        except Exception as err:
            print(err)
        finally:
            self.lock.release()
        return rtn
    pass

tlog = TrainLog()

if __name__ == "__main__":
    tlog.add("./1.csv",(1,2,3,4))
    tlog.add("./1.csv",(1,2,3,4))
    tlog.add("./1.csv",(1,2,3,4))
    tlog.get("./1.csv")
    pass