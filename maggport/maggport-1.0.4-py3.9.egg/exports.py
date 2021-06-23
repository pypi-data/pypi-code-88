import json
import pandas

def export_csv(docs_list: list, out: str, header: bool) -> None:  # type: ignore
    """
    Export file to csv

    Args:
        docs (list): Queried docs from mongodb
        out (str): Output file
    """
    # create empty DataFrame to store docs
    df_doc = pandas.DataFrame(columns=[])

    # prepare result to be exported
    for doc in docs_list:
        series_obj = pandas.Series(doc)
        df_doc = df_doc.append(series_obj, ignore_index=True)

    df_doc.to_csv(out, sep=',', index=False, header=header)


def export_json(**kwargs) -> None:  # type: ignore
    """
    Export file to json

    Args:
        docs (list): Queried docs from mongodb
        out (str): Output file
    """
    with open(kwargs['out'], 'w') as outfile:
        json.dump(kwargs['docs_list'], outfile, indent=2)


def export_txt(docs_list: list, out: str, header: bool) -> None:  # type: ignore
    """
    Export file to txt

    Args:
        docs (list): Queried docs from mongodb
        out (str): Output file
    """
    # create empty DataFrame to store docs
    df_doc = pandas.DataFrame(columns=[])

    # prepare result to be exported
    for doc in docs_list:
        series_obj = pandas.Series(doc)
        df_doc = df_doc.append(series_obj, ignore_index=True)

    df_doc.to_csv(out, index=False, header=header)
