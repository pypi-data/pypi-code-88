from byteplus.core.context import Context
from byteplus.core.host_availabler import HostAvailabler
from byteplus.core.url_center import URLCenter

# The URL template of "predict" request, which need fill with "scene" info when use
# Example: https://tob.sgsnssdk.com/predict/api/retail/demo/home
_PREDICT_URL_FORMAT = "{}://{}/predict/api/retail/{}/#"

# The URL format of reporting the real exposure list
# Example: https://tob.sgsnssdk.com/predict/api/retail/demo/ack_impression
_ACK_IMPRESSION_URL_FORMAT = "{}://{}/predict/api/retail/{}/ack_server_impressions"

# The URL format of data uploading
# Example: https://tob.sgsnssdk.com/data/api/retail/retail_demo/user?method=write
_UPLOAD_URL_FORMAT = "{}://{}/data/api/retail/{}/{}?method={}"

# The URL format of operation information
# Example: https://tob.sgsnssdk.com/data/api/retail/retail_demo/operation?method=get
_OPERATION_URL_FORMAT = "{}://{}/data/api/retail/{}/operation?method={}"


class _RetailURL(URLCenter):

    def __init__(self, context: Context):
        self.context: Context = context
        self._hostAvailable: HostAvailabler = HostAvailabler(self, context)
        self.predict_url_format: str = ""
        self.ack_impression_url: str = ""
        self.write_users_url: str = ""
        self.import_users_url: str = ""
        self.write_products_url: str = ""
        self.import_products_url: str = ""
        self.write_user_events_url: str = ""
        self.import_user_events_url: str = ""
        self.get_operation_url: str = ""
        self.list_operations_url: str = ""

        self.refresh(context.hosts[0])

    def refresh(self, host: str) -> None:
        self.predict_url_format: str = self._generate_predict_url(host)
        self.ack_impression_url: str = self._generate_ack_url(host)
        self.write_users_url: str = self._generate_upload_url(host, "user", "write")
        self.import_users_url: str = self._generate_upload_url(host, "user", "import")
        self.write_products_url: str = self._generate_upload_url(host, "product", "write")
        self.import_products_url: str = self._generate_upload_url(host, "product", "import")
        self.write_user_events_url: str = self._generate_upload_url(host, "user_event", "write")
        self.import_user_events_url: str = self._generate_upload_url(host, "user_event", "import")
        self.get_operation_url: str = self._generate_operation_url(host, "get")
        self.list_operations_url: str = self._generate_operation_url(host, "list")

    def _generate_predict_url(self, host) -> str:
        schema = self.context.schema
        tenant = self.context.tenant
        return _PREDICT_URL_FORMAT.format(schema, host, tenant)

    def _generate_ack_url(self, host) -> str:
        schema = self.context.schema
        tenant = self.context.tenant
        return _ACK_IMPRESSION_URL_FORMAT.format(schema, host, tenant)

    def _generate_upload_url(self, host, topic, method) -> str:
        schema = self.context.schema
        tenant = self.context.tenant
        return _UPLOAD_URL_FORMAT.format(schema, host, tenant, topic, method)

    def _generate_operation_url(self, host, method) -> str:
        schema = self.context.schema
        tenant = self.context.tenant
        return _OPERATION_URL_FORMAT.format(schema, host, tenant, method)
