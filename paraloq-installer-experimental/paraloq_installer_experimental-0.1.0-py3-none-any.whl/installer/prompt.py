import re
import os
import sys
import json
from typing import Dict, Union

from rich.prompt import PromptBase, PromptType, InvalidResponse, Confirm
import pydantic

from paraloq.core.logging import start_logging

log = start_logging(__name__)


class RegexPrompt(PromptBase[str]):
    def __init__(self, prompt, *, regex: str = None, **kwargs):
        super(RegexPrompt, self).__init__(prompt, **kwargs)
        self.regex = regex

    def check_regex(self, value: str) -> bool:
        return bool(re.match(self.regex, value))

    def process_response(self, value: str) -> PromptType:
        response = super(RegexPrompt, self).process_response(value)
        if self.regex is not None and not self.check_regex(value):
            raise InvalidResponse(
                f"This value must match the following regex: \n {self.regex}"
            )
        return response

    @classmethod
    def ask(cls, prompt, **kwargs):
        return cls(prompt=prompt, **kwargs)()


class ParaloqConfig(pydantic.BaseModel):
    """Representation of the paraloq configuration file. Implements checking the access
    permissions for the file to stay save. Note that the file stores credentials in plain text."""

    login_url_host: pydantic.HttpUrl
    api_url: pydantic.HttpUrl
    client_id: str
    region: str = None
    cached_bearer: Dict[str, Union[float, str]] = pydantic.Field(default_factory=dict)

    @classmethod
    def _from_prompt(cls) -> "ParaloqConfig":
        login_url_host = RegexPrompt.ask("Please enter your login url")
        client_id = RegexPrompt.ask("Please enter your client id")
        api_url = RegexPrompt.ask("Please enter your paraloq API URL")

        region = login_url_host.split(".")[2]

        return cls(
            login_url_host=login_url_host,
            client_id=client_id,
            api_url=api_url,
            region=region,
        )

    @property
    def login_url(self) -> pydantic.HttpUrl:
        return pydantic.parse_obj_as(
            pydantic.HttpUrl,
            f"{self.login_url_host}/login?client_id={self.client_id}&"
            f"response_type=code&"
            f"scope=openid+aws.cognito.signin.user.admin&"
            f"redirect_uri=http://localhost:8085/",
        )

    @staticmethod
    def _pq_path() -> str:
        return os.path.join(os.path.expanduser("~"), ".paraloq")

    @classmethod
    def _initiate(cls) -> "ParaloqConfig":
        config = cls._from_prompt()
        config.commit()
        return config

    @classmethod
    def _set_permission(cls, access: str):
        if sys.platform.startswith("win"):
            cls._win_set_permission(access=access)
        else:
            cls._unix_set_permission(access=access)

    @classmethod
    def _unix_set_permission(cls, access: str):
        if access == "read":
            permission = 0o400
        elif access == "write":
            permission = 0o200
        elif access == "deny":
            permission = 0o000
        else:
            raise ValueError("Access mode not allowed!")
        os.chmod(cls._pq_path(), permission)

    @classmethod
    def _win_set_permission(cls, access: str):
        try:
            import win32security
            import win32api
            import ntsecuritycon as con
            from win32security import error as pywinerror
        except ImportError:
            raise ImportError(
                "Please install pywin32 by running: 'pip install pywin32'"
            )

        if access == "read":
            permission = con.FILE_GENERIC_READ
        elif access == "write":
            permission = con.FILE_GENERIC_WRITE
        elif access == "deny":
            permission = None
        else:
            raise ValueError("Access mode not allowed!")
        try:
            user, domain, type = win32security.LookupAccountName(
                "", win32api.GetUserName()
            )
            sd = win32security.GetFileSecurity(
                cls._pq_path(), win32security.DACL_SECURITY_INFORMATION
            )
            dacl = win32security.ACL()
            if permission is not None:
                dacl.AddAccessAllowedAce(win32security.ACL_REVISION, permission, user)
            sd.SetSecurityDescriptorDacl(1, dacl, 0)
            win32security.SetFileSecurity(
                cls._pq_path(), win32security.DACL_SECURITY_INFORMATION, sd
            )
        except pywinerror:
            raise FileNotFoundError

    def commit(self) -> None:
        try:
            self._set_permission(access="write")
        except FileNotFoundError:
            # When the file is first created, we cannot allow read on the non existing file.
            pass
        with open(self._pq_path(), "w") as file:
            file.write(self.json())
        self._set_permission(access="deny")

    @classmethod
    def from_disc(cls) -> "ParaloqConfig":
        if not os.path.exists(cls._pq_path()):
            create = Confirm.ask(
                "No valid paraloq profile could be found. \n"
                "Do you want to create one now?"
            )
            if create:
                cls._initiate()
            else:
                raise FileNotFoundError("The paraloq config file could not be located.")
        if (
            not sys.platform.startswith("win")
            and os.stat(cls._pq_path()).st_mode != 32768
        ):
            raise PermissionError(
                "The .paraloq config file has the wrong permissions. Please make sure to change"
                " permission to Octal 000."
            )
        cls._set_permission(access="read")
        with open(cls._pq_path(), "r") as file:
            contents = json.load(file)
        cls._set_permission(access="deny")
        return cls(**contents)

    @classmethod
    def erase(cls):
        sure = Confirm.ask(
            "Are you sure you want to erase the .paraloq file from your disc?"
        )
        if not sure:
            raise KeyboardInterrupt("Action aborted.")
        cls._set_permission(access="write")
        os.remove(cls._pq_path())
        log.info(".paraloq file deleted.")
