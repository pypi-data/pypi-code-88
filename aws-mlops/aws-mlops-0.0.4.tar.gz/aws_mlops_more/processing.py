"""The class for managing your processes

The class accepts a dictionary with all properties of the AWS services methods used.
Here's an example:

    >>> from aws_mlops.processing import Processing
    >>> p = Processing(processor_input)
    >>> processor = p.run(p.create())
    >>> processing_job_description = processor.jobs[-1].describe()

# license MIT
# author Alessandra Bilardi <alessandra.bilardi@gmail.com>
# see https://github.com/bilardi/aws-mlops for details
"""
from sagemaker import get_execution_role
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput

class Processing():
    processor_input = None
    def __init__(self, processor_input):
        self.processor_input = processor_input
    def create_processing_input(self, config):
        """
        creates processing input objects
            Arguments:
                config (array of inputs): s3 uls and local path of inputs where to load
            Returns:
                array of processing input objects
        """
        inputs = []
        for input in config:
            inputs.append(ProcessingInput(
                source=input['s3_url'],
                destination=input['local_path']
            ))
        return inputs
    def create_processing_output(self, config):
        """
        creates processing output objects
            Arguments:
                config (array of outputs): local path and s3 uls of outputs where to load
            Returns:
                array of processing output objects
        """
        outputs = []
        for output in config:
            outputs.append(ProcessingOutput(
                output_name=output['name'],
                source=output['local_path'],
                destination=output['s3_url']
            ))
        return outputs
    def create(self, processor_input=None):
        """
        creates the processor object
            Arguments:
                processor_input (dict): dictionary of all properties of sagemaker.sklearn.processing.SKLearnProcessor and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type sagemaker.sklearn.processing.SKLearnProcessor
        """
        if processor_input is None:
            processor_input = self.processor_input
        role = get_execution_role()
        # https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/sagemaker.sklearn.html#sagemaker.sklearn.processing.SKLearnProcessor
        return SKLearnProcessor(
            framework_version=processor_input['framework_version'],
            role=role,
            instance_type=processor_input['instance_type'],
            instance_count=processor_input['instance_count'],
            tags=[
                {
                    'Key': 'Environment',
                    'Value': processor_input['environment']
                },
                {
                    'Key': 'Application',
                    'Value': processor_input['application']
                },
            ]
        )
    def run(self, processor, processor_input=None):
        """
        run the processor
            Arguments:
                processor (sagemaker.sklearn.processing.SKLearnProcessor): the processor object created by self.create()
                processor_input (dict): dictionary of all properties of sagemaker.sklearn.processing.SKLearnProcessor and the properties for tagging:
                    'environment' (string): name of the environment
                    'application' (string): name of the application
            Returns:
                an object of type SKLearnProcessor
        """
        if processor_input is None:
            processor_input = self.processor_input
        # https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.Processor.run
        processor.run(
            code='processing.py',
            # https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ProcessingInput
            inputs=self.create_processing_input(processor_input['inputs']),
            # https://sagemaker.readthedocs.io/en/stable/api/training/processing.html#sagemaker.processing.ProcessingOutput
            outputs=self.create_processing_output(processor_input['outputs']),
            arguments=processor_input['arguments']
         )
        return processor
