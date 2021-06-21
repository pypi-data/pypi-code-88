import os
import pathlib
from typing import Any, Dict, Optional, Type

from pydantic import SecretStr

from toucan_connectors import snowflake
from toucan_connectors.snowflake import (
    AuthenticationMethod,
    SnowflakeConnector,
    SnowflakeDataSource,
)
from toucan_connectors.toucan_connector import ConnectorSecretsForm

AUTHORIZATION_URL = (
    'https://toucantocopartner.west-europe.azure.snowflakecomputing.com/oauth/authorize'
)
SCOPE = 'refresh_token'
TOKEN_URL = 'https://toucantocopartner.west-europe.azure.snowflakecomputing.com/oauth/token-request'

from toucan_connectors.oauth2_connector.oauth2connector import (
    OAuth2Connector,
    OAuth2ConnectorConfig,
)


class DictCursor:
    pass


class SnowflakeoAuth2DataSource(SnowflakeDataSource):
    """Nothing reimplemented from inherited class"""


class SnowflakeoAuth2Connector(SnowflakeConnector):
    client_id: SecretStr
    client_secret: SecretStr
    auth_flow_id: Optional[str]
    _auth_flow = 'oauth2'
    user = 'ToucanToco'

    class Config:
        @staticmethod
        def schema_extra(schema: Dict[str, Any], model: Type['SnowflakeoAuth2Connector']) -> None:
            keys = schema['properties'].keys()
            hidden_keys = ['user', 'password', 'oauth_token', 'oauth_args']
            new_keys = [k for k in keys if k not in hidden_keys]
            schema['properties'] = {k: schema['properties'][k] for k in new_keys}

    def __init__(self, *args, **kwargs):
        super().__init__(
            **{k: v for k, v in kwargs.items() if k not in OAuth2Connector.init_params}
        )
        self.__dict__['_oauth2_connector'] = OAuth2Connector(
            auth_flow_id=self.auth_flow_id,
            authorization_url=AUTHORIZATION_URL,
            scope=SCOPE,
            token_url=TOKEN_URL,
            redirect_uri=kwargs['redirect_uri'],
            config=OAuth2ConnectorConfig(
                client_id=kwargs['client_id'],
                client_secret=kwargs['client_secret'],
            ),
            secrets_keeper=kwargs['secrets_keeper'],
        )

    @staticmethod
    def get_connector_secrets_form() -> ConnectorSecretsForm:
        return ConnectorSecretsForm(
            documentation_md=(pathlib.Path(os.path.dirname(__file__)) / 'doc.md').read_text(),
            secrets_schema=OAuth2ConnectorConfig.schema(),
        )

    def build_authorization_url(self, **kwargs):
        return self.__dict__['_oauth2_connector'].build_authorization_url(**kwargs)

    def retrieve_tokens(self, authorization_response: str):
        return self.__dict__['_oauth2_connector'].retrieve_tokens(authorization_response)

    def get_access_token(self):
        return self.__dict__['_oauth2_connector'].get_access_token()

    def connect(self) -> snowflake.connector.SnowflakeConnection:
        # This needs to be set before we connect
        snowflake.connector.paramstyle = 'qmark'
        connection_params = {
            'account': self.account,
            'authenticator': AuthenticationMethod.OAUTH,
            'application': 'ToucanToco',
            'token': self.get_access_token(),
        }
        return snowflake.connector.connect(**connection_params)
