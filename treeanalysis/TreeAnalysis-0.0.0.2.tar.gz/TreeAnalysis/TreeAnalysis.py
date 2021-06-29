import json,logging,math
from datetime import datetime,timedelta,date
from dateutil.parser import parse as parseDate
from multiprocessing import Process,Pool
from itertools import repeat

#See logging
logging.basicConfig(level=logging.INFO)

#Used to pickle datetimes into json files
def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()
  if isinstance(o, date):
      return o.__str__()
   
class TreeAnalysis:
    def __init__(self,path,filename="Looper_output.json"):
        self.filename = filename
        self.listeners = []
        self.data = json.load(open(path))
        
    def addListener(self,function,event):
        listener = (function,event)
        self.listeners.append(listener)
        
    def emit(self,event_name,*args,**kwargs):
        logging.debug(f'Emitting event: {event_name}')
        for function,event in self.listeners:
            if event.upper() in event_name.upper():
                logging.debug(f'Listener triggered: {event}')
                function(*args)

    def loop(self,data=None,processes=None,write=True):
        if data is None: data = self.data
        if processes is None:
            self.bubbleLayer(data)
        else:
            elements = [element for element in data]
            batch_size = len(people)/processes
            batches = [
                elements[ round(i*batch_size) : round((1+i)*batch_size) ]
                for i in range(processes)
            ]
            with Pool(processes) as pool:
                outputs = pool.starmap(self.loop,zip(repeat(batches,repeat(None))))
            if write:
                logging.info(f'Writing data; len({len(outputs)})')
                self.write(outputs)
            lopping.info("Finished loop.")
        
    def bubbleLayer(self,layer,history='',*args,parent=None,**kwargs):
        for obj in layer:
            logging.debug(history+'/before')
            self.emit(history+'/each',obj,*args,**kwargs)
            self.emit(history+'/before',obj,*args,**kwargs)
            for key,value in obj.items():
                if isinstance(value,list) and len(value)>0:
                    #Enter item
                    prefix = history +'/'+ key
                    self.bubbleLayer(value,prefix,obj,*args,**kwargs)
            logging.debug(history+'/after')
            self.emit(history+'/after',obj,*args,**kwargs)
    def save(data):
        with open(self.filename,'w+') as f:
            json.dump(data,outfile,indent=2,default=defaultconverter)
        
