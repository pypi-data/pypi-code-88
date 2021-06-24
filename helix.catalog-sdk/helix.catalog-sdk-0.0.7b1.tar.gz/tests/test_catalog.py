import json
from types import SimpleNamespace
from typing import Tuple, List
from unittest.mock import patch, MagicMock

from helix_catalog_sdk.catalog import Catalog
from helix_catalog_sdk.data_source import DataSource
from helix_catalog_sdk.enums import HelixEnvironment


def get_contents_as_string(self: object, data_source: str) -> Tuple[str, str]:
    return (
        """
    {
  "base_connection": "s3://bwell-ingestion/raw/medstar/mp3/",
  "production": "",
  "staging":  "",
  "qa": "",
  "dev": "",
  "connection_type": "file",
  "resources": [
    {
      "name": "insurance",
      "path_slug": "Insurance_MP3/bwellInsuranceFeed_",
      "path": "Insurance_MP3/bwellInsuranceFeed_05062021.json"
    },
    {
      "name": "practices",
      "path_slug": "Practices_MP3/bwellPracticeFeed_",
      "path": "Practices_MP3/bwellPracticeFeed_05062021.json"
    },
    {
      "name": "providers",
      "path_slug": "Providers_MP3/bwellProviderFeed_",
      "path": "Providers_MP3/bwellProviderFeed_05062021.json"
    }
  ],
  "pipeline_subscriptions": [
    {
      "flow_name": "Medstar Data Ingestion",
      "flow_parameters": [
         "practices",
         "providers"
      ]
    },
    {
        "flow_name": "Test Flow"
    }
  ]

}
    """,
        "sha",
    )


def get_all_data_sources(self: object) -> List[Tuple[DataSource, str]]:
    data_source: str = "catalog/raw/medstar/mp3.json"
    decoded_contents, sha = get_contents_as_string(None, data_source)
    contents: SimpleNamespace = json.loads(
        decoded_contents, object_hook=lambda d: SimpleNamespace(**d)
    )
    return [(DataSource(data_source, contents, HelixEnvironment.PRODUCTION), sha)]


@patch.object(Catalog, "get_repo")
@patch.object(Catalog, "get_contents_as_string", new=get_contents_as_string)
@patch.object(Catalog, "get_all_data_sources", new=get_all_data_sources)
def test_catalog_get_data_source(mock_get_repo: MagicMock) -> None:
    repo = "icanbwell/helix.orchestration"
    catalog = Catalog(repo=repo, access_token="fake_token")
    data_source, sha = catalog.get_data_source(
        "catalog/raw/medstar/mp3.json", HelixEnvironment.PRODUCTION
    )

    mock_get_repo.assert_called_with(repo)

    assert data_source.base_connection == "s3://bwell-ingestion/raw/medstar/mp3/"
    assert len(data_source.resources) == 3

    insurance_resource = data_source.resources[0]
    assert insurance_resource.name == "insurance"
    assert (
        insurance_resource.full_path
        == "s3://bwell-ingestion/raw/medstar/mp3/Insurance_MP3/bwellInsuranceFeed_05062021.json"
    )

    practices_resource = data_source.resources[1]
    assert practices_resource.name == "practices"
    assert (
        practices_resource.full_path
        == "s3://bwell-ingestion/raw/medstar/mp3/Practices_MP3/bwellPracticeFeed_05062021.json"
    )

    providers_resource = data_source.resources[2]
    assert providers_resource.name == "providers"
    assert (
        providers_resource.full_path
        == "s3://bwell-ingestion/raw/medstar/mp3/Providers_MP3/bwellProviderFeed_05062021.json"
    )

    assert len(data_source.pipeline_subscriptions) == 2
    pipeline_subscription = data_source.pipeline_subscriptions[0]
    assert pipeline_subscription.flow_name == "Medstar Data Ingestion"
    assert pipeline_subscription.flow_parameters == ["practices", "providers"]

    pipeline_subscription = data_source.pipeline_subscriptions[1]
    assert pipeline_subscription.flow_name == "Test Flow"
    assert len(pipeline_subscription.flow_parameters) == 0
    assert pipeline_subscription.flow_parameters == []

    assert data_source.connection_type == "file"


@patch.object(Catalog, "get_repo")
@patch.object(Catalog, "update_data_source")
@patch.object(Catalog, "get_all_data_sources", new=get_all_data_sources)
def test_catalog_update_data_source_resource(
    mock_update_data_source: MagicMock, mock_get_repo: MagicMock
) -> None:
    repo = "icanbwell/helix.orchestration"
    catalog = Catalog(repo=repo, access_token="fake_token")
    updated_data_source_tuple = catalog.update_data_source_resource(
        "s3://bwell-ingestion/raw/medstar/mp3/Insurance_MP3/bwellInsuranceFeed_05142021.json"
    )
    assert updated_data_source_tuple is not None
    updated_data_source = updated_data_source_tuple[0]
    sha = updated_data_source_tuple[1]

    mock_get_repo.assert_called_with(repo)
    mock_update_data_source.assert_called_with(
        updated_data_source.name, updated_data_source.to_json(), sha
    )

    assert (
        updated_data_source.base_connection == "s3://bwell-ingestion/raw/medstar/mp3/"
    )
    assert len(updated_data_source.resources) == 3

    insurance_resource = updated_data_source.resources[0]
    assert insurance_resource.name == "insurance"
    assert insurance_resource.path == "Insurance_MP3/bwellInsuranceFeed_05142021.json"

    practices_resource = updated_data_source.resources[1]
    assert practices_resource.name == "practices"
    assert practices_resource.path == "Practices_MP3/bwellPracticeFeed_05062021.json"

    providers_resource = updated_data_source.resources[2]
    assert providers_resource.name == "providers"
    assert providers_resource.path == "Providers_MP3/bwellProviderFeed_05062021.json"

    assert len(updated_data_source.pipeline_subscriptions) == 2
    pipeline_subscription = updated_data_source.pipeline_subscriptions[0]
    assert pipeline_subscription.flow_name == "Medstar Data Ingestion"
    assert pipeline_subscription.flow_parameters == ["practices", "providers"]

    pipeline_subscription = updated_data_source.pipeline_subscriptions[1]
    assert pipeline_subscription.flow_name == "Test Flow"
    assert len(pipeline_subscription.flow_parameters) == 0
    assert pipeline_subscription.flow_parameters == []

    assert updated_data_source.connection_type == "file"


@patch.object(Catalog, "get_repo")
@patch.object(Catalog, "update_data_source")
@patch.object(Catalog, "get_all_data_sources", new=get_all_data_sources)
def test_catalog_update_data_source_resource_returns_none(
    mock_update_data_source: MagicMock, mock_get_repo: MagicMock
) -> None:
    repo = "icanbwell/helix.orchestration"
    catalog = Catalog(repo=repo, access_token="fake_token")
    updated_data_source = catalog.update_data_source_resource(
        "s3://bwell-ingestion/raw/medstar/mp3/test/does_not_exist.csv"
    )
    assert updated_data_source is None
