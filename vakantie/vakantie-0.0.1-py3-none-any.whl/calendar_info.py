from .calendar_extractor import ExtractCalendar
import pandas as pd

class Holidays:
    def __init__(self, year="2021", country="bangladesh"):
        self.calender_extractor = ExtractCalendar(year=year, country=country)

    def get_holidays(self, data_type="holiday_api"):
        columns, holiday_data = self.calender_extractor.extract_calendar()
        if data_type == "json":
            holidays = self._format_json(columns, holiday_data)
        elif data_type == "holiday_api":
            holidays = self._format_holiday_api(holiday_data)
        elif data_type == "csv":
            holidays = self._format_dataframe(columns, holiday_data)
        return holidays

    def _format_json(self, columns, data):
        holidays = {}
        transposed_data = list(zip(*data))
        for i in range(len(columns)):
            holidays[columns[i]] = transposed_data[i]
        return holidays

    def _format_holiday_api(self, data):
        holidays = {}
        for holiday in data:
            holidays[holiday[1]] = holiday[2]
        return holidays

    def _format_dataframe(self, columns, data):
        return pd.DataFrame(data=data, columns=columns)