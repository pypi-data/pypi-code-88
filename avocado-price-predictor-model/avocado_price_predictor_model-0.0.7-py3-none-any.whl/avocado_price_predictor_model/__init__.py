import pickle
import gdown


# Download model
url = 'https://drive.google.com/uc?id=1UiH6y3kvlWcGTpH9AV9qsQrjJZ-X9f2s'
path = 'model.pkl'
gdown.download(url, path)

# Load model
with open(path, 'rb') as f:
    model = pickle.loads(f.read())
