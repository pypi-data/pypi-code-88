# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:45:09 2021

@author: Michael ODonnell

@purpose: scrape NBA draft picks by year
"""

# import needed libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# function to scrape a list of years of NBA Drafts
def nba_draft_data(start_year = 2017, end_year = 2020, export = True):
    # turn inputs into a list of years
    if end_year > start_year:
        years = list(range(end_year, start_year-1,-1))
        
    elif end_year < start_year:
        years = list(range(end_year, start_year+1))
        
    else:
        years = [start_year]
    
    # create empty dataframe
    final_df = pd.DataFrame(columns = ['Pk', 'Tm', 'Player', 'College', 'Yrs',
                                       'G', 'MP', 'PTS', 'TRB', 'AST','FG%',
                                       '3P%', 'FT%', 'MP', 'PTS', 'TRB', 'AST',
                                       'WS', 'WS/48', 'BPM', 'VORP', 'round',
                                       'year'])
    # scape one year at a time
    for y in years:
    
        # define URL of draft class
        url = f'https://www.basketball-reference.com/draft/NBA_{y}.html'
        
        # create bs4 object using requests and bs4
        response = requests.get(url)
        
        # if response code != 200, print and exit
        if response.status_code != 200:  
            print("invalid url response code:", response.status_code)
            break
        
        html = response.text
        soup = BeautifulSoup(response.content, features = 'lxml')
        column_names = [th.getText() for th in soup.findAll('tr', limit=2)[1].findAll('th')]
        table_rows = soup.findAll('tr')[0:]
        draft_picks = [[td.getText() for td in table_rows[i].findAll('td')]
                        for i in range(len(table_rows))]
        
        # function to find length of each draft round
        def find_draft_rounds(draft_picks:list):
            # this will store number of picks in each round
            round_cutoffs = []
            
            # find empty lists, they indicate new draft round
            for index, value in enumerate(draft_picks[2:]):
                if value == []:
                    round_cutoffs.append(index)
            
            # since there are always 2 empty lists in a row, only use 2nd
            round_cutoffs = round_cutoffs[::2]
            
            # print the total number of round in draft class
            print(f"total rounds of the {y} draft:", len(round_cutoffs)+1)
            print(f"picks per round in {y} draft:", round_cutoffs[0])
            
            return round_cutoffs
        
        
        # call find_draft_rounds on the data
        round_cutoffs = find_draft_rounds(draft_picks)
        
        # remove empty rows from draft_picks
        draft_picks = [e for e in draft_picks if len(e) > 10]
        
        # create dataframe for all draft_picks
        draft_picks_df = pd.DataFrame(draft_picks, columns = column_names[1:])
        print(f"total draft picks in the {y} draft:", len(draft_picks_df["Pk"]))
        
        # create column for draft round and draft year
        draft_picks_df["round"] = 1
        draft_picks_df["year"] = y
        
        # change column Pk to integer
        draft_picks_df["Pk"] = pd.to_numeric(draft_picks_df["Pk"])
        
        # assign correct draft round to each row
        for index, picks in enumerate(round_cutoffs):
            draft_picks_df.loc[(draft_picks_df.Pk > picks), "round"] = int(index)+2
        
        # add draft picks to final_df (with all draft picks)
        try:
            final_df = final_df.append(draft_picks_df)
            print(f"draft year {y} added to final dataframe")
            
        except:
            print(f"error with draft year {y}, data not collected")
        
        # sleep for short duration before moving onto next year
        print('='*5, f"end of year {y}", '='*5)
        time.sleep(2)
        
    # rename final_df columns
    final_df = final_df.rename(columns = {final_df.columns[0]: "Pick",
                                          final_df.columns[1]: "Team",
                                          final_df.columns[4]: "Years",
                                          final_df.columns[5]: "Career_Games",
                                          final_df.columns[8]: "Career_Rb",
                                          final_df.columns[9]: "Career_Ast",
                                          final_df.columns[13]: "MPG",
                                          final_df.columns[14]: "PPG",
                                          final_df.columns[15]: "RbsPG",
                                          final_df.columns[16]: "AstPG",
                                          final_df.columns[7]: "Career_Pts",
                                          final_df.columns[6]: "Career_Minutes"})
    # export and return the dataframe
    if export == True:
        export_name = f"nba_draft_data_{start_year}_to_{end_year}" + ".csv"
        final_df.to_csv(export_name, index = False)
        
    return final_df