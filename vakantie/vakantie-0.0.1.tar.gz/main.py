# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import argparse
import yearlyholidays
parser = argparse.ArgumentParser()
parser.add_argument('--year', default='2021')
parser.add_argument('--country', default="usa")
parser.add_argument('--data_type', default="holiday_api")
args = parser.parse_args()

holidays = yearlyholidays.Holidays(year=2021, country='Bangladesh')
print(holidays.get_holidays())