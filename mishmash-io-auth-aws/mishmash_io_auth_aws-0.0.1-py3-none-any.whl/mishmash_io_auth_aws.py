# Copyright 2019 MISHMASH I O OOD
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import json
from datetime import datetime

import botocore
import boto3

class MishmashWrongCredentialsException(Exception):
    pass


class MishmashUnauthorizedException(Exception):
    pass


class MishmashAuth():

    def __init__(self, config_file_path=None):

        config_data = self.get_configuration()

        self.__aws_access_key_id = config_data["AWS_ACCESS_KEY_ID"]
        self.__aws_secret_access_key = config_data["AWS_SECRET_ACCESS_KEY"]

        self.__sts_connection = None
        self.__credentials = None

    def get_configuration(self):

        config_file_path = os.environ.get("AWS_CONFIG_FILE_PATH", None)

        if config_file_path:
            config_data = self.get_configuration_from_file(config_file_path)
        else:
            config_data = self.get_configuration_from_env()

        if not config_data:
            raise MishmashUnauthorizedException("set aws config variables")

        if not config_data["AWS_ACCESS_KEY_ID"]:
            raise MishmashUnauthorizedException(
                "please add AWS_ACCESS_KEY_ID as config variable")

        if not config_data["AWS_SECRET_ACCESS_KEY"]:
            raise MishmashUnauthorizedException(
                "please add AWS_SECRET_ACCESS_KEY as config variable")

        return config_data

    def get_configuration_from_file(self, config_file_path):
        try:
            with open(config_file_path, "r") as f:
                return json.load(f)

        except FileNotFoundError:
            return None

    def get_configuration_from_env(self):

        return {
            "AWS_ACCESS_KEY_ID": os.environ.get("AWS_ACCESS_KEY_ID", None),
            "AWS_SECRET_ACCESS_KEY": os.environ.get("AWS_SECRET_ACCESS_KEY", None),
        }

    def __get_aws_session_token(self):

        if not self.__sts_connection:
            self.__sts_connection = boto3.client('sts',
                                                 aws_access_key_id=self.__aws_access_key_id,
                                                 aws_secret_access_key=self.__aws_secret_access_key)
            

      
        try:
            token = self.__sts_connection.get_session_token()
        except botocore.exceptions.ClientError as e:

            if e.response['Error']['Code'] == "InvalidAccessKeyId" or \
                e.response['Error']['Code'] == "InvalidClientTokenId":
                error_message = 'AWS_ACCESS_KEY_ID'
            elif e.response['Error']['Code'] == "SignatureDoesNotMatch":
                error_message = 'Invalid AWS_SECRET_ACCESS_KEY'
            else:
                raise 

            raise MishmashWrongCredentialsException(error_message)
         
            
        if not token:
            raise MishmashUnauthorizedException("Cannot generate access token")
        
        return token

    def is_access_token_expired(self):
     
        if self.__credentials['Credentials']["Expiration"] <= \
            datetime.now().astimezone(self.__credentials['Credentials']["Expiration"].tzinfo):
            return True

        return False
        
    def get_or_create_access_token(self):
        """
            Check if access token is outdated and create new one if so
        """

        if not self.__credentials:
            self.__credentials = self.__get_aws_session_token()
            return self.__credentials['Credentials']['SessionToken']

        if self.is_access_token_expired():
            self.__credentials = self.__get_aws_session_token()
            return self.__credentials['Credentials']['SessionToken']

        return self.__credentials['Credentials']['SessionToken']

    @property
    def authorization_header(self):
        return f"{self.access_token}"

    @property
    def access_token(self):

        access_token = self.get_or_create_access_token()

        if not access_token:
            raise MishmashUnauthorizedException("invalid access token")

        return access_token

    @property
    def app_id(self):
        return self.__aws_access_key_id
