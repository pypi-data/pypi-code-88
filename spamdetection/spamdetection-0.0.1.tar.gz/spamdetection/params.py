"""
Declares parameters used by other modules contained in the package.
"""

import os.path
    
# Path to the model file
MODEL_FILENAME = "sms_model_v1.pkl"
MODEL_DIRECTORY = "Model"
MODEL_PATH = os.path.join(MODEL_DIRECTORY, MODEL_FILENAME)
    
# With this threshold, there are no false positives in the validation set
PERMISSIVE_THRESHOLD = .61
    
# With this threshold, there are no false negatives in the validation set
AGGRESSIVE_THRESHOLD = .07

# URL for the web app
WEB_APP_URL = 'https://nuveo-teste-ia.herokuapp.com/'