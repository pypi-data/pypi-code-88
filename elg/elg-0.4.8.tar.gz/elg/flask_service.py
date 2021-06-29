import inspect
import json
import re
from pathlib import Path
from posixpath import expanduser
from typing import Dict, List

from loguru import logger

try:
    import docker
    from flask import Flask
    from flask import request as flask_request
    from flask_json import JsonError, as_json
    from requests_toolbelt import MultipartDecoder
except:
    raise ImportError(
        "Extra dependencies need to be install to use the FlaskService class. Please run: `pip install elg[provider]`."
    )

from .model import AudioRequest, StructuredTextRequest, TextRequest
from .utils.docker import COPY_FOLDER, DOCKERFILE, ENTRYPOINT


class FlaskService:
    """
    Class to help the creation of an ELG compatible service from a python model.
    Extra dependencies need to be install to use the FlaskService class. Please run: `pip install elg[provider]`.
    """

    requirements = ["gunicorn", "elg[provider]"]

    def __init__(self, name: str):
        """
        Init function of the FlaskService

        Args:
            name (str): Name of the service. It doesn't have any importance.
        """
        self.name = name
        self.app = Flask(name)
        # Don't add an extra "status" property to JSON responses - this would break the API contract
        self.app.config["JSON_ADD_STATUS"] = False
        # Don't sort properties alphabetically in response JSON
        self.app.config["JSON_SORT_KEYS"] = False
        self.app.add_url_rule("/process", "process", self.process, methods=["POST"])

    def run(self):
        """
        Method to start the flask app.
        """
        self.app.run()

    @as_json
    def process(self):
        """
        Main request processing logic - accepts a JSON request and returns a JSON response.
        """
        logger.info("Process request")
        if "application/json" in flask_request.content_type:
            data = flask_request.get_json()
        elif "multipart/form-data" in flask_request.content_type:
            decoder = MultipartDecoder(flask_request.get_data(), flask_request.content_type)
            data = {}
            for part in decoder.parts:
                headers = {k.decode(): v.decode() for k, v in part.headers.items()}
                if "application/json" in headers["Content-Type"]:
                    for k, v in json.loads(part.content.decode()).items():
                        data[k] = v
                elif "audio" in headers["Content-Type"]:
                    data["content"] = part.content
                else:
                    raise ValueError("Unknown Content-Type in multipart request")
        else:
            raise ValueError()

        if data.get("type") == "audio":
            request = AudioRequest(**data)
        elif data.get("type") == "text":
            request = TextRequest(**data)
        elif data.get("type") == "structuredText":
            request = StructuredTextRequest(**data)
        else:
            self.invalid_request_error()
        logger.info(f"Call with the input: {request}")
        response = self.process_request(request)
        logger.info(f"Get response: {response}")
        response = {"response": response.dict(by_alias=True)}
        logger.info(f"Return: {response}")
        return response

    def invalid_request_error(self):
        """
        Generates a valid ELG "failure" response if the request cannot be parsed
        """
        raise JsonError(
            status_=400, failure={"errors": [{"code": "elg.request.invalid", "text": "Invalid request message"}]}
        )

    def process_request(self, request):
        """
        Method to process the request object. This method only calls the right process method regarding the type of the request.
        """
        if request.type == "text":
            return self.process_text(request)
        elif request.type == "structuredText":
            return self.process_structured_text(request)
        elif request.type == "audio":
            return self.process_audio(request)
        self.invalid_request_error()

    def process_text(self, request: TextRequest):
        """
        Method to implement if the service takes text as input.

        Args:
            request (TextRequest): TextRequest object.
        """
        raise NotImplementedError()

    def process_structured_text(self, request: StructuredTextRequest):
        """
        Method to implement if the service takes structured text as input.

        Args:
            request (StructuredTextRequest): StructuredTextRequest object.
        """
        raise NotImplementedError()

    def process_audio(self, request: AudioRequest):
        """
        Method to implement if the service takes audio as input.

        Args:
            request (AudioRequest): AudioRequest object.
        """
        raise NotImplementedError()

    @classmethod
    def create_requirements(cls, requirements: List = [], path: str = None):
        """
        Class method to create the correct requirements.txt file.

        Args:
            requirements (List, optional): List of required pip packages. Defaults to [].
            path (str, optional): Path where to generate the file. Defaults to None.
        """
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        requirements = cls.requirements + requirements
        with open(path.parent / "requirements.txt", "w") as f:
            f.write("\n".join(set(requirements)))

    @classmethod
    def create_docker_files(cls, required_files: List = [], required_folders: List = [], path: str = None):
        """Class method to create the correct Dockerfile.

        Args:
            required_files (List, optional): List of files needed for the service. Defaults to [].
            required_folders (List, optional): List of folders needed for the service. Defaults to [].
            path (str, optional): Path where to generate the file. Defaults to None.
        """
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        required_files = [path.name] + required_files
        required_folders = "\n".join(
            [COPY_FOLDER.format(folder_name=str(Path(folder))) for folder in required_folders]
        )
        service_script = path.name[:-3]  # to remove .py
        # The docker-entrypoint file is a Linux shell script so _must_ be
        # written with Unix-style line endings, even if the build is being done
        # on Windows.  To ensure this we write in binary mode.
        with open(path.parent / "docker-entrypoint.sh", "wb") as f:
            f.write(ENTRYPOINT.format(service_script=service_script).encode('utf-8'))
        with open(path.parent / "Dockerfile", "w") as f:
            f.write(DOCKERFILE.format(required_files=" ".join(required_files), required_folders=required_folders))

    @classmethod
    def docker_build_image(cls, tag: str, pull: bool = True, path: str = None, **kwargs):
        """
        Class method to do `docker build ...` in python.
        """
        if path == None:
            path = Path(inspect.getsourcefile(cls))
        else:
            path = Path(path)
        client = docker.from_env()
        image, _ = client.images.build(path=str(path.parent), tag=tag, pull=pull, **kwargs)
        return image

    @classmethod
    def docker_push_image(cls, repository: str, tag: str, username: str = None, password: str = None, **kwargs):
        """
        Class method to do `docker push ...` in python.
        """
        client = docker.from_env()
        if username is not None and password is not None:
            auth_config = {"username": username, "password": password}
            client.images.push(repository=repository, tag=tag, auth_config=auth_config, stream=True, **kwargs)
        client.images.push(repository=repository, tag=tag, stream=True, **kwargs)
        return

    @classmethod
    def docker_build_push_image(
        cls,
        repository: str,
        tag: str,
        pull: bool = True,
        username: str = None,
        password: str = None,
        build_kwargs: Dict = {},
        push_kwargs: Dict = {},
    ):
        cls.docker_build_image(tag=f"{repository}:{tag}", pull=pull, **build_kwargs)
        cls.docker_push_image(repository=repository, tag=tag, username=username, password=password, **push_kwargs)
        return None
