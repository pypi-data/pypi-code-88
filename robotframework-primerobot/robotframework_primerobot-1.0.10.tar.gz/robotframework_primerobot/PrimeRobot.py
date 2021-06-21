import os
from os.path import isfile, join
from typing import Any, Optional, Dict, List
import yaml
import pandas as pd
import boto3
import json
from datetime import datetime, timedelta
from gql import gql, Client, AIOHTTPTransport
from zipfile import ZipFile
import re
import traceback


class GraphQLClient:

    def __init__(self):
        transport = AIOHTTPTransport(
            url=os.environ.get(
                'GRAPHQL_URL', 'https://mqj2oaop3fdcplw5ev3vxsqewi.appsync-api.us-east-2.amazonaws.com/graphql'),
            headers={
                'X-Api-Key': os.environ.get('GRAPHQL_API_KEY', 'da2-7ym5pekywrbrrotak7hvlqq4vi')}
        )
        self.client = Client(
            transport=transport,
            fetch_schema_from_transport=True)

    def atualizar_task_progress(self,
                                id: str,
                                description: Optional[str] = None,
                                total: Optional[int] = None,
                                actual: Optional[int] = None,
                                completed: Optional[bool] = None,
                                error: Optional[str] = None,
                                success: Optional[str] = None,
                                stop: Optional[bool] = None) -> None:
        mutation = gql("""
            mutation updateTaskProgress($input: UpdateTaskProgressInput!) {
                updateTaskProgress(input: $input) {
                    id
                    description
                    total
                    actual
                    completed
                    custom_name
                    error
                    success
                    start_date
                    end_date
                    stop
                }
            }
        """)

        data = {
            'id': id,
            'description': description,
            'total': total,
            'actual': actual,
            'completed': completed,
            'error': error,
            'success': success,
            'stop': stop
        }
        copy_data = data.copy()
        for key in copy_data.keys():
            if data[key] is None:
                del data[key]

        if error or success:
            data['end_date'] = self.get_date_now_dynamo()
            data['completed'] = True
        else:
            print(data.get('description'))

        self.client.execute(mutation, variable_values={'input': data})

    def get_date_now_dynamo(self) -> str:
        dynamo_date_format = '%Y-%m-%dT%H:%M:%SZ'
        start_date = datetime.now() + timedelta(hours=3)
        start_date_string = start_date.strftime(dynamo_date_format)
        return start_date_string


class TaskProgressRepositorio:

    table: Any

    def __init__(self):
        dynamodb_client = boto3.resource('dynamodb')
        self.table = dynamodb_client.Table(
            os.getenv('DB_TASK_PROGRESS', 'task_progress_dev3'))

    def obter_por_id(self, task_id):
        response = self.table.get_item(
            Key={'id': task_id}
        )
        return response.get('Item')


class PrimeRobot:

    ROBOT_LISTENER_API_VERSION = 2
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    task_id: Optional[str] = os.getenv('TASK_ID')
    task_progress_repositorio: TaskProgressRepositorio
    task_progress: GraphQLClient
    s3_client: Any
    first_error = ''
    zips_output: Dict[str, List[str]] = {}

    def __init__(self):
        self.ROBOT_LIBRARY_LISTENER = self
        if self.is_aws():
            self.task_progress_repositorio = TaskProgressRepositorio()
            self.task_progress = GraphQLClient()
            self.s3_client = boto3.client('s3')

    def _start_test(self, name, attrs):
        if self.is_aws():
            self.task_progress.atualizar_task_progress(
                id=self.task_id,
                description=name
            )

    def _end_test(self, name, attrs):
        if 'FAIL' in attrs['status'] and not self.first_error:
            self.first_error = attrs['message']

    def _end_suite(self, name, attrs):
        if self.is_aws():
            if attrs['status'] == 'PASS':
                self.task_progress.atualizar_task_progress(
                    id=self.task_id,
                    success='Task finalizada com sucesso!!!'
                )
            else:
                self.task_progress.atualizar_task_progress(
                    id=self.task_id,
                    error=self.first_error
                )
        if len(self.zips_output.keys()) != 0:
            for zipdata in self.zips_output:
                if len(self.zips_output[zipdata]):
                    zipObj = ZipFile(zipdata, 'w')

                    for file in self.zips_output[zipdata]:
                        zipObj.write(f'output/{file}', file)

                    zipObj.close()
                    if self.is_aws():
                        self.s3_client.upload_file(zipdata, os.environ['BUCKET_RESULTADOS'],
                                                   f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/{zipdata}')

    def _close(self):
        for file in os.listdir('output'):
            full_path = join('output', file)
            if isfile(full_path):
                if self.is_aws():
                    self.s3_client.upload_file(
                        full_path, os.environ['BUCKET_RESULTADOS'], f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/{file}')

    def _obter_primerobot_content(self):
        with open("primerobot.yaml") as primerobotfile:
            content = primerobotfile.read()
            return yaml.load(content, Loader=yaml.FullLoader)

    def is_aws(self):
        return self.task_id is not None

    def obter_parametros(self):
        parameters_values = {}
        if self.is_aws():
            task_progress = self.task_progress_repositorio.obter_por_id(
                self.task_id)
            parameters_values = task_progress['parameters']
        else:
            primerobot_dict = self._obter_primerobot_content()

            parameters_values = {}
            if primerobot_dict['parameters'].get('data'):
                file_data = primerobot_dict['parameters']['data']
                if '.json' in file_data:
                    with open(file_data, 'rb') as jsonfile:
                        parameters_values = json.load(jsonfile)
            else:
                for parameter in primerobot_dict['parameters']:
                    if not parameters_values.get(parameter):
                        if primerobot_dict['parameters'][parameter]['type'] == 'array':
                            parameters_values[parameter] = []

                    file_data = primerobot_dict['parameters'][parameter].get(
                        'data')
                    if file_data:
                        if '.xlsx' in file_data:
                            dataframe = pd.read_excel(file_data)
                            for item, key in dataframe.iterrows():
                                value = str(key[parameter])
                                parameters_values[parameter].append(value)
                        elif '.json' in file_data:
                            with open(file_data, 'rb') as jsonfile:
                                parameters_values = json.load(jsonfile)
                        else:
                            print('Arquivo não implementado como input')

        return parameters_values

    def salvar_output(self, content, output: Optional[str] = None, save_as: Optional[str] = None):
        try:
            primerobot_dict = self._obter_primerobot_content()
            output_section = primerobot_dict.get('output')
            if output_section:
                if output_section.get('data'):
                    content.to_excel(output_section['data'], index=False)
                    if self.is_aws():
                        self.s3_client.upload_file(output_section['data'], os.environ['BUCKET_RESULTADOS'],
                                                   f'{os.environ["CLIENTE_ID"]}/{os.environ["TASK_ID"]}/{output_section["data"]}')
                else:
                    if output:
                        zip_file = output_section[output]['data']
                        self.zips_output[zip_file] = self.zips_output[zip_file] if self.zips_output.get(zip_file) else [
                        ]
                        index = len(self.zips_output[zip_file])
                        new_file = re.sub(
                            r"(\..*)", f"_{index}\\1", save_as if save_as else content["suggestedFilename"], 0, re.MULTILINE)
                        try:
                            os.remove(f'output/{new_file}')
                        except:
                            print('Arquivo ja existe')
                        os.rename(content['saveAs'], f'output/{new_file}')

                        self.zips_output[zip_file].append(new_file)
        except Exception as e:
            traceback.print_exc()
            raise Exception('Falha ao salvar output') from e
