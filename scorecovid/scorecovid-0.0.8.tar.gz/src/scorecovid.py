import requests,re
import pandas as pd

def main():
 url='https://www.worldometers.info/world-population/population-by-country/'
 print('scraping population...')
 page=requests.get(url)
 df = pd.read_html(page.text)[0]
 df.columns.values[1]='Country'
 df.columns.values[2]='Population'
 #df = pd.read_html(page.text,flavor='html5lib')[0]
 df.to_csv('pop.csv')
 print('pop.csv was created')

 print('downloading total_deaths.csv file')
 import subprocess as sp
 sp.call("wget https://github.com/owid/covid-19-data/raw/master/public/data/jhu/total_deaths.csv",shell=True)
 p=pd.read_csv('total_deaths.csv')
 date=p['date'][len(p)-1]

#
#from urllib.request import Request, urlopen
#url='https://www.worldometers.info/coronavirus/#nav-today/'
#print('scraping deaths informationi...')
#req = Request(url, headers={'User-Agent': 'Firefox/76.0.1'})
#page = re.sub(r'<.*?>', lambda g: g.group(0).upper(), urlopen(req).read().decode('utf-8') )
#df = pd.read_html(page)[0]
#df.to_csv('deaths.csv')
#print('deaths.csv was created')
#

 import os.path
 if os.path.exists('countries'):
  print('countries file was read...')
  d=open('countries').read().strip()
  d=d.split(',')
 else:
  sp.call("wget https://github.com/ytakefuji/score-covid-19-policy/raw/main/countries",shell=True)
  print('countries file was read...')
  d=open('countries').read().strip()
  d=d.split(',')
 print('scoring the following ',len(d),' countries...')
 print(d)

 dd=pd.DataFrame(
  { 
   "country": d,
   "deaths": range(len(d)),
   "population": range(len(d)),
   "score": range(len(d)),
  })
 
 pp=pd.read_csv('pop.csv')
 print('calculating scores of countries\n')
 print('score is created in result.csv')
 print('date is ',date)
 
 for i in d:
 # print(p[i][len(p)-1])
  dd.loc[dd.country==i,'deaths']=int(p[i][len(p)-1])
 # print(pp.loc[pp.Country==i,'Population'])
  dd.loc[dd.country==i,'population']=round(float(pp.loc[pp.Country==i,'Population']/1000000),2)
  dd.loc[dd.country==i,'score']=round(dd.loc[dd.country==i,'deaths']/dd.loc[dd.country==i,'population'],1)
 dd=dd.sort_values(by=['score'])
 dd.to_csv('result.csv',index=False)
 dd=pd.read_csv('result.csv',index_col=0)
 print(dd)
 sp.call("rm total_deaths.csv pop.csv",shell=True)

if __name__ == "__main__":
 main()
