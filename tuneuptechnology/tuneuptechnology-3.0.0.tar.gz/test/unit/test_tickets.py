import vcr
from tuneuptechnology.client import Client


@vcr.use_cassette('test/cassettes/tickets/test_ticket_create.yml', filter_headers=['Email', 'Api-Key'])
def test_ticket_create(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Tickets.create(
        data={
            'customer_id': 2,
            'ticket_type_id': 1,
            'serial': '10000',
            'user_id': 1,
            'notes': 'here are some notes',
            'title': 'Fancy Title',
            'status': 1,
            'device': 'iPhone',
            'imei': 10000,
            'location_id': 2
        }
    )

    assert response['title'] == 'Fancy Title'


@vcr.use_cassette('test/cassettes/tickets/test_ticket_all.yml', filter_headers=['Email', 'Api-Key'])
def test_ticket_all(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Tickets.all()

    assert len(response['data']) > 1


@vcr.use_cassette('test/cassettes/tickets/test_ticket_retrieve.yml', filter_headers=['Email', 'Api-Key'])
def test_ticket_retrieve(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Tickets.retrieve(id=1)

    assert response['title']


@vcr.use_cassette('test/cassettes/tickets/test_ticket_update.yml', filter_headers=['Email', 'Api-Key'])
def test_ticket_update(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Tickets.update(
        id=1,
        data={
            'customer_id': 2,
            'ticket_type_id': 1,
            'serial': '10000',
            'user_id': 1,
            'notes': 'here are some notes',
            'title': 'Fancy Title',
            'status': 1,
            'device': 'iPhone',
            'imei': 10000,
            'location_id': 2
        }
    )

    assert response['title'] == 'Fancy Title'


@vcr.use_cassette('test/cassettes/tickets/test_ticket_delete.yml', filter_headers=['Email', 'Api-Key'])
def test_ticket_delete(api_email, api_key, base_url):
    client = Client(api_email, api_key, base_url)
    response = client.Tickets.delete(id=1)

    assert response['deleted_at']
