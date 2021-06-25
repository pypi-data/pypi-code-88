def get_dataframe_as_csv(event, wsc):
    """
    Sends a dataframe as a CSV string
    """
    sheet_index = event['sheet_index']
    df = wsc.dfs[sheet_index]

    return df.to_csv(index=False)