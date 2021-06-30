import fastapi
import uvicorn
import logging
import traceback
from opentelemetry import trace
from starlette.responses import RedirectResponse
from starlette.middleware.base import BaseHTTPMiddleware

from energinetml.settings import (
    PACKAGE_REQUIREMENT,
    APP_INSIGHT_INSTRUMENTATION_KEY,
)

from .predicting import PredictionController

logger = logging.getLogger(__name__)
tracer = trace.get_tracer(__name__)


def create_app(model, trained_model, model_version=None):
    """
    :param energinetml.Model model:
    :param energinetml.TrainedModel trained_model:
    :param str model_version:
    :rtype: fastapi.FastAPI
    """
    controller = PredictionController(
        model=model,
        trained_model=trained_model,
        model_version=model_version,
    )

    async def opentelemetry_middleware(request: fastapi.Request, call_next):
        """
        FastAPI middleware to record HTTP requests.

        Can not access request body in middleware (for logging):
        Issue description: https://github.com/tiangolo/fastapi/issues/394
        """
        from opentelemetry.trace import SpanKind, Status
        from opentelemetry.trace.status import StatusCode

        start_span = tracer.start_span(
            name='request',
            kind=SpanKind.SERVER,
        )

        with start_span as span:
            span.set_attribute('http.url', str(request.url))
            span.set_attribute('http_url', str(request.url))
            span.set_attribute('model_name', model.name)
            if model_version is not None:
                span.set_attribute('model_version', model_version)

            try:
                response = await call_next(request)
            except Exception as e:
                logger.exception('Prediction failed')
                span.record_exception(e)
                span.set_status(Status(status_code=StatusCode.ERROR))
                span.set_attribute('http.status_code', 500)
                span.set_attribute('http_status_code', 500)
                span.set_attribute('error.name', e.__class__.__name__)
                span.set_attribute('error.message', str(e))
                span.set_attribute('error.stacktrace', traceback.format_exc())
                return fastapi.Response(status_code=500)
            else:
                span.set_status(Status(status_code=StatusCode.OK))
                span.set_attribute('http.status_code', response.status_code)
                span.set_attribute('http_status_code', response.status_code)
                return response

    async def root_http_endpoint():
        """
        / should redirect to /docs
        """
        return RedirectResponse(url='/docs')

    async def predict_http_endpoint(
            request: controller.request_model,
            response: fastapi.Response):
        """
        Model prediction HTTP endpoint.
        """
        response.headers['X-sdk-version'] = str(PACKAGE_REQUIREMENT)

        return controller.predict(request)

    async def health_http_endpoint(response: fastapi.Response):
        """
        Health endpoint, should return status 200 with no specific body.
        """
        response.status_code = 200
        return response

    # -- Setup app -----------------------------------------------------------

    app = fastapi.FastAPI(
        title=model.name,
        description=(
            'Model version: %s' % model_version
            if model_version
            else None
        )
    )

    if APP_INSIGHT_INSTRUMENTATION_KEY:
        app.add_middleware(
            middleware_class=BaseHTTPMiddleware,
            dispatch=opentelemetry_middleware,
        )

    app.router.add_api_route(
        path='/',
        methods=['GET'],
        endpoint=root_http_endpoint,
    )

    app.router.add_api_route(
        path='/predict',
        methods=['POST'],
        endpoint=predict_http_endpoint,
        response_model=controller.response_model,
        tags=['model'],
        summary='Predict using the model',
    )

    app.router.add_api_route(
        path='/health',
        methods=['GET'],
        endpoint=health_http_endpoint,
        tags=['health'],
        summary='Health endpoint',
        description='Health endpoint, returns status 200',
    )

    return app


def run_predict_api(model, trained_model, host, port, model_version=None):
    """
    :param energinetml.Model model:
    :param energinetml.TrainedModel trained_model:
    :param str host:
    :param int port:
    :param typing.Optional[str] model_version:
    """
    app = create_app(
        model=model,
        trained_model=trained_model,
        model_version=model_version,
    )

    uvicorn.run(app=app, host=host, port=port)
