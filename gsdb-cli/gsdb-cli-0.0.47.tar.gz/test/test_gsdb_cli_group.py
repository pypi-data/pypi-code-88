# Copyright (c) 2014-2020 GeoSpock Ltd.

import json
import requests_mock
from click.testing import CliRunner

from geospock_cli.geospockcli import geospock_cli

dummy_endpoint = 'http://local:8080'


def test_get_group_list():
    dummy_groups = ["group1", "group2"]
    mock_response = json.dumps(dummy_groups)
    with requests_mock.Mocker() as m:
        m.register_uri('GET', dummy_endpoint + '/groups', text=mock_response)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "group",
                                "list"])
        assert result.exit_code == 0
        assert json.loads(result.output) == dummy_groups


def test_create_group():
    mock_response = 201
    expected_result = '{\n  "response": "Created"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('PUT', dummy_endpoint + '/groups/dummyGroup', status_code=mock_response)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "group",
                                "create", "--group", "dummyGroup"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_delete_group():
    mock_response = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/groups/dummyGroup', status_code=mock_response)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "group",
                                "delete", "--group", "dummyGroup"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_group_add_user():
    mock_response = 201
    expected_result = '{\n  "response": "Created"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('PUT', dummy_endpoint + '/groups/dummyGroup/users/dummyUser', status_code=mock_response)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "group",
                                "add-user", "--group", "dummyGroup", "--user", "dummyUser"])
        assert result.exit_code == 0
        assert result.output == expected_result


def test_group_remove_user():
    mock_response = 204
    expected_result = '{\n  "response": "No Content"\n}\n'
    with requests_mock.Mocker() as m:
        m.register_uri('DELETE', dummy_endpoint + '/groups/dummyGroup/users/dummyUser', status_code=mock_response)
        runner = CliRunner()
        result = runner.invoke(geospock_cli,
                               ["--endpoint", dummy_endpoint, "--user", "dummy", "--password", "dummy", "group",
                                "remove-user", "--group", "dummyGroup", "--user", "dummyUser"])
        assert result.exit_code == 0
        assert result.output == expected_result
