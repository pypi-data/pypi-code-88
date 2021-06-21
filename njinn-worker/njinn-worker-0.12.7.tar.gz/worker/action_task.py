from __future__ import annotations

"""
The action task takes care of
* Installing pack dependencies
* Running the action in a separate thread
* Cancelling the action if a SIGTERM is received
* Reporting the result of the action execution to the API
* Keeping action execution specific logs around until the result has been reported successfully
"""

import json
import logging
import os
import queue
import shutil
import signal
import stat
import subprocess
import sys
import traceback
from pathlib import Path

import backoff
import requests

# ensure imports keep working when invoked directly
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import threading
from datetime import datetime, timedelta
from logging.handlers import QueueHandler, QueueListener
from traceback import format_exc

# use absolute paths to be consistent & compatible bewteen worker code and the scripts
from worker.config import ActionExecutionConfig
from worker.packinstall import PackInstallation
from worker.postprocess import postproces_output
from worker.utils import (
    MAXIMUM_API_REQUEST_RETRY_DURATION_SECONDS,
    MAXIMUM_API_REQUEST_WAIT_TIME_SECONDS,
    ProcessTerminator,
    api_response_predicate,
    is_windows,
    read_stdout,
    report_action_result,
    setup_backoff_handler,
)

log = logging.getLogger(__name__)


@backoff.on_exception(
    backoff.expo,
    requests.exceptions.RequestException,
    max_value=MAXIMUM_API_REQUEST_WAIT_TIME_SECONDS,
    max_time=MAXIMUM_API_REQUEST_RETRY_DURATION_SECONDS,
)
@backoff.on_predicate(
    backoff.expo,
    api_response_predicate,
    max_value=MAXIMUM_API_REQUEST_WAIT_TIME_SECONDS,
    max_time=MAXIMUM_API_REQUEST_RETRY_DURATION_SECONDS,
)
def __try_pick(action_config):
    njinn_api = action_config.njinn_api
    data = {
        "context": action_config.action_context,
        "worker": njinn_api.config.worker_name,
    }

    picked_api = "/api/v1/workercom/picked"
    log.info(f"Calling {picked_api} with data {json.dumps(data)}")

    return njinn_api.put(picked_api, json=data)


def try_pick(action_config):
    """
    Try to pick the task, and return whether it should be executed.
    """

    r = __try_pick(action_config)
    if r.status_code == 409 or r.status_code == 404:
        log.info(f"Did not pick task due to response: {r.status_code} {r.text}")
        return False
    else:
        log.info(f"Picked task due to response: {r.status_code} {r.text}")
        return True


class TaskLogging:
    """Logs task specific output into a file that gets deleted
    after result was sent to the server.

    All file operations are done asynchronously to not block the worker
    in the unlikely but real edge case that file creation or writing blocks.
    """

    def __init__(self, action_config: ActionExecutionConfig):
        self.action_config = action_config
        task_log_dir = "./task_logs"
        os.makedirs(task_log_dir, exist_ok=True)
        self.logfile = os.path.join(
            task_log_dir,
            f"{action_config.execution_id}-{action_config.task_name}-{action_config.action_execution_id}.log",
        )
        logging_queue = queue.Queue()
        queue_handler = QueueHandler(logging_queue)
        root_logger = logging.getLogger()
        root_logger.setLevel(logging.DEBUG)
        root_logger.addHandler(queue_handler)
        sh = logging.StreamHandler()
        sh.setLevel(action_config.worker_config.log_level)
        sh.setFormatter(
            logging.Formatter(
                "[%(asctime)s %(levelname)s/ActionTask-%(thread)d] "
                + f"njinn_execute[{action_config.action_execution_id}]"
                + ": %(message)s"
            )
        )
        root_logger.addHandler(sh)
        setup_backoff_handler(handler=queue_handler)

        def setup_file_logging_in_thread():
            # manually set up logfile to be unicode
            # https://stackoverflow.com/questions/10706547/add-encoding-parameter-to-logging-basicconfig
            # python 3.9 has an encoding parameter in logging.basicConfig(),
            # but we support older versions as well
            file_handler = logging.FileHandler(self.logfile, "w", "utf-8")
            formatter = logging.Formatter("%(asctime)s %(message)s")
            file_handler.setFormatter(formatter)
            queue_listener = QueueListener(logging_queue, file_handler)
            queue_listener.start()

        threading.Thread(target=setup_file_logging_in_thread).start()

    def read_logfile(self) -> str:
        """
        Flushes logging and reads current content of logfile.
        """

        result = ["Reading logfile timed out."]

        def read_logfile_in_thread():
            try:
                for handler in log.handlers:
                    handler.flush()
                with open(self.logfile, "rt", encoding="utf-8") as f:
                    result[0] = f.read()
            except Exception as e:
                log.warning("Error reading log %s", e, exc_info=e)

        t = threading.Thread(target=read_logfile_in_thread)
        t.start()
        t.join(self.action_config.worker_config.log_file_timeout)
        return result[0]

    def delete_logfile(self) -> bool:
        is_success = [False]

        def delete_logfile_in_thread():
            logging.shutdown()
            if os.path.exists(self.logfile):
                os.remove(self.logfile)
            is_success[0] = True

        t = threading.Thread(target=delete_logfile_in_thread)
        t.start()
        t.join(self.action_config.worker_config.log_file_timeout)
        return is_success[0]


def success_result(output_file_content, action_config, pack_installation, output_lines):
    """
    Creates a result dict of a finished execution.

    Most of the output comes from the output file of the action, only stdout and
    variable postprocessing happens here.
    """
    stdout = "".join(output_lines)
    stdout_variables = postproces_output(stdout or "")
    # precedence for results from script, but don't overwrite with None
    stdout_variables.update(output_file_content.get("output", {}) or {})
    output_file_content["output"] = stdout_variables
    output_file_content["log"] = f"{pack_installation.status}\n{stdout}"
    log.debug("Result after timeout: %s", output_file_content)
    return output_file_content


def cancelled_result(action_config, pack_installation, output_lines):
    """
    Creates a result dict of an interrupted execution.

    The status is ERROR, and we don't have an output file to read, so
    we construct most of the result.
    """
    process_log = "".join(output_lines)
    stdout_variables = postproces_output(process_log or "")
    log.debug("Process stdout: %s", process_log)
    error = "Time limit reached. This may be due to a timeout or a cancel request."
    process_log = process_log or error
    output = stdout_variables.update({"error": error})
    result = {
        "state": "ERROR",
        "output": output,
        "log": f"{pack_installation.status}\n{process_log}",
        "state_info": error,
    }
    log.debug("Result after timeout: %s", result)
    return result


def error_result(error_log, pack_installation, task_logging):
    """
    Creates a result dict of a failed execution.

    The status is ERROR, and we don't have an output file to read, so
    we construct most of the result.
    
    If pack installation was not successful, the pack installation's outpout from the logfile is
    added to the regular stdout output..
    """
    if pack_installation.status is None:
        error = "Pack installation failed."
        error_log = f"Output during pack setup:\n{'-' * 20}\n{task_logging.read_logfile()}{'-' * 20}\n{error_log}"
    else:
        error = "Error during action execution."
        error_log = f"{pack_installation.status}\n{error_log}"
    output = postproces_output(error_log or "")
    output.update({"error": error})
    result = {
        "state": "ERROR",
        "output": output,
        "log": f"{error_log}",
        "state_info": error,
    }
    log.debug("Result on error: %s", result)
    return result


class ActionTask:
    def __init__(self, working_directory):
        self.working_directory = working_directory
        self.action_config = ActionExecutionConfig(self.working_directory).load()
        self.pack_installation = PackInstallation(
            self.action_config.pack, self.action_config.njinn_api
        )
        self.cancelled = False

    def run(self):
        try:
            task_logging = TaskLogging(self.action_config)

            pid_dir = Path(__file__).parent / "pids"
            pid_dir.mkdir(exist_ok=True)
            pidfile = pid_dir / f"{self.action_config.action_execution_id}.pid"

            if not is_windows():
                pidfile.write_text(f"{os.getpid()}\n")

            result = {}

            output_lines = []
            proc = None
        except Exception as e:
            result = {
                "state": "ERROR",
                "log": f"Worker error preparing action execution:\n{format_exc()}",
                "state_info": f"Worker error preparing action execution: {e}",
            }
            report_action_result(
                self.action_config.njinn_api, result, self.action_config.action_context
            )
            return
        if not try_pick(self.action_config):
            """
            API told us task was already executed
            """
            if not task_logging.delete_logfile():
                sys.exit(1)
            return
        try:

            self.pack_installation.setup()
            env = self.pack_installation.virtualenv_env()
            env["njinn_secrets_key"] = self.action_config.secrets_key

            cmd = [
                self.pack_installation.get_python(),
                "action.py",
                f"{self.working_directory}",
            ]
            log.info("Running %s", cmd)

            worker_codepage = self.action_config.worker_config.codepage
            # If `encoding` is None, the defaule value
            # will be used i.e. locale.getprefferedencoding(False)
            proc = subprocess.Popen(
                cmd,
                universal_newlines=True,
                stderr=subprocess.STDOUT,
                stdout=subprocess.PIPE,
                start_new_session=True,
                env=env,
                text=True,
                bufsize=1,
                encoding=worker_codepage,
                errors="replace",
            )

            process_terminator = ProcessTerminator()

            def signal_handler(sig, frame):
                # Don't do anything here that could cause exceptions, or prepare for
                # weird behavior:
                # https://anonbadger.wordpress.com/2018/12/15/python-signal-handlers-and-exceptions/
                self.cancelled = True

                process_terminator.terminate_then_kill(
                    proc,
                    datetime.now()
                    + timedelta(
                        seconds=self.action_config.worker_config.hard_kill_timeout
                    ),
                )
                # control flow will continue in read_stdout below, i.e. all
                # remaining output will be read.

            signal.signal(signal.SIGTERM, signal_handler)

            log.debug("Action process started.")
            read_stdout(proc, output_lines, process_terminator=process_terminator)
            log.debug("Action process finished.")

            if self.cancelled or proc.returncode == int(signal.SIGTERM):
                log.info("Calculating result after cancellation")
                result = cancelled_result(
                    self.action_config, self.pack_installation, output_lines
                )
            elif proc.returncode != 0:
                log.info("Return code %s", proc.returncode)
                stdout = "".join(output_lines)
                error_log = (
                    f"Return code from action execution {proc.returncode}.\n{stdout}"
                )
                result = error_result(error_log, self.pack_installation, task_logging)
            else:
                with open(
                    os.path.join(self.action_config.working_dir, "out.json")
                ) as output_file:
                    output_file_content = json.load(output_file)
                    log.info("Read output from file: %s", output_file_content)
                    result = success_result(
                        output_file_content,
                        self.action_config,
                        self.pack_installation,
                        output_lines,
                    )
        except Exception as e:
            if proc is not None:
                # only defined after pack installation
                read_stdout(proc, output_lines)
            log.error("Error while running process: %s", e)
            # read remaining lines
            stdout = "".join(output_lines)
            error_log = stdout + "\n" + str(e) + "\n" + traceback.format_exc()
            result = error_result(error_log, self.pack_installation, task_logging)
        finally:
            if result.setdefault("state", "ERROR") == "ERROR":
                result.setdefault("state_info", "Task interrupted.")
            response = report_action_result(
                self.action_config.njinn_api, result, self.action_config.action_context,
            )
            log.info("Removing working_dir %s", self.action_config.working_dir)

            def on_rm_error(func, path, exc_info):
                # path contains the path of the file that couldn't be removed
                # let's just assume that it's read-only and unlink it.
                os.chmod(path, stat.S_IWRITE)
                os.unlink(path)

            shutil.rmtree(self.action_config.working_dir, onerror=on_rm_error)

            if pidfile.exists():
                log.info("Pidfile %s exists, deleting", pidfile)
                pidfile.unlink()
            else:
                log.info("Pidfile %s does not exist", pidfile)
            if response.status_code == 200:
                # remove logfile on successful reporting of the result,
                # independend of whether the action was successful
                if not task_logging.delete_logfile():
                    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        log.error("Invalid call: action_task.py <working_directory>")
        sys.exit(1)
    ActionTask(sys.argv[1]).run()

