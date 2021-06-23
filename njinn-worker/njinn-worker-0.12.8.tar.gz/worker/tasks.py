import os
import signal
import subprocess
import sys
import threading
from logging.handlers import QueueHandler, QueueListener
from multiprocessing import Process
from pathlib import Path
from queue import Queue
from time import sleep
from traceback import format_exc

from celery import exceptions
from celery.signals import after_setup_logger, after_setup_task_logger
from celery.utils.log import get_task_logger
from celery.worker.control import control_command, inspect_command

from worker import shared_logging

# use absolute paths to be consistent & compatible bewteen worker code and the scripts
from worker.api_client import NjinnAPI
from worker.celery_utils import get_celery_app
from worker.config import ActionExecutionConfig, WorkerConfig
from worker.utils import is_windows, report_action_result


@after_setup_logger.connect
def setup_loggers(logger, *args, **kwargs):
    async_handlers = []
    listeners = []
    for handler in logger.handlers:
        if isinstance(handler, QueueHandler):
            queue = Queue()
            async_handlers.append(QueueHandler(queue))
            listeners.append(QueueListener(queue, handler))
        else:
            async_handlers.append(handler)
    logger.handlers.clear()
    logger.handlers.extend(async_handlers)
    listener: QueueListener
    for listener in listeners:
        listener.start()

    logger.addHandler(shared_logging.shared_handler)


@after_setup_task_logger.connect
def setup_task_loggers(logger, *args, **kwargs):
    logger.addHandler(shared_logging.shared_handler)


config = WorkerConfig.initialize_from_default_location()
app = get_celery_app(config.messaging_url)
log = get_task_logger(__name__)
pid = os.getpid()


def njinn_execute_internal(action, pack, action_context):
    """Extracted to separate method for testing purposes only"""
    proc = None
    working_dir = None

    current_directory = None
    # do anything that can fail within try/catch for error reporting.
    try:
        current_directory = os.getcwd()
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)
        os.chdir(dname)

        dir_path = os.path.dirname(os.path.realpath(__file__))

        log.info("Njinn task initiating %s %s", pid, os.getpid())

        action_execution_id = action_context.get("action_execution_id")
        working_dir = os.path.join("working", action_execution_id)
        log.debug("Creating working directory %s", working_dir)
        os.makedirs(working_dir)

        ActionExecutionConfig(
            working_dir,
            config_path=os.path.abspath(config.config_path),
            action=action,
            pack=pack,
            action_context=action_context,
        ).save()

        # Run detached, without a shell, and start a new group
        py_cmd = sys.executable

        cmd = [
            py_cmd,
            "action_task.py",
            f"{working_dir}",
        ]

        log.info("Running: %s", cmd)
        env = os.environ.copy()
        env["njinn_secrets_key"] = config.secrets_key
        proc = subprocess.Popen(cmd, cwd=dir_path, start_new_session=True, env=env)
        proc.wait()
        log.info("Finished waiting, return code %s.", proc.returncode)
    except exceptions.SoftTimeLimitExceeded:
        log.info("Timeout")
        _cancel_action_execution(str(action_execution_id))
    except Exception as e:
        result = {
            "state": "ERROR",
            "log": f"Worker error launching action task:\n{format_exc()}",
            "state_info": f"Worker error launching action task: {e}",
        }
        report_action_result(config.njinn_api, result, action_context)
    finally:
        # Reset current directory
        # Otherwise causes weird behavior during tests, where files/directories get
        # created or deleted
        if current_directory is not None:
            os.chdir(current_directory)

    return None


@app.task(name="njinn_execute")
def njinn_execute(action, pack, action_context):
    njinn_execute_internal(action, pack, action_context)


@inspect_command(args=[("action_context", dict)])
def njinn_upload_action_execution_log(state, action_context):
    log.info("Uploading log for %s", action_context)
    task_log_dir = "./task_logs"
    logfile = os.path.join(
        task_log_dir,
        f"{action_context['execution_id']}-{action_context['task_name']}-{action_context['action_execution_id']}.log",
    )
    log_content = ["Reading log file timed out."]

    def read_logfile_in_thread():
        try:
            with open(logfile, "rt") as f:
                log_content[0] = f.read()
        except Exception as e:
            log_content[0] = f"Error reading log content: {e}"
            log.debug("Could not read: %s", logfile)

    t = threading.Thread(target=read_logfile_in_thread)
    t.start()
    t.join(config.log_file_timeout)
    report_action_result(
        NjinnAPI(config),
        {"log": log_content[0]},
        action_context,
        result_url="/api/v1/workercom/action_execution_log",
    )
    return {}


def _cancel_action_execution(action_execution_id: str):
    log.info("Cancel requested for %s.", action_execution_id)
    pid_dir = Path(__file__).parent / "pids"
    pidfile = pid_dir / f"{action_execution_id}.pid"
    if pidfile.exists():
        try:
            pid = int(float(pidfile.read_text().split("\n")[0]))
            log.info(
                "Terminating action process for %s with PID %s",
                action_execution_id,
                pid,
            )
            os.kill(pid, signal.SIGTERM)
        except FileNotFoundError:
            log.info("Not running anymore %s.", action_execution_id)
        except Exception as e:
            log.warning(
                "Error cancelling task %s: %s", action_execution_id, str(e), exc_info=e
            )
    else:
        log.info("Not running anymore %s.", action_execution_id)
    return {}


@control_command(args=[("action_execution_id", str)])
def njinn_cancel_action_execution(state, action_execution_id):
    _cancel_action_execution(action_execution_id)


@inspect_command()
def njinn_upload_worker_log(state):
    # ensure buffer isn't empty
    log.info("Worker log requested by server.")
    shared_logging.flush()
    return {}


@inspect_command(args=[("log_level", str)])
def njinn_set_log_level(state, log_level):
    log.info("Ignoring log level change to %s", log_level)
    # shared_logging.set_level(log_level)
    # log.debug("This is a debug message after log level change.")
    # log.info("This is a info message after log level change.")
    # log.warning("This is a warning message after log level change.")
    # log.error("This is a error message after log level change.")
    return {}


@inspect_command(
    args=[("action", str), ("pack", str), ("action_context", dict), ("timeout", int)],
)
def run_ad_hoc(state, action, pack, action_context, timeout):
    """
    Run `njinn_execute` in separate process and wait `timeout` seconds for a result.
    If the action execution is longer than `timeout` command return and
    forget about it (however it's still processed).
    """

    p = Process(target=njinn_execute, args=(action, pack, action_context))
    p.start()
    t = 0
    while t <= timeout:
        sleep_value = 0.1
        sleep(sleep_value)
        t += sleep_value
        if not p.is_alive():
            break

