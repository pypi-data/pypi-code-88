import pexpect
import json
import time
import os


def move_customer_ca_cert(count=0):
    exists = os.path.exists(os.path.join(os.getcwd(), 'customerCA.crt'))
    moved = os.path.exists('/opt/cloudhsm/etc/customerCA.crt')
    assert count < 5, 'Move customerCA.crt failed.'

    if exists is False and moved is True:
        return
    elif exists is False and moved is False:
        raise FileNotFoundError('customerCA.crt file not found.')
    elif exists is True and moved is True:
        os.remove(os.path.join(os.getcwd(), 'customerCA.crt'))
    elif exists is True and moved is False:
        (output, exitstatus) = pexpect.run(
            'sudo mv customerCA.crt /opt/cloudhsm/etc/customerCA.crt', withexitstatus=1)
        assert exitstatus == 0, 'sudo mv customerCA.crt /opt/cloudhsm/etc/customerCA.crt failed.'

    count += 1
    move_customer_ca_cert(count)


def configure_cloudhsm_mgmt_utility(eni_ip, count=0):
    hostname = _get_cmu_hostname()
    assert count < 5, "Configure CloudHSM Mgmt Utility failed."

    if hostname == eni_ip:
        return
    else:
        (output, exitstatus) = pexpect.run(
            f'sudo /opt/cloudhsm/bin/configure -a {eni_ip}', withexitstatus=1)
        assert exitstatus == 0, f'sudo /opt/cloudhsm/bin/configure -a {eni_ip} failed.'

    time.sleep(1)
    count += 1
    configure_cloudhsm_mgmt_utility(eni_ip, count)


def configure_cloudhsm_client(eni_ip, count=0):
    hostname = _get_cloudhsm_client_hostname()
    assert count < 5, 'Configure CloudHSM Client Failed'

    if hostname == eni_ip:
        return
    else:
        (output, exitstatus) = pexpect.run(
            'sudo service cloudhsm-client stop', withexitstatus=1)
        assert exitstatus == 0, 'sudo service cloudhsm-client stop failed.'
        (output, exitstatus) = pexpect.run(
            f'sudo /opt/cloudhsm/bin/configure -a {eni_ip}', withexitstatus=1)
        assert exitstatus == 0, f'sudo /opt/cloudhsm/bin/configure -a {eni_ip} failed.'

        (output, exitstatus) = pexpect.run(
            'sudo service cloudhsm-client start', withexitstatus=1)
        assert exitstatus == 0, 'sudo service cloudhsm-client start failed.'

        (output, exitstatus) = pexpect.run(
            'sudo /opt/cloudhsm/bin/configure -m', withexitstatus=1)
        assert exitstatus == 0, 'sudo /opt/cloudhsm/bin/configure -m failed.'

    time.sleep(1)
    count += 1
    configure_cloudhsm_client(eni_ip, count)


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


class FileNotFoundError(Exception):
    pass
