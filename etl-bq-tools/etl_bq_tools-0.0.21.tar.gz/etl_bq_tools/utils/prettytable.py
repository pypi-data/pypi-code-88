from prettytable import PrettyTable


def format_for_print(df):
    """This method is for convert a dataframe to pretty table

       :param df: Dataframe
       :return: pretty table
       """

    table = PrettyTable(list(df.columns))
    for row in df.itertuples():
        table.add_row(row[1:])
    return str(table)
