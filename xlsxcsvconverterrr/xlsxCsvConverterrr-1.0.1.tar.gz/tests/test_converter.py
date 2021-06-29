from unittest import TestCase, main
from os import getcwd, remove
from os.path import join
from converter.converter import csv_to_xlsx, xlsx_to_csv
import pandas as pd


class ConverterTest(TestCase):

    test_folder = join(getcwd(), 'tests', 'test_files')

    def test_xlsx_to_csv_v1(self):
        output = join(self.test_folder, 'output', 'out_test1.csv')
        input = join(self.test_folder, 'test1.xlsx')

        res = join(self.test_folder, 'out_test1.csv')

        xlsx_to_csv(input, res)

        with open(output) as output_file, open(res) as result:
            self.assertEqual(output_file.read(), result.read())

        remove(res)

    def test_csv_to_xlsx_v1(self):
        output = join(self.test_folder, 'output', 'out_test2.xlsx')
        input = join(self.test_folder, 'test2.csv')

        res = join(self.test_folder, 'out_test2.xlsx')

        csv_to_xlsx(input, res)
        

        self.assertTrue(pd.read_excel(res).equals(pd.read_excel(output)))

        remove(res)

    def test_csv_to_xlsx_v2(self):
        output = join(self.test_folder, 'output', 'out_test3.xlsx')
        input = join(self.test_folder, 'test3.csv')

        res = join(self.test_folder, 'out_test3.xlsx')

        csv_to_xlsx(input, res)

        self.assertTrue(pd.read_excel(res).equals(pd.read_excel(output)))

        remove(res)


if __name__ == '__main__':
    main()