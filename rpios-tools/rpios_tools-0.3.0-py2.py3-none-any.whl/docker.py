import argparse
from .utils import run


docker_tag = 'rpios-tools/imagebuilder:latest'
IMAGE_CACHE_VOLUME = 'raspios-image-cache-volume'

def build_docker(version: str, release: str):
    run(
        'docker', 'build', '--no-cache', '-t', docker_tag, '--build-arg', f'VERSION={version}', '--build-arg', f'RELEASE={release}', '.'
    )

def build_wheel():
    run(
        'rm', '-rf', 'dist/'
    )
    run(
        'python', 'setup.py', 'bdist_wheel', '--universal'
    )


def docker_volume():
    stdout, stderr, returncode = run(
        'docker', 'inspect', IMAGE_CACHE_VOLUME
    )
    if returncode == 1:
        run(
            'docker', 'volume', 'create', IMAGE_CACHE_VOLUME
        )


def run_docker():
    stdout, stderr, returncode = run(
        'docker', 'run', '--mount', f'source={IMAGE_CACHE_VOLUME},target=/images' '--privileged', docker_tag
    )
    print(stdout.decode('ascii'))
    print(stderr.decode('ascii'))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('version', type=str, help='raspios version')
    p.add_argument('release', type=str, help='raspios release')
    args = p.parse_args()

    print('packaging rpios_tools...')
    build_wheel()
    print('checking for image cache docker Volume...')
    docker_volume()
    print('building docker...')
    build_docker(args.version, args.release)
    print('running docker...')
    run_docker()



if __name__ == '__main__':
    main()