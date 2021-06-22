# pylint: disable=super-with-arguments
# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

"""
    GLUE TASK CODE
        - these are used in pythonOperator steps as a way \
            to flexibly call boto3 and perform any special requirements
"""
import logging
import time
import warnings

import boto3
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

logger = logging.getLogger(None)


class RunGlueJob(BaseOperator):
    """Runs Glue Job, and can consume variables for the job."""
    template_fields = ('config', 'xcom_tasks')

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(RunGlueJob, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
            :config.job_name: str. the name of the glue job to run.
            :config.job_arguments: dict. the key value arguments send to the job.
            :xcom_push: str. glue_job_run_id.
        """
        CLIENT = boto3.client('glue')

        job_name = self.config.get('job_name', None)
        job_arguments = self.config.get('job_arguments', None)

        if job_name is None:
            raise ValueError('Job name is required for task.')
        if job_arguments is None:
            warnings.warn('Job arguments are empty.')

        try:
            logging.info('Running glue job {name} with envs {envs}.'.format(
                name=job_name,
                envs=job_arguments)
            )

            response = CLIENT.start_job_run(
                JobName=job_name,
                Arguments=job_arguments
            )

            # push job_run_id to xcom
            context['task_instance'].xcom_push(
                key='job_run_id',
                value=response['JobRunId']
            )

            # push job_name to xcom for other glue tasks to reference
            context['task_instance'].xcom_push(
                key='job_name',
                value=job_name
            )

        except Exception as err:
            raise err


class MonitorGlueJob(BaseOperator):
    """Monitors Glue Job until SUCCESS state."""
    template_fields = ('config', 'xcom_tasks',)

    @apply_defaults
    def __init__(self, config, xcom_tasks, *args, **kwargs):
        super(MonitorGlueJob, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
            :config.job_name: str. optional the name of the glue job to monitor.
                             if not monitored, name is pulled from xcom_tasks.
            :config.job_run_id: str. optional run id of the job to monitor
                               if not monitored, id is pulled from xcom_tasks.
            xcom_tasks:
                job_name:
                    task_id: str.
                    key: job_name
                job_run_id:
                    task_id: str
                    key: job_run_id
        """
        CLIENT = boto3.client('glue')

        try:
            job_name = self.config.get('job_name', None)
            job_run_id = self.config.get('job_run_id', None)

            task_ids = self.xcom_tasks['job_name']['task_id']

            if job_name is None:
                # if optional config job_name is None, pull from xcom
                job_name = context['task_instance'].xcom_pull(
                    task_ids=task_ids,
                    key=self.xcom_tasks['job_name']['key']
                )

            if job_run_id is None:
                # if optional config job_run_id is None, pull from xcom
                job_run_id = context['task_instance'].xcom_pull(
                    task_ids=task_ids,
                    key=self.xcom_tasks['job_run_id']['key']
                )

            logging.info('Got glue job name and run id from xcom: {name}:{id}'.format(
                name=job_name, id=job_run_id))

            while True:
                response = CLIENT.get_job_run(
                    JobName=job_name,
                    RunId=job_run_id,
                )

                state = response['JobRun']['JobRunState']
                if state == 'SUCCEEDED':
                    break
                if state == 'STOPPED':
                    break
                if state == 'FAILED':
                    raise RuntimeError('Glue Job failed.', response)
                if state == 'TIMEOUT':
                    raise RuntimeError('Glue Job timed out.')

                logging.info('Monitoring glue job: {name}.\n State: {state}'.format(
                    name=job_name,
                    state=state)
                )

                time.sleep(10)

        except Exception as err:
            raise err


class TagGlueJob(BaseOperator):
    """Adds a tag to the resource specified."""
    template_fields = ('config', 'xcom_tasks',)

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(TagGlueJob, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """

        """
        CLIENT = boto3.client('glue')

        job_name = self.config.get('job_name', None)
        resource_tags = self.config.get('resource_tags', None)

        if job_name is None:
            # if optional config job_name is None, pull from xcom
            job_name = context['task_instance'].xcom_pull(
                self.xcom_tasks['job_name']['task_id'],
                key=self.xcom_tasks['job_name']['key']
            )

        if resource_tags is None:
            raise ValueError('Resource tags are required for task.')

        try:
            account_id = boto3.client('sts').get_caller_identity().get('Account')
            glue_resource_arn = 'arn:aws:glue:eu-west-1:{account_id}:job/{name}'.format(
                account_id=account_id, name=job_name
            )

            CLIENT.tag_resource(
                ResourceArn=glue_resource_arn,
                TagsToAdd=resource_tags
            )

            # push resource_tags to xcom for other glue tasks to reference
            context['task_instance'].xcom_push(
                key='resource_tags',
                value=resource_tags
            )

        except Exception as err:
            raise err


class UnTagGlueJob(BaseOperator):
    """Removes a tag to the resource specified."""
    template_fields = ('config', 'xcom_tasks',)

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(UnTagGlueJob, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
            :glue_resource_arn: str. the Arn of the glue resource.
            :resource_tags: dict. the key value pairs of the
                                 relevant tags to remove.
        """
        CLIENT = boto3.client('glue')

        job_name = self.config.get('job_name', None)
        resource_tags = self.config.get('resource_tags', None)

        task_ids = self.xcom_tasks['job_name']['task_id']

        if job_name is None:
            # if optional config job_name is None, pull from xcom
            job_name = context['task_instance'].xcom_pull(
                task_ids=task_ids,
                key=self.xcom_tasks['job_name']['key']
            )

        if resource_tags is None:
            # if optional config resource_tags None, pull from xcom
            resource_tags = context['task_instance'].xcom_pull(
                task_ids=task_ids,
                key=self.xcom_tasks['resource_tags']['key']
            )

        try:
            account_id = boto3.client('sts').get_caller_identity().get('Account')
            glue_resource_arn = 'arn:aws:glue:eu-west-1:{account_id}:job/{name}'.format(
                account_id=account_id, name=job_name
            )

            tags_to_remove = list(key for key in resource_tags.keys())

            CLIENT.untag_resource(
                ResourceArn=glue_resource_arn,
                TagsToRemove=tags_to_remove
            )

        except Exception as err:
            raise err


class RunGlueCrawler(BaseOperator):
    """Runs Glue Crawler."""
    template_fields = ('config', 'xcom_tasks',)

    @apply_defaults
    def __init__(self, config=None, xcom_tasks=None, *args, **kwargs):
        super(RunGlueCrawler, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
            :glue_crawler_name: str. the name of the crawler to be triggered.
        """
        CLIENT = boto3.client('glue')

        crawler_name = self.config.get('crawler_name', None)
        if crawler_name is None:
            raise ValueError('Crawler name needed for task.')

        try:
            logging.info(
                'Running glue crawler {name}'.format(
                    name=crawler_name
                )
            )

            CLIENT.start_crawler(
                Name=crawler_name
            )

            # push crawler_name to xcom
            context['task_instance'].xcom_push(
                key='crawler_name',
                value=crawler_name
            )

        except Exception as err:
            raise err


class MonitorGlueCrawler(BaseOperator):
    """Monitors Glue Crawler until complete."""
    template_fields = ('config', 'xcom_tasks',)

    @apply_defaults
    def __init__(self, config, xcom_tasks=None, *args, **kwargs):
        super(MonitorGlueCrawler, self).__init__(*args, **kwargs)

        self.config = config
        self.xcom_tasks = xcom_tasks

    def execute(self, context):
        """
            :glue_crawler_name: str. the name of crawler to be monitored.
        """
        CLIENT = boto3.client('glue')

        crawler_name = self.config.get('crawler_name', None)
        task_ids = self.xcom_tasks['job_name']['task_id']

        if crawler_name is None:
            crawler_name = context['task_instance'].xcom_pull(
                task_ids=task_ids,
                key=self.xcom_tasks['crawler_name']['key']
            )

        try:
            wait = 0
            while True:
                state = CLIENT.get_crawler(
                    Name=crawler_name
                )['Crawler']['State']

                if state == 'READY':
                    break
                if state == 180:
                    raise RuntimeError('Pre crawler: {name} failed. Timeout.'.format(
                        name=crawler_name)
                    )

                logging.info('Monitoring glue crawler: {name}.\n State: {state}'.format(
                    name=crawler_name, state=state)
                )

                wait += 1
                time.sleep(10)
        except Exception as err:
            raise err
