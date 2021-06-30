import subprocess
import json
from pathlib import Path


class Tf:
    def __init__(self, region, ssh_key_name, aws_access_key_id, aws_secret_access_key):
        self.region = region
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.ssh_key_name = ssh_key_name
        self.dir = Path(__file__).parent

    @property
    def cluster_id(self):
        return self.outputs['cluster_id']['value'] if self.outputs else None

    @property
    def vpc_id(self):
        return self.outputs['vpc_id']['value'] if self.outputs else None

    @property
    def ec2_instance_id(self):
        return self.outputs['ec2_instance_id']['value'] if self.outputs else None

    @property
    def outputs(self):
        with open('app/utilities/terraform/terraform.tfstate', 'r') as file:
            state = json.load(file)
        return state['outputs']

    def init(self):
        cmds = ['terraform', 'init']
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform initialization failed'
        return True

    def init_validate(self):
        cmds = ['terraform', 'init', '-var', 'backend=false']
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform initialization failed'
        return True

    def validate(self):
        self.init_validate()
        cmds = ['terraform', 'validate']
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform validation failed'
        self._clean_up()
        return True

    def build(self):
        self.init()
        cmds = self._add_vars(['terraform', 'apply', '-auto-approve'])
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform build failed'
        self._clean_up()
        return {'cluster_id': self.cluster_id, 'vpc_id': self.vpc_id, 'instance_id': self.ec2_instance_id}

    def destroy(self):
        self.init()
        cmds = self._add_vars(['terraform', 'destroy', '-auto-approve'])
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform destroy failed'
        self._clean_up()
        return True

    def _add_vars(self, cmds):
        vars = {"region": self.region, "ssh_key_name": self.ssh_key_name,
                "aws_access_key_id": self.aws_access_key_id, 'aws_secret_access_key': self.aws_secret_access_key}
        for var, value in vars.items():
            cmds.append('-var')
            cmds.append(f'{var}={value}')
        return cmds

    def _clean_up(self):
        cmds = ['rm', '-r', '.terraform']
        resp = subprocess.run(cmds, cwd=self.dir, capture_output=False)
        assert resp.returncode == 0, 'Terraform clean up failed'
        return True
