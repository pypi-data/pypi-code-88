import json
import logging
import traceback
from .constants.error_constants import ErrorConstants
from flask import Flask, request, Response, g
from .security.generic import is_allowed_by_all
from werkzeug.exceptions import Unauthorized, Forbidden, NotFound, MethodNotAllowed

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('microgue')


class AbstractApp:
    app = None
    views = []
    blueprints = []
    mask_request_headers_fields = []
    mask_request_data_fields = []

    def __init__(self):
        self.app = Flask(__name__)
        self.app.url_map.strict_slashes = False
        self.register_index()
        self.register_views()
        self.register_blueprints()
        self.register_before_request_handler()
        self.register_after_request_handler()
        self.register_error_handlers()

    def register_index(self):
        @self.app.route("/", methods=['GET'])
        @is_allowed_by_all
        def index():
            return Response(json.dumps({'message': 'success'}), status=200)

    def register_views(self):
        for view in self.views:
            view.register(self.app)

    def register_blueprints(self):
        for blueprint in self.blueprints:
            self.app.register_blueprint(blueprint)

    def register_before_request_handler(self):
        def before_request_handler():
            # mask request header fields
            try:
                request_headers = dict(request.headers)
                for mask_request_header_field in self.mask_request_headers_fields:
                    if mask_request_header_field in request_headers:
                        request_headers[mask_request_header_field] = '*****'
            except:
                request_headers = {}

            # mask request data fields
            try:
                request_data = json.loads(request.data.decode('utf-8'))
                for mask_request_data_field in self.mask_request_data_fields:
                    if mask_request_data_field in request_data:
                        request_data[mask_request_data_field] = '*****'
            except:
                request_data = {}

            logger.debug('########## Request Received ########################################')
            logger.debug("method: {}".format(request.method))
            logger.debug("url: {}".format(request.url))
            logger.debug("headers: {}".format(request_headers))
            logger.debug("body: {}".format(request_data))

        self.app.before_request(before_request_handler)

    def register_after_request_handler(self):
        def after_request_handler(response):
            if not g.get('authenticated') and int(response.status_code) < 400:
                response = Response(json.dumps({'error': ErrorConstants.App.UNABLE_TO_AUTHENTICATE}), status=401)

            response.headers = {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "*",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Allow-Credentials": "true"
            }

            logger.debug('########## Response Sent ########################################')
            logger.debug("status: {}".format(response.status))
            logger.debug("headers: {}".format(response.headers))
            logger.debug("body: {}".format(response.response))

            return response

        self.app.after_request(after_request_handler)

    def register_error_handlers(self):
        self.register_unauthorized_error()
        self.register_forbidden_error()
        self.register_not_found_error()
        self.register_method_not_allowed_error()
        self.register_internal_server_error()

    def register_unauthorized_error(self):
        def unauthorized_error(e):
            logger.debug('########## Authentication Error ########################################')
            logger.debug("{}: {}".format(e.__class__.__name__, e))
            return Response(json.dumps({'error': ErrorConstants.App.UNABLE_TO_AUTHENTICATE}), status=401)
        self.app.register_error_handler(Unauthorized, unauthorized_error)

    def register_forbidden_error(self):
        def forbidden_error(e):
            logger.debug('########## Authorization Error ########################################')
            logger.debug("{}: {}".format(e.__class__.__name__, e))
            return Response(json.dumps({'error': ErrorConstants.App.UNABLE_TO_AUTHORIZE}), status=403)
        self.app.register_error_handler(Forbidden, forbidden_error)

    def register_not_found_error(self):
        def not_found_error(e):
            logger.debug('########## Not Found Error ########################################')
            logger.debug("{}: {}".format(e.__class__.__name__, e))
            return Response(json.dumps({'error': ErrorConstants.App.REQUESTED_URL_NOT_FOUND}), status=404)
        self.app.register_error_handler(NotFound, not_found_error)

    def register_method_not_allowed_error(self):
        def method_not_allowed_error(e):
            logger.debug('########## Method Not Allowed Error ########################################')
            logger.debug("{}: {}".format(e.__class__.__name__, e))
            return Response(json.dumps({'error': ErrorConstants.App.METHOD_NOT_ALLOWED}), status=405)
        self.app.register_error_handler(MethodNotAllowed, method_not_allowed_error)

    def register_internal_server_error(self):
        def internal_server_error(e):
            logger.critical('########## Internal Server Error ########################################')
            logger.critical("{}: {}".format(e.__class__.__name__, e))
            logger.critical(traceback.format_exc())
            return Response(json.dumps({'error': ErrorConstants.App.INTERNAL_SERVER_ERROR}), status=500)
        self.app.register_error_handler(Exception, internal_server_error)
