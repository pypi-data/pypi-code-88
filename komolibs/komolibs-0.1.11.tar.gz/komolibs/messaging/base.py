from komolibs.messaging import confluent_cloud


class MessageBase:

    def __init__(self, config_file: str):
        super().__init__()

        self._config_file = config_file
        self._conf = None
        self._bootstrap_servers: str = ""
        self._sasl_mechanisms: str = ""
        self._security_protocol: str = ""
        self._sasl_username: str = ""
        self._sasl_password: str = ""
        self.initialize()

    def initialize(self):
        if self._config_file is None:
            raise Exception("Confluent config path has not been provided.")

        try:
            self._conf = confluent_cloud.read_ccloud_config(self._config_file)
            self._bootstrap_servers: str = self._conf["bootstrap.servers"]
            self._sasl_mechanisms: str = self._conf["sasl.mechanisms"]
            self._security_protocol: str = self._conf["security.protocol"]
            self._sasl_username: str = self._conf["sasl.username"]
            self._sasl_password: str = self._conf["sasl.password"]
        except Exception:
            raise Exception("Failed to configure messaging. "
                            "Please ensure correct confluent config file path is supplied.")

    @property
    def display_name(self) -> str:
        return self.name

    @property
    def name(self) -> str:
        return self.__class__.__name__
