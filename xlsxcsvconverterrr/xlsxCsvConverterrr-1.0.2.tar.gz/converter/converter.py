import pandas as pd


def xlsx_to_csv(input_file: str, output_file: str):
        data_xls = pd.read_excel(input_file)
        data_xls.to_csv(output_file, encoding='utf-8', index=False)

        return True


def csv_to_xlsx(input_file: str, output_file: str):

        read_file = pd.read_csv(input_file)
        read_file.to_excel(output_file, index=None, header=True)

        return True