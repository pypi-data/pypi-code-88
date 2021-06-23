# Importing ascii is necessary for file open to work in some environments
import random
from queue import Queue
import platform
from encodings import ascii  # pylint: disable=redefined-builtin, unused-import
from pathlib import Path
import http.server
import asyncio
import base64
import logging
import os
import re
import shutil
import time
import signal
import socketserver
import subprocess
import sys
import tempfile
import threading
import shlex

# necessary for making RSA import work
from Crypto.IO import PEM  # pylint: disable=redefined-builtin, unused-import

import nest_asyncio  # necessary import fix required for async to work in notebooks
import yaml

from biolib import cli_utils
from biolib.nitro_enclave_utils import NitroEnclaveUtils
from biolib.biolib_binary_format import ModuleInput, ModuleOutput, RsaEncryptedAesPackage, AesEncryptedPackage
from biolib.pyppeteer.pyppeteer import launch, command
from biolib.pyppeteer.pyppeteer.launcher import resolveExecutablePath, __chromium_revision__
from biolib.compute_node.compute_process.compute_process import ComputeProcess
from biolib.biolib_api_client import BiolibApiClient
from biolib.biolib_docker_client import BiolibDockerClient
from biolib.compute_node.compute_process.biolib_container import BiolibContainer
from biolib.biolib_api_client.biolib_app_api import BiolibAppApi
from biolib.biolib_api_client.biolib_job_api import BiolibJobApi
from biolib.biolib_errors import BioLibError
from biolib.biolib_logging import logger, TRACE

if platform.system() != 'Windows':
    from biolib.compute_node.webserver import webserver

nest_asyncio.apply()

# specifically limit logs from pyppeteer
logging.getLogger('biolib.pyppeteer.pyppeteer').setLevel(logging.ERROR)
logging.getLogger('biolib.pyppeteer.pyppeteer.connection').setLevel(logging.ERROR)


class CompletedProcess:
    def __init__(self, stdout, stderr, exitcode):
        self.stdout = stdout
        self.stderr = stderr
        self.exitcode = exitcode

    def __str__(self):
        return cli_utils.get_pretty_print_module_output_string(self.stdout, self.stderr, self.exitcode)

    def ipython_markdown(self):
        from IPython.display import display, Markdown  # pylint: disable=import-error, import-outside-toplevel
        markdown_str = self.stdout.decode('utf-8')
        # prepend ./biolib_results/ to all paths
        # ie [SeqLogo](./SeqLogo2.png) test ![SeqLogo](./SeqLogo.png)
        # ![SeqLogo](SeqLogo.png)  ![SeqLogo](/SeqLogo.png)
        # is transformed to ![SeqLogo](./biolib_results/SeqLogo2.png) test ![SeqLogo](./biolib_results/SeqLogo.png)
        # ![SeqLogo](./biolib_results/SeqLogo.png)  ![SeqLogo](./biolib_results/SeqLogo.png)
        markdown_str_modified = re.sub(r'\!\[([^\]]*)\]\((\.\/|\/|)([^\)]*)\)',
                                       r'![\\1](./biolib_results/\\3)',
                                       markdown_str)
        display(Markdown(markdown_str_modified))


class BioLibServer(socketserver.TCPServer):
    log_level = logging.INFO


class BioLibHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):  # pylint: disable=redefined-builtin
        if self.server.log_level == TRACE:
            http.server.SimpleHTTPRequestHandler.log_message(self, format, *args)


def js_to_python_byte_array_converter(js_encoded):
    try:
        return bytes(list([js_encoded[str(i)] for i in range(len(js_encoded))]))
    except Exception as error:
        logger.error("Failed to decode response from browser")
        logger.error(error)
        logger.error(js_encoded)
        raise BioLibError(js_encoded) from error


def python_bytes_to_byte64(data):
    return base64.b64encode(data).decode('ascii')


class BioLib:
    executable_path = None
    no_sandbox = True
    auth_api_token = None
    host = 'https://biolib.com'

    @staticmethod
    def set_chrome_path(path):
        BioLib.executable_path = path

    @staticmethod
    def set_sandbox(use_sandbox):
        BioLib.no_sandbox = not use_sandbox

    @staticmethod
    def set_api_token(api_token):
        BioLib.auth_api_token = api_token

    @staticmethod
    def push(author_and_app_name, app_path):
        # prepare zip file
        if not Path(f'{app_path}/.biolib/config.yml').is_file():
            raise BioLibError('The file .biolib/config.yml was not found in the application directory')
        cwd = os.getcwd()
        temp_dir = tempfile.TemporaryDirectory()
        os.chdir(app_path)
        try:
            zip_path_without_file_extension = os.path.join(temp_dir.name, 'biolib-cli-build-tmp-zip')
            zip_path = f'{zip_path_without_file_extension}.zip'
            app_folder_name = Path(app_path).absolute().parts[-1]
            shutil.make_archive(zip_path_without_file_extension, 'zip', root_dir='..', base_dir=app_folder_name)
            zip_file = open(zip_path, 'rb')
            zip_binary = zip_file.read()
            zip_file.close()
        except Exception as error:
            raise Exception("Failed to create zip of application") from error
        finally:
            temp_dir.cleanup()
            # change back to old working directory
            os.chdir(cwd)

        # login and get app data
        BiolibApiClient.get().login(BioLib.auth_api_token, exit_on_failure=True)
        author, app_name = author_and_app_name.split('/')
        app = BiolibAppApi.fetch_by_name(author, app_name)
        # push new app version
        new_app_version_json = BiolibAppApi.push_app_version(
            app_id=app['public_id'],
            zip_binary=zip_binary,
            author=author,
            app_name=app_name,
            set_as_active=False
        )

        docker_tags = new_app_version_json.get('docker_tags', {})
        if docker_tags:
            logger.info('Found docker images to push.')

            try:
                yaml_file = open(f'{app_path}/.biolib/config.yml', 'r', encoding='utf-8')

            except Exception as error:  # pylint: disable=broad-except
                raise BioLibError('Could not open the config file .biolib/config.yml') from error

            try:
                config_data = yaml.safe_load(yaml_file)

            except Exception as error:  # pylint: disable=broad-except
                raise BioLibError('Could not parse .biolib/config.yml. Please make sure it is valid YAML') from error

            # Auth to be sent to proxy
            # The tokens are sent as "{access_token},{job_id}". We leave job_id blank on push.
            tokens = f'{BiolibApiClient.get().access_token},'
            auth_config = {'username': 'biolib', 'password': tokens}

            docker_client = BiolibDockerClient.get_docker_client()

            for module_name, repo_and_tag in docker_tags.items():
                docker_image_definition = config_data['modules'][module_name]['image']
                repo, tag = repo_and_tag.split(':')

                if docker_image_definition.startswith('dockerhub://'):
                    docker_image_name = docker_image_definition.replace('dockerhub://', 'docker.io/', 1)
                    logger.info(
                        f'Pulling image {docker_image_name} defined on module {module_name} from Dockerhub.')
                    dockerhub_repo, dockerhub_tag = docker_image_name.split(':')
                    docker_client.images.pull(dockerhub_repo, tag=dockerhub_tag)

                elif docker_image_definition.startswith('local-docker://'):
                    docker_image_name = docker_image_definition.replace('local-docker://', '', 1)

                try:
                    logger.info(f'Trying to push image {docker_image_name} defined on module {module_name}.')
                    image = docker_client.images.get(docker_image_name)
                    ecr_proxy_host = f'containers.{BioLib.host.split("://")[1]}/{repo}'
                    image.tag(ecr_proxy_host, tag)
                    for line in docker_client.images.push(ecr_proxy_host, tag=tag, stream=True,
                                                          decode=True, auth_config=auth_config):
                        logger.info(line)

                except Exception as exception:  # pylint: disable=broad-except
                    raise BioLibError(f'Failed to tag and push image {docker_image_name}.') from exception

                logger.info(f'Successfully pushed {docker_image_name}')

            logger.info('Successfully pushed all docker images')

        # Set new app version as active
        BiolibAppApi.update_app_version(
            app_version_id=new_app_version_json['public_id'],
            data={
                'set_as_active': True
            }
        )

    @staticmethod
    def start_compute_node(port, host, is_running_in_enclave=False):
        if platform.system() == 'Windows':
            raise BioLibError('Starting a compute node is currently not supported on Windows')
        webserver.start_webserver(
            port=port,
            host=host,
            specified_biolib_host=BioLib.host,
            is_running_in_enclave=is_running_in_enclave
        )

    @staticmethod
    def start_compute_process(socket_port, is_running_in_enclave):
        ComputeProcess(socket_port, is_running_in_enclave).run()
        # Kill the compute process which is the current process
        os.kill(os.getpid(), signal.SIGKILL)

    @staticmethod
    def run_local_docker_app(input_files, args, module, source_files_temp_dir):
        error_queue = Queue()
        biolib_container = BiolibContainer(is_running_in_enclave=False, messages_to_send_queue=error_queue)
        biolib_container.initialize_docker_container(
            image=module["image"],
            command=f'{module["command"]} {" ".join(args)}',
            working_dir=module['working_directory']
        )

        biolib_container.set_mappings(
            module['input_files_mappings'],
            module['source_files_mappings'],
            module['output_files_mappings'],
            args
        )

        try:
            if input_files:
                biolib_container.map_and_copy_input_files_to_container(input_files)
            if source_files_temp_dir:
                runtime_zip_data = open(f'{source_files_temp_dir.name}/biolib_run_dev.zip', 'rb').read()
                biolib_container.map_and_copy_runtime_files_to_container(runtime_zip_data, remove_root_folder=False)

            stdout, stderr, exit_code, mapped_output_files = biolib_container.run()
            cli_utils.write_output_files(mapped_output_files)
            print(cli_utils.get_pretty_print_module_output_string(stdout, stderr, exit_code))

        finally:
            biolib_container.cleanup()

    @staticmethod
    def get_pybiolib_root():
        # Use dirname() twice to get pybiolib/ as __file__ pybiolib/biolib/app.py
        return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @staticmethod
    def set_host(host):
        if host:
            BioLib.host = host
            BiolibApiClient.get().set_host(host)


# initialize API client
BiolibApiClient.initialize(BioLib.host)


class BioLibApp:
    app_author = None
    app_name = None

    def __init__(self, uri: str):
        account_handle, name, semantic_version = BioLibApp._parse_app_uri(uri)

        if semantic_version is not None:
            raise Exception('Loading specific version currently not supported')

        self.app_author = account_handle
        self.app_name = name
        self.app_version_public_id = None

    @staticmethod
    def _parse_app_uri(uri: str):

        uri_regex = r'((https:\/\/)?biolib\.com\/)?(?P<account>[\w-]+)\/(?P<name>[\w-]+)(\/version\/(?P<version>\d+\.\d+\.\d+)?)?(\/)?'  # pylint: disable=line-too-long

        matches = re.search(uri_regex, uri)

        if matches is None:
            raise Exception('Application URI was incorrectly formatted. Please use the format: account_handle/app_name')

        account_handle = matches.group('account')
        name = matches.group('name')
        semantic_version = matches.group('version')

        return account_handle, name, semantic_version

    def run_cloud_job(self, job_id, module_input):
        cloud_job = BiolibJobApi.create_cloud_job(module_name='main', job_id=job_id)
        logger.debug(f'Cloud: Job created with id {cloud_job["public_id"]}')
        node_url = cloud_job['compute_node_info']['url']
        attestation_document_bytes = base64.b64decode(cloud_job['compute_node_info']['attestation_document_base64'])
        expected_pcrs_and_aws_cert = BiolibJobApi.get_enclave_json(BioLib.host)

        rsa_public_key_der = NitroEnclaveUtils().attest_enclave_and_get_rsa_public_key(expected_pcrs_and_aws_cert,
                                                                                       attestation_document_bytes)
        serialized_data_to_send, aes_key_buffer = RsaEncryptedAesPackage().create(rsa_public_key_der, module_input)
        compute_result = self.compute_remote_job(
            job_id=job_id,
            compute_type='Cloud',
            serialized_data_to_send=serialized_data_to_send,
            node_url=node_url)
        seralized_module_output = AesEncryptedPackage(compute_result).decrypt(aes_key_buffer)
        module_output = ModuleOutput(seralized_module_output).deserialize()
        return module_output

    def run_local_compute_node_job(self, job, module_input):
        host = '127.0.0.1'
        port = str(random.choice(range(5000, 65000)))
        node_url = f'http://{host}:{port}'
        job_id = job['public_id']
        compute_node_process = subprocess.Popen(shlex.split(f'biolib start --host {host} --port {port}'))
        try:
            time.sleep(4)
            for retry in range(5):
                try:
                    BiolibJobApi.save_compute_node_job(
                        job=job,
                        module_name='main',
                        access_token=BiolibApiClient.get().access_token,
                        node_url=node_url
                    )
                    break

                except Exception as exception:  # pylint: disable=broad-except
                    if retry == 4:
                        raise BioLibError('Could not connect to local compute node') from exception
                    time.sleep(0.5)

            compute_result = self.compute_remote_job(
                job_id=job_id,
                compute_type='Compute Node',
                serialized_data_to_send=module_input,
                node_url=node_url
            )

            module_output = ModuleOutput(compute_result).deserialize()
            return module_output

        finally:
            compute_node_process.terminate()

    def compute_remote_job(self, job_id, compute_type, serialized_data_to_send, node_url):
        BiolibJobApi.start_cloud_job(job_id, serialized_data_to_send, node_url)
        BiolibJobApi.await_compute_node_status(
            retry_interval_seconds=1.5,
            retry_limit_minutes=30,
            status_to_await='Result Ready',
            compute_type=compute_type,
            job_id=job_id,
            node_url=node_url
        )

        result = BiolibJobApi.get_cloud_result(job_id, node_url)
        return result

    async def call_pyppeteer(self, port, args, stdin, files):
        if not BioLib.executable_path:
            mac_chrome_path = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
            if os.path.isfile(mac_chrome_path):
                BioLib.set_chrome_path(mac_chrome_path)

        if not BioLib.executable_path:
            linux_chrome_path = '/usr/lib/chromium-browser/chromium-browser'

            # special install for google colab
            if not os.path.isfile(linux_chrome_path) and 'google.colab' in sys.modules:
                subprocess.run('apt-get update', shell=True, check=True)
                subprocess.run('apt install chromium-chromedriver', shell=True, check=True)

            if os.path.isfile(linux_chrome_path):
                BioLib.set_chrome_path(linux_chrome_path)

        resolved_path = resolveExecutablePath(None, __chromium_revision__)
        if not BioLib.executable_path and resolved_path[1]:
            # if executable_path is not set explicit,
            # and resolveExecutablePath failed (== we got an error message back in resolved_path[1])
            logging.info('Installing dependencies...')
            os.environ['PYPPETEER_NO_PROGRESS_BAR'] = 'true'
            command.install()

        logging.info('Computing...')

        chrome_arguments = [
            '--disable-web-security',
        ]
        if BioLib.no_sandbox:
            chrome_arguments.append('--no-sandbox')

        browser = await launch(args=chrome_arguments, executablePath=BioLib.executable_path)

        # start new page
        page = await browser.newPage()

        await page.goto('http://localhost:' + str(port))

        def get_data():
            input_serialized = ModuleInput().serialize(stdin, args, files)
            return python_bytes_to_byte64(input_serialized)

        def set_progress_compute(value):
            logger.debug(f'Compute progress: {value}')

        def set_progress_initialization(value):
            logger.debug(f'Initialization progress: {value}')

        def add_log_message(value):
            logger.debug(f'Log message: {value}')

        await page.exposeFunction('getData', get_data)
        await page.exposeFunction('setProgressCompute', set_progress_compute)
        await page.exposeFunction('setProgressInitialization', set_progress_initialization)
        await page.exposeFunction('addLogMessage', add_log_message)

        refresh_token = 'undefined'
        if BiolibApiClient.get().refresh_token:
            refresh_token = f'\'{BiolibApiClient.get().refresh_token}\''

        output_serialized_js_bytes = await page.evaluate('''
        async function() {
          const refreshToken = ''' + refresh_token + ''';
          const appVersionId = \'''' + self.app_version_public_id + '''\';
          const baseUrl = \'''' + BioLib.host + '''\';

          const { BioLibSingleton, AppClient } = window.BioLib;
          BioLibSingleton.setConfig({ baseUrl, refreshToken });
          AppClient.setApiClient(BioLibSingleton.get());

          const inputBase64 = await window.getData();
          const inputByteArray = Uint8Array.from(atob(inputBase64), c => c.charCodeAt(0));

          const jobUtils = {
              setProgressCompute: window.setProgressCompute,
              setProgressInitialization: window.setProgressInitialization,
              addLogMessage: window.addLogMessage,
          };

          try {
            const moduleOutput = await AppClient.runAppVersion(appVersionId, inputByteArray, jobUtils);
            return moduleOutput.serialize();
          } catch(err) {
            return err.toString();
          }
        }
        ''')
        logging.debug('Closing browser')
        await browser.close()

        output_serialized = js_to_python_byte_array_converter(output_serialized_js_bytes)
        module_output = ModuleOutput(output_serialized).deserialize()

        if isinstance(module_output, dict):
            return module_output
        else:
            raise BioLibError(module_output)

    def __call__(self, args=None, stdin=None, files=None, output_path='biolib_results'):
        try:
            if args is None:
                args = []
            BiolibApiClient.get().login(BioLib.auth_api_token)
            logging.info('Loading package...')
            app = BiolibAppApi.fetch_by_name(self.app_author, self.app_name)
            active_version = app['active_version']
            self.app_version_public_id = active_version['public_id']

            logging.info(f'Loaded package: {self.app_author}/{self.app_name}')

            cwd = os.getcwd()

            if stdin is None:
                stdin = b''

            if not output_path.startswith('/'):
                # output_path is relative, make absolute
                output_path = f'{cwd}/{output_path}'

            if isinstance(args, str):
                args = list(filter(lambda p: p != '', args.split(' ')))

            if not isinstance(args, list):
                raise Exception('The given input arguments must be list or str')

            if isinstance(stdin, str):
                stdin = stdin.encode('utf-8')

            if files is None:
                files = []
                for idx, arg in enumerate(args):
                    if os.path.isfile(arg):
                        files.append(arg)
                        args[idx] = arg.split('/')[-1]

            files_dict = {}

            for file in files:
                path = file
                if not file.startswith('/'):
                    # make path absolute
                    path = cwd + '/' + file

                arg_split = path.split('/')
                file = open(path, 'rb')
                path = '/' + arg_split[-1]

                files_dict[path] = file.read()
                file.close()

            # Start Job
            job = BiolibJobApi.create(self.app_version_public_id)

            run_job_in_a_compute_node = False
            if not 'modules' in job['app_version']:
                run_job_in_a_compute_node = True
            else:
                for module in job['app_version']['modules']:
                    run_job_in_a_compute_node = True if module['name'] == 'main' \
                                                        and module['environment'] == 'biolib-ecr' else False

            if run_job_in_a_compute_node:
                module_input = ModuleInput().serialize(stdin=b'', arguments=args, files=files_dict)
                # Run job locally if app allows client side execution and docker is running.
                if app['allow_client_side_execution'] and BiolibDockerClient.is_docker_running() \
                        and platform.system() != 'Windows':
                    module_output = self.run_local_compute_node_job(job, module_input)
                else:
                    module_output = self.run_cloud_job(job['public_id'], module_input)

            else:
                BioLibServer.log_level = logger.level
                with BioLibServer(('127.0.0.1', 0), BioLibHandler) as httpd:
                    port = httpd.server_address[1]
                    thread = threading.Thread(target=httpd.serve_forever)
                    # TODO: figure out how we can avoid changing the current directory
                    os.chdir(os.path.dirname(os.path.realpath(__file__)) + '/biolib-js/')
                    try:
                        thread.start()
                        module_output = asyncio.get_event_loop().run_until_complete(
                            self.call_pyppeteer(port=port, args=args, stdin=stdin, files=files_dict))
                    finally:
                        os.chdir(cwd)
                        httpd.shutdown()
                        thread.join()

            cli_utils.write_output_files(
                mapped_output_files=module_output['files']
            )

            return CompletedProcess(module_output['stdout'], module_output['stderr'], module_output['exit_code'])

        except BioLibError as exception:
            logger.error('An error has occurred')
            logger.error(exception.message)
            raise exception

        except Exception as exception:
            raise exception
