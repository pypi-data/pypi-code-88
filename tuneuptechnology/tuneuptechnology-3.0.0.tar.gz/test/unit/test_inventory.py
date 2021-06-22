import vcr
from tuneuptechnology.client import Client


@vcr.use_cassette('test/cassettes/inventory/test_inventory_create.yml', filter_headers=['Email', 'Api-Key'])
def test_inventory_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.create(
        data={
            'name': 'Inventory Item',
            'inventory_type_id': 1,
            'part_number': '1234',
            'sku': '1234',
            'notes': 'here are some notes',
            'part_price': '19.99',
            'location_id': 2,
            'quantity': 1
        }
    )

    assert response['name'] == 'Inventory Item'


@vcr.use_cassette('test/cassettes/inventory/test_inventory_all.yml', filter_headers=['Email', 'Api-Key'])
def test_inventory_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.all()

    assert len(response['data']) > 1


@vcr.use_cassette('test/cassettes/inventory/test_inventory_retrieve.yml', filter_headers=['Email', 'Api-Key'])
def test_inventory_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.retrieve(id=1)

    assert response['name']


@vcr.use_cassette('test/cassettes/inventory/test_inventory_update.yml', filter_headers=['Email', 'Api-Key'])
def test_inventory_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.update(
        id=1,
        data={
            'name': 'Inventory Item',
            'inventory_type_id': 1,
            'part_number': '1234',
            'sku': '1234',
            'notes': 'here are some notes',
            'part_price': '19.99',
            'location_id': 2,
            'quantity': 1
        }
    )

    assert response['name'] == 'Inventory Item'


@vcr.use_cassette('test/cassettes/inventory/test_inventory_delete.yml', filter_headers=['Email', 'Api-Key'])
def test_inventory_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Inventory.delete(id=1)

    assert response['deleted_at']
