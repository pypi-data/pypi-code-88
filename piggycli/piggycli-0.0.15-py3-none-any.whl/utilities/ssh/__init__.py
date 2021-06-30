import paramiko
from scp import SCPClient
import time
import os
import json


class SSH:
    def __init__(self, ip_address, ssh_key_file_path):
        self.ip_address = ip_address
        self.ssh_key_file_path = ssh_key_file_path

        self.username = 'ec2-user'
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.load_system_host_keys()

    def connect(self, retries=0):
        if retries > 3:
            return False
        interval = 5
        try:
            retries += 1
            self.client.connect(
                hostname=self.ip_address,
                username=self.username,
                key_filename=self.ssh_key_file_path
            )
            return True
        except Exception as e:
            print(e)
            time.sleep(interval)
            print('Retrying SSH connection to {}'.format(self.ip_address))
            self.connect(retries)

    def run(self, cmd):
        try:
            stdin, stdout, stderr = self.client.exec_command(cmd)
            output = stdout.read().decode()
            error = stderr.read().decode()
            return output, error
        except Exception as Error:
            raise Exception(Error.args[0])

    def put(self, file):
        try:
            with SCPClient(self.client.get_transport()) as scp:
                scp.put(file)
            return True
        except Exception as Error:
            raise Exception(Error.args[0])

    def get(self, file, local_path):
        try:
            with SCPClient(self.client.get_transport()) as scp:
                scp.get(file, local_path)

            return True
        except Exception as Error:
            raise Exception(Error.args[0])

    def close(self):
        try:
            self.client.close()
            return True
        except Exception as e:
            print(e)
            return False


def install_packages(ip_address, ssh_key_file_path):
    try:
        print('Installing Packages')
        ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
        ssh.connect()

        output, error = ssh.run('sudo yum update -y')

        ssh.put('app/utilities/ssh/install.sh')
        output, error = ssh.run('ls')
        assert bool(error) is False, error
        home_dir = output.split('\n')
        assert 'install.sh' in home_dir, 'install.sh was not uploaded'

        output, error = ssh.run('bash install.sh')

        output, error = ssh.run(
            'sudo yum list installed | grep -i cloudhsm-client')
        yum_list_grep = output.split()
        assert bool(yum_list_grep), 'cloudhsm-client was not installed.'

        output, error = ssh.run('rm cloudhsm-client-latest.el7.x86_64.rpm')
        assert bool(error) is False, error
        output, error = ssh.run('rm install.sh')
        assert bool(error) is False, error

        ssh.close()
        return
    except Exception as Error:
        raise Exception(Error.args[0])


def upload_file_to_instance(ip_address, ssh_key_file_path, file_path):
    try:
        ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
        ssh.connect()

        ssh.put(file_path)
        output, error = ssh.run('ls')
        assert bool(error) is False, error
        home_dir = output.split('\n')
        assert file_path.split(
            '/')[-1] in home_dir, f"{file_path.split('/')[-1]} was not uploaded."
        return

    except Exception as Error:
        raise Exception(Error.args[0])


def activate_cluster(
        ip_address, ssh_key_file_path, eni_ip, crypto_officer_username, crypto_officer_password, crypto_user_username, crypto_user_password):
    try:
        ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
        ssh.connect()
        output, error = ssh.run(
            f'script activate -eniip {eni_ip} -cousername {crypto_officer_username} -copassword {crypto_officer_password} -cuusername {crypto_user_username} -cupassword {crypto_user_password}')
        assert bool(error) is False, error
        return output

    except Exception as Error:
        raise Exception(Error.args[0])


def configure_cloudhsm_client(ip_address, ssh_key_file_path, hsm_ip_address):
    print('Configure CloudHSM-Client')
    try:
        ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
        ssh.connect()

        output, error = ssh.run(
            f'sudo /opt/cloudhsm/bin/configure -a {hsm_ip_address}')
        assert bool(error) is False, error

        ssh.get('/opt/cloudhsm/etc/cloudhsm_client.cfg')
        with open('cloudhsm_client.cfg') as file:
            data = file.read()
        cloudhsm_configure = json.loads(data)
        os.remove('cloudhsm_client.cfg')
        assert cloudhsm_configure['server']['hostname'] == hsm_ip_address, 'CloudHSM Client Configue Failed'

        ssh.close()
        return
    except Exception as Error:
        raise Exception(Error.args[0])


def gen_ecc_key_pair(ip_address, ssh_key_file_path, eni_ip, crypto_user_username, crypto_user_password, key_label):
    try:
        ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
        ssh.connect()
        output, error = ssh.run(
            f'script gen-ecc-key-pair -eniip {eni_ip} -username {crypto_user_username} -password {crypto_user_password} -label {key_label}')
        assert bool(error) is False, error
        ssh.close()

        return json.loads(output)

    except Exception as Error:
        raise Exception(Error.args[0])


def download_file_from_instance(ip_address, ssh_key_file_path, file, local_path):
    ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
    ssh.connect()
    resp = ssh.get(file=file, local_path=local_path)
    ssh.close()
    return


def sign_tx(ip_address, ssh_key_file_path, eni_ip, unsigned_tx_file, pub_key_handle, private_key_handle, crypto_user_username, crypto_user_password, count, cluster_path):

    ssh = SSH(ip_address=ip_address, ssh_key_file_path=ssh_key_file_path)
    ssh.connect()
    ssh.put(unsigned_tx_file['file_path'])

    cmds = [
        'script',
        'sign',
        '-eniip', eni_ip,
        '-username', crypto_user_username,
        '-password', crypto_user_password,
        '-tx', unsigned_tx_file['file_name'],
        '-vkhandle', pub_key_handle,
        '-skhandle', private_key_handle,
        '-count', str(count)
    ]
    output, error = ssh.run(' '.join(cmds))
    assert bool(error) is False, error

    signature_file_name = output.split()[0]
    assert signature_file_name == f"signedTx{count}.der"

    ssh.get(signature_file_name, cluster_path)

    output, error = ssh.run(f"rm {unsigned_tx_file['file_name']}")
    assert bool(error) is False, error

    output, error = ssh.run(f"rm {signature_file_name}")
    assert bool(error) is False, error

    ssh.close()

    return os.path.join(cluster_path, signature_file_name)
