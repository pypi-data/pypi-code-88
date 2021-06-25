import pexpect
import json
import time
import os


def move_customer_ca_cert(count=0):
    count += 1
    exists = os.path.exists(os.path.join(os.getcwd(), 'customerCA.crt'))
    moved = os.path.exists('/opt/cloudhsm/etc/customerCA.crt')

    if exists is False and moved is True:
        return True
    elif exists is False and moved is False:
        return False
    else:
        if count > 5:
            return False
        elif exists is True and moved is True:
            os.remove(os.path.join(os.getcwd(), 'customerCA.crt'))
            return move_customer_ca_cert(count=count)
        else:
            (output, exitstatus) = pexpect.run(
                'sudo mv customerCA.crt /opt/cloudhsm/etc/customerCA.crt', withexitstatus=1)
            return move_customer_ca_cert(count=count)


def configure_cloudhsm_mgmt_util(eni_ip):
    output, exitstatus = pexpect.run(
        f'sudo /opt/cloudhsm/bin/configure -a {eni_ip}', withexitstatus=1)
    assert exitstatus == 0

    return output


def configure_cloudhsm_client(eni_ip, count=0):
    count += 1
    hostname = _get_cloudhsm_client_hostname()
    if hostname == eni_ip:
        return True
    elif count < 6:
        (output, exitstatus) = pexpect.run(
            'sudo service cloudhsm-client stop', withexitstatus=1)
        (output, exitstatus) = pexpect.run(
            f'sudo /opt/cloudhsm/bin/configure -a {eni_ip}', withexitstatus=1)
        time.sleep(1)
        configure_cloudhsm_client(eni_ip, count)
    else:
        return False

        # (output, exitstatus) = pexpect.run(
        #     'sudo /opt/cloudhsm/bin/configure -m', withexitstatus=1)
        # assert exitstatus == 0, 'sudo /opt/cloudhsm/bin/configure -m failed.'


def start_cloudhsm_client(count=0):
    count += 1
    started = _is_cloudhsm_client_service_started()
    if started is True:
        return True
    elif count < 6:
        time.sleep(1)
        (output, exitstatus) = pexpect.run(
            'sudo service cloudhsm-client start', withexitstatus=1)
        start_cloudhsm_client(count=count)
    else:
        return False


def _is_cloudhsm_client_service_started():
    (output, exitstatus) = pexpect.run(
        'sudo service cloudhsm-client status -l', withexitstatus=1)
    responses = []
    for elem in output.decode().split('\r\n'):
        if 'Active' in elem:
            if 'running' in elem:
                return True
            else:
                return False

    raise CloudHSMClientStatusError(
        'Unable to determine the status of the CloudHSM Client')


def _get_cmu_hostname():
    with open('/opt/cloudhsm/etc/cloudhsm_mgmt_util.cfg', 'r') as file:
        cmu_data_json = file.read()
    cmu_data = json.loads(cmu_data_json)
    return cmu_data['servers'][0]['hostname']


def _get_cloudhsm_client_hostname():
    with open('/opt/cloudhsm/etc/cloudhsm_client.cfg', 'r') as file:
        client_data_json = file.read()
    client_data = json.loads(client_data_json)
    return client_data['server']['hostname']


class CloudHSMClientStatusError(Exception):
    pass


class DuplicateFileError(Exception):
    pass


class FileNotMovedError(Exception):
    pass
