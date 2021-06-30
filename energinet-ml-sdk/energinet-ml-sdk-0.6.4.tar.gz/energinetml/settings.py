import os
from packaging import version
from pkg_resources import Requirement


# -- Directories/paths -------------------------------------------------------

__current_file = os.path.abspath(__file__)
__current_folder = os.path.split(__current_file)[0]

SOURCE_DIR = os.path.abspath(__current_folder)
STATIC_DIR = os.path.join(SOURCE_DIR, 'static')
EMPTY_MODEL_TEMPLATE_DIR = os.path.join(STATIC_DIR, 'model-template')
DOCKERFILE_PATH_ML_MODEL = os.path.join(STATIC_DIR, 'Dockerfile')
GITIGNORE_PATH = os.path.join(STATIC_DIR, 'gitignore.txt')
WEB_APP_PIPELINES_TEMPLATES_PATH = os.path.join(STATIC_DIR, 'webapppipelines')


def __read_meta(fn):
    with open(os.path.join(__current_folder, 'meta', fn)) as f:
        return f.read().strip()


# -- Cloud -------------------------------------------------------------------

DEFAULT_LOCATION = 'westeurope'
DEFAULT_VM_CPU = 'Standard_D1_v2'
DEFAULT_VM_GPU = 'Standard_NV6'

CLUSTER_IDLE_SECONDS_BEFORE_SCALEDOWN = 60 * 60 * 2  # 2 hours


# -- Package details ---------------------------------------------------------

# TODO Rename "PACKAGE" to "SDK" (here and elsewhere in general)

PYTHON_VERSION = __read_meta('PYTHON_VERSION')
PACKAGE_NAME = __read_meta('PACKAGE_NAME')
COMMAND_NAME = __read_meta('COMMAND_NAME')
PACKAGE_VERSION = version.parse(__read_meta('PACKAGE_VERSION'))
PACKAGE_REQUIREMENT = Requirement('%s==%s' % (
    PACKAGE_NAME, PACKAGE_VERSION))


# -- Misc --------------------------------------------------------------------

APP_INSIGHT_INSTRUMENTATION_KEY = os.environ.get(
    'APP_INSIGHT_INSTRUMENTATION_KEY')

# Git repository containing template files
TEMPLATES_GIT_URL = 'https://github.com/AnalyticsOps/templates.git'
TEMPLATES_SUBNET_WHITELIST = '/subscriptions/2c63e008-0007-4b92-bfe5-b1fdc94697d5/resourceGroups/analyticsops-devops-agents/providers/Microsoft.Network/virtualNetworks/vnet-devops-agent-001/subnets/agent-subnet'  # noqa: E501
TEMPLATES_IP_WHITELIST = '194.239.2.0/24'
