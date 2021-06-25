# Copyright 2021 ONDEWO GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import uuid
from typing import List

from ondewo.nlu import context_pb2
from ondewo.vtsi import voip_pb2

from ondewo.vtsi.dataclasses.server_configurations_dataclasses import CallConfig
from ondewo.vtsi.voip_server_client import ConfigManager


def create_manifest(
    manager: ConfigManager,
    manifest_id: str,
    sip_sim_version: str,
    project_id: str,
    contexts: List[context_pb2.Context],
    numbers_to_call: List[str],
    number_of_listeners: int,
) -> voip_pb2.VoipManifest:
    """create a manifest of callers and listeners to deploy"""
    callers = []
    for phone_number in numbers_to_call:
        call_id = str(uuid.uuid4())
        callers.append(
            CallConfig.get_caller_proto_request(
                manager=manager,
                phone_number=phone_number,
                project_id=project_id,
                contexts=contexts,
                call_id=call_id,
                sip_sim_version=sip_sim_version,
            )
        )
    listeners = []
    for _ in range(0, number_of_listeners):
        call_id = str(uuid.uuid4())
        listeners.append(
            CallConfig.get_listener_proto_request(
                manager=manager,
                project_id=project_id,
                call_id=call_id,
                sip_sim_version=sip_sim_version,
                init_text="",
            )
        )
    return voip_pb2.VoipManifest(manifest_id=manifest_id, contexts=contexts, callers=callers, listeners=listeners,)
