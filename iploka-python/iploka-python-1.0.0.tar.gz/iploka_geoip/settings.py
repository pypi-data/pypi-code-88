"""
iploka_settings.settings
~~~~~~~~~~~~~~~~~~~~~

This module contains internal settings that make our iploka-geoip library simpler.
"""


from platform import mac_ver, win32_ver, system
from distro import linux_distribution
from sys import version_info as vi

from . import __version__


# This is the iploka service base URI.  This is where all API requests go.
API_URI = 'https://api.iploka.com/'

# The maximum amount of retries to attempt when making API calls.
MAX_RETRIES = 3

# This dictionary is used to dynamically select the appropriate platform for
# the user agent string.
OS_VERSION_INFO = {
    'Linux': '%s' % (linux_distribution()[0]),
    'Windows': '%s' % (win32_ver()[0]),
    'Darwin': '%s' % (mac_ver()[0]),
}

# The user-agent string is provided so that We can (eventually) keep track of
# what libraries to support over time.  EG: Maybe the service is used primarily
# by Windows developers, and I should invest more time in improving those
# integrations.
USER_AGENT = 'python-iploka-geoip/%s python/%s %s/%s' % (
    __version__,
    '%s.%s.%s' % (vi.major, vi.minor, vi.micro),
    system(),
    OS_VERSION_INFO.get(system(), ''),
)
