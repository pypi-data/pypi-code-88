import json
import os
import time
import base64
import logging
from typing import Dict
import requests
from flask import Flask, request, Response, jsonify
from flask_cors import CORS

from biolib.biolib_binary_format import SavedJob
from biolib.compute_node.compute_process import compute_process_config
from biolib.compute_node.webserver import webserver_utils
from biolib.compute_node.webserver import webserver_config
from biolib.compute_node.webserver.gunicorn_flask_application import GunicornFlaskApplication
from biolib.biolib_logging import logger, TRACE

# Disable warning about using the "global" statement for the rest of this file
# pylint: disable=global-statement

# Global constants
DEV_MODE = os.getenv('COMPUTE_NODE_ENV') == 'dev'
BASE_URL = ''

# Only for enclaves
RUNNING_IN_ENCLAVE = False
COMPUTE_NODE_INFO = {}
ENCLAVE_ECR_TOKEN = ''

JOB_ID_TO_COMPUTE_STATE_DICT: Dict = {}
UNASSIGNED_COMPUTE_PROCESSES = []

app = Flask(__name__)
CORS(app)


def shutdown_after_response():
    logger.debug("Shutting down...")
    if not DEV_MODE:
        webserver_utils.deregister(BASE_URL, COMPUTE_NODE_INFO)
        webserver_utils.start_shutdown_timer('now')


@app.route('/hello/')
def hello():
    return 'Hello'


@app.route('/v1/job/', methods=['POST'])
def start_job():
    global JOB_ID_TO_COMPUTE_STATE_DICT, BASE_URL, ENCLAVE_ECR_TOKEN
    saved_job = json.loads(request.data.decode())

    if not webserver_utils.validate_saved_job(saved_job):
        return jsonify({'job': 'Invalid job'}), 400

    job_id = saved_job['job']['public_id']
    saved_job['BASE_URL'] = BASE_URL

    compute_state = webserver_utils.get_compute_state(UNASSIGNED_COMPUTE_PROCESSES)
    JOB_ID_TO_COMPUTE_STATE_DICT[job_id] = compute_state

    if RUNNING_IN_ENCLAVE:
        saved_job['enclave_ecr_token'] = ENCLAVE_ECR_TOKEN
        if not DEV_MODE:
            # Cancel the long general timer and replace with shorter shutdown timer
            webserver_utils.start_shutdown_timer(webserver_config.COMPUTE_NODE_RUNNING_JOB_SHUTDOWN_TIME_MINUTES)

    saved_job_bbf_package = SavedJob().serialize(json.dumps(saved_job))
    send_package_to_compute_process(job_id, saved_job_bbf_package)

    if RUNNING_IN_ENCLAVE:
        return Response(base64.b64encode(compute_state['attestation_document']), status=201)
    else:
        return '', 201


@app.route('/v1/job/<job_id>/start/', methods=['POST'])
def start_compute(job_id):
    module_input_package = request.data
    send_package_to_compute_process(job_id, module_input_package)
    return '', 201


@app.route('/v1/job/<job_id>/status/')
def status(job_id):
    # TODO Implement auth token
    global JOB_ID_TO_COMPUTE_STATE_DICT
    current_status = JOB_ID_TO_COMPUTE_STATE_DICT[job_id]['status'].copy()

    if current_status['status_updates']:
        JOB_ID_TO_COMPUTE_STATE_DICT[job_id]['status']['status_updates'] = []

    # Check if any error occured
    if 'error_code' in current_status:
        if RUNNING_IN_ENCLAVE:
            error_response = app.response_class(response=json.dumps(current_status),
                                                status=201,
                                                mimetype='application/json')
            error_response.call_on_close(shutdown_after_response)
            return error_response
        else:
            # Remove failed job
            JOB_ID_TO_COMPUTE_STATE_DICT.pop(job_id)

    return jsonify(current_status)


@app.route('/v1/job/<job_id>/result/')
def result(job_id):
    global JOB_ID_TO_COMPUTE_STATE_DICT
    if JOB_ID_TO_COMPUTE_STATE_DICT[job_id]['result']:
        result_data = JOB_ID_TO_COMPUTE_STATE_DICT[job_id]['result']
        result_response = Response(result_data)

        if RUNNING_IN_ENCLAVE:
            result_response.call_on_close(shutdown_after_response)
        else:
            # Remove finished job
            JOB_ID_TO_COMPUTE_STATE_DICT.pop(job_id)

        return result_response
    else:
        return '', 404


def send_package_to_compute_process(job_id, package_bytes):
    global JOB_ID_TO_COMPUTE_STATE_DICT
    message_queue = JOB_ID_TO_COMPUTE_STATE_DICT[job_id]['messages_to_send_queue']
    message_queue.put(package_bytes)


def start_webserver(port, host, specified_biolib_host, is_running_in_enclave=False):
    global RUNNING_IN_ENCLAVE, BASE_URL, UNASSIGNED_COMPUTE_PROCESSES, JOB_ID_TO_COMPUTE_STATE_DICT
    BASE_URL = specified_biolib_host

    if is_running_in_enclave:
        RUNNING_IN_ENCLAVE = True

    def worker_exit(server, worker):  # pylint: disable=unused-argument
        active_compute_states = list(JOB_ID_TO_COMPUTE_STATE_DICT.values()) + UNASSIGNED_COMPUTE_PROCESSES
        logger.info(f"Sending kill signal to {len(active_compute_states)} compute processes")
        if active_compute_states:
            for compute_state in active_compute_states:
                if compute_state['worker_thread']:
                    compute_state['worker_thread'].terminate()
            time.sleep(4)
        return

    def post_fork(server, worker):  # pylint: disable=unused-argument
        global UNASSIGNED_COMPUTE_PROCESSES, RUNNING_IN_ENCLAVE, COMPUTE_NODE_INFO, BASE_URL, \
            ENCLAVE_ECR_TOKEN, DEV_MODE
        logger.info("Started compute node")
        webserver_utils.start_compute_process(UNASSIGNED_COMPUTE_PROCESSES, RUNNING_IN_ENCLAVE)

        if RUNNING_IN_ENCLAVE:
            res = requests.get(f'{compute_process_config.PARENT_REST_SERVER_URL}/init_enclave/')
            enclave_data = res.json()
            COMPUTE_NODE_INFO = enclave_data['compute_node_info']
            BASE_URL = enclave_data['base_url']
            ENCLAVE_ECR_TOKEN = enclave_data['enclave_ecr_token']
            DEV_MODE = enclave_data['dev_mode']
            webserver_utils.report_availability(COMPUTE_NODE_INFO, BASE_URL, DEV_MODE)

    if logger.level == TRACE:
        gunicorn_log_level_name = 'DEBUG'
    elif logger.level == logging.DEBUG:
        gunicorn_log_level_name = 'INFO'
    else:
        gunicorn_log_level_name = logging.getLevelName(logger.level)

    options = {
        'bind': f'{host}:{port}',
        'workers': 1,
        'post_fork': post_fork,
        'worker_exit': worker_exit,
        'timeout': webserver_config.GUNICORN_REQUEST_TIMEOUT,
        'graceful_timeout': 4,
        'loglevel': gunicorn_log_level_name,
    }

    GunicornFlaskApplication(app, options).run()
