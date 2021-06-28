import pytest
from dataclasses import dataclass
import thlink_backend_app_lib
import thlink_backend_db_lib
import thlink_backend_object_storage_lib
import thlink_backend_notification_lib
from aws_lambda_powertools.utilities.parser.models import SnsModel, SnsRecordModel, SnsNotificationModel


@pytest.fixture
def middleware_mock(monkeypatch):
    monkeypatch.setattr(thlink_backend_app_lib, "middleware", thlink_backend_app_lib.middleware_mock)
    return thlink_backend_app_lib.middleware_mock


@pytest.fixture(autouse=True)
def DBMock(monkeypatch):
    thlink_backend_db_lib.DBMock._table = {}
    thlink_backend_db_lib.DBMock.count_query_operations = 0
    thlink_backend_db_lib.DBMock.count_get_operations = 0
    thlink_backend_db_lib.DBMock.count_put_operations = 0
    thlink_backend_db_lib.DBMock.count_update_operations = 0
    thlink_backend_db_lib.DBMock.count_delete_operations = 0
    monkeypatch.setattr(thlink_backend_db_lib, "DB", thlink_backend_db_lib.DBMock)
    return thlink_backend_db_lib.DBMock


@pytest.fixture(autouse=True)
def ObjectStorageMock(monkeypatch):
    thlink_backend_object_storage_lib.ObjectStorageMock._storage = {}
    thlink_backend_object_storage_lib.ObjectStorageMock.count_get_operations = 0
    thlink_backend_object_storage_lib.ObjectStorageMock.count_get_url_operations = 0
    thlink_backend_object_storage_lib.ObjectStorageMock.count_put_operations = 0
    thlink_backend_object_storage_lib.ObjectStorageMock.count_delete_operations = 0
    monkeypatch.setattr(thlink_backend_object_storage_lib, "ObjectStorage",
                        thlink_backend_object_storage_lib.ObjectStorageMock)
    return thlink_backend_object_storage_lib.ObjectStorageMock


@pytest.fixture(autouse=True)
def NotificationManagerMock(monkeypatch):
    monkeypatch.setattr(thlink_backend_notification_lib, "NotificationManager",
                        thlink_backend_notification_lib.NotificationManagerMock)
    return thlink_backend_notification_lib.NotificationManagerMock


@dataclass
class _LambdaContextMock:
    function_name: str = "test"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:test"
    aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"


@pytest.fixture
def lambda_context_mock():
    return _LambdaContextMock()


def _get_sns_lambda_event_mock(message):
    # model
    return SnsModel(Records=[SnsRecordModel(
        EventSource="aws:sns",
        EventVersion="",
        EventSubscriptionArn="",
        Sns=SnsNotificationModel(
            Subject="",
            TopicArn="",
            UnsubscribeUrl="http://google.com",
            Type="Notification",
            MessageAttributes={},
            Message=message,
            MessageId="",
            SigningCertUrl="http://google.com",
            Signature="",
            Timestamp="2021-06-03 00:00:00",
            SignatureVersion="",
        ),
    )])


@pytest.fixture
def get_sns_lambda_event_mock():
    # model
    return _get_sns_lambda_event_mock
