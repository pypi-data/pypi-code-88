from context import signalboxclient
import environment

creds = signalboxclient.Credentials(environment.api_key)
config = signalboxclient.Configuration(
    host=environment.host, port=environment.port)
client = signalboxclient.client.SignalBoxClient(creds)

# create some offers
offer_ids = []
for i in range(4):
    offer = client.create_offer(name=f'offer{i}', currency='AUD', price=(i+1)*5, cost=(i+1)*2)
    offer_ids.append(offer['id'])

# create an experiment
experiment = client.create_experiment(offer_ids, name='sim_experiment')

# export/print the experimentID
print(f'experiment id: {experiment["id"]}')
