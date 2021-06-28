import argparse
import os
import sys
from pathlib import Path

import requests

health_check_file = "/tmp/healthcheck"

parser = argparse.ArgumentParser(description='Healthcheck')
parser.add_argument('url', help='URL to GET for testing.')
args = parser.parse_args()

if not(os.path.exists(health_check_file)):
    try:
        status_code = requests.get(args.url).status_code
        if status_code != 200:
            sys.exit(1)
    except Exception:
        sys.exit(1)

    Path(health_check_file).touch()
