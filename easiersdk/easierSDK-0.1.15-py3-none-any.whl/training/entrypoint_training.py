import time as time_lib
import argparse
import os, sys
import joblib
import json
import tensorflow as tf
import pandas
import numpy
import joblib
import tempfile

from easierSDK.easier import EasierSDK
from easierSDK.classes.categories import Categories
from easierSDK.classes.model_metadata import ModelMetadata
from easierSDK.classes.easier_model import EasierModel
import easierSDK.classes.constants as constants
from easierSDK import datasetsAPI

# Variable definition
easier = None
easier_model = None

# Environment variables loading
checkpoint_dir = os.getenv('CHECKPOINT_DIR', '/train/checkpoint')
data_dir = os.getenv('DATA_DIR', '/train/data')
model_dir = os.getenv('MODEL_DIR', '/train/model')
model_name = os.getenv('MODEL_NAME', 'model')

save_freq = os.getenv('SAVE_FREQ', 10)



def build_compile_model(model_dir:str, model_name:str):
    pass
    model = tf.keras.models.model_from_json(json.loads(model_dir + '/' + model_name + '.json'), 
                custom_objects=None)
    model.compile(
        optimizer='rmsprop', 
        loss=tf.keras.losses.categorical_crossentropy,
        metrics=[tf.keras.metrics.mean_squared_error]
    )
    return model

def compile_model(easier_model:EasierModel):
    # TF Compile should be done within distributed strategy
    easier_model.model.compile(
        optimizer=easier_model.training_metadata.optimizer, 
        loss=easier_model.training_metadata.loss,
        metrics=easier_model.training_metadata.metrics
    )
    easier_model.model.summary()
    return easier_model

if __name__ == "__main__":
    
    # Initializations
    easier_user = os.getenv("easier_user")
    easier_password = os.getenv("easier_password")
    
    ignore_cert_warning = os.getenv("ignore_cert_warning")
    ignore_cert_warning = True if str(ignore_cert_warning).lower() == 'true' else False

    minio_region = os.getenv("minio_region")
    
    minio_secure = os.getenv("minio_secure")
    minio_secure = True if str(minio_secure).lower() == 'true' else False
    
    easier_url = os.getenv("easier_url")
    easier = EasierSDK(easier_user=easier_user, easier_password=easier_password, easier_url=easier_url, minio_secure=minio_secure, minio_region=minio_region, ignore_cert_warning=ignore_cert_warning)

    repo = os.getenv("repo")
    category = os.getenv("category")
    model_name = os.getenv("model_name")
    experimentID = os.getenv("experimentID")
    data_path = os.getenv("data_path")

    easier_model = easier.models.get_model(repo_name=repo, category=category, model_name=model_name, experimentID=experimentID, load_level=constants.FULL, training=True)

    x, y, x_test, y_test = easier.training.get_training_data(repo_path=data_path)

    easier_model = compile_model(easier_model)

    if x_test is not None and y_test is not None:
        history = easier_model.model.fit(x, y, validation_data=(x_test, y_test), epochs=easier_model.training_metadata.epochs, batch_size=easier_model.training_metadata.batch_size, verbose=2)
    else:
        history = easier_model.model.fit(x, y, epochs=easier_model.training_metadata.epochs, batch_size=easier_model.training_metadata.batch_size, verbose=2)

    easier.training.clear_training_data(repo_path=data_path, repo_name=repo)

    easier.models._finish_model_training(easier_model, repo_name=repo, category=category, experimentID=experimentID)

    # Successfull exit
    sys.exit()
