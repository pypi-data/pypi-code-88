from src.aws import connector

# connect to dynamo
dynamodb = connector.session().resource('dynamodb')


def select_by_name(name, table_name):
    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key={
            'name': name
        }
    )
    print(table.creation_date_time)
    print(response)


def select_all(table_name):
    table = dynamodb.Table(table_name)
    items = table.scan()['Items']
    names = []
    for item in items:
        names.append(item['name'])
    print(names)
    return names

def create_table(table_name):
    table = dynamodb.create_table(
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'username',
                'KeyType': 'HASH'
            },
            {
                'AttributeName': 'last_name',
                'KeyType': 'RANGE'
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'username',
                'AttributeType': 'S'
            },
            {
                'AttributeName': 'last_name',
                'AttributeType': 'S'
            },
        ]
    )
    table.meta.client.get_waiter('table_exists').wait(TableName='users')

    # Print out some data about the table.
    print(table.item_count)

