import argparse
import itertools
import json
import os
import requests
import sys
import threading
import time
import zipfile
from certora_cli.certoraCollectRunMetadata import CERTORA_METADATA_FILE
from certora_cli.certoraJobList import JobList
from certora_cli.certoraUtils import as_posix, debug_print_, flush_stdout, get_version, check_results, \
    COINBASE_FEATURES_MODE_CONFIG_FLAG
from certora_cli.certoraUtils import CERTORA_BUILD_FILE, CERTORA_VERIFY_FILE, CERTORA_CONFIG_DIR
from certora_cli.certoraUtils import print_error, print_warning, print_completion_message
from certora_cli.certoraUtils import DEFAULT_CLOUD_ENV, DEFAULT_STAGING_ENV
from certora_cli.certoraUtils import Mode

from typing import Optional, Dict, Any, List, cast
from tqdm import tqdm  # type: ignore

MAX_FILE_SIZE = 10 * 1024 * 1024
NO_OUTPUT_LIMIT_MINUTES = 15
MAX_POLLING_TIME_MINUTES = 120
LOG_READ_FREQUENCY = 10
MAX_ATTEMPTS_TO_FETCH_OUTPUT = 3
DELAY_FETCH_OUTPUT_SECONDS = 10

# error messages
CONNECTION_ERR_PREFIX = "Connection error:"
GENERAL_ERR_PREFIX = "An error occurred:"
SERVER_ERR_PREFIX = "Server Error:"
STATUS_ERR_PREFIX = "Error Status:"
TIMEOUT_MSG_PREFIX = "Request timed out."
VAAS_ERR_PREFIX = "Server reported an error:"

CONTACT_CERTORA_MSG = "please contact Certora on https://www.certora.com"

CompressingProgress = "  - compressing  ({}/{})\r"
Response = requests.models.Response


class TimeError(Exception):
    """A custom exception used to report on time elapsed errors"""


def check_version(version: str) -> bool:
    """
    Gets the latest package version and compares to the supplied one
    :param version: A string (X.Y.Z format)
    :return: A boolean (false if supplied version is not compatible with the latest)
    """
    try:
        response = requests.get("https://pypi.org/pypi/certora-cli/json", timeout=10)
        out = response.json()  # raises ValueError: No JSON object could be decoded
        latest = out['info']['version']
        if "." in latest and "." in version:
            main, sub, patch = latest.split(".")
            current_main, current_sub, current_patch = version.split(".")
            if int(main) > int(current_main):  # raises ValueError: invalid literal for int() with base 10
                print_error(GENERAL_ERR_PREFIX, "Incompatible package version. "
                                                "Please upgrade by running: pip install certora-cli --upgrade")
                return False
            elif int(sub) > int(current_sub) or int(patch) > int(current_patch):
                print_warning(f"You are using certora-cli {version}; however, version {latest} is available.")
    except (requests.exceptions.RequestException, ValueError) as e:
        debug_print_(str(e))
    return True


def progress_bar(total: int = 70, describe: str = "Initializing verification") -> None:
    for _ in tqdm(range(total),
                  bar_format="{l_bar}{bar}| [remaining-{remaining}]",
                  ncols=70, desc=describe, ascii=".#"):
        time.sleep(1)


def get_url(env: str) -> str:
    if env == DEFAULT_STAGING_ENV:
        url = 'https://vaas-stg.certora.com'
    elif env == DEFAULT_CLOUD_ENV:
        url = 'https://prover.certora.com'
    else:
        raise Exception(f"Undefined environment {env}")
    return url


def parse_json(response: Response) -> Dict[str, Any]:
    try:
        json_response = response.json()
    except ValueError:
        print_error(GENERAL_ERR_PREFIX, "Could not parse JSON response")
        print(response.text)  # Should we print the whole response here?
        return {}
    return json_response


def compress_files(zip_file_name: str, *file_names: Any) -> bool:
    zip_obj = zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED)

    total_files = 0
    for file_name in file_names:
        if os.path.isdir(file_name):
            total_dir_files = get_total_files(file_name)
            if total_dir_files == 0:
                print_error(GENERAL_ERR_PREFIX, f"Provided directory - '{file_name}' is empty.")
                return False
            elif total_dir_files > 0:
                total_files += total_dir_files
        elif os.path.isfile(file_name):
            total_files += 1
        else:
            print_error(GENERAL_ERR_PREFIX, f"Provided file - '{file_name}' does not exist.")
            return False
    if total_files < 1:
        if len(file_names) == 0:
            print_error(GENERAL_ERR_PREFIX, f"No file was provided. {CONTACT_CERTORA_MSG}")
        else:
            print_error(GENERAL_ERR_PREFIX, f"Provided file(s) - {', '.join(file_names)} do(es) not exist.")
        return False

    i = 0

    for file_name in file_names:
        if os.path.isdir(file_name):
            try:
                # traverse a directory
                for root, _, files in os.walk(file_name):
                    for f in files:
                        f_name = as_posix(os.path.join(root, f))
                        zip_obj.write(f_name)
                        i += 1
                        print(CompressingProgress.format(i, total_files), flush=True, end="")
            except OSError:
                flush_stdout()
                print_error(GENERAL_ERR_PREFIX, f"Could not compress a directory - {file_name}")
                return False
        else:  # zip file
            try:
                base_name = os.path.basename(file_name)
                '''
                Why do we use the base name? Otherwise, when we provide a relative path dir_a/dir_b/file.tac,
                the zip function will create a directory dir_a, inside it a directory dir_b and inside that file.tac
                '''

                zip_obj.write(file_name, base_name)
                i += 1
                print(CompressingProgress.format(i, total_files), flush=True, end="")
            except OSError:
                flush_stdout()
                print_error(GENERAL_ERR_PREFIX, f"Could not compress {file_name}")
                return False
    zip_obj.close()
    return True


def get_total_files(directory: str) -> int:
    try:
        total_files = sum(len(files) for _, _, files in os.walk(directory))
        return total_files
    except OSError:
        print_error(GENERAL_ERR_PREFIX, f"Could not traverse {directory}")
        return -1


def output_error_response(response: Response) -> None:
    print_error(STATUS_ERR_PREFIX, str(response.status_code))
    if response.status_code == 500:
        print_error(SERVER_ERR_PREFIX, CONTACT_CERTORA_MSG)
        return
    try:
        error_response = response.json()
        debug_print_(error_response)
        if "errorString" in error_response:
            print_error(VAAS_ERR_PREFIX, error_response["errorString"])
        elif "message" in error_response:
            print_error(VAAS_ERR_PREFIX, error_response["message"])
    except Exception as e:
        print_error(GENERAL_ERR_PREFIX, str(e))
        print(response.text)


def is_success_response(json_response: Dict[str, Any], status_url: str = "") -> bool:
    """
    @param json_response:
    @param status_url:
    @return: False when the server response missing the success field or success value False
    """
    if "success" not in json_response:
        print_error(GENERAL_ERR_PREFIX, "The server returned an unexpected response:")
        print(json_response)
        print(CONTACT_CERTORA_MSG)
        return False
    if not json_response["success"]:
        if "errorString" in json_response:
            print_error(json_response["errorString"], status_url)
        else:
            print_error(GENERAL_ERR_PREFIX, "The server returned an error with no message:")
            print(json_response)
            print(CONTACT_CERTORA_MSG)
        return False
    return True


def print_conn_error() -> None:
    print_error(CONNECTION_ERR_PREFIX, "Server is currently unavailable. Please try again later.")
    print(f"For further information, {CONTACT_CERTORA_MSG}", flush=True)


def print_error_and_status_url(err_msg: str, status_url: str) -> None:
    print_error(GENERAL_ERR_PREFIX, err_msg)
    if status_url:
        print("For further details visit", status_url)
    print("Closing connection...", flush=True)


def look_for_path(path: str) -> Optional[Response]:
    try:
        r = requests.get(path, timeout=10)
        if r.status_code == requests.codes.ok:
            # read
            return r.json()
        else:
            return None
    except json.decoder.JSONDecodeError:
        # when '' is returned
        return None
    except (requests.exceptions.Timeout, requests.exceptions.RequestException, ConnectionError):
        print_conn_error()
        return None


def fetch_results_from_web(output_URL: str, max_attempts: int, delay_between_attempts_seconds: int) -> \
        Optional[Response]:
    attempts = 0
    actual = None
    while actual is None and attempts < max_attempts:
        attempts += 1
        actual = look_for_path(output_URL)
        if actual is None and attempts < max_attempts:
            time.sleep(delay_between_attempts_seconds)
    return actual


def check_results_from_web(output_URL: str, max_attempts: int, delay_between_attempts_seconds: int) -> bool:
    actual = fetch_results_from_web(output_URL, max_attempts, delay_between_attempts_seconds)
    if actual is None:
        print("Could not find actual results file output.json")
        return False
    return check_results(cast(dict, actual))


def save_features_json_from_web(output_URL: str, max_attempts: int, delay_between_attempts_seconds: int) -> None:
    features_json_content = fetch_results_from_web(output_URL, max_attempts, delay_between_attempts_seconds)
    if features_json_content is None:
        print_error(GENERAL_ERR_PREFIX, "Could not download features report file (featuresReport.json)")
        return
    with open("featuresReport.json", 'w') as featuresReportFile:
        json.dump(features_json_content, featuresReportFile)
    print_completion_message("featuresReport.json was successfully created")
    return


class CloudVerification:
    """Represents an AWS Cloud verification"""
    done = False

    def __init__(self, args: argparse.Namespace) -> None:
        self.args = args
        self.queue_wait_minutes = NO_OUTPUT_LIMIT_MINUTES
        self.max_poll_minutes = MAX_POLLING_TIME_MINUTES
        self.log_query_frequency_seconds = LOG_READ_FREQUENCY
        self.max_attempts_to_fetch_output = MAX_ATTEMPTS_TO_FETCH_OUTPUT
        self.delay_fetch_output_seconds = DELAY_FETCH_OUTPUT_SECONDS

        for timer in ['queue_wait_minutes', 'max_poll_minutes', 'log_query_frequency_seconds',
                      'max_attempts_to_fetch_output', 'delay_fetch_output_seconds']:
            val = getattr(self.args, timer)
            if val is not None:
                setattr(self, timer, val)

        self.runName = os.urandom(10).hex()
        self.ZipFileName = self.runName + ".zip"
        self.env = ""
        self.url = ""
        self.jsonOutputUrl = ""
        self.outputUrl = ""
        self.statusUrl = ""
        self.reportUrl = ""
        self.zipOutputUrl = ""
        self.featuresResults = ""
        self.anim_thread = threading.Thread(target=self.animate)

    def __set_url(self, url_attr: str, index: str, user_id: int, current_job_anonymous_key: str,
                  requested_resource: str = None) -> None:
        """
        DO NOT USE THIS, use set_output_url() etc. instead.
        This function is intended for internal use by the aforementioned functions. We DO NOT check that the url_attr is
        defined!
        @param url_attr: name of the attribute we want to set in self. For example, if url_attr == "outputUrl",
                         then self.outputUrl will be set.
        @param index: name of the url index of this request
        @param user_id: id number of the user sending the request
        @param current_job_anonymous_key: user's anonymous key
        """
        if self.url == "":
            debug_print_(f"setting {url_attr}: url is not defined.", self.args.debug)
        elif self.runName == "":
            debug_print_(f"setting {url_attr}: runName is not defined.", self.args.debug)
        else:
            resource_req = f"{'/' + requested_resource if requested_resource is not None else ''}"
            url = f"{self.url}/{index}/{user_id}/{self.runName}{resource_req}?anonymousKey={current_job_anonymous_key}"
            setattr(self, url_attr, url)

    # jar output (logs) url
    def set_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("outputUrl", "job", user_id, anonymous_key)

    # index report url
    def set_report_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("reportUrl", "output", user_id, anonymous_key)

    # index report url
    def set_requested_resource_url(self, user_id: int, resource_name: str, resource_file: str, anonymous_key: str) \
            -> None:
        self.__set_url(resource_name, "output", user_id, anonymous_key, requested_resource=resource_file)

    # status page url
    def set_status_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("statusUrl", "jobStatus", user_id, anonymous_key)

    # compressed output folder url
    def set_zip_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("zipOutputUrl", "zipOutput", user_id, anonymous_key)

    # json output url
    def set_json_output_url(self, user_id: int, anonymous_key: str) -> None:
        self.__set_url("jsonOutputUrl", "jsonOutput", user_id, anonymous_key)

    def prepare_auth_data(self, cl_args: str) -> Optional[Dict[str, Any]]:
        """
        :param cl_args: A string that can be copied to and run by the shell to recreate this run.
        @return: An authentication data dictionary to send to server
        """

        authData = {
            "certoraKey": self.args.key,
            "process": self.args.process,
            "runName": self.runName
        }  # type: Dict[str, Any]

        if self.args.staging is not None:
            authData["branch"] = self.args.staging

        authData["version"] = get_version()

        if self.args.settings is not None:
            jar_settings = []  # type: List[str]
            for settings_exp in self.args.settings:  # It is in standard form
                jar_settings.extend(settings_exp.split("="))

            authData["jarSettings"] = jar_settings

        if self.args.coinbaseMode:
            if "jarSettings" not in authData:
                authData["jarSettings"] = [COINBASE_FEATURES_MODE_CONFIG_FLAG]
            else:
                authData["jarSettings"].append(COINBASE_FEATURES_MODE_CONFIG_FLAG)

        if self.args.java_args is not None:
            authData["javaArgs"] = self.args.java_args

        if self.args.cache is not None:
            authData["toolSceneCacheKey"] = self.args.cache

        if self.args.msg is not None:
            authData["msg"] = self.args.msg

        authData["buildArgs"] = cl_args

        debug_print_(f'authdata = {authData}', self.args.debug)
        return authData

    def print_output_links(self) -> None:
        print("You can follow up on the status:", self.statusUrl)
        print("You will also receive an email notification when this process is completed.")
        print("When the job is completed, use the following link for downloading compressed results folder: ",
              self.zipOutputUrl)
        print("When the job is completed without errors, the results will be presented in", self.outputUrl)

    def print_verification_summary(self) -> None:
        print("Status page:", self.statusUrl)
        print("Verification report:", self.reportUrl)
        print("Full report:", self.zipOutputUrl)
        print("Finished verification request")

    def cli_verify(self, cl_args: str) -> bool:
        """
        Sends a verification request to HTTP Handler, uploads a zip file, and outputs the results.
        :param cl_args: A string that can be copied to and run by the shell to recreate this run.
        @returns If compareToExpected is True, returns True when the expected output equals the actual results.
                 Otherwise, returns False if there was at least one violated rule.
        """
        self.env = self.args.env

        self.url = get_url(self.env)
        version = get_version()
        if not check_version(version):
            return False

        auth_data = self.prepare_auth_data(cl_args)
        if auth_data is None:
            return False

        resp = self.verification_request(auth_data)  # send post request to /cli/verify

        if resp is None:  # on error
            return False

        json_response = parse_json(resp)
        if not json_response:
            return False

        if not is_success_response(json_response):
            return False

        try:
            anonymousKey = json_response["anonymousKey"]
            presigned_url = json_response["presigned_url"]
            userId = json_response["userId"]
        except Exception as e:  # (Json) ValueError
            print_error(GENERAL_ERR_PREFIX, f"Unexpected response {e}")
            return False

        print("Compressing the files...", flush=True)
        print()
        # remove previous zip file
        if os.path.exists(self.ZipFileName):
            os.remove(self.ZipFileName)

        # create new zip file
        if self.args.mode == Mode.TAC:
            result = compress_files(self.ZipFileName, self.args.files[0])  # We zip the tac file itself
        else:
            result = compress_files(self.ZipFileName, CERTORA_BUILD_FILE, CERTORA_VERIFY_FILE, CERTORA_CONFIG_DIR,
                                    CERTORA_METADATA_FILE)

        flush_stdout()
        if not result:
            return False

        if os.path.getsize(self.ZipFileName) > MAX_FILE_SIZE:
            print_error(GENERAL_ERR_PREFIX, "Max 10MB file size exceeded.", flush=True)
            return False

        print_completion_message("Finished compressing")
        print()
        print("Uploading files...", flush=True)
        if self.upload(presigned_url, self.ZipFileName):
            print_completion_message("Job submitted to server")
            print()
        else:  # upload error
            return False
        os.remove(self.ZipFileName)  # remove zip file

        # set results url
        self.set_output_url(userId, anonymousKey)
        self.set_status_url(userId, anonymousKey)
        self.set_report_url(userId, anonymousKey)
        self.set_zip_output_url(userId, anonymousKey)
        self.set_json_output_url(userId, anonymousKey)

        if self.args.coinbaseMode:
            self.set_requested_resource_url(userId, 'featuresResults', 'featuresResults.json', anonymousKey)

        if self.outputUrl == "":  # on error
            return False

        print("You can follow up on the status:", self.statusUrl)
        print()
        print("Output:", flush=True)

        # update jobs list
        job_list = JobList(debug=self.args.debug)
        job_list.add_job(self.runName, self.reportUrl, auth_data.get("msg", ""))
        thread = threading.Thread(target=job_list.save_data)
        thread.start()

        try:
            self.new_poll_output()
            thread.join()
        except KeyboardInterrupt:
            # wait for the threads to finish
            self.done = True
            self.anim_thread.join()
            thread.join()
            print("You were disconnected from server, but your request is still being processed.")
            self.print_output_links()
            return False
        except requests.exceptions.RequestException:
            # other requests exceptions
            print_conn_error()
            # wait for the threads to finish
            self.done = True
            self.anim_thread.join()
            thread.join()
            return False
        except TimeError:
            # stop the animation
            self.done = True
            self.anim_thread.join()
            thread.join()
            self.print_output_links()
            return False
        except Exception as e:
            # wait for the threads to finish
            self.done = True
            self.anim_thread.join()
            thread.join()
            print("Encountered an error: ", e)
            return False

        print()
        self.print_verification_summary()

        if self.args.no_compare:
            return True

        result_check_success = check_results_from_web(self.jsonOutputUrl,
                                                      self.max_attempts_to_fetch_output,
                                                      self.delay_fetch_output_seconds)
        if self.args.coinbaseMode:
            save_features_json_from_web(self.featuresResults, self.max_attempts_to_fetch_output,
                                        self.delay_fetch_output_seconds)

        return result_check_success

    def verification_request(self, auth_data: Dict[str, Any]) -> Optional[Response]:
        verify_url = self.url + "/cli/verify"
        response = None
        print(f"requesting verification from {verify_url}")
        # retry on request timeout or 502 (must take no more than 3 minutes)
        # print error message on the 3rd exception and return
        for i in range(3):
            try:
                response = requests.post(verify_url, data=auth_data, timeout=60)
                if response is None:
                    break
                status = response.status_code
                if status == requests.codes.ok:  # 200
                    break
                if status == 403:
                    print("You have no permission. Please, make sure you entered a valid key.")
                    return None
                elif status == 502:
                    debug_print_("502 Bad Gateway", self.args.debug)
                    if i < 2:
                        print("Received an invalid response. Retry...")
                    else:
                        print("Oops, an error occurred when sending your request. Please try again later")
                        return None
                else:  # status != 200, 403, 502
                    output_error_response(response)
                    return None
            except requests.exceptions.Timeout:
                if i < 2:
                    print("Request timeout. Retry...")
                else:
                    print_error(TIMEOUT_MSG_PREFIX, CONTACT_CERTORA_MSG, flush=True)
                    return None
            except (requests.exceptions.RequestException, ConnectionError):
                print_conn_error()
                break
        return response

    def new_poll_output(self, lim: int = 60) -> bool:
        has_output = True
        params = ""
        next_token = ""
        result = False
        start_poll_t = time.perf_counter()
        # start animation
        self.anim_thread.start()
        s = requests.Session()

        while True:
            try:
                if next_token:  # used for retrieving the logs in chunks
                    params = "&nextToken=" + next_token

                #  if no bytes have been received for lim (seconds) requests.exceptions.Timeout is thrown
                r = s.get(self.outputUrl + params, timeout=lim)
                if r.status_code != requests.codes.ok:
                    if r.status_code != 502:
                        output_error_response(r)
                        raise requests.exceptions.RequestException
                        # raise Exception('No additional output is available')
                    else:
                        debug_print_("502 Bad Gateway", self.args.debug)
                        all_output = None
                        new_token = next_token  # keep the same token
                        status = "PROCESSED"
                else:
                    json_response = parse_json(r)
                    if not json_response:  # Error parsing json
                        print_error_and_status_url("Failed to parse response. For more information visit",
                                                   self.statusUrl)
                        break
                    if not is_success_response(json_response, self.statusUrl):  # look for execution exceptions
                        break
                    try:
                        status = json_response["status"]
                    except KeyError:
                        print_error_and_status_url("No status", self.statusUrl)
                        break
                    try:
                        new_token = json_response["nextToken"]
                    except KeyError:
                        print_error_and_status_url("No token", self.statusUrl)
                        break

                    try:
                        all_output = json_response["logEventsList"]
                    except KeyError:
                        print_error_and_status_url("No output is available.", self.statusUrl)
                        break

                if all_output:
                    has_output = True
                    self.done = True  # used for stopping the animation
                    self.anim_thread.join()  # wait for a thread
                    for outputLog in all_output:
                        msg = outputLog["message"]
                        print(msg, flush=True)
                elif has_output:  # first missing output
                    has_output = False
                    first_miss_out = time.perf_counter()  # start a timer
                else:  # missing output
                    curr_miss_out = time.perf_counter()
                    if curr_miss_out - first_miss_out > self.queue_wait_minutes * 60:  # more than N min
                        error_msg = f"There was no output for {self.queue_wait_minutes} minutes."
                        print_error_and_status_url(error_msg, '')
                        raise TimeError()
                if new_token == next_token and next_token != "":
                    if status == "SUCCEEDED" or status == "FAILED":
                        # When finished it returns the same token you passed in
                        break
                    else:  # the job is still being processed
                        time.sleep(self.log_query_frequency_seconds)
                next_token = new_token
            except requests.exceptions.Timeout:  # catch timeout and resend request
                # print("processing user request...")
                pass
            except requests.exceptions.ConnectionError:  # retry on connection error
                pass
            curr_poll_t = time.perf_counter()
            if curr_poll_t - start_poll_t > self.max_poll_minutes * 60:  # polling for more than 30 min
                error_msg = f"The contract is being processed for more than {self.max_poll_minutes} minutes"
                print_error_and_status_url(error_msg, '')
                raise TimeError()
            time.sleep(0.5)
        return result

    @staticmethod
    def upload(presigned_url: str, file_to_upload: str) -> Optional[Response]:
        """
        Uploads user contract/s as a zip file to S3

        Parameters
        ----------
        presigned_url : str
            S3 presigned url
        file_to_upload : str
            zip file name

        Returns
        -------
        Response
            S3 response - can be handled as a json object
        """
        upload_fail_msg = f"couldn't upload file - {file_to_upload}"
        try:
            with open(file_to_upload, "rb") as my_file:
                http_response = requests.put(presigned_url, data=my_file, headers={"content-type": "application/zip"})
        except ConnectionError as e:
            print_error(CONNECTION_ERR_PREFIX, upload_fail_msg)
            debug_print_(str(e))
        except requests.exceptions.Timeout as e:
            print_error(TIMEOUT_MSG_PREFIX, upload_fail_msg)
            debug_print_(str(e))
        except requests.exceptions.RequestException as e:
            print_error(GENERAL_ERR_PREFIX, upload_fail_msg)
            debug_print_(str(e))
            return None
        except OSError as e:
            print_error("OSError:", upload_fail_msg)
            debug_print_(str(e))

        return http_response

    def animate(self, status: str = "processing") -> None:
        for c in itertools.cycle(['|', '/', '-', '\\']):
            if self.done:
                break
            sys.stdout.write(f'\r{status} ' + c)
            sys.stdout.flush()
            time.sleep(0.1)
        sys.stdout.write('\r')
