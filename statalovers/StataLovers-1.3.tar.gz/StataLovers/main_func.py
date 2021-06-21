import pandas as pd

def summarize(vars, df):
    '''
    this function prints out descriptive statistics in the similar way that Stata function sum does.
    Args:
    pandas column of a df
    Output: None (print out)
    '''
    num = max([len(i) for i in vars])
    if num < 13:
        num = 13
    
    print("{} |        Obs        Mean    Std. Dev.       Min        Max ".format('Variable'.rjust(num)))
    print("{}-+----------------------------------------------------------".format('-'*num))
    
    for var in vars:
        temp = df[var].describe()
        print("{} |{}{}{}{}{}".format(var.rjust(num), round(temp['count'], 1).astype(str).rjust(11), \
                                     round(temp['mean'], 3).astype(str).rjust(12), \
                                     round(temp['std'], 3).astype(str).rjust(13), \
                                     round(temp['min'], 3).astype(str).rjust(11), \
                                     round(temp['max'], 3).astype(str).rjust(11) \
                                                           ))

def tab(var1, var2=None):
    '''
    This is a function that gives an output similar to the tab function in Stata.
    ARGs:
    it takes columns of a dataframe as arguments.
    '''
    
    if var2 is None:
        print("{}|      Freq.     Percent        Cum.".format(var1.name.rjust(12)))
        print("------------+-----------------------------------")
        temp = pd.DataFrame(var1.value_counts())
        temp.reset_index(inplace=True)
        temp = temp.sort_values(by="index").reset_index(drop=True)
        tots = temp[temp.columns[1]].sum()
        temp['percent']=100*(temp[temp.columns[1]]/tots)
        temp['cum_percent'] = 100*(temp[temp.columns[1]].cumsum()/tots)
        for y in range(0, len(temp)):
            print("{}|{}{}{}".format(round(temp.loc[y, temp.columns[0]], 3).astype(str).rjust(12), \
                                    round(temp.loc[y, temp.columns[1]], 3).astype(str).rjust(11), \
                                    round(temp.loc[y, 'percent'], 3).astype(str).rjust(12), \
                                    round(temp.loc[y, 'cum_percent'], 3).astype(str).rjust(12)))
        print("------------+-----------------------------------")
        print("      Total |{}      100.00".format(tots.astype(str).rjust(11)))
    else:
        assert len(var1)==len(var2), "Columns are not of the same length, check if they belong to the same dataframe"
        dict1 = {var1.name: var1, var2.name: var2}
        df1 = pd.DataFrame(dict1, columns=[var1.name, var2.name])
        number = len(var2.value_counts())
        temp1= pd.DataFrame(var1.value_counts())
        temp1.reset_index(inplace=True)
        temp1 = temp1.sort_values(by="index").reset_index(drop=True)
        temp2= pd.DataFrame(var2.value_counts())        
        temp2.reset_index(inplace=True)
        temp2 = temp2.sort_values(by="index").reset_index(drop=True)
        print("             |{}".format(var2.name.rjust(round(len(var2.value_counts())*12/2))))
        string1 = str('{} |'.format(var1.name.rjust(12)))
        for i in range(number):
            string1+='{}'.format(temp2.loc[i, 'index'].astype(str).rjust(12))
        string1+= str('|     Total')
        print(string1)
        print('-------------+------------------------+----------')
        for j in range(len(temp1)):
            string2 = str('{} |'.format(round(temp1.loc[j, 'index'], 3).astype(str).rjust(12)))
            num2 = 0
            for i in range(number):
                num1 = df1.loc[(df1[var1.name]==temp1.loc[j, 'index']) \
                                             & (df1[var2.name]==temp2.loc[i, 'index']), \
                                             var1.name].count()
                string2+='{}'.format(num1.astype(str).rjust(12))
                num2 +=num1
            string2 += '|{}'.format(num2.astype(str).rjust(10))
            print(string2)
        print('-------------+------------------------+----------')
        string3 = str('       Total |')
        for i in range(number):
            string3 +='{}'.format(temp2.loc[i, var2.name].astype(str).rjust(12))
        string3 +='|{}'.format(var2.count().astype(str).rjust(10))
        print(string3)