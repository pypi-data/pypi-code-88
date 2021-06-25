# -*- coding: utf-8 -*-


import click
import os
import requests
import sys
import logging
import json
from time import sleep


from tpcli.exceptions import (
    UnknownTokenError,
    NoAuthorizationError,
    FileConflictError,
)

UPLOAD_QUEUE = []
PRESIGNED = []
RESULTS = {}
RETRIES = 1
WAITTIME = 10


def good_response(code):
    if code in [200, 204]:
        return True
    return False


def scan_for_files(target):
    myfiles = []

    if os.path.isdir(target):
        entries = os.walk(target)
        for e in entries:
            (dirname, subdirs, files) = e
            # all all files in this dir
            myfiles.extend([os.path.join(dirname, x) for x in files])
            # scan through the subdirs recursively
            for d in subdirs:
                myfiles.extend(scan_for_files(os.path.join(dirname, d)))
    elif os.path.isfile(target):
        myfiles.append(target)
    else:
        raise Exception(
            "Unknown filetype included.. {0}... skipping".format(target)
        )

    return myfiles


def list_server_buckets(url, token=None):
    headers = {"X-tuxput-token": token}
    full_url = url + "buckets"
    resp = requests.get(full_url, headers=headers)

    return resp.content


def list_server_authorizations(url, token=None):
    headers = {"X-tuxput-token": token}
    full_url = url + "authorizations"
    resp = requests.get(full_url, headers=headers)

    return resp.content


def get_presigned_url(url, token, upload_file, bucket=None):
    retries = RETRIES
    headers = {"X-tuxput-token": token}
    if bucket is not None:
        headers["X-tuxput-bucket"] = bucket
    full_url = url + "/" + upload_file
    while retries > 0:
        retries -= 1

        logging.info(
            "sending req to {0}/{1} -- attempt {2}/{3}".format(
                url, upload_file, retries, RETRIES
            )
        )

        resp = requests.post(full_url, headers=headers)
        logging.debug("<- response {0}".format(resp.status_code))
        # if successful, we can just duck out
        if good_response(resp.status_code):
            logging.info("presigned url successful")
            return resp

        # can't login, so.. bad token.  Let's bail.
        if resp.status_code == 401:
            logging.debug("raising UnknownTokenError")
            raise UnknownTokenError
        # we don't have permission for this upload.
        elif resp.status_code == 403:
            logging.debug("raising NoAuthorizationError")
            raise NoAuthorizationError
        # file already exists
        elif resp.status_code == 409:
            logging.debug("raising FileConflictError")
            raise FileConflictError

        # Any other problem is most likely an internal server error
        # or a another transient problem... hang out for a second and
        # try it again
        logging.info(
            " waiting for retry {0}/{1} in {2}s".format(
                RETRIES - retries, RETRIES, WAITTIME
            )
        )
        sleep(WAITTIME)

    # If we get here, then we've failed all retries and still haven't been
    # successful.  Let's return the last response and let the caller figure it
    # out
    return resp


def do_s3_upload(presigned, upload_file):
    files = {}
    files["file"] = (upload_file, open(upload_file, "rb"))
    pdata = presigned.json()

    logging.info("Posting to S3..")
    resp = requests.post(pdata["url"], data=pdata["fields"], files=files)
    logging.info(" returned {0}".format(resp.status_code))
    return resp


@click.command()
@click.argument("url", nargs=1)
@click.argument("targets", nargs=-1)
@click.option("--dry-run", "-n", default=False, is_flag=True)
@click.option("--token", "-t", required=True, type=str)
@click.option("--bucket", "-b", required=False, type=str)
@click.option(
    "--list_buckets", "-l", required=False, default=False, is_flag=True
)
@click.option(
    "--list_auths", "-A", required=False, default=False, is_flag=True
)
@click.option("--sign-only", "-s", default=False, is_flag=True)
def tuxput_cli(
    url, targets, dry_run, token, bucket, list_buckets, list_auths, sign_only
):

    if list_buckets:
        print(list_server_buckets(url, token))
        return

    if list_auths:
        print(list_server_authorizations(url, token))
        return

    # collect the files we'll be uploading
    for t in targets:
        UPLOAD_QUEUE.extend(scan_for_files(t))

    for f in UPLOAD_QUEUE:
        logging.info("-- Processing {0}".format(f))

        if dry_run:
            logging.debug("dry-run enabled... skipping")
            continue

        presigned = None
        try:
            presigned = get_presigned_url(url, token, f, bucket)
            if not good_response(presigned.status_code):
                # server errors that the timeout/retry couldn't resolve.  Log
                # the fail and move on.
                RESULTS[
                    f
                ] = "Failed to get presigned URL:  {0}{1}... skipping".format(
                    f, presigned.status_code
                )
                continue
            else:
                PRESIGNED.append({f: presigned.json()})
                RESULTS[f] = "presigned URL created '{0}'".format(
                    presigned.status_code
                )
        except requests.exceptions.ConnectionError as e:
            # server's not there, so don't bother with the rest
            logging.error("unable to contact server: {0}".format(e))
            sys.exit(1)
        except UnknownTokenError:
            # token is invalid, so no point trying to upload the others
            logging.error("invalid token")
            sys.exit(1)
        except FileConflictError:
            RESULTS[f] = "{0} file already exists".format(f)
            continue
        except NoAuthorizationError:
            # Not necessarily fatal.  Log the fail and move on.
            RESULTS[f] = "no authorization to get presigned url"
            continue

        if sign_only:
            logging.info("presigned only... skipping do_s3_upload")
            continue

        if presigned is not None:
            upload = do_s3_upload(presigned, f)
            if not good_response(upload.status_code):
                RESULTS[f] = " failed to upload to AWS: {0}: {1}".format(
                    upload.status_code, upload.text
                )
            else:
                RESULTS[f] = " uploaded to AWS: {0}".format(upload.status_code)

    if sign_only:
        print(json.dumps(PRESIGNED, indent=2))

    print("Results\n--------------")
    for x in RESULTS:
        print("{0} -{1}".format(x, RESULTS[x]))


# TODO possibly in version 2.0?
# --pre/-p pre-run command
# --post/-P post-run command
# --exclude/-x  exclude file or pattern from the targets list


if __name__ == "__main__":
    tuxput_cli(auto_envvar_prefix="TUXPUT_CLI")
