import argparse
import json
import os
import pathlib
import uuid
from datetime import datetime, timedelta
from typing import Dict, List

import OpenSSL
import jwt
import pem
import requests
from PyInquirer import prompt

from utils import (
    encode_jwt,
    decode_jwt_claims_without_verification,
    decode_jwt_header_without_verification,
    generate_payload,
)

SIGNATURE_ALGORITHM = "PS512"


class FITConnectAuthClient(object):
    config: Dict[str, str] = None

    def __init__(self, config: Dict[str, str]):
        """
        creates a new Instance of FITConnectAuthClient
        :param config: config dictionary
        """
        self.config = config

    def get_oauth_token(self) -> Dict[str, str]:
        """
        retrieves a JWT token from the auth server
        :return: the response as json
        """
        headers = {
            "content-type": "application/x-www-form-urlencoded",
        }

        data = {
            "grant_type": "client_credentials",
            "client_id": self.config["client_id"],
            "client_secret": self.config["client_secret"],
        }

        response = requests.post(
            self.config["oauth_token_url"], headers=headers, data=data
        )

        return response.json()

    def get_jwt(self, destinations: List[str] = None) -> Dict[str, str]:
        """
        get one or multiple jwts based on config
        :param destinations: list of destinations the sender jwt should be for (optional)
        :return: the JWT tokens as dict
        """
        token = self.get_oauth_token()
        if self.config["client_type"] == "receiver":
            return {"token": token["access_token_jwt"]}
        elif self.config["client_type"] == "sender":
            if not destinations:
                raise Exception(
                    "For a sender there need to be at least one destination"
                )
            decoded_jwt = jwt.decode(
                token["access_token_jwt"], options={"verify_signature": False}
            )

            return {
                "online-service-token": token["access_token_jwt"],
                "token": self.generate_user_jwt(
                    decoded_jwt, self.config["private_key"], destinations
                ),
            }

    def generate_user_jwt(
        self,
        online_service_jwt: Dict[str, str],
        private_key: str,
        destinations: List[str],
    ):
        """generate the user token with limited scopes for an online service
        :param destinations: list of destination ids that should be added
        :param private_key: the private key used for signing
        :param online_service_jwt: the base jwt the user token should be derived from
        :returns: a jwt as string

        """
        now = datetime.utcnow()
        payload = generate_payload(
            "Onlineservice",
            now + timedelta(hours=2),
            domains=online_service_jwt["domains"],
            scope=[f"destination:{destination}" for destination in destinations],
        )
        payload["clientType"] = "user-sender"
        return encode_jwt(payload, SIGNATURE_ALGORITHM, private_key)



def generate_set(config: Dict[str, str]):
    """
    generate security event tokens for testing interactively (only supports one Event for now)
    :param config: the config dict
    :return: string with the set in it
    """
    questions = [
        {
            "type": "input",
            "name": "iss",
            "message": "Issuer:",
        },
        {
            "type": "input",
            "name": "sub",
            "message": "Subject:",
        },
        {
            "type": "input",
            "name": "events",
            "message": "Events:",
        },
        {
            "type": "input",
            "name": "txn",
            "message": "Transaction Identifier:",
        },
    ]

    answers = prompt(questions)
    answers["sub"] = {answers["sub"]: {}}
    answers["jti"] = str(uuid.uuid4())
    now = datetime.utcnow()
    payload = generate_payload(answers["iss"], now + timedelta(days=730),**answers)
    return encode_jwt(payload, SIGNATURE_ALGORITHM, config["private_key"], headers={"typ": "secevent+jwt"})



def generate_config(config_file_path: pathlib.Path):
    """generates a fitconnect config file
    :param config_file_path: the path to the config file that should be created
    """

    def validate_token_url(text):
        return (
            text.startswith(("http://", "https://"))
            or "URL must start with http:// or https://"
        )

    questions = [
        {
            "type": "list",
            "name": "client_type",
            "message": "Do you want to setup a config for a sender (e.g. onlineservice) or receiver?",
            "choices": ["sender", "receiver"],
        },
        {
            "type": "input",
            "name": "oauth_token_url",
            "message": "OAuth Token URL:",
            "validate": validate_token_url,
        },
        {
            "type": "input",
            "name": "client_id",
            "message": "Client id:",
        },
        {
            "type": "input",
            "name": "client_secret",
            "message": "Client secret:",
        },
    ]
    answers = prompt(questions)
    if answers["client_type"] == "sender":
        jwt_key_yes_no = prompt(
            [
                {
                    "type": "list",
                    "name": "choice",
                    "message": "Do you want to create a jwt signature key?",
                    "choices": ["yes", "no"],
                }
            ]
        )
        if jwt_key_yes_no["choice"] == "yes":
            key = OpenSSL.crypto.PKey()
            key.generate_key(OpenSSL.crypto.TYPE_RSA, 4096)
            answers["public_key"] = pem.parse(
                OpenSSL.crypto.dump_publickey(OpenSSL.crypto.FILETYPE_PEM, key)
            )[0].as_text()
            answers["private_key"] = pem.parse(
                OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, key)
            )[0].as_text()

            print(answers["public_key"])

    with config_file_path.open("w+") as config_file:
        config_file.write(json.dumps(answers))


def _decode_tokens(token_response):
    only_tokens = {k: v for k, v in token_response.items() if v.startswith("ey")}
    decoded_tokens = {}
    for token_name, token_value in only_tokens.items():
        decoded_tokens[
            f"_{token_name}_decoded_claims"
        ] = decode_jwt_claims_without_verification(token_value)
        decoded_tokens[
            f"_{token_name}_decoded_header"
        ] = decode_jwt_header_without_verification(token_value)
    return decoded_tokens


def main():
    os.environ["TZ"] = "UTC"

    parser = argparse.ArgumentParser(description="Generate jwt tokens.")
    task_choices = ["get_jwt", "create_config", "generate_set"]
    parser.add_argument(
        "task",
        metavar="task",
        help=f'one of {", ".join(task_choices)}',
        type=str,
        choices=task_choices,
    )
    parser.add_argument(
        "config",
        help="Configuration file to use",
        type=pathlib.Path,
    )
    parser.add_argument(
        "--decode",
        help="Decodes the token payload for you. For testing purposes only!",
        action="store_const",
        const=True,
        default=False,
    )
    parser.add_argument(
        "-d",
        "--destinations",
        nargs="+",
        default=[],
        help="Adds the destinations to an online service key.",
    )
    args = parser.parse_args()

    if args.task == "create_config":
        generate_config(args.config)
    elif args.task == "get_jwt":
        with args.config.open("r+") as config:
            config_dct = json.loads(config.read())
        fit_connect_auth = FITConnectAuthClient(config_dct)
        token_response: dict = fit_connect_auth.get_jwt(destinations=args.destinations)

        if args.decode:
            decoded_tokens = _decode_tokens(token_response)
            token_response = {**token_response, **decoded_tokens}

        print(json.dumps(token_response, sort_keys=True, indent=4))
    elif args.task == "generate_set":
        with args.config.open("r+") as config:
            config_dct = json.loads(config.read())
            token = generate_set(config_dct)
            if args.decode:
                decoded_token = decode_jwt_claims_without_verification(token)
                print(decoded_token)
            print(
                token
            )

if __name__ == "__main__":
    main()
