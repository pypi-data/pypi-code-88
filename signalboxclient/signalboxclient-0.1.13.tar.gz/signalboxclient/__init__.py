"""A library used as a Four2/SignalBox client."""

__version__ = '0.1.13'
from .client import SignalBoxClient, Credentials, Configuration
from .client_functions import construct_user, construct_event
