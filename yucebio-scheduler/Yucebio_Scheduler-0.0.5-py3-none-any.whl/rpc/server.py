"""
This is an example showing how to make the scheduler into a remotely accessible service.
It uses RPyC to set up a service through which the scheduler can be made to add, modify and remove
jobs.

To run, first install RPyC using pip. Then change the working directory to the ``rpc`` directory
and run it with ``python -m server``.


"""
import click
import rpyc
from rpyc.utils.server import ThreadedServer
from yucebio_scheduler.scheduler import YucebioScheduler
from yucebio_scheduler.utils import job_to_dict


class SchedulerService(rpyc.Service):
    def __init__(self, prefix: str, uri: str) -> None:
        super().__init__()

        ycScheduler = YucebioScheduler(prefix = prefix, uri = uri)
        self.scheduler = ycScheduler.create_scheduler()
        self.scheduler.start()

    # def on_connect(self, conn):
        # return super().on_connect(conn)

    # def on_disconnect(self, conn):
        # self.scheduler.shutdown()
        # return super().on_disconnect(conn)

    def exposed_add_job(self, **kwargs):
        """
        add_job(func, trigger=None, args=None, kwargs=None, id=None, \
            name=None, misfire_grace_time=undefined, coalesce=undefined, \
            max_instances=undefined, next_run_time=undefined, \
            jobstore='default', executor='default', \
            replace_existing=False, **trigger_args)
        """
        return self.scheduler.add_job(**kwargs)

    def exposed_modify_job(self, job_id, jobstore=None, **changes):
        return self.scheduler.modify_job(job_id, jobstore, **changes)

    def exposed_reschedule_job(self, job_id, jobstore=None, trigger=None, **trigger_args):
        return self.scheduler.reschedule_job(job_id, jobstore, trigger, **trigger_args)

    def exposed_pause_job(self, job_id, jobstore=None):
        job = self.scheduler.pause_job(job_id, jobstore)
        return job_to_dict(job)

    def exposed_resume_job(self, job_id, jobstore=None):
        job = self.scheduler.resume_job(job_id, jobstore)
        return job_to_dict(job)

    def exposed_remove_job(self, job_id, jobstore=None):
        self.scheduler.remove_job(job_id, jobstore)

    def exposed_get_job(self, job_id):
        return job_to_dict(self.scheduler.get_job(job_id))

    def exposed_get_jobs(self, jobstore=None):
        return [job_to_dict(job) for job in self.scheduler.get_jobs(jobstore)]


def create_server(port: int, uri: str):
    protocol_config = {'allow_public_attrs': True}
    schedulerserver = SchedulerService(f'scheduler_{port}', uri)
    server = ThreadedServer(schedulerserver, port=port, protocol_config=protocol_config)
    try:
        click.secho(f'server start on localhost:{port} ...', fg='yellow')
        server.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    finally:
        schedulerserver.scheduler.shutdown()

def connect_server(port: int, host: str='localhost') -> SchedulerService:
    conn = rpyc.connect(host=host, port=port)
    return conn.root

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) < 3:
        raise RuntimeError("参数错误，请提供端口号和jobstore地址")
    create_server(*sys.argv[1:])

