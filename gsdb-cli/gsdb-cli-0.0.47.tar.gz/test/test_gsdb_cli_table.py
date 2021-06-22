# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import requests_mock
from click.testing import CliRunner

from geospock_cli.geospockcli import geospock_cli

dummy_endpoint = 'http://local:8080'


def test_get_table_list():
    dummy_tables = ["table1", "table2"]
    mock_response_code = 200
    mock_response_text = json.dumps(dummy_tables)
    with requests_mock.Mocker() as m:
        m.register_uri('GET', dummy_endpoint + '/schemas/dummySchema/tables', text=mock_response_text,
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "list", "--schema", "dummySchema"])
        assert result.exit_code == 0
        assert json.loads(result.output) == dummy_tables


def test_insert_into_table():
    mock_response_code = 202
    expected_result = '{\n  "response": "Accepted"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('POST', dummy_endpoint + '/schemas/dummySchema/tables/dummyTable', text="",
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "insert", "--schema", "dummySchema", "--table", "dummyTable", "--instance-count", "3",
                                "--data-url", "s3://something"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_drop_table():
    mock_response_code = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/schemas/dummySchema/tables/dummyTable', text="",
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "table",
                                "drop", "--schema", "dummySchema", "--table", "dummyTable"])
        assert result.exit_code == 0
        assert result.output == expected_result
