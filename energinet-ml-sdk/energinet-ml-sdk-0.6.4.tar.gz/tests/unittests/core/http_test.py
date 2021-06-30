import pytest
import typing
import pydantic
from enum import Enum
from unittest.mock import Mock, patch, PropertyMock, ANY
from fastapi.testclient import TestClient

from energinetml.core.http import create_app, run_predict_api
from energinetml.settings import PACKAGE_REQUIREMENT


MODEL_NAME = 'model-name'
MODEL_VERSION = '123'
TEST_SERVER_BASE_URL = 'https://testserver'

PREDICT_ENDPOINT = '/predict'
HEALTH_ENDPOINT = '/health'


# -- Request & Response models -----------------------------------------------


class IdentifierEnum(Enum):
    identifier1 = 'identifier1'
    identifier2 = 'identifier2'


class PredictFeatures(pydantic.BaseModel):
    feature1: int
    feature2: int


class PredictInput(pydantic.BaseModel):
    identifier: IdentifierEnum
    features: PredictFeatures


class PredictRequest(pydantic.BaseModel):
    inputs: typing.List[PredictInput]


class PredictResponse(pydantic.BaseModel):
    predictions: typing.List[typing.Any]


# -- Fixtures ----------------------------------------------------------------


@pytest.fixture
def controller():
    yield Mock(
        request_model=PredictRequest,
        response_model=PredictResponse,
    )


@pytest.fixture
def client(controller):
    with patch('energinetml.core.http.PredictionController') as PredictionController_mock:  # noqa: E501

        PredictionController_mock.return_value = controller

        # Workaround: Can not mock property "name" of Mock object
        model = Mock()
        type(model).name = PropertyMock(return_value='model-name')

        app = create_app(
            model=model,
            trained_model=Mock(),
            model_version='123',
        )

        yield TestClient(app)


@pytest.fixture
def client_with_opentelemetry(controller):
    with patch('energinetml.core.http.PredictionController') \
            as PredictionController_mock, \
            patch('energinetml.core.http.APP_INSIGHT_INSTRUMENTATION_KEY'):

        PredictionController_mock.return_value = controller

        # Workaround: Can not mock property "name" of Mock object
        model = Mock()
        type(model).name = PropertyMock(return_value=MODEL_NAME)

        app = create_app(
            model=model,
            trained_model=Mock(),
            model_version=MODEL_VERSION,
        )

        yield TestClient(
            app=app,
            base_url=TEST_SERVER_BASE_URL,
        )


# -- health_http_endpoint() Tests --------------------------------------------


def test__health_http_endpoint__should_return_status_200(client):
    """
    :param TestClient client:
    """
    # Act
    response = client.get(HEALTH_ENDPOINT)

    # Assert
    assert response.status_code == 200


# -- predict_http_endpoint() Tests -------------------------------------------


def test__predict_http_endpoint__omit_inputs__should_return_status_422(
        client, controller):
    """
    :param TestClient client:
    :param Mock controller:
    """
    # Act
    response = client.post(PREDICT_ENDPOINT)

    # Assert
    assert response.status_code == 422
    controller.predict.assert_not_called()


def test__predict_http_endpoint__omit_identifier__should_return_status_422(
        client, controller):
    """
    :param TestClient client:
    :param Mock controller:
    """
    # Act
    response = client.post(PREDICT_ENDPOINT, json={
        'inputs': [
            {
                'features': {
                    'feature1': 1,
                    'feature2': 2,
                }
            }
        ]
    })

    # Assert
    assert response.status_code == 422
    controller.predict.assert_not_called()


def test__predict_http_endpoint__omit_feature__should_return_status_422(
        client, controller):
    """
    :param TestClient client:
    :param Mock controller:
    """
    # Act
    response = client.post(PREDICT_ENDPOINT, json={
        'inputs': [
            {
                'identifier': 'identifier1',
                'features': {
                    'feature1': 1,
                    # feature2 missing
                }
            }
        ]
    })

    # Assert
    assert response.status_code == 422
    controller.predict.assert_not_called()


def test__predict_http_endpoint__should_return_status_200(
        client, controller):
    """
    :param TestClient client:
    :param Mock controller:
    """
    controller.predict.return_value = PredictResponse(
        predictions=[1, 2],
    )

    # Act
    response = client.post(PREDICT_ENDPOINT, json={
        'inputs': [
            {
                'identifier': 'identifier1',
                'features': {
                    'feature1': 1,
                    'feature2': 2,
                }
            }
        ]
    })

    # Assert
    assert response.status_code == 200
    assert response.headers['X-sdk-version'] == str(PACKAGE_REQUIREMENT)
    assert response.json() == {'predictions': [1, 2]}

    controller.predict.assert_called_once()


# -- OpenTelemetry middleware Tests ------------------------------------------


@patch('energinetml.core.http.tracer')
def test__opentelemetry_middleware__predict_raised_exception__should_log_exception(
        tracer_mock, client_with_opentelemetry, controller):
    """
    :param Mock tracer_mock:
    :param TestClient client_with_opentelemetry:
    :param Mock controller:
    """
    controller.predict.side_effect = RuntimeError

    span = Mock()
    tracer_mock.start_span.return_value.__enter__.return_value = span

    # Act
    response = client_with_opentelemetry.post(PREDICT_ENDPOINT, json={
        'inputs': [
            {
                'identifier': 'identifier1',
                'features': {
                    'feature1': 1,
                    'feature2': 2,
                }
            }
        ]
    })

    # Assert
    assert response.status_code == 500
    controller.predict.assert_called_once()

    # Common attributes
    span.set_attribute.assert_any_call('http.url', f'{TEST_SERVER_BASE_URL}/predict')
    span.set_attribute.assert_any_call('http_url', f'{TEST_SERVER_BASE_URL}/predict')
    span.set_attribute.assert_any_call('model_name', MODEL_NAME)
    span.set_attribute.assert_any_call('model_version', MODEL_VERSION)

    # Error attributes
    span.record_exception.assert_called_once()
    span.set_status.assert_called_once()
    span.set_attribute.assert_any_call('http.status_code', 500)
    span.set_attribute.assert_any_call('http_status_code', 500)
    span.set_attribute.assert_any_call('error.name', ANY)
    span.set_attribute.assert_any_call('error.message', ANY)
    span.set_attribute.assert_any_call('error.stacktrace', ANY)


@patch('energinetml.core.http.tracer')
def test__opentelemetry_middleware__predict_ok__should_log_status_code(
        tracer_mock, client_with_opentelemetry, controller):
    """
    :param Mock tracer_mock:
    :param TestClient client_with_opentelemetry:
    :param Mock controller:
    """
    controller.predict.return_value = PredictResponse(
        predictions=[1, 2],
    )

    span = Mock()
    tracer_mock.start_span.return_value.__enter__.return_value = span

    # Act
    response = client_with_opentelemetry.post(PREDICT_ENDPOINT, json={
        'inputs': [
            {
                'identifier': 'identifier1',
                'features': {
                    'feature1': 1,
                    'feature2': 2,
                }
            }
        ]
    })

    # Assert
    assert response.status_code == 200
    controller.predict.assert_called_once()

    # Common attributes
    span.set_attribute.assert_any_call('http.url', f'{TEST_SERVER_BASE_URL}/predict')
    span.set_attribute.assert_any_call('http_url', f'{TEST_SERVER_BASE_URL}/predict')
    span.set_attribute.assert_any_call('model_name', MODEL_NAME)
    span.set_attribute.assert_any_call('model_version', MODEL_VERSION)

    # Success attributes
    span.set_status.assert_called_once()
    span.set_attribute.assert_any_call('http.status_code', 200)
    span.set_attribute.assert_any_call('http_status_code', 200)


# -- run_predict_api() Tests -------------------------------------------------


@patch('energinetml.core.http.create_app')
@patch('energinetml.core.http.uvicorn.run')
def test__run_predict_api__should_create_and_run_app(run_mock, create_app_mock):
    """
    :param Mock run_mock:
    :param Mock create_app_mock:
    """
    model = Mock()
    trained_model = Mock()
    model_version = '123'
    host = 'ip-address'
    port = 5678

    app = Mock()

    create_app_mock.return_value = app

    # Act
    run_predict_api(
        model=model,
        trained_model=trained_model,
        model_version=model_version,
        host=host,
        port=port,
    )

    # Assert
    create_app_mock.assert_called_once_with(
        model=model,
        trained_model=trained_model,
        model_version=model_version,
    )

    run_mock.assert_called_once_with(
        app=app,
        host=host,
        port=port
    )
