# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 16:47:30 2021

@author: ODsLaptop
"""

# import needed libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# this function will scrape team performance by year for multiple years
def nba_team_data(start_year = 2017, end_year = 2020, export = True):
    # turn inputs into a list of years
    if end_year > start_year:
        years = list(range(end_year, start_year-1,-1))
        
    elif end_year < start_year:
        years = list(range(end_year, start_year+1))
        
    else:
        years = [start_year]
    
    # first, create empty dataframe with needed column headers
    final_df = pd.DataFrame(columns = ["Year", "Team", "W", "L",
                                       "W/L%", "GB", "PS/G", "PA/G",
                                       "SRS", "Playoffs",
                                       "Losing_season"])
    
    # loop through each year, scraping team performance that year
    for y in years:
        
        # URL to scrape
        url = f'https://www.basketball-reference.com/leagues/NBA_{y}_standings.html'
        
        # HTML data collected
        response = requests.get(url)
        
        # if response code != 200, print and exit
        if response.status_code != 200:  
            print("invalid url response code:", response.status_code)
            break
        
        # create beautiful soup object from HTML
        soup = BeautifulSoup(response.content, features="lxml")
        
        # use getText()to extract the headers into a list
        titles = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
        
        # first, find only column headers
        headers = titles[1:titles.index("SRS")+1]
        
        # then, update the titles list to exclude first set of column headers
        titles = titles[titles.index("SRS")+1:]
        
        # then, grab all row titles (ex: Boston Celtics, Toronto Raptors, etc)
        try:
            row_titles = titles[0:titles.index("Eastern Conference")]
        except:
            row_titles = titles
        # remove the non-teams from this list
        for i in headers:
            row_titles.remove(i)
        row_titles.remove("Western Conference")
        divisions = ["Atlantic Division", "Central Division",
                     "Southeast Division", "Northwest Division",
                     "Pacific Division", "Southwest Division",
                     "Midwest Division"]
        for d in divisions:
            try:
                row_titles.remove(d)
            except:
                pass
        
        # next, grab all data from rows (avoid first row)
        rows = soup.findAll('tr')[1:]
        team_stats = [[td.getText() for td in rows[i].findAll('td')]
                    for i in range(len(rows))]
        # remove empty elements
        team_stats = [e for e in team_stats if e != []]
        # only keep needed rows
        team_stats = team_stats[0:len(row_titles)]
        
        # add team name to each row in team_stats
        for i in range(0, len(team_stats)):
            team_stats[i].insert(0, row_titles[i])
            team_stats[i].insert(0, y)
            
        # add team, year columns to headers
        headers.insert(0, "Team")
        headers.insert(0, "Year")
        
        # create a dataframe with all aquired info
        year_standings = pd.DataFrame(team_stats, columns = headers)
        
        # add a column to dataframe to indicate playoff appearance
        year_standings["Playoffs"] = ["Y" if "*" in ele else "N" for ele in year_standings["Team"]]
        # remove * from team names
        year_standings["Team"] = [ele.replace('*', '') for ele in year_standings["Team"]]
        # add a column to dataframe to indicate a losing season (win % < .5)
        year_standings["Losing_season"] = ["Y" if float(ele) < .5 else "N" for ele in year_standings["W/L%"]]
        
        # append new dataframe to final_df
        final_df = final_df.append(year_standings)
        
        # sleep for short duration before moving onto next year
        teams_per_year = len(year_standings["Team"])
        print(f"scraped {teams_per_year} teams for {y} season")
        print('='*5, f"end of year {y}", '='*5)
        time.sleep(2)
        
    # print final_df
    print("===== complete =====")
    
    # export and return dataframe
    if export == True:
        export_name = f"nba_team_data_{start_year}_to_{end_year}" + ".csv"
        final_df.to_csv(export_name, index = False)
        
    return final_df

# test on 2015 and 2016 because 2015 is old format and 2016 is new format
# nba_team_data(start_year = 2014, end_year = 2017)