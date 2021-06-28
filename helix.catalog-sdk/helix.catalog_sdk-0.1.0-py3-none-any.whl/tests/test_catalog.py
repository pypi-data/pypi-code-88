import json
import os.path
import shutil
from types import ModuleType

from helix_catalog_sdk.catalog import Catalog
from helix_catalog_sdk.repo import DirectoryRepo
from helix_catalog_sdk.enums import HelixEnvironment


TEST_DIR = os.path.dirname(__file__)
SOURCE_CATALOG = os.path.join(TEST_DIR, "test_catalog")


def setup_module(module: ModuleType) -> None:
    print("Setting up")
    print(" * Copying directory 'test_catalog' to 'catalog' for testing")
    shutil.copytree(
        src=SOURCE_CATALOG, dst="catalog",
    )


def teardown_module(module: ModuleType) -> None:
    print("Tearing down")
    print(" * Removing directory 'catalog'")
    shutil.rmtree("catalog", ignore_errors=True)


def test_catalog_get_data_source() -> None:

    repo = DirectoryRepo(location="")
    catalog = Catalog(repo=repo)

    data_source = catalog.get_data_source(
        "catalog/raw/gencon/icd.json", HelixEnvironment.PRODUCTION
    )
    assert data_source is not None

    assert (
        data_source.base_connection_formatted == "s3://prod-ingestion/raw/gencon/icd/"
    )
    assert len(data_source.resources) == 3

    people_resource = data_source.resources[0]
    assert people_resource.name == "people"
    assert (
        people_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/People/PeopleFeed_06092021.json"
    )

    places_resource = data_source.resources[1]
    assert places_resource.name == "places"
    assert (
        places_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/Places/PlaceFeed_06172021.json"
    )

    things_resource = data_source.resources[2]
    assert things_resource.name == "things"
    assert (
        things_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/Things/ThingFeed_06092021.json"
    )

    assert len(data_source.pipeline_subscriptions) == 2
    pipeline_subscription = data_source.pipeline_subscriptions[0]
    assert pipeline_subscription.flow_name == "INGEN Data Ingestion"
    assert pipeline_subscription.flow_parameters == ["people", "places"]

    pipeline_subscription = data_source.pipeline_subscriptions[1]
    assert pipeline_subscription.flow_name == "Test Flow"
    assert len(pipeline_subscription.flow_parameters) == 0
    assert pipeline_subscription.flow_parameters == []

    assert data_source.connection_type == "file"


def test_catalog_update_data_source_resource() -> None:

    repo = DirectoryRepo(location="")
    catalog = Catalog(repo=repo)
    catalog.get_all_data_sources()

    updated_data_source = catalog.update_data_source_resource(
        "s3://prod-ingestion/raw/gencon/icd/People/PeopleFeed_06142021.json"
    )

    assert updated_data_source is not None

    assert (
        updated_data_source.base_connection_formatted
        == "s3://prod-ingestion/raw/gencon/icd/"
    )
    assert len(updated_data_source.resources) == 3

    people_resource = updated_data_source.resources[0]
    assert people_resource.name == "people"
    assert (
        people_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/People/PeopleFeed_06142021.json"
    )

    places_resource = updated_data_source.resources[1]
    assert places_resource.name == "places"
    assert (
        places_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/Places/PlaceFeed_06172021.json"
    )

    things_resource = updated_data_source.resources[2]
    assert things_resource.name == "things"
    assert (
        things_resource.full_path
        == "s3://prod-ingestion/raw/gencon/icd/Things/ThingFeed_06092021.json"
    )

    assert len(updated_data_source.pipeline_subscriptions) == 2
    pipeline_subscription = updated_data_source.pipeline_subscriptions[0]
    assert pipeline_subscription.flow_name == "INGEN Data Ingestion"
    assert pipeline_subscription.flow_parameters == ["people", "places"]

    pipeline_subscription = updated_data_source.pipeline_subscriptions[1]
    assert pipeline_subscription.flow_name == "Test Flow"
    assert len(pipeline_subscription.flow_parameters) == 0
    assert pipeline_subscription.flow_parameters == []

    assert updated_data_source.connection_type == "file"

    # Load json from file for comparison as well, not just from in-memory object and confirm data properly updated
    json_file = "catalog/raw/gencon/icd.json"
    json_data = json.load(open(json_file))
    json_resources = json_data.get("resources")
    assert json_resources == [
        {
            "name": "people",
            "path": "People/PeopleFeed_06142021.json",
            "path_slug": "People/PeopleFeed_",
        },
        {
            "name": "places",
            "path": "Places/PlaceFeed_06172021.json",
            "path_slug": "Places/PlaceFeed_",
        },
        {
            "name": "things",
            "path": "Things/ThingFeed_06092021.json",
            "path_slug": "Things/ThingFeed_",
        },
    ]


def test_catalog_update_data_source_resource_returns_none() -> None:
    repo = DirectoryRepo(location="")
    catalog = Catalog(repo=repo)
    catalog.get_all_data_sources()

    updated_data_source = catalog.update_data_source_resource(
        "s3://prod-ingestion/raw/gencon/icd/test/does_not_exist.csv"
    )
    assert updated_data_source is None
