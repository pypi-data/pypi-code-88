import re
import sys
import uuid
import yaml


def gen_manifest(name, pod_name, image_name, version, saved_path, registry='docker-registry.default.svc.cluster.local:5000'):
    manifest = {
        'apiVersion': 'v1',
        'kind': 'Pod',
        'metadata': {
            'name': pod_name,
        },
        'spec': {
            'containers': [
                {
                    'name': image_name,
                    'image': 'gcr.io/kaniko-project/executor:latest',
                    'args': [
                        '--dockerfile=Dockerfile',
                        '--context={}'.format(saved_path),
                        '--context-sub-path={}'.format(name),
                        '--destination={}/{}:{}'.format(registry, image_name, version),
                        '--snapshotMode=redo',
                    ],
                    'volumeMounts': [
                        {
                            'name': 'kaniko-secret',
                            'mountPath': '/secret',
                        },
                    ],
                    'env': [
                        {
                            'name': 'GOOGLE_APPLICATION_CREDENTIALS',
                            'value': '/secret/kaniko-secret.json',
                        },
                        {
                            'name': 'AWS_ACCESS_KEY_ID',
                            'value': 'minio',
                        },
                        {
                            'name': 'AWS_SECRET_ACCESS_KEY',
                            'value': 'zIMPl2xty67P5KoaLczB',
                        },
                        {
                            'name': 'AWS_REGION',
                            'value': 'us-east-1',
                        },
                        {
                            'name': 'S3_ENDPOINT',
                            'value': 'http://minio.default.svc.cluster.local:9000',
                        },
                        {
                            'name': 'S3_FORCE_PATH_STYLE',
                            'value': 'true',
                        },
                    ],
                },
            ],
            'restartPolicy': 'Never',
            'volumes': [
                {
                    'name': 'kaniko-secret',
                    'secret': {
                        'secretName': 'kaniko-secret',
                    },
                },
            ],
        },
    }
    return yaml.dump(manifest)


def camel_to_kebab(name):
    out = re.sub(r'([a-z0-9]|(?=[A-Z]))([A-Z])', r'\1-\2', name)
    out = out.lower()
    if out[0] == '-':
        out = out[1:]
    return out


if __name__ == '__main__':
    bento = str(sys.argv[1])
    if ':' in bento:
        name, version = bento.split(':')
    else:
        name = bento
        version = 'latest'

    image_name = camel_to_kebab(name)
    uid = str(uuid.uuid4())[:5]
    pod_name = '{}-{}'.format(image_name, uid)

    if len(sys.argv) == 4:
        saved_path = str(sys.argv[2])
        registry = str(sys.argv[3])
        print(gen_manifest(name, pod_name, image_name, version, saved_path, registry))
    else:
        print(pod_name)
