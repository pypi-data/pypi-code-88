import base64
import time
import requests
from pathlib import Path
import shutil
import yaml
import oschmod
import re
import os
import stat
from urllib.parse import urlencode, quote_plus
from qualys_etl.etld_lib import etld_lib_functions as etld_lib_functions
from qualys_etl.etld_lib import etld_lib_config as etld_lib_config
from qualys_etl.etld_lib import etld_lib_date_time_functions as api_datetime
import qualys_etl

global cred_dir
global cookie_file
global cred_file
global use_cookie
global login_failed
global http_return_code


def get_qualys_headers(request=None):
    # 'X-Powered-By': 'Qualys:USPOD1:a6df6808-8c45-eb8c-e040-10ac13041e17:9e42af6e-c5a2-4d9e-825c-449440445cc8'
    # 'X-RateLimit-Limit': '2000'
    # 'X-RateLimit-Window-Sec': '3600'
    # 'X-Concurrency-Limit-Limit': '10'
    # 'X-Concurrency-Limit-Running': '0'
    # 'X-RateLimit-ToWait-Sec': '0'
    # 'X-RateLimit-Remaining': '1999'
    # 'Keep-Alive': 'timeout=300, max=250'
    # 'Connection': 'Keep-Alive'
    # 'Transfer-Encoding': 'chunked'
    # 'Content-Type': 'application/xml'
    if request is None:
        pass
    else:
        request_url = request.url
        url_fqdn = re.sub("(https://)([0-9a-zA-Z\.\_\-]+)(/.*$)", "\g<2>", request_url)
        url_end_point = re.sub("(https://[0-9a-zA-Z\.\_\-]+)/", "", request_url)
        x_ratelimit_limit = request.headers['X-RateLimit-Limit']
        x_ratelimit_window_sec = request.headers['X-RateLimit-Window-Sec']
        x_ratelimit_towait_sec = request.headers['X-RateLimit-ToWait-Sec']
        x_ratelimit_remaining = request.headers['X-RateLimit-Remaining']
        x_concurrency_limit_limit = request.headers['X-Concurrency-Limit-Limit']
        x_concurrency_limit_running = request.headers['X-Concurrency-Limit-Running']
        headers = {'url': request_url,
                   'api_fqdn_server': url_fqdn,
                   'api_end_point': url_end_point,
                   'x_ratelimit_limit': x_ratelimit_limit,
                   'x_ratelimit_window_sec': x_ratelimit_window_sec,
                   'x_ratelimit_towait_sec': x_ratelimit_towait_sec,
                   'x_ratelimit_remaining': x_ratelimit_remaining,
                   'x_concurrency_limit_limit': x_concurrency_limit_limit,
                   'x_concurrency_limit_running': x_concurrency_limit_running}
        return headers


def update_cred(new_cred):
    cred_example_file_path = Path(etld_lib_functions.qetl_code_dir, "qualys_etl", "etld_templates", ".etld_cred.yaml")
    destination_file_path = Path(cred_dir, ".etld_cred.yaml")
    # Get Current .etld_cred.yaml file
    with open(cred_file, 'r', encoding='utf-8') as cred_yaml_file:
        current_cred = yaml.safe_load(cred_yaml_file)
    # Get Template
    with open(str(cred_example_file_path), "r", encoding='utf-8') as cred_template_file:
        cred_template_string = cred_template_file.read()
    # Update Template # username: initialuser  password: initialpassword  api_fqdn_server: qualysapi.qualys.com
    if current_cred == new_cred:
        pass
    else:
        new_username = f"username: '{new_cred.get('username')}'"
        new_password = f"password: '{new_cred.get('password')}'"
        new_api_fqdn_server = f"api_fqdn_server: '{new_cred.get('api_fqdn_server')}'"
        local_date = api_datetime.get_local_date()
        cred_template_string = re.sub('\$DATE', local_date, cred_template_string)
        cred_template_string = re.sub('username: initialuser', new_username, cred_template_string)
        cred_template_string = re.sub('password: initialpassword', new_password, cred_template_string)
        cred_template_string = re.sub('api_fqdn_server: qualysapi\.qualys\.com', new_api_fqdn_server, cred_template_string)
        with open(str(cred_file), 'w', encoding='utf-8') as cred_file_to_update:
            cred_file_to_update.write(cred_template_string)


def get_cred():
    """ Return dict - api_fqdn_url, authorization, username, password """
    if not Path.is_file(cred_file):
        cred_example_file_path = Path(etld_lib_functions.qetl_code_dir, "qualys_etl", "etld_templates", ".etld_cred.yaml")
        destination_file_path = Path(cred_dir, ".etld_cred.yaml")
        shutil.copy(str(cred_example_file_path), str(destination_file_path), follow_symlinks=True)
        cred_example_file = open(str(cred_example_file_path), "r", encoding='utf-8')
        cred_example = cred_example_file.read()
        cred_example_file.close()
        local_date = api_datetime.get_local_date() # Add date updated to file
        cred_example = re.sub('\$DATE', local_date, cred_example)
        cred_file_example = open(str(cred_file), 'w', encoding='utf-8')
        cred_file_example.write(cred_example)
        cred_file_example.close()

    oschmod.set_mode(str(cred_file), "u+rw,u-x,go-rwx")
    try:
        with open(cred_file, 'r', encoding='utf-8') as cred_yaml_file:
            cred = yaml.safe_load(cred_yaml_file)
            api_fqdn_server = cred.get('api_fqdn_server')
            authorization = 'Basic ' + \
                            base64.b64encode(f"{cred.get('username')}:{cred.get('password')}".encode('utf-8')).decode('utf-8')
            username, password = base64.b64decode(authorization.replace("Basic ", "")).decode('utf-8').split(":")
            etld_lib_functions.logger.info(f"Found your subscription credentials file:  {cred_file}")
            etld_lib_functions.logger.info(f"username: {username}, api_fqdn_server:  {api_fqdn_server}")
            cred_file_mode = stat.filemode(os.stat(cred_file).st_mode)
            etld_lib_functions.logger.info(f" ** Notice: Ensure Credential File permissions are correct for your company.")
            etld_lib_functions.logger.info(f" ** Notice: Credentials File: {cred_file}")
            etld_lib_functions.logger.info(f" ** Permissions are: {cred_file_mode} for {cred_file}")
            return {'api_fqdn_server': api_fqdn_server,
                    'authorization': authorization,
                    'username': username,
                    'password': password}
    except Exception as e:
        etld_lib_functions.logger.error(f"Please add your subscription credentials to the:  {cred_file}")
        etld_lib_functions.logger.error(f"   ** Warning: Ensure Credential File permissions are correct for your company.")
        etld_lib_functions.logger.error(f"   ** Warning: Credentials File: {cred_file}")
        cred_file_mode = stat.filemode(os.stat(cred_file).st_mode)
        etld_lib_functions.logger.error(f"   ** Permissions are: {cred_file_mode} for {cred_file}")
        etld_lib_functions.logger.error(f"Exception: {e}")
        exit(1)


def get_cookie():
    try:
        with open(cookie_file, 'r', encoding='utf-8') as f:
            cookie = f.read().replace('\n', '').replace('\r', '')
    except Exception as e:
        etld_lib_functions.logger.error(f"Error in File: {__file__} Line: {etld_lib_functions.lineno()}")
        etld_lib_functions.logger.error(f"               Credentials Dir:  {cred_dir}")
        etld_lib_functions.logger.error(f"              Credentials File:  {cred_file}")
        etld_lib_functions.logger.error(f"Exception: {e}")
        exit(1)

    return cookie


def qualys_login():
    global use_cookie
    global login_failed
    global http_return_code
    login_failed = True
    cred_dict = get_cred()
    """Login to Qualys, return cookie.  Keep cookie if """
    url = f"https://{cred_dict['api_fqdn_server']}/api/2.0/fo/session/"  # Qualys Endpoint
    payload = {'action': 'login', 'username': cred_dict['username'], 'password': cred_dict['password']}
    payload = urlencode(payload, quote_via=quote_plus)

    headers = {
        'X-Requested-With': f'qualysetl_v{qualys_etl.__version__}',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    headers['User-Agent'] = f"qualysetl_v{qualys_etl.__version__}"

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        http_return_code = response.status_code
        if response.status_code == 200:
            cookie_dict = response.cookies.get_dict()
            cookie = f"DWRSESSIONID={cookie_dict['DWRSESSIONID']}; QualysSession={cookie_dict['QualysSession']}"
            with open(cookie_file, 'w', encoding='utf-8') as cookiefile:
                cookiefile.write(cookie)
            etld_lib_functions.logger.info(f"LOGIN - Qualys Login Success with user: {cred_dict['username']}")
            login_failed = False
        else:
            etld_lib_functions.logger.error(f"Fail - Qualys Login Failed with user: {cred_dict['username']}")
            etld_lib_functions.logger.error(f"       HTTP {response.status_code}")
            etld_lib_functions.logger.error(f"       Verify Qualys username, password and api_fqdn_server in Credentials File")
            etld_lib_functions.logger.error(f"             Credentials File: {cred_file}")
            etld_lib_functions.logger.error(f"             username:         {cred_dict['username']}")
            etld_lib_functions.logger.error(f"             api_fqdn_server:  {cred_dict['api_fqdn_server']}")
            exit(1)
        use_cookie = True
    except requests.exceptions.RequestException as e:
        etld_lib_functions.logger.error(f"Fail - Qualys Login Failed with user")
        etld_lib_functions.logger.error(f"       Verify Qualys username, password and api_fqdn_server in Credentials File")
        etld_lib_functions.logger.error(f"             Credentials File: {cred_file}")
        etld_lib_functions.logger.error(f"             username:         {cred_dict['username']}")
        etld_lib_functions.logger.error(f"             api_fqdn_server:  {cred_dict['api_fqdn_server']}")
        etld_lib_functions.logger.error(f"Exception: {e}")
        exit(1)


def qualys_logout():
    global use_cookie
    cred_dict = get_cred()
    url = f"https://{cred_dict['api_fqdn_server']}/api/2.0/fo/session/"  # Qualys Endpoint
    payload = {'action': 'logout'}
    headers = {
        'X-Requested-With': f'qualysetl_v{qualys_etl.__version__}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': get_cookie()
    }
    headers['User-Agent'] = f"qualysetl_v{qualys_etl.__version__}"
    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code == 200:
            etld_lib_functions.logger.info(f"LOGOUT - Qualys Logout Success with user: {cred_dict['username']}")
        else:
            etld_lib_functions.logger.warning(f"LOGOUT FAILED - probably stale cookie, continue with warning")
    except Exception as e:
        etld_lib_functions.logger.warning(f"LOGOUT FAILED, probably connectivity issue, continue with warning")
        etld_lib_functions.logger.warning(f"Exception: {e}")

    use_cookie = False


def main():
    global cred_dir
    global cookie_file
    global cred_file
    global use_cookie
    cred_dir = Path(etld_lib_config.qetl_user_cred_dir)  # Credentials Directory
    cookie_file = Path(cred_dir, ".etld_cookie")  # Cookie File
    cred_file = Path(cred_dir, ".etld_cred.yaml")  # YAML Format Qualys Credentials
    use_cookie = False  # Set to true by qualys_login()
    # Override if running from


def test_basic_auth():
    qualys_login()
    time.sleep(2)
    qualys_logout()
    time.sleep(0.5)


if __name__ == '__main__':
    etld_lib_functions.main()
    etld_lib_config.main()
    main()
    test_basic_auth()
