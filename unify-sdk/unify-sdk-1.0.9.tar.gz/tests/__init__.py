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

import os
import uuid

from unify.orgadmin import OrgAdmin
from unify.properties import Properties
from unify.properties import ClusterSetting

cluster_name = "qa"
props = Properties(clusterSetting=ClusterSetting.MEMORY)

props.store_cluster(
    username=os.environ.get("username"),
    password=os.environ.get("password"),
    name=cluster_name,
    cluster=os.environ.get("cluster")
)

org_admin = OrgAdmin(props=props, cluster=cluster_name)
props.set_auth_token(
    token=org_admin.auth_token(),
    cluster=cluster_name
)
test_org = org_admin.create_organization(
    org_name="zQA-{}".format(str(uuid.uuid4()))
)

print("--------Created organization {} for testing------", format(test_org))
