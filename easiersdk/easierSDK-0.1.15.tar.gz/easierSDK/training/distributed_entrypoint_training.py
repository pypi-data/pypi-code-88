import time as time_lib
from datetime import datetime
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

# Important readings
# https://www.tensorflow.org/tutorials/distribute/input
# https://www.tensorflow.org/api_docs/python/tf/distribute/MultiWorkerMirroredStrategy
# https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras


# Variable definition
easier = None
easier_model = None
x = None
y = None
x_test = None
y_test = None

# Environment variables loading
tf_config = json.loads(os.environ['TF_CONFIG'])
num_workers = len(tf_config['cluster']['worker'])

checkpoint_dir = os.getenv('CHECKPOINT_DIR', '/train/checkpoint')
tf_log_dir = os.getenv('LOG_DIR', '/train/tf_logs/')
data_dir = os.getenv('DATA_DIR', '/train/data')
model_dir = os.getenv('MODEL_DIR', '/train/model')
model_name = os.getenv('MODEL_NAME', 'model')

per_worker_batch_size = os.getenv('WORKER_BATCH_SIZE', 64)
global_batch_size = per_worker_batch_size * num_workers
save_freq = os.getenv('SAVE_FREQ', 10)

def easier_dataset(input_context):
    # Ideally here we would call the easierSDK to get the training data.
    # Create dataset object
    global x
    global y
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    
    # Shard the dataset between the workers
    dataset = dataset.shard(input_context.num_input_pipelines, input_context.input_pipeline_id)
    
    # Repeat this dataset infinitely (every time this function is called, a counter is reduced, if we do not set this, then the dataset is returned only once)
    dataset = dataset.repeat()

    # Get batch_size from global_batch_size and batch the dataset
    batch_size = input_context.get_per_replica_batch_size(global_batch_size)
    dataset = dataset.batch(batch_size)
    
    # Prefetch 2 batches per device.
    dataset = dataset.prefetch(2) 
    
    return dataset

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
    
    start = time_lib.time()

    # Initializations
    cluster_resolver = tf.distribute.cluster_resolver.TFConfigClusterResolver()

    strategy = tf.distribute.MultiWorkerMirroredStrategy(cluster_resolver=cluster_resolver)

    print("Task type, id: " + str(cluster_resolver.task_type) + ", " + str(cluster_resolver.task_id))

    # ------------------------- Distributed Parameter Training -------------------------
    # if cluster_resolver.task_type in ("worker", "ps"):
    #     # start a TensorFlow server and wait.
    #     print("Starting TF server...")
    #     server = tf.distribute.Server(
    #         cluster_resolver.cluster_spec(),
    #         job_name=cluster_resolver.task_type,
    #         task_index=cluster_resolver.task_id,
    #         protocol=None,
    #         start=True)
    #     server.join()
    # elif cluster_resolver.task_type == "evaluator":
    #     # run side-car evaluation
    #     continue
    # else:
        # run the coordinator/chief
    # -------------------------------------------------------------------------

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

    # Ideally, this should be called within the easier_dataset function. But we keep it here to obtain also the validation data
    x, y, x_test, y_test = easier.training.get_training_data(repo_path=data_path)

    # ------------------------- DATASET DISTRIBUTION -------------------------

    # ------------- Method 1 -------------
    # options = tf.data.Options()
    # options.experimental_distribute.auto_shard_policy = tf.data.experimental.AutoShardPolicy.DATA    
    # Read data from /train/data
    # dataset = tf.data.Dataset.from_tensor_slices((x, y)).with_options(options)
    # multi_worker_dataset = strategy.experimental_distribute_dataset(dataset, options)
    # ---------------------------------------

    # ------------- Method 2 - supposedly better --------
    multi_worker_dataset = strategy.distribute_datasets_from_function(easier_dataset)
    # , 
    #                     options=tf.distribute.InputOptions(
    #                         experimental_prefetch_to_device=True,
    #                         experimental_replication_mode=tf.distribute.InputReplicationMode.PER_WORKER,
    #                         experimental_place_dataset_on_device=False
    # ))
    # -----------------------------------------------

    # -------------------------------------------------------------------------

    with strategy.scope():
        easier_model = easier.models.get_model(repo_name=repo, category=category, model_name=model_name, experimentID=experimentID, load_level=constants.FULL, training=True)

        # Model building/compiling need to be within `strategy.scope()`.
        multi_worker_model = compile_model(easier_model)

    # if cluster_resolver.task_id == 0:
    #     os.system("nohup tensorboard --logdir " + tf_log_dir + " --bind_all &")
    #     tensorboard_callback = tf.keras.callbacks.TensorBoard(log_dir=tf_log_dir + datetime.now().strftime("%Y%m%d-%H%M%S"))
    #     callbacks = [tensorboard_callback]
    # else:
    #   callbacks = None
    # callbacks = [
    #         # This callback saves a SavedModel every epoch
    #         # We include the current epoch in the folder name.
    #         tf.keras.callbacks.ModelCheckpoint(
    #             filepath=checkpoint_dir + "/ckpt-{epoch}", save_freq=save_freq
    #         )
    #     ]
    callbacks = None
    
    # steps_per_epoch must be set when using distributed training. Usually it is set as len(x)/global_batch_size
    if x_test is not None and y_test is not None:
        history = multi_worker_model.model.fit(multi_worker_dataset, validation_data=(x_test, y_test), 
                    epochs=easier_model.training_metadata.epochs, verbose=2, 
                    steps_per_epoch=int(len(x)/global_batch_size),
                    callbacks=callbacks)
    else:
        history = multi_worker_model.model.fit(multi_worker_dataset, 
                epochs=easier_model.training_metadata.epochs, verbose=2, 
                steps_per_epoch=int(len(x)/global_batch_size),
                callbacks=callbacks)
    
    # If we are chief (worker 0)
    if cluster_resolver.task_id == 0:
        
        multi_worker_model.model.save(checkpoint_dir + "/final_model.h5")
        
        easier.training.clear_training_data(repo_path=data_path, repo_name=repo)

        easier.models._finish_model_training(multi_worker_model, repo_name=repo, category=category, experimentID=experimentID)

    end = time_lib.time()
    print("Total execution time: " + str(end))

    # Successfull exit
    sys.exit()