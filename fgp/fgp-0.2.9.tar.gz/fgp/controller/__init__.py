from .client import Client
from .store import Store
from .device import Device
from .reference import Reference
from .event import Event
from .extension import Extension
from .relation import Relation
from .lambdas import Lambdas

class ApiClient:
    _client: Client = None
    store: Store = None
    reference: Reference = None
    device: Device = None
    client: Client = None
    event: Event = None
    extension: Extension = None
    relation: Relation = None
    lambdas: Lambdas

    def __init__(self, url, application, headers=None):
        self._client = Client(url, application, headers=headers)
        self.store = Store(self._client)
        self.reference = Reference(self._client)
        self.device = Device(self._client)
        self.event = Event(self._client)
        self.extension = Extension(self._client)
        self.relation = Relation(self._client)
        self.lambdas = Lambdas(self._client)
