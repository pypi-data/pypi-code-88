"""
Response handler helpers for AWS API Gateway
"""
from json import dumps

from ckf_api_toolkit.tools.api_response_handler import ApiResponseFactory, Header
from ckf_api_toolkit.tools.logger import LogLevel, Logger


class AwsApiGatewayResponseFactory(ApiResponseFactory):
    """Factory class for creating API Gateway responses. Inherits ApiResponseFactory.

    Attributes:
        headers (dict): Headers dictionary for this response
    """

    headers: dict

    def __init__(self, *, return_trace=False):
        """Inits ApiResponseFactory with an empty body

        Keyword Args:
            return_trace (bool): include any exception traces in the API Response (default is False)
        """
        super(AwsApiGatewayResponseFactory, self).__init__(return_trace=return_trace)
        self.headers = {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Credentials": True,
        }

    def add_header(self, header: Header):
        """Add a header to the API Response

        Args:
            header (Header): Header object containing the key and value to add
        """
        self.headers[header.key] = header.value

    def get_response(self) -> dict:
        """Get the response from this factory instance

        Returns:
            (dict) The instance's response
        """
        Logger().log(
            LogLevel.debug,
            {
                'statusCode': self.status_code,
                'body': self.body_dict,
                'headers': self.headers,
            },
            title="API Response",
            pretty_json=True
        )

        return {
            'statusCode': self.status_code,
            'body': dumps(self.body_dict),
            'headers': self.headers
        }
