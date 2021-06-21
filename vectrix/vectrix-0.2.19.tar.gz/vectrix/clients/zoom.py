from ast import parse
import json
import logging
import os
import time

import requests

from enum import Enum

logger = logging.getLogger(__name__)

ACCESS_TOKEN_EXPIRED = 124

RATE_LIMIT = 429
DAILY_RATE_LIMIT = "You have reached the maximum daily rate limit for this API. Refer to the response header for details on when you can make another request."


class DailyRateLimitException(Exception):
    def __init__(self, message="Daily rate limit exception hit."):
        return super().__init__(message)


class PaidAccountException(Exception):
    def __init__(self, message):
        return super().__init__(message)


class RetryLimitExceeded(Exception):
    def __init__(
        self,
        message="Rate-limit retry limit was exceeded. Please try again later or contact support if this persists."
    ):

        return super().__init__(message)


class ZoomLoginTypes(Enum):
    FACEBOOK = 0
    GOOGLE = 1
    API = 99
    ZOOM = 100
    SSO = 101


class ZoomClient:
    endpoint = "https://api.zoom.us/v2"
    """
    A thin client around Zoom API http requests
    """
    def __init__(self, access_token):
        self.access_token = access_token

    def __zoom_headers(self):
        return {
            'authorization': f"Bearer {self.access_token}",
            'content-type': "application/json"
        }

    def __handle_rate_limit(self, wait_for_sec, resp):
        message = resp.get("message")

        if DAILY_RATE_LIMIT == message:
            raise DailyRateLimitException(message)
        else:
            time.sleep(wait_for_sec)

    def get_request(self, path, params=None, retry_limit=3, wait_for_sec=2):
        success = False
        retries = 0

        try:
            while not success and retries < retry_limit:
                headers = self.__zoom_headers()
                full_path = f"{self.endpoint}{path}"
                resp = requests.get(full_path, headers=headers, params=params)
                parsed_resp = json.loads(resp.text)

                if parsed_resp.get("code") == 200:
                    raise PaidAccountException(parsed_resp.get("message"))

                elif resp.status_code == RATE_LIMIT:
                    backoff = wait_for_sec * retries if retries > 0 else wait_for_sec

                    self.__handle_rate_limit(backoff, parsed_resp)
                    retries += 1

                else:
                    success = True

            if not success and retries >= retry_limit:

                raise RetryLimitExceeded()

            return parsed_resp

        except Exception as e:
            logger.exception(e)
            raise e

    def paginated_request(self,
                          base_path,
                          key=None,
                          page_number=None,
                          additional_params={}):

        if not key:
            raise Exception(
                "Missing a key to use for retrieving paginated data. Check the Zoom API docs to find the key associated with the list of results"
            )

        items = []
        page_size = 30
        params = {"page_size": page_size, **additional_params}

        if page_number:
            params["page_number"] = page_number

        paginated_results = self.get_request(base_path, params=params)

        if paginated_results:
            next_page_token = paginated_results.get("next_page_token")
            items = paginated_results.get(key, [])

            while next_page_token is not None and next_page_token != '':
                if page_number:
                    page_number += 1

                updated_params = {
                    "page_number": page_number,
                    "next_page_token": next_page_token,
                    **params
                }

                paginated_response = self.get_request(base_path,
                                                      params=updated_params)

                next_page_token = paginated_response.get("next_page_token")

                items.extend(paginated_response.get(key))

        return items

    def get_user(self, user_id):
        """
        Fetch user info
        """
        user_response = self.get_request(f"/users/{user_id}")

        return user_response

    def get_user_permissions(self, user_id):
        """
        Fetch permissions a zoom user has.
        
        returns: a list(str) of permissions.
        """

        user_permission_response = self.get_request(
            f"/users/{user_id}/permissions")

        return user_permission_response

    def get_user_login_type(self, user_obj):
        """
        Given an object returned by get_user(id), 
        return human-readable login method associated with the user
        """
        types = []
        login_types = user_obj.get("login_types") or []

        for login_type in login_types:

            if login_type == ZoomLoginTypes.FACEBOOK.value:
                types.append(ZoomLoginTypes.FACEBOOK.name)

            elif login_type == ZoomLoginTypes.GOOGLE.value:
                types.append(ZoomLoginTypes.GOOGLE.name)

            elif login_type == ZoomLoginTypes.API.value:
                types.append(ZoomLoginTypes.API.name)

            elif login_type == ZoomLoginTypes.ZOOM.value:
                types.append(ZoomLoginTypes.ZOOM.name)

            elif login_type == ZoomLoginTypes.SSO.value:
                types.append(ZoomLoginTypes.SSO.name)

        return types

    def get_users(self):
        """
        Fetch user info return a list of users.
        """

        return self.paginated_request("/users", key="users")

    def get_user_settings(self,
                          user_id,
                          meeting_authentication=False,
                          recording_authentication=False,
                          meeting_security=False):
        """
        Return user settings

        Arguments:
          {user_id}: The user to fetch settings for
          {meeting_authentication}: Return user's meeting authentication settings
          {recording_authentication}: Return user's recording authentication settings
          {meeting_security}: Return user's meeting security settings

        For detailed list of objects schemas, refer to the following documentation:
          https://marketplace.zoom.us/docs/api-reference/zoom-api/users/usersettings
        """
        path_params = {}

        updates = 0

        if meeting_authentication:
            path_params["option"] = "meeting_authentication"
            updates += 1
        if recording_authentication:
            path_params["option"] = "recording_authentication"
            updates += 1
        if meeting_security:
            path_params["option"] = "meeting_security"
            updates += 1

        if updates > 1:
            raise Exception(
                "Error: tried passing multiple option params to the same request."
            )

        return self.get_request(f"/users/{user_id}/settings",
                                params=path_params)

    def get_meetings(self, user_id):
        return self.paginated_request(f"/users/{user_id}/meetings",
                                      key="meetings")

    def get_meeting(self, meeting_id):
        return self.get_request(f"/meetings/{meeting_id}")

    def get_cloud_recordings(self, user_id):
        """
        Get the list of cloud recordings associated with a user
        """

        cloud_recordings = self.paginated_request(
            f"/users/{user_id}/recordings", key="meetings")

        return cloud_recordings

    def get_meeting_recordings(self, meeting_id):
        """
         Get all the recordings from a meeting or webinar instance
        """
        return self.get_request(f"/meetings/{meeting_id}/recordings")

    def get_meeting_recording_settings(self, meeting_id):
        """
        For a given meeting, get the settings applied to its cloud recordings.
        """

        return self.get_request(f"/meetings/{meeting_id}/recordings/settings")

    def get_im_groups(self):
        return self.get_request("/im/groups")

    def get_operation_logs(
        self,
        category_type="all",
        date_from=None,
        date_to=None,
    ):
        params = {"category_type": category_type}

        if date_from:
            params["from"] = date_from
        if date_to:
            params["to"] = date_to

        operation_logs = self.paginated_request("/report/operationlogs",
                                                key="operation_logs",
                                                additional_params=params)

        return operation_logs

    def get_role(self, role_id):
        return self.get_request(f"/roles/{role_id}")

    def get_roles(self):
        roles = []
        try:
            roles_resp = self.get_request("/roles")
            roles = roles_resp.get(
                "roles"
            ) if roles_resp is not None and roles_resp.get("roles") else []

        except Exception as e:
            print(e)

        return roles

    def get_locked_settings(self, account_id, meeting_security=False):
        params = {}
        if meeting_security:
            params["option"] = "meeting_security"

        return self.get_request(f"/accounts/{account_id}/lock_settings",
                                params=params)
