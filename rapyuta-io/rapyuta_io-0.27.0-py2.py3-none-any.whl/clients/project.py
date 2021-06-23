from __future__ import absolute_import
import re

import enum

from rapyuta_io.utils import RestClient, InvalidParameterException
from rapyuta_io.utils.object_converter import ObjBase, list_field
from rapyuta_io.utils.rest_client import HttpMethod
from rapyuta_io.utils.utils import create_auth_header, get_api_response_data

project_name_regex = re.compile('^[a-z0-9-]{3,15}$')


class Project(ObjBase):
    """
    Project is an organizational unit and all the resources must belong to a Project.

    :param guid: guid of the Project
    :type guid: str
    :param created_at: creation time of the Project
    :type created_at: str
    :param name: name of the Project
    :type name: str
    :param creator: GUID of the User that created the Project
    :type creator: str
    :param users: Users that have access to the Project
    :type users:   list(:py:class:`~rapyuta_io.clients.project.User`)
    """
    PROJECT_PATH = '/api/project'

    def __init__(self, name):
        self.validate(name)
        self.name = name
        self.guid = None
        self.created_at = None
        self.creator = None
        self.users = None

    def get_deserialize_map(self):
        return {
            'guid': 'guid',
            'created_at': 'CreatedAt',
            'name': 'name',
            'creator': 'creator',
            'users': list_field('users', User)
        }

    def get_serialize_map(self):
        return {
            'name': 'name'
        }

    @staticmethod
    def validate(name):
        if not isinstance(name, str):
            raise InvalidParameterException('name must be a string')
        length = len(name)
        if length < 3 or length > 15:
            raise InvalidParameterException('length of name must be between 3 and 15 characters')
        if not project_name_regex.match(name):
            raise InvalidParameterException('name can have alphabets, numbers or - only')

    def delete(self):
        if not (hasattr(self, '_core_api_host') and hasattr(self, '_auth_token')):
            raise InvalidParameterException('Project must be created first')
        url = self._core_api_host + self.PROJECT_PATH + '/delete'
        headers = create_auth_header(self._auth_token, self.guid)
        payload = {'guid': self.guid}
        response = RestClient(url).method(HttpMethod.DELETE).headers(headers).execute(payload)
        get_api_response_data(response, parse_full=True)


class User(ObjBase):
    """
    User is the representation of a Human user on the Platform. Users can be part of one of more Projects.

    :param guid: guid of the User
    :type guid: str
    :param first_name: First name of the User
    :type first_name: str
    :param last_name: Last name of the User
    :type last_name: str
    :param email_id: Email of the User
    :type email_id: str
    :param state: The state of the User on the Platform
    :type state: :py:class:`~rapyuta_io.clients.project.UserState`
    """
    def __init__(self, first_name, last_name, email_id, state='ACTIVATED', role='Admin'):
        self.guid = None
        self.first_name = first_name
        self.last_name = last_name
        self.email_id = email_id
        self.state = state
        self.role = role

    def get_deserialize_map(self):
        return {
            'guid': 'guid',
            'first_name': 'firstName',
            'last_name': 'lastName',
            'email_id': 'emailID',
            'state': 'state',
            'role': 'role'
        }

    def get_serialize_map(self):
        pass


class UserState(str, enum.Enum):
    """
    Enumeration variables for UserState.

    UserState can be any of the following types \n

    UserState.REGISTERED \n
    UserState.ACTIVATED \n
    UserState.DEACTIVATED \n
    UserState.SUSPENDED \n
    UserState.INVITED \n
    """
    REGISTERED = 'REGISTERED'
    ACTIVATED = 'ACTIVATED'
    DEACTIVATED = 'DEACTIVATED'
    SUSPENDED = 'SUSPENDED'
    INVITED = 'INVITED'
