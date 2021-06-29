from bs4 import BeautifulSoup
import requests
import json
import re
import calendar
from datetime import date

class ExtractCalendar:
    def __init__(self, year, country):
        self.url = f"https://www.officeholidays.com/countries/{country}/{year}"
        self.months = {month: index for index, month in enumerate(calendar.month_abbr) if month}

    def extract_calendar(self):
        html_content = requests.get(self.url).text

        # Parse HTML code for the entire site
        soup = BeautifulSoup(html_content, "lxml")
        gdp = soup.find_all("table", attrs={"class": "country-table"})
        for table in gdp:
            body = table.find_all("tr")
            head = body[0]
            web_data = body[1:]
            columns = []
            for item in head.find_all("th"):  # loop through all th elements
                # convert the th elements to text and strip "\n"
                item = (item.text).rstrip("\n")
                # append the clean column name to headings
                columns.append(item)
            # holiday_info = {}  # will be a list for list for all rows
            # holidate = None
            holiday_info = []
            for row_num in range(len(web_data)):  # A row at a time
                row = []  # this will old entries for one row
                i = 0
                for row_item in web_data[row_num].find_all("td"):  # loop through all row entries
                    # row_item.text removes the tags from the entries
                    # the following regex is to remove \xa0 and \n and comma from row_item.text
                    # xa0 encodes the flag, \n is the newline and comma separates thousands in numbers
                    aa = re.sub("(\xa0)|(\n)|,", "", row_item.text)

                    # print(row)
                    if i == 1:
                        date_info = aa.split(" ")
                        aa = date(year=2021, month=self.months[date_info[0]], day=int(date_info[1]))
                    #
                    # # append aa to row - note one row entry is being appended
                    # else:
                    row.append(aa)
                    i += 1
                # append one row to all_rows
                holiday_info.append(row)
                # holiday_info[holidate.isoformat()] = row
        return columns, holiday_info
        with open('banglades-2021.json', 'w') as outfile:
            json.dump(holiday_info, outfile)