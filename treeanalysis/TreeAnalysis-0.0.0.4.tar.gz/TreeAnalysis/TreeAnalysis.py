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
    
#Event tree class used to analyize one-to-many-many-many relationships.
#Use addListener to attache a function to one of the keys of the lists in the one-many relationships.
class TreeAnalysis:
    def __init__(self,path,filename="Looper_output.json"):
        self.filename = filename
        self.listeners = []
        self.data = json.load(open(path))

    #Add a function based on the key attached to the one-many relationship in the json
    def addListener(self,function,event):
        listener = (function,event)
        self.listeners.append(listener)

    #Emit an event callaing all the functions with matching event names (case insensitive). 
    def emit(self,event_name,*args,**kwargs):
        logging.debug(f'Emitting event: {event_name}')
        for function,event in self.listeners:
            if event.upper() == event_name.upper():
                logging.debug(f'Listener triggered: {event}')
                function(*args)

    #Loop through every list in every dict of dataset
    #If pocesses is not None then multiprocessing will be enables throughb batches.
    def loop(self,data=None,processes=None,write=True):
        if data is None: data = self.data
        self.emit('/start')
        if processes is None:
            self.bubbleLayer(data)
            if write:
              self.save()
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
                self.save(outputs)
            lopping.info("Finished loop.")
        self.emit('/end')

    #Recusivly look through dicts in list looking for nested lists
    #Will emit an even on any key that defines a list for each object.
    def bubbleLayer(self,layer,history='',*args,parent=None,**kwargs):
      for obj in layer:
        if not isinstance(obj,dict):
          continue
        logging.debug(history+'/before')
        self.emit(history+'/each',obj,*args,**kwargs)
        self.emit(history+'/before',obj,*args,**kwargs)
        for key,value in obj.items():
          if isinstance(value,list) and len(value)>0:
            #Enter item
            prefix = history +'/'+ key
            self.bubbleLayer(value,key,obj,*args,**kwargs)
        logging.debug(history+'/after')
        self.emit(history+'/after',obj,*args,**kwargs)

    #Save the data to the specified output file. 
    def save(self,data=None):
      if data is None:
        data = self.data
      if self.filename is None:
        print("No output filename specified.")
      else:
        with open(self.filename,'w+') as f:
          json.dump(data,f,indent=2,default=defaultconverter)
          logging.info(f'Saved to {self.filename}')
        
