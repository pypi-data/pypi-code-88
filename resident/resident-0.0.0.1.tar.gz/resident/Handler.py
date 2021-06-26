import json,logging
from datetime import datetime,timedelta,date
from dateutil.parser import parse as parseDate

WARN_NICKNAME = "Nickname is not installed: pip install -U --no-cache-dir nickname"
try:
    from nickname import Name
except:

    logging.warning(WARN_NICKNAME)

#Used to pickle datetimes into json files
def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()
  if isinstance(o, date):
      return o.__str__()
   
    
#Handler for FamilyTreeNow type of data
class Handler:
  UnknownEventExeption = Exception("Event is not known.")
  def __init__(self,filename,write=None):
    self.write = write
    self.events=[]
    if isinstance(filename,str) and '.json' in filename:
      self.people = json.load(open(filename))
    else:
      raise Exception("Filename Invaled: Must instantiate Handler with path to .json.")

  def startLoop(self,write=None):
    #Execute events on each stage while looping through whole dataset.
    for person in self.people:
      name = self.getName(person)
      self.onPersonBefore(person,name)
      for query in self.getQuery(person):
        for result in self.getResults(query):
            self.onResultBefore(result,person,name)
            for address in self.getAddresses(result):
                self.onAddress(address,result,person,name)
            self.onResultAfter(result,person,name)
      self.onPersonAfter(person,name)
    self.onEndLoop()

    #Writing
    if self.write is not None or write is not None:
        outFile = open('updated_'+self.filename,'w+')
        json.dump(self.people,outFile,indent=2, default=defaultconverter)

  def addListener(self,listener,event_name:str):
    self.events.append((listener,event_name.upper()))

  def _onEvent(self,*args,**kwargs):
    event = args[0]
    for listener,event_name in self.events:
      if event_name.upper() in event.upper():
          listener(*args[1:])
    
  def onPersonBefore(self,person,name):
    self._onEvent('onPersonBefore',person,name)
    
  def onPersonAfter(self,person,name):
    self._onEvent('onPersonAfter',person,name)
  
  def onResultBefore(self,result,person,name):
    self._onEvent('onResultBefore',result,person,name)
  
  def onResultAfter(self,result,person,name):
    self._onEvent('onResultAfter',result,person,name)
    
  def onAddress(self,address,result,person,name):
    self._onEvent('onAddress',address,result,person,name)
    
  def onEndLoop(self):
    self._onEvent('onEndLoop')

  
  def getName(self,person):
    try:
      return Name(person['first'],person['middle'],person['last'])
    except Exception as e:
      logging.warning(WARN_NICKNAME)
      raise e
    return f"{person['first']} {person['middle']} {person['last']}"

  #Sometimes there is an extra depth layer for the query parameters before results.
  def getQuery(self,person):
    if 'details' in person:
      #Details is depricated use 'results' for any nested data.
      results = person['details']
    else:
      results = person['results']
    return results

  #Confusing way to get around different depth levels
  def getResults(self,result):
      if 'record_type' in result:
          return result['results']
      return [result] #No query data

  def getAddresses(self,result):
    if 'addresses' in result:
      #Depricated: Use results as the key to all nested values.
      addresses = result['addresses']
    else:
      addresses = result['results']
    return addresses

