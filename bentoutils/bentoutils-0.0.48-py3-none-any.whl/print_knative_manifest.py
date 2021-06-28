import os
import re
import sys
import yaml


def gen_manifest(pod_name, version, registry='registry.devsheds.io'):
    envvars = read_env_variables()
    manifest = {
        'apiVersion': 'serving.knative.dev/v1',
        'kind': 'Service',
        'metadata': {
            'name': pod_name,
            'namespace': 'default',
        },
        'spec': {
            'template': {
                'spec': {
                    'containers': [
                        {
                            'image': '{}/{}:{}'.format(registry, pod_name, version),
                            'args': [
                                '--workers=1',
                                '--timeout=1000000000'
                            ],
                            'env': [{'name': key, 'value': val} for key, val in envvars.items()],
                            'ports': [
                                {
                                    'containerPort': 5000,
                                },
                            ],
                            # big models are taking a long time to start
                            # 'livenessProbe': {
                            #     'httpGet': {
                            #         'path': '/healthz',
                            #     },
                            #     'initialDelaySeconds': 3,
                            #     'periodSeconds': 5,
                            # },
                            # 'readinessProbe': {
                            #     'httpGet': {
                            #         'path': '/healthz',
                            #     },
                            #     'initialDelaySeconds': 3,
                            #     'periodSeconds': 5,
                            #     'failureThreshold': 3,
                            #     'timeoutSeconds': 60,
                            # },
                        },
                    ],
                },
            },
        },
    }
    if envvars.get('GPU_ENABLED', None) == 'true':
        manifest['spec']['template']['spec']['containers'][0]['resources'] = {
            'limits': {
                'nvidia.com/gpu': 1
            }
        }

    replicas = int(envvars.get('MIN_REPLICAS', '0'))
    if replicas > 0:
        manifest['spec']['template']['metadata'] = {
            'annotations': {
                'autoscaling.knative.dev/minScale': str(replicas)
            }
        }

    return yaml.dump(manifest)


def camel_to_kebab(name):
    out = re.sub(r'([a-z0-9]|(?=[A-Z]))([A-Z])', r'\1-\2', name)
    out = out.lower()
    if out[0] == '-':
        out = out[1:]
    return out


def read_env_variables():
    envvars = {}
    if not os.path.exists('.env'):
        return envvars

    with open('.env', 'r') as f:
        for line in f:
            key, val = line.split('=')
            envvars[key] = val.strip()

    return envvars


if __name__ == '__main__':
    bento = str(sys.argv[1])
    if ':' in bento:
        name, version = bento.split(':')
    else:
        name = bento
        version = 'latest'

    if len(sys.argv) == 4:
        pod_name = str(sys.argv[2])
        registry = str(sys.argv[3])
        print(gen_manifest(pod_name, version, registry))

    else:
        print('Error: insufficient args')
