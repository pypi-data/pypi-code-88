# Copyright 2021 Element Analytics, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Common utils for agents
"""
from datetime import datetime
import io
import csv

def serialize_csv(fieldnames, jsons):
    """
    Convert json of contents into string
    """
    csv_output = io.StringIO()
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()
    for json_obj in jsons:
        writer.writerow(json_obj)
    csv_str = csv_output.getvalue()
    csv_output.close()
    return csv_str

def save_csv(name, text):
    """
    Write text to file
    """
    with open(name, "a") as csv_file:
        csv_file.write(text)


def get_name(prefix):
    """
    Construct name with current timestamp
    """
    time_stamp = datetime.utcnow().strftime("%H-%M-%S")
    return '{}-{}'.format(prefix, time_stamp)
