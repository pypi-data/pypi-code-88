from googlewrapper.connect import Connection
from pandas import DataFrame


class GoogleSheets:
    """
    Uses the pygsheets library
    https://pygsheets.readthedocs.io/en/stable/index.html
    """
    def __init__(self,url, auth = Connection().pygsheets()):
        self.url = url
        self.id = self.__get_id()
        self.auth = auth
        self.wb = self.auth.open_by_url(self.url)
        self.sheet = self.wb.sheet1

    def __get_id(self):
        return self.url.split('d/')[1].split('/edit')[0]

    def set_sheet(self,sheet_name):
        self.sheet = self.wb.worksheet('title',sheet_name)

    # Spreadsheet/Tab Methods
    def df(self,start = 'a1',index=1):
        # https://pygsheets.readthedocs.io/en/stable/worksheet.html#pygsheets.Worksheet.get_as_df
        try:
            return self.sheet.get_as_df(start=start,index_column=index)
        except AttributeError:
            raise AttributeError('Please declare your sheet name using .set_sheet(name)')

    def save(self,df,start = 'a1',index=True,header=True,extend=True):
        if isinstance(df,DataFrame):
            self.sheet.set_dataframe(df,start,copy_index=index,copy_head=header,extend=extend)
        else:
            raise TypeError("Please pass in a pd.DataFrame to save to Google Sheets")

    def clear(self,start,end):
        self.sheet.clear(start,end)

    def row(self,row_number):
        return self.sheet.get_row(row_number,include_tailing_empty=False)

    def col(self,col_number):
        return self.sheet.get_col(col_number,include_tailing_empty=False)
        
    # Entire Workbook Methods
    def add_sheet(self,sheet,data = None):
        self.wb.add_worksheet(sheet)
        self.set_sheet(sheet)
        if data is not None:
            self.save(data)

    def delete_sheet(self,sheet):
        self.wb.del_worksheet(sheet)

    def share(self,email_list,role = 'reader'):
        for email in email_list:
            self.wb.share(email,role,'user')

