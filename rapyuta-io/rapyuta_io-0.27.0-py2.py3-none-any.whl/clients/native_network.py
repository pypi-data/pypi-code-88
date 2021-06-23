from __future__ import absolute_import

from rapyuta_io.clients.deployment import _poll_till_ready
import rapyuta_io
from rapyuta_io.clients.common_models import InternalDeploymentStatus
from rapyuta_io.utils import RestClient
from rapyuta_io.utils.error import InvalidParameterException, OperationNotAllowedError
from rapyuta_io.utils.rest_client import HttpMethod
from rapyuta_io.utils.utils import create_auth_header, get_api_response_data
from rapyuta_io.utils.object_converter import ObjBase, enum_field, nested_field
from rapyuta_io.utils.partials import PartialMixin
import six


class NativeNetwork(PartialMixin, ObjBase):
    """
    NativeNetwork represents native network. \n
    Variables marked as (full-only) are only available on a full object. Use `refresh()` to convert a
    partial object into a full one.

    :ivar name: name of the native network
    :vartype name: str
    :ivar runtime: runtime of the native network
    :vartype runtime: :py:class:`~rapyuta_io.clients.package.Runtime`
    :ivar ros_distro: ROS distribution
    :vartype ros_distro: :py:class:`~rapyuta_io.clients.package.ROSDistro`
    :ivar parameters: parameters of the native network
    :vartype parameters: :py:class:`~rapyuta_io.clients.native_network.Parameters`
    :ivar created_at: creation time of the native network
    :vartype created_at: str
    :ivar updated_at: updating time of the native network
    :vartype updated_at: str
    :ivar guid: native network guid
    :vartype guid: str
    :ivar owner_project: project id
    :vartype owner_project: str
    :ivar creator: user id
    :vartype creator: str
    :ivar internal_deployment_guid: guid of the internal deployment
    :vartype internal_deployment_guid: str
    :ivar internal_deployment_status: internal deployment status of the native network
    :vartype internal_deployment_status: :py:class:`~rapyuta_io.clients.common_models.InternalDeploymentStatus`

    :param name: name of the native network
    :type name: str
    :param runtime: runtime of the native network
    :type runtime: :py:class:`~rapyuta_io.clients.package.Runtime`
    :param ros_distro: ROS distribution
    :type ros_distro: :py:class:`~rapyuta_io.clients.package.ROSDistro`
    :param parameters: parameters of the native network
    :type parameters: :py:class:`~rapyuta_io.clients.native_network.Parameters`
    """
    NATIVE_NETWORK_PATH = 'nativenetwork'

    def __init__(self, name, runtime, ros_distro, parameters=None):
        self.validate(name, runtime, ros_distro, parameters)
        self.name = name
        self.runtime = runtime
        self.ros_distro = ros_distro
        self.parameters = parameters
        self.created_at = None
        self.updated_at = None
        self.guid = None
        self.owner_project = None
        self.creator = None
        self.internal_deployment_guid = None
        self.internal_deployment_status = None

    @staticmethod
    def validate(name, runtime, ros_distro, parameters=None):

        if not name or not isinstance(name, six.string_types):
            raise InvalidParameterException('name must be a non-empty string')
        if ros_distro not in list(rapyuta_io.clients.package.ROSDistro.__members__.values()) \
                or not isinstance(ros_distro, rapyuta_io.clients.package.ROSDistro):
            raise InvalidParameterException('ros_distro must be one of rapyuta_io.clients.package.ROSDistro')
        if runtime not in list(rapyuta_io.clients.package.Runtime.__members__.values()) \
                or not isinstance(runtime, rapyuta_io.clients.package.Runtime):
            raise InvalidParameterException('runtime must be one of rapyuta_io.clients.package.Runtime')
        if parameters is not None and not isinstance(parameters, Parameters):
            raise InvalidParameterException('parameters must be of type rapyuta_io.clients.native_network.Parameters')

    def get_deserialize_map(self):
        return {
            'name': 'name',
            'guid': 'guid',
            'owner_project': 'ownerProject',
            'creator': 'creator',
            'runtime': enum_field('runtime', rapyuta_io.clients.package.Runtime),
            'ros_distro': enum_field('rosDistro', rapyuta_io.clients.package.ROSDistro),
            'internal_deployment_guid': 'internalDeploymentGUID',
            'internal_deployment_status':  nested_field('internalDeploymentStatus', InternalDeploymentStatus),
            'parameters': nested_field('parameters', Parameters),
            'created_at':'CreatedAt',
            'updated_at':'UpdatedAt'
        }

    def get_serialize_map(self):
        return {
            'name': 'name',
            'runtime': 'runtime',
            'rosDistro': 'ros_distro',
            'parameters': 'parameters'
        }

    def poll_native_network_till_ready(self, retry_count=120, sleep_interval=5):
        _poll_till_ready(self, retry_count, sleep_interval)
        return self

    def get_status(self):
        if self.guid is None:
            raise OperationNotAllowedError('resource has not been created')
        native_network = NativeNetwork.deserialize(self._get_full_resource())
        internal_deployment_status = native_network.internal_deployment_status
        internal_deployment_status.errors = native_network.get_error_code()
        return internal_deployment_status

    def _get_full_resource(self):
        url = '{}/{}/{}'.format(self._host, self.NATIVE_NETWORK_PATH, self.guid)
        headers = create_auth_header(self._auth_token, self._project)
        response = RestClient(url).method(HttpMethod.GET).headers(headers).execute()
        return get_api_response_data(response, parse_full=True)

    def refresh(self):
        NativeNetwork.deserialize(self._get_full_resource(), obj=self)
        self.is_partial = False

    def get_error_code(self):
        getattr(self.internal_deployment_status, "error_code", [])


class Parameters(ObjBase):
    """
    Parameters represents Native Network Parameters

    :ivar limits: Values corresponding to limits of the parameters
    :vartype limits: :py:class:`~rapyuta_io.clients.native_network.NativeNetworkLimits`

    :param limits: Values corresponding to limits of the parameters
    :type limits: :py:class:`~rapyuta_io.clients.native_network.NativeNetworkLimits`
    """
    def __init__(self, limits):
        self.validate(limits)
        self.limits = limits

    @staticmethod
    def validate(limits):
        if not isinstance(limits, _Limits):
            raise InvalidParameterException('limits must be one of '
                                            'rapyuta_io.clients.native_network.NativeNetworkLimits')

    def get_deserialize_map(self):
        return {
            'limits': nested_field('limits', _Limits)
        }

    def get_serialize_map(self):
        return {
            'limits': 'limits'
        }


class _Limits(ObjBase):
    """
    Limits represents cpu, memory details of the parameter

    :ivar cpu: cpu
    :vartype cpu: Union [float, integer]
    :ivar memory: memory
    :vartype memory: integer

    :param cpu: cpu
    :type cpu: Union [float, integer]
    :param memory: memory
    :type memory: integer
    """

    def __init__(self, cpu, memory):
        self.validate(cpu, memory)
        self.cpu = cpu
        self.memory = memory

    @staticmethod
    def validate(cpu, memory):
        if (not isinstance(cpu, float) and not isinstance(cpu, six.integer_types)) or cpu <= 0:
            raise InvalidParameterException('cpu must be a positive float or integer')
        if not isinstance(memory, six.integer_types) or memory <= 0:
            raise InvalidParameterException('memory must be a positive integer')

    def get_deserialize_map(self):
        return {
            'cpu': 'cpu',
            'memory': 'memory'
        }

    def get_serialize_map(self):
        return {
            'cpu': 'cpu',
            'memory': 'memory'
        }


class NativeNetworkLimits(object):
    """
    NativeNetworkLimits may be one of: \n
    NativeNetworkLimits.X_SMALL (cpu: 0.5core, memory: 2GB) \n
    NativeNetworkLimits.SMALL (cpu: 1core, memory: 4GB) \n
    NativeNetworkLimits.MEDIUM (cpu: 2cores, memory: 8GB) \n
    NativeNetworkLimits.LARGE (cpu: 4cores, memory: 16GB) \n
    """

    X_SMALL = _Limits(0.5, 2048)
    SMALL = _Limits(1, 4096)
    MEDIUM = _Limits(2, 8192)
    LARGE = _Limits(4, 16384)
