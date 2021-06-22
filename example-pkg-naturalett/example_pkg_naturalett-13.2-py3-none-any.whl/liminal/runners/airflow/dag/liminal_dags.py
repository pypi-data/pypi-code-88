#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

# from liminal.runners.airflow.dag import liminal_register_dags as liminal
import pip
installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
     for i in installed_packages])
print(installed_packages_list)

from liminal.runners.airflow.dag import liminal_register_dags
from liminal.core import environment as env
import os
import logging
import traceback

pipelines = liminal_register_dags.register_dags(os.path.join(env.get_airflow_home_dir(), env.DEFAULT_PIPELINES_SUBDIR))

for pipeline, dag in pipelines:
    try:
        globals()[pipeline] = dag
        logging.info(f'registered DAG {dag.dag_id}: {dag.tasks}')
    except Exception:
        logging.error(f'Failed to register DAGs for {pipeline}')
        traceback.print_exc()