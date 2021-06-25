"""The class for managing your MLOps cycle

The class accepts two properties:
    'bucket' (string): the bucket name where to save or restore the data
    'key' (string): the path where to save or restore the data

These properties are mandatory. Here's an example:

    >>> from aws_mlops.data_storage import DataStorage
    >>> ds = DataStorage('your-bucket-name', 'key/of/your/files/without/filename')
    >>> ds.checkpoint(my_dataframe)
    >>> my_dataframe = ds.restore()
    >>> ds.save_test(test, [target_column, identifier_column])
    >>> [test, columns, target, identifier] = ds.restore_test([target_column, identifier_column])
    >>> ds.save_report([train, validation])

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/aws-mlops for details
"""
class MLOps():
    config = None
    def __init__(self, config):
        self.config = config
    def create_step_functions_definition(self, config = None):
        if config is None:
            config = self.config
        # https://docs.aws.amazon.com/step-functions/latest/dg/connect-sagemaker.html
        preprocessing = {'Type': 'Task', 'Resource': 'arn:aws:states:::sagemaker:createProcessingJob.sync',
            'Next': 'Tuning',
            'Parameters': {
                'AppSpecification': {
                    'ImageUri.$': '$.'
                }
            }
        }
        tuning = {'Type': 'Task', 'Resource': 'arn:aws:states:::sagemaker:createHyperParameterTuningJob.sync',
            'Next': 'Transform',
            'Parameters': {}
        }
        # https://docs.aws.amazon.com/step-functions/latest/dg/connect-stepfunctions.html
        transform = {'Type': 'Task', 'Resource': 'arn:aws:states:::sagemaker:createTransformJob.sync',
            'Next': 'TestProcessing',
            'Parameters': {}
        }
        testprocessing = {'Type': 'Task', 'Resource': 'arn:aws:states:::sagemaker:createProcessingJob.sync',
            'End':True,
            'Parameters': {}
        }
        definition = {'Comment':'MLOps state machine', 'StartAt': 'PreProcessing',
            'States': {
                'PreProcessing': preprocessing,
                'Tuning': tuning,
                'Transform': transform,
                'TestProcessing': testprocessing
            }
        }
        return definition
