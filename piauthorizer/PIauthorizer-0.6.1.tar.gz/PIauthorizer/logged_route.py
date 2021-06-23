import logging
import time
import traceback
from typing import Callable

route_logger = logging.getLogger("RouteLogger")
route_logger.addHandler(logging.NullHandler())

from fastapi import Request, Response
from fastapi.exceptions import HTTPException
from fastapi.routing import APIRoute
from fastapi.security.utils import get_authorization_scheme_param
from starlette.datastructures import FormData

from PIauthorizer.authorization import decode_token


class LoggedRoute(APIRoute):
    """A custom implementation of APIRoute class that handles logging of requests.
    Logs include info about request status, method, path, time taken, and also 
    tenant name and external ID for traceability. 

    Args:
        APIRoute (class): fastapi.routing.APIRoute class
    """
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            """Custom route handler that logs request information.

            Args:
                request (Request): a FastAPI request

            Raises:
                Exception: If the authentication token cannot be decoded.
                Exception: If the authentication scheme is not bearer token.

            Returns:
                Response: a FastAPI Response
            """
            
            tenant_name = "N/A"
            external_id = "N/A"
            
            start_time = time.perf_counter()
            try:
                response: Response = await original_route_handler(request)
                finish_time = time.perf_counter()
                
                overall_status = "successful" if response.status_code < 400 else "failed"
                status_code = response.status_code
            except HTTPException as e_http:
                finish_time = time.perf_counter()
                
                overall_status = "failed"
                status_code = e_http.status_code
                raise
            except Exception:
                traceback.print_exc()
                raise
            finally:
                execution_time = finish_time - start_time
                
                # Obtain the tenant name if they have been authenticated.
                auth_header = request.headers.get("Authorization", None)
                if(auth_header):
                    scheme, param = get_authorization_scheme_param(auth_header)
                    if scheme.lower() != "bearer":
                        raise Exception("Authentication scheme is not using bearer token.")
                    
                    try:
                        decoded_token = decode_token(param)
                    except Exception:
                        traceback.print_exc()
                        raise Exception("Unable to decode token.")
                        
                    tenant_name = decoded_token.get('tenantname', tenant_name)
                
                form: FormData = await request.form()
                
                if "file" not in form.keys():
                    # Obtain the external ID from the request body if available.
                    if await request.body():
                        body = await request.json()
                        
                        external_id = body.get('ExternalID', external_id)            

                route_logger.info(f"Request {overall_status}, {request.method} {request.url.path}, "
                                  f"status code={status_code}, tenant={tenant_name}, "
                                  f"externalID={external_id} took={execution_time:0.4f}s")
                
            return response

        return custom_route_handler
