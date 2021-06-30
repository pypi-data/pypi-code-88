from pyapacheatlas.readers import ExcelConfiguration,ExcelReader
import json
import os

def __get_configuration():
    with open('configs.json') as json_file:
        return json.load(json_file)

def make_excel_template(excel_file):
    if not os.path.exists(excel_file):
        ExcelReader.make_template(excel_file)

def parse_excel_file_to_entities():
    configs = __get_configuration()
    excel_file = configs["Purview-Excel-file"]
    
    # setup
    excel_config = ExcelConfiguration()
    excel_reader = ExcelReader(excel_config)

    # Create an empty excel template to be populated
    make_excel_template(excel_file)
    # This is just a helper to fill in some demo data
    # fill_in_workbook(file_path, excel_config)

    # Parses the excel file and creates a batch to upload
    entities = excel_reader.parse_bulk_entities(excel_file)

    # This is what is getting sent to your Atlas server
    # print(json.dumps(entities,indent=2))
    return entities
    

if __name__ == "__main__":
    pass