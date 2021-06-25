import vaex
import os
import pandas as pd
import numpy as np

def dummydata():
    df = vaex.example()
    return df

def dummydata2():
    """ for plot_type2 """
    cwd = os.getcwd()#.rstrip("slotpy")
    file = os.path.join(cwd, "examples/example_data/run_GGM_1M_CRlER_norm_st.csv")
    pdf = pd.read_csv(file, index_col="Unnamed: 0", float_precision='round_trip')
    pslider_cols = np.array([c for c in pdf.columns if 'R_' in c])
    return pdf, pslider_cols

class DataFrame():
    '''Reads the data'''
    def __init__(self,path):
        # check if path is valid
        if os.path.isfile(path):
            self.path = path
        else:
            self.path = 'None.'
            self.msg = 'Please enter a valid path!'

    def to_csv(self):
        # turn input into csv
        if self.path.endswith('.csv'):
            new_path = self.path
        else:
            os.system("tr -s '[:blank:]' ',' < " + self.path + " > " + self.path + ".csv")
            new_path = self.path + '.csv'
        return new_path

    def read_data(self, path_to_csv):
        '''
        We can add some functionality here
        '''
        print('Success!\n')
        print('I read in the following file:\n')
        print(path_to_csv)
        print('\n')
        if not path_to_csv.endswith('.csv'):
            df.to_csv()
            path_to_csv=df.path
            col_num = os.popen("awk -F, '{print NF; exit}' " + path_to_csv).read()
            column_header = ['col' + str(i) for i in np.arange(int(col_num))]
            print('This is not a .csv file.\n')
            print('I automatically assigned a number to each column starting from 0.')
            slider_cols = column_header
            self.df = vaex.open(path_to_csv)
# Test
            pdf = pd.read_csv(path_to_csv, index_col="Unnamed: 0", float_precision='round_trip')
            pslider_cols = np.array([c for c in pdf.columns if 'R_' in c])
        else:
            self.df = vaex.open(path_to_csv)
            slider_cols = np.array([c for c in self.df.columns if 'R_' in c])
            print('This is a .csv file.\n')
# Test
            pdf = pd.read_csv(path_to_csv, index_col="Unnamed: 0", float_precision='round_trip')
            pslider_cols = np.array([c for c in pdf.columns if 'R_' in c])

            print('The columns are: ', slider_cols)

# Test
        return pdf, pslider_cols
        # return self.df, slider_cols
