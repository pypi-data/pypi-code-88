import pickle


with open('model.pkl', 'rb') as f:
    model = pickle.loads(f.read())
