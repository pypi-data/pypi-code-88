from datetime import datetime, timedelta
from typing import List
from apscheduler.schedulers.base import BaseScheduler, JobLookupError
from apscheduler.job import Job
from collections import OrderedDict
from apscheduler.triggers.cron import CronTrigger, BaseTrigger
from apscheduler.triggers.date import DateTrigger
from apscheduler.triggers.interval import IntervalTrigger
import six
import dateutil
import socket


class API(object):

    def __init__(self, scheduler: BaseScheduler) -> None:
        self.scheduler = scheduler
        self.host_name = socket.gethostname().lower()
        self.allowed_hosts = ["*"]

    def get_scheduler_info(self) -> dict:
        """Gets the scheduler info."""

        scheduler = self.scheduler

        return OrderedDict([
            ('current_host', self.host_name),
            ('allowed_hosts', self.allowed_hosts),
            ('running', scheduler.running)
        ])

    def add_job(self, **data) -> Job:
        """添加自定义作业

        Returns:
            Job: 作业数据
        Raise:
            apscheduler.jobstores.base.ConflictingIdError 作业已存在，建议返回409状态
            Exception 其他任意可能的错误，建议返回500状态
        """
        return self.scheduler.add_job(**data)

    def remove_job(self, job_id) -> None:
        """Deletes a job.

        Returns: 
            None    删除成功，建议返回204状态
        Raises:
            apscheduler.jobstores.base.JobLookupError 作业不存在，建议返回404状态
            Exception 其他任意可能的错误，建议返回500状态
        """
        self.scheduler.remove_job(job_id)

    def get_job(self, job_id) -> Job:
        """Gets a job.

        Args:
            job_id (str): 作业编号

        Raises:
            JobLookupError: 作业不存在，建议返回404状态

        Returns:
            Job: 作业实例
        """

        job = self.scheduler.get_job(job_id)

        if not job:
            raise JobLookupError(f'Job {job_id} not found')

        return job

    def get_jobs(self) -> List[Job]:
        """Gets all scheduled jobs."""

        jobs = self.scheduler.get_jobs()

        job_states = []

        for job in jobs:
            job_states.append(job)

        return job_states

    def modify_job(self, job_id, **data) -> Job:
        """Updates a job.
        
        Raises:
            apscheduler.jobstores.base.JobLookupError 作业不存在，建议返回404状态
            Exception 其他任意可能的错误，建议返回500状态

        Returns:
            Job: 作业实例
        """
        self.scheduler.modify_job(job_id, **data)
        return self.scheduler.get_job(job_id)

    def pause_job(self, job_id) -> Job:
        """Pauses a job.
        
        Raises:
            apscheduler.jobstores.base.JobLookupError 作业不存在，建议返回404状态
            Exception 其他任意可能的错误，建议返回500状态

        Returns:
            Job: 作业实例
        """

        self.scheduler.pause_job(job_id)
        return self.scheduler.get_job(job_id)

    def resume_job(self, job_id) -> Job:
        """Resumes a job.
        
        Raises:
            apscheduler.jobstores.base.JobLookupError 作业不存在，建议返回404状态
            Exception 其他任意可能的错误，建议返回500状态

        Returns:
            Job: 作业实例
        """

        self.scheduler.resume_job(job_id)
        return self.scheduler.get_job(job_id)

    def run_job(self, job_id) -> Job:
        """Run the given job without scheduling it.
        
        Raises:
            apscheduler.jobstores.base.JobLookupError 作业不存在，建议返回404状态
            Exception 其他任意可能的错误，建议返回500状态

        Returns:
            Job: 作业实例
        """
        job: Job = self.scheduler.get_job(job_id)
        if not job:
            raise JobLookupError(id)

        job.func(*job.args, **job.kwargs)
        return job

    def job_to_dict(self, job: Job):
        """Converts a job to an OrderedDict."""

        data = OrderedDict()
        data['id'] = job.id
        data['name'] = job.name
        data['func'] = job.func_ref
        data['args'] = job.args
        data['kwargs'] = job.kwargs

        data.update(self.trigger_to_dict(job.trigger))

        if not job.pending:
            data['misfire_grace_time'] = job.misfire_grace_time
            data['max_instances'] = job.max_instances
            data['next_run_time'] = None if job.next_run_time is None else job.next_run_time

        return data

    def trigger_to_dict(self, trigger: BaseTrigger):
        """Converts a trigger to an OrderedDict."""

        data = OrderedDict()

        if isinstance(trigger, DateTrigger):
            data['trigger'] = 'date'
            data['run_date'] = trigger.run_date
        elif isinstance(trigger, IntervalTrigger):
            data['trigger'] = 'interval'
            data['start_date'] = trigger.start_date

            if trigger.end_date:
                data['end_date'] = trigger.end_date

            w, d, hh, mm, ss = self.extract_timedelta(trigger.interval)

            if w > 0:
                data['weeks'] = w
            if d > 0:
                data['days'] = d
            if hh > 0:
                data['hours'] = hh
            if mm > 0:
                data['minutes'] = mm
            if ss > 0:
                data['seconds'] = ss
        elif isinstance(trigger, CronTrigger):
            data['trigger'] = 'cron'

            if trigger.start_date:
                data['start_date'] = trigger.start_date

            if trigger.end_date:
                data['end_date'] = trigger.end_date

            for field in trigger.fields:
                if not field.is_default:
                    data[field.name] = str(field)
        else:
            data['trigger'] = str(trigger)

        return data

    def fix_job_def(self, job_def):
        """
        Replaces the datetime in string by datetime object.
        """
        if six.PY2 and isinstance(job_def.get('func'), six.text_type):
            # when a job comes from the endpoint, strings are unicode
            # because that's how json package deserialize the bytes.
            # we had a case where APScheduler failed to import the func based
            # on its name because Py2 expected a str and not unicode on __import__().
            # it happened only for a user, I wasn't able to determine why that occurred for him,
            # a workaround is to convert the func to str.

            # full story: https://github.com/viniciuschiele/flask-apscheduler/issues/75

            job_def['func'] = str(job_def.get('func'))

        if isinstance(job_def.get('start_date'), six.string_types):
            job_def['start_date'] = dateutil.parser.parse(job_def.get('start_date'))

        if isinstance(job_def.get('end_date'), six.string_types):
            job_def['end_date'] = dateutil.parser.parse(job_def.get('end_date'))

        if isinstance(job_def.get('run_date'), six.string_types):
            job_def['run_date'] = dateutil.parser.parse(job_def.get('run_date'))

        # it keeps compatibility backward
        if isinstance(job_def.get('trigger'), dict):
            trigger = job_def.pop('trigger')
            job_def['trigger'] = trigger.pop('type', 'date')
            job_def.update(trigger)

    def extract_timedelta(self, delta: timedelta):
        w, d = divmod(delta.days, 7)
        mm, ss = divmod(delta.seconds, 60)
        hh, mm = divmod(mm, 60)
        return w, d, hh, mm, ss
