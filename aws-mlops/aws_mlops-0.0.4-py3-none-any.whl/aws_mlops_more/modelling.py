"""The class for managing the training and testing of your model

The class contains the methods useful for managing your model cycle.
Here's an example:

    >>> from aws_mlops.modelling import Modelling
    >>> mlg = Modelling()
    >>> (train_input, val_input) = mlg.create_training_input([train_input_path, val_input_path])
    >>> estimator = mlg.create_estimator(estimator_input)
    >>> estimator.set_hyperparameters()
    >>> tuner = mlg.create_turner(estimator, tuner_input)
    >>> tuner.fit({'train': train_input, 'validation': val_input})
    >>> best_training_job = tuner.best_training_job()
    >>> model_input['model_data'] = f'{estimator_input['output_path']}/{best_training_job}/output/model.tar.gz'
    >>> transformer = mlg.create_transformer(mlg.create_model(model_input), transformer_input)
    >>> transformer.transform(transformer_input['test_data'], content_type = 'text/csv', split_type = 'Line', job_name = 'transformer_job_name'])

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/aws-mlops for details
"""
import boto3
import sagemaker
from sagemaker.inputs import TrainingInput
from sagemaker.tuner import HyperparameterTuner, IntegerParameter, ContinuousParameter

class Modelling():
    def create_training_input(self, input_paths):
        """
        creates training objects
            Arguments:
                input_paths (array of string): s3 uls of inputs with csv format
            Returns:
                array of training objects
        """
        inputs = []
        for input_path in input_paths:
            inputs.append(TrainingInput(
                s3_data=input_path,
                content_type='csv'
            ))
        return inputs
    def create_environment(self, container_input):
        """
        creates session, role and container
            Arguments:
                container_input (dict): dictionary of all properties to configure an object of type sagemaker.image_uris.retrieve
            Returns:
                array of [session, role, container]
        """
        session = sagemaker.Session()
        role = sagemaker.get_execution_role()
        # https://sagemaker.readthedocs.io/en/stable/api/utility/image_uris.html
        container = sagemaker.image_uris.retrieve(
            container_input['framework'],
            boto3.Session().region_name,    
            container_input['version'])
            #link a un container docker xgboost di amazon versione latest
        return [session, role, container]
    def create_estimator(self, estimator_input):
        """
        create estimator object
            Arguments:
                container_input (dict): dictionary of all properties of sagemaker.estimator.Estimator and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type sagemaker.estimator.Estimator
        """
        [ session, role, container ] = self.create_environment(estimator_input['container'])
        # https://sagemaker.readthedocs.io/en/stable/api/training/estimators.html#sagemaker.estimator.Estimator
        return sagemaker.estimator.Estimator(
            container,
            role,
            instance_count=1,
            instance_type=estimator_input['instance_type'],
            output_path=estimator_input['output_path'],
            sagemaker_session=session,
            tags=[
                {
                    'Key': 'Environment',
                    'Value': estimator_input['environment']
                },
                {
                    'Key': 'Application',
                    'Value': estimator_input['application']
                },
            ],
            #use_spot_instances = True, max_wait = 30,
            volume_size = estimator_input['volume_size']
        )
    def create_turner(estimator, tuner_input):
        """
        create turner object
            Arguments:
                tuner_input (dict): dictionary of all properties of HyperparameterTuner and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type HyperparameterTuner
        """
        # https://sagemaker.readthedocs.io/en/stable/api/training/tuner.html
        return HyperparameterTuner(
            estimator,
            tuner_input['objective_metric_name'],
            tuner_input['hyperparameter_ranges'],
            max_jobs=tuner_input['max_jobs'],
            max_parallel_jobs=tuner_input['max_parallel_jobs'],
            strategy=tuner_input['strategy'], #Bayesian è il default
            objective_type=tuner_input['objective_type'],
            base_tuning_job_name=tuner_input['base_tuning_job_name'],
            tags=[
                {
                    'Key': 'Environment',
                    'Value': tuner_input['environment']
                },
                {
                    'Key': 'Application',
                    'Value': tuner_input['application']
                },
            ]
        )
    def create_model(self, model_input):
        """
        create model object
            Arguments:
                model_input (dict): dictionary of all properties of sagemaker.model.Model and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type sagemaker.model.Model
        """
        [ session, role, container ] = self.create_environment(model_input['container'])
        # https://sagemaker.readthedocs.io/en/stable/api/inference/model.html
        return sagemaker.model.Model(
            image_uri = container,
            model_data=model_input['model_data'],
            role=role, 
            sagemaker_session=session
        )
    def create_transformer(model, transformer_input):
        """
        creates transformer object
            Arguments:
                transformer_input (dict): dictionary of all properties of sagemaker.model.Model.transformer and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type sagemaker.model.Model.transformer
        """
        # https://sagemaker.readthedocs.io/en/stable/api/inference/model.html#sagemaker.model.Model.transformer
        return model.transformer(
            output_path=transformer_input['output_path'],
            instance_type=transformer_input['instance_type'],
            instance_count=transformer_input['instance_count'],
            tags=[
                {
                    'Key': 'Environment',
                    'Value': transformer_input['environment']
                },
                {
                    'Key': 'Application',
                    'Value': transformer_input['application']
                },
            ]
        )
