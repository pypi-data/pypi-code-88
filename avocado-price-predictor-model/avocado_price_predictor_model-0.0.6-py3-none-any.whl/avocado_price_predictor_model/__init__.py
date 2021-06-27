import pickle
from os.path import isfile, join


path = '.'
file = 'model.pkl'

if not isfile(file):
    path = 'avocado_price_predictor_model'

with open(join(path, file), 'rb') as f:
    model = pickle.loads(f.read())
