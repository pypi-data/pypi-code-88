import json
from pathlib import Path

from starlette.responses import Response
from pymultirole_plugins.v1.schema import Document

from pyformatters_tabular.tabular import TabularFormatter, TabularParameters, OutputFormat


def test_xlsx():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/response_1621334812115.json')
    with source.open("r") as fin:
        docs = json.load(fin)
        doc = Document(**docs[0])
        formatter = TabularFormatter()
        options = TabularParameters(format=OutputFormat.xlsx)
        resp: Response = formatter.format(doc, options)
        assert resp.status_code == 200
        assert resp.media_type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        result = Path(testdir, 'data/response_1621334812115.xlsx')
        with result.open("wb") as fout:
            fout.write(resp.body)


def test_csv():
    testdir = Path(__file__).parent
    source = Path(testdir, 'data/response_1621334812115.json')
    with source.open("r") as fin:
        docs = json.load(fin)
        doc = Document(**docs[0])
        formatter = TabularFormatter()
        options = TabularParameters(format=OutputFormat.csv)
        resp: Response = formatter.format(doc, options)
        assert resp.status_code == 200
        assert resp.media_type == "text/csv"
        result = Path(testdir, 'data/response_1621334812115.csv')
        with result.open("wb") as fout:
            fout.write(resp.body)
