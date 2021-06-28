from context import signalboxclient
import environment
import time
import uuid
import random

creds = signalboxclient.Credentials(environment.api_key)
config = signalboxclient.Configuration(
    host=environment.host, port=environment.port)
client = signalboxclient.client.SignalBoxClient(creds)

# grab the experimentID from setup_simulation.py
experiment_id = 1
num_presentations = 200

# Agent classes


class Agent:
    def __init__(self, label):
        self.id = str(uuid.uuid1())
        self.label = label


class ProbAgent(Agent):
    def __init__(self, label, acceptance_probs):
        Agent.__init__(self, label)
        self.acceptance_probs = acceptance_probs

    def handle_offers(self, offers):

        if random.uniform(0, 1) <= self.acceptance_probs[offers[0]["name"]]:
            return (offers[0], 'accept')
        else:
            return (offers[0], 'reject')


# initialises type of agent with corresponding prob distribution for acceptance
def get_agent(label):
    if label == 'French':
        return ProbAgent('French', {'offer0': 0.9, 'offer1': 0.875, 'offer2': 0.85, 'offer3': 0.8})
        # return ProbAgent('French', {'offer0': 0, 'offer1': 0, 'offer2': 0, 'offer3': 1})
    elif label == 'German':
        return ProbAgent('German', {'offer0': 0.8, 'offer1': 0.775, 'offer2': 0.75, 'offer3': 0.7})

    raise Error('agent label does not exist')


num_accepted = 0
start = time.time()
print("Starting presentations...")
for i in range(num_presentations):
    agent = get_agent(random.choice(['French', 'German']))
    if (i % 25) == 0:
        print(f"Presenting offer {i}")
    recommendation = client.recommend_offer(
        experiment_id, agent.id, {'country': agent.label})
    (offer, outcome) = agent.handle_offers(recommendation['offers'])
    tracked_outcome = client.track_recommendation_outcome(
        recommendation=recommendation, offerId=offer["id"], outcome=outcome)
    if tracked_outcome['outcome'] == 'accept':
        num_accepted += 1

print(f'{100*num_accepted/num_presentations}% outcomes accepted from {num_presentations} runs')

end = time.time()
print('Time elapsed:', end - start)
