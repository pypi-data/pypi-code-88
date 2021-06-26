'''
around June 9th
'''
import matplotlib.pyplot as plt
from name_parser import getName
from dateutil.parser import parse as parseDate
import json,os,logging,random,csv
from nickname.Name import Name
from datetime import datetime,timedelta
from geopy import distance
from officer_utilities import *
import statistics
dallas = (32.779167, -96.808891)
age_offset = []
best_results = []
number_of_addresses = []

def defaultconverter(o):
  if isinstance(o, datetime):
      return o.__str__()


def end():
  average = statistics.mean(number_of_addresses)
  plt.hist(number_of_addresses,123)
  plt.yscale('log')
  plt.title(f"Distribution of Addresses Per Result; count({sum(number_of_addresses)}) mean({average})")
  plt.xlabel("Number of Addresses (#)")
  plt.ylabel("Log-Frequency log(#)")
  plt.show()
  json.dump(best_results, open('best_officer.json','w+'),indent=2, default=defaultconverter)
  print("Written")
  #plt.hist(age_offset)
  #plt.show()
  pass


def eachOfficerBefore(officer,name):
    start,end,duration,years = getEmploymentTime(officer)
    officer['start_date'] = start
    
            
def eachOfficerAfter(officer,name):
  if 'details' in officer:
    results = officer['details']
  else:
    results = officer['results']
  result = results[0]
  name_score = result['name_score']
  age_difference = result['abs_year_difference']
  if len(results)==1 and name_score == 1 and age_difference < 3:
    best_results.append(officer)
    #print(officer['first'],officer['middle'],officer['last'])
    del officer['details']
    officer['result'] = result


def eachResultBefore(result,officer,name):
    year_difference = result['year_difference']
    age_offset.append(year_difference)

def eachResultAfter(result,officer,name):
  generate_spells(result,officer,name,display=False)
  number_of_addresses.append(len(result['addresses']))

def eachAddress(address,result,officer,name):
  parse_address_dates(address,officer,name)

def remove_duplicates(result,officer,name,distance_tolerance=1):
  addresses = sorted(result['addresses'],key=lambda a: (a['start'],a['end']))
  result['addresses'] = []
  for addr in addresses:
    existing = False
    for address in result['addresses']:
      same_start = addr['start'] == address['start']
      same_end   = addr['end'] == address['end']
      same_distance = abs(addr['dallas_distance'] - address['dallas_distance']) < distance_tolerance
      if same_start and same_end and same_distance:
        existing = True
        break
    if not existing:
      result['addresses'].append(addr)
  removed = len(addresses)-len(result['addresses'])
  if removed > 0:
    #print(name,"removed",removed)
    pass
  return removed

def remove_zero_duration(result,officer,name,distance_tolerance=1):
  pass


# Generating Spells for People
# 
# 
# 
def generate_spells(result,officer,name,display=False,check=False):
    if check and 'spells_generated' in result: return
    remove_duplicates(result,officer,name)
    
    #Sort by start date
    result['addresses'] = sorted(result['addresses'],key=lambda a: a['start'])
    
    #Find one-dates; set their end date to nearest start date
    for i,address in enumerate(result['addresses']):
        if 'only_date' not in address: continue
        if i+1 == len(result['addresses']): continue #Not enough results to patch
        address['end'] = result['addresses'][i+1]['start']

    result['addresses'] = sorted(result['addresses'],key=lambda a: (a['end'],a['start']))
    #Find current-address; set their start date to last end date.
    for i,address in enumerate(result['addresses']):
      if 'current_date' not in address: continue
      if len(result['addresses']) == 1: continue #Not enough results to path
      #Possible error if i==0 but that only happens if
      address['start'] = result['addresses'][i-1]['end']
    intervals = result['addresses']
    #Fill in the gaps & remove duplicates
    #result['addresses'] = sorted(result['addresses'],key=lambda a: (a['start'],a['end']))

    
    result['addresses'] = sorted(result['addresses'],key=lambda a: (a['start'],a['end']))
    if display:
        print(name)
    for address in result['addresses']:
        address['time_until_employment'] = officer['start_date'] - address['start']
        #When I stopped living there, was I employed?
        if (officer['start_date'] - address['end']).total_seconds() > 0:
            address['after_employment'] = False
            address['before_employment'] = True
        else:
            address['after_employment'] = True
            address['before_employment'] = False        
        if display:
            print(f"----- From({address['start'].date()}) to({address['end'].date()}) at({address['address']}) given({address['date']})")
    if display:
        print("")
    #Formulate a unique interval using Dallas and non-dallas as the only important characteristic to define uniqueness.
    result['spells_generated'] = True
    
def parse_address_dates(address,officer,name):
  address['date'] = address['date'].replace('(','').replace(')','')
  if address['date'] == 'current':
    # Current Date
    # Set end date to now
    # Set start date to birthday
    address['start'] = datetime.now().date()
    address['end'] = datetime.now().date()
    address['current_date']=True
  elif '-' in address['date']:
    # Two Dates
    # Nothin interesting
    # Set start date and end date.
    start,end = address['date'].split('-')
    address['start'] = parseDate(start).date()
    address['end'] = parseDate(end).date()
  else:
    # One-Date
    # Set start date to date
    # Set end date to now
    address['start'] = parseDate(address['date'].strip('(').strip(')')).date()
    address['end'] = datetime.now().date()
    address['only_date']=True

    
    
if __name__=="__main__":
    police = json.load(open('database.json'))
    for officer in police:
        name = Name(officer['first'],officer['middle'],officer['last'])
        eachOfficerBefore(officer,name)
        results = officer['details']
        for result in results:
            eachResultBefore(result,officer,name)
            for address in result['addresses']:
                eachAddress(address,result,officer,name)
            eachResultAfter(result,officer,name)
        eachOfficerAfter(officer,name)
    end()
