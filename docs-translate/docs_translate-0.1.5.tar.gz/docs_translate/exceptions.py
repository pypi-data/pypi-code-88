from pathlib import Path


class DocsTranslateBaseException(Exception):
    pass


class UnknownServiceError(DocsTranslateBaseException):
    def __init__(self, service_name: str) -> None:
        super().__init__(f'{service_name} service is unknown')


class ConfigurationError(DocsTranslateBaseException):
    def __init__(self, property_name: str) -> None:
        super().__init__(
            f'The setting "{property_name}" is missing. Check your config file or cli arguments'
        )


class ObjectNotFoundException(DocsTranslateBaseException):
    def __init__(self, obj: Path) -> None:
        super().__init__(f'{obj} not found')


class NoApiKeyFileError(DocsTranslateBaseException):
    def __init__(self, api_key_path: Path) -> None:
        super().__init__(
            f'API_KEY file in location "{api_key_path}" not found\n'
            'Provide API_KEY file path or create it, if not exist'
        )


class NoConfigFileError(DocsTranslateBaseException):
    def __init__(self, not_found_file: Path) -> None:
        super().__init__(
            f'No config file found. Create file {not_found_file} or pass custom file  with `-c` param'
        )


class FileIsNotMarkdown(DocsTranslateBaseException):
    def __init__(self, not_md_obj: Path) -> None:
        super().__init__(f'{not_md_obj} is not a Markdown or a restructuredtext file!')


class DocsFileNotFoundError(FileNotFoundError):
    def __init__(self, not_md_obj: Path) -> None:
        super().__init__(f'{not_md_obj} is not found Markdown or a restructuredtext files!')


class FileCreateError(DocsTranslateBaseException):
    def __init__(self, not_md_obj: Path) -> None:
        super().__init__(f'{not_md_obj} is not create translate file!')
