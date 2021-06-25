from google.oauth2 import service_account
from googleapiclient.discovery import build

class Client:
  def __init__(self, spreadsheet_id, path_to_credentials) -> None:
    self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    self.SHEET_ID = spreadsheet_id
    self.CREDS_PATH = path_to_credentials

    creds = None
    creds = service_account.Credentials.from_service_account_file(
      self.CREDS_PATH, scopes=self.SCOPES
    )

    self.SERVICE = build('sheets', 'v4', credentials=creds)
    self.SHEET = self.SERVICE.spreadsheets()

    # self.load_db_config()

    self.default_table_range = 'A:ZZZ'

  ### Work in progress ###

  # def load_db_config(self):
  #   template = {"tables": []}
  #   if not os.path.exists('db'):
  #     os.makedirs('db')
  #     json.dump(template, open('./db/dbconfig.json'))
  #     self.DB_CONFIG = json.load(open('./db/dbconfig.json'))
  #   
  #   elif not os.path.isfile('./db/dbconfig.json'):
  #     json.dump(template, open('./db/dbconfig.json', 'w'))
  #   
  #   else: self.DB_CONFIG = json.load(open('./db/dbconfig.json'))


  def get(self, table_name):
    response = self.SHEET.values().get(
      spreadsheetId=self.SHEET_ID, 
      range=f'{table_name}!{self.default_table_range}'
      ).execute()
    return response.get('values', None)
  
  def insert(self, table_name, values, valueInputOption = "USER_ENTERED"):
    existing = self.get(table_name)
    cardinality = len(existing) if existing else 0
    response = self.SHEET.values().update(
      spreadsheetId=self.SHEET_ID, 
      range=f'{table_name}!A{cardinality + 1}',
      valueInputOption=valueInputOption,
      body={"values":values} if type(values[0]) == list else {"values":[values]}
      ).execute()
    return response

  def overwrite(self, table_name, data, valueInputOption = "USER_ENTERED"):
    oresponse = self.SHEET.values().clear(
      spreadsheetId=self.SHEET_ID, 
      range=f'{table_name}!A1:ZZZ',
      ).execute()
    iresponse = self.insert(table_name, data, valueInputOption)
    return (oresponse, iresponse)

  def set(self, table_name, field_to_set, value_to_set, where_statement):
    data = self.get(table_name)
    fields = data.pop(0)
    modified_data = []
    for record in data: modified_data.append({fields[index]: item for index, item in enumerate(record)})
    for record in modified_data:
      if eval(where_statement): 
        record[field_to_set] = value_to_set
    payload = [fields]
    for record in modified_data: payload.append([x for x in record.values()])
    return self.overwrite(table_name, payload)

  def delete_rows(self, table_name, where_statement):
    data = self.get(table_name)
    fields = data.pop(0)
    modified_data = []
    for record in data: modified_data.append({fields[index]: item for index, item in enumerate(record)})
    for record in modified_data:
      if eval(where_statement): 
        modified_data.remove(record)
    payload = [fields]
    for record in modified_data: payload.append([x for x in record.values()])
    return self.overwrite(table_name, payload)
