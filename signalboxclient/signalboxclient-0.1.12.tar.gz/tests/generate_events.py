from client import Credentials, Four2Client, Configuration
import environment
import uuid

creds = Credentials(environment.api_key)
config = Configuration(host= environment.host, port=environment.port)
client = Four2Client(creds, configuration=config)

user1 = str(uuid.uuid1())
user2 = str(uuid.uuid1())

events = [
    client.construct_event(user1, str(uuid.uuid1()), "PLAN_START", "BILLING", {'sku': 'starter' }),
    client.construct_event(user2, str(uuid.uuid1()), "PLAN_END", "BILLING" ,{'sku': 'enterprise' })
]

r = client.log_events(events)

print(r)
print('events generated.')