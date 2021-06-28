import logging
import os
import typing

# using 'import' here instead of 'from' to avoid polluting the root namespace of the biolib package
# this is to keep public API as simple as possible
import biolib.app
import biolib.biolib_logging
import biolib.cli
import biolib.utils


# ------------------------------------ Function definitions for public Python API ------------------------------------

def call_cli() -> None:
    biolib.cli.main()


def load(uri: str) -> biolib.app.BioLibApp:
    return biolib.app.BioLibApp(uri)


def set_api_base_url(api_base_url: str) -> None:
    # TODO: Refactor naming in BioLib class from 'host' to 'api_base_url'
    biolib.app.BioLib.set_host(api_base_url)


def set_api_token(api_token: str) -> None:
    biolib.app.BioLib.set_api_token(api_token)


def set_log_level(level: typing.Union[str, int]) -> None:
    biolib.biolib_logging.logger.setLevel(level)


# -------------------------------------------------- Configuration ---------------------------------------------------
__version__ = biolib.utils.BIOLIB_PACKAGE_VERSION
biolib.biolib_logging.logger.configure(default_log_level=logging.INFO)

set_api_base_url(os.getenv('BIOLIB_HOST', default=''))
set_api_token(os.getenv('BIOLIB_TOKEN', default=''))

# allow this script to be called without poetry in dev e.g. by an IDE debugger
if biolib.utils.IS_DEV and __name__ == '__main__':
    call_cli()
