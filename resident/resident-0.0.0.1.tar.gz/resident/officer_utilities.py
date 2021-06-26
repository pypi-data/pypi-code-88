from datetime import datetime,timedelta,date
from dateutil.parser import parse as parseDate
import json,os,logging,random,csv

dallas_radius = 45
share_limit = 0.40


#Requires 
def officerLoop(filename,officerBefore=None,officerAfter=None,resultBefore=None,resultAfter=None,eachAddress=None,end=None,write=False):
    police = json.load(open(filename))
    for officer in police:
        name = f"{officer['first']} {officer['middle']} {officer['last']}"
        if officerBefore is not None: officerBefore(officer,name)
        for result in results:
            if resultBefore: resultBefore(result,officer,name)
            for address in addresses:
                if eachAddress is not None: eachAddress(address,result,officer,name)
            if resultAfter: resultAfter(result,officer,name)
        if officerAfter is not None: officerAfter(officer,name)
    if end is not None: end()
    if writeopt:
        json.dump(police,open('updated_'+filename,'w+'),indent=2, default=defaultconverter)

def getEmploymentTime(officer):
    return parse_officer_dates(officer,check=False)

def parse_officer_dates(officer,check=True):
  if check and 'start_date' in officer and 'end_date' in officer: return
  officer['start_date'] = parseDate(officer['Adjusted Hire Date'].strip()).date()
  endDate = officer['Termination Date'].strip()
  if endDate == '':
    officer['end_date'] = datetime.now().date()
  else:
    officer['end_date'] = parseDate(endDate).date()
  delta = officer['end_date']-officer['start_date']
  secconds = delta.total_seconds()
  years = secconds/60/60/24/365
  return officer['start_date'],officer['end_date'],secconds,years

def freq(data,verbose=True,keys=None):
  if keys is None:
    output = {}
  else:
    output = {a: 0 for a in keys}

  for datum in data:
    if datum not in output:
      output[datum] = 1
    else:
      output[datum] += 1
    if verbose:
      for key,value in output.items():
        print(key,value)
  return output
