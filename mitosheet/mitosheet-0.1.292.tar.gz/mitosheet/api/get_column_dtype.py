

def get_column_dtype(event, wsc):
    """
    Sends back the dtype of the column
    """
    sheet_index = event['sheet_index']
    column_header = event['column_header']

    series = wsc.dfs[sheet_index][column_header]

    return str(series.dtype)