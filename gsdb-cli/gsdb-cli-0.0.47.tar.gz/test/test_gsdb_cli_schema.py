# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import requests_mock
from click.testing import CliRunner

from geospock_cli.geospockcli import geospock_cli

dummy_endpoint = 'http://local:8080'


def test_get_schema_list():
    dummy_schemas = ["schema1", "schema2"]
    mock_response_code = 200
    mock_response_text = json.dumps(dummy_schemas)
    with requests_mock.Mocker() as m:
        m.register_uri('GET', dummy_endpoint + '/schemas', text=mock_response_text, status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "schema",
                                "list"])
        assert result.exit_code == 0
        assert json.loads(result.output) == dummy_schemas


def test_create_schema():
    mock_response_code = 201
    expected_result = '{\n  "response": "Created"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('PUT', dummy_endpoint + '/schemas/dummySchema', text="", status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "schema",
                                "create", "--schema", "dummySchema"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_drop_schema():
    mock_response_code = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/schemas/dummySchema', text="", status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "schema",
                                "drop", "--schema", "dummySchema"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_create_schema_with_invalid_name():
    mock_response_code = 400
    mock_response_text = 'Invalid schema name'
    with requests_mock.Mocker() as m:
        m.register_uri('PUT', dummy_endpoint + '/schemas/dummySchema', text=mock_response_text,
                       status_code=mock_response_code)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "schema",
                                "create", "--schema", "dummySchema"])
        assert result.exit_code == 1
        assert "Bad Request - " + mock_response_text in str(result.exception)
