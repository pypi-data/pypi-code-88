import pandas as pd

def create_dimension(dataframe, column_name):
    """
    [summary]

    Args:
        dataframe (dataframe): [description]
        column_name (string): [description]

    Returns:
        dataframe: [description]
    """    
    
    dimension = dataframe[column_name]
    dimension = pd.DataFrame(dimension.unique()).reset_index()
    dimension.columns = ['id'+column_name, column_name]
    return dimension

def modelate_database(dataframe,columns):
    ret = dict()
    
    ## create the dimensions
    for i in columns:
        dim_temp = create_dimension(dataframe,i)
        ret[i] = dim_temp
        dataframe = dataframe.merge(dim_temp,on=i,how='left')
    
    ## add fact to return
    ret['fact'] = dataframe.drop(columns,axis=1)
    return ret

