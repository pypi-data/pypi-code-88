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
from dataclasses import dataclass, field
from typing import List, TYPE_CHECKING, Optional, Dict

from ondewo.nlu import context_pb2
from ondewo.vtsi import voip_pb2
from ondewo.vtsi.voip_pb2 import ServiceConfig

from google.protobuf.struct_pb2 import Struct

if TYPE_CHECKING:
    from ondewo.vtsi.client import ConfigManager


@dataclass
class AudioConfiguration:
    """language and location of audio services (s2t, t2s)"""

    # text-to-speech
    t2s_host: str = "grpc-t2s.ondewo.com"
    t2s_port: int = 443
    t2s_type: str = "ONDEWO"

    # speech-to-text
    s2t_host: str = "grpc-s2t.ondewo.com"
    s2t_port: int = 443
    s2t_type: str = "ONDEWO"

    language_code: Optional[str] = None
    t2s_language: Optional[str] = None
    s2t_language: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.t2s_language:
            self.t2s_language = self.language_code

        if not self.s2t_language:
            self.s2t_language = self.language_code


@dataclass
class CaiConfiguration:
    """location of cai"""

    cai_project_id: str
    cai_contexts: List[context_pb2.Context] = field(default_factory=list)

    host: str = "grpc-nlu.ondewo.com"
    port: int = 443
    context_session_id: str = str(uuid.uuid4())  # overwritten by sip-sim
    cai_type: str = ""  # can be set to "mirror" to activate CAI="mirror" environment variable when deploying sip-sim
    cai_language: str = "de"


@dataclass
class AsteriskConfiguration:
    """location of asterisk"""

    host: str = "127.0.0.1"
    port: int = 5060  # unused / not transferred (hardcoded in sip-sim)


@dataclass
class VtsiConfiguration:
    """location of voip server"""
    host: str = "grpc-vtsi.ondewo.com"
    port: int = 443
    secure: bool = False
    cert_path: str = ''


class CallConfig:
    """
    provides functions to create
        StartCallInstanceRequest
    requests from data in the ConfigManager
    """

    @staticmethod
    def get_call_proto_request(
            manager: "ConfigManager",
            project_id: str,
            call_id: str,
            sip_sim_version: str,
            init_text: str,
            initial_intent: str,
            contexts: List[context_pb2.Context],
            phone_number: Optional[str] = None,
            sip_name: Optional[str] = None,
            sip_prefix: Optional[str] = None,
            password_dictionary: Optional[Dict[str, str]] = None,
    ):
        password_struct = Struct()
        if password_dictionary:
            password_struct.update(password_dictionary)
        return voip_pb2.StartCallInstanceRequest(
            call_id=call_id,
            project_id=project_id,
            sip_sim_version=sip_sim_version,
            phone_number=phone_number,
            contexts=contexts,
            init_text=init_text,
            initial_intent=initial_intent,
            sip_name=sip_name,
            sip_prefix=sip_prefix,
            password_dictionary=password_struct,
            asterisk_config=ServiceConfig(
                host=manager.config_asterisk.host, port=manager.config_asterisk.port,
                service_identifier="asterisk",
            ),
            cai_config=ServiceConfig(
                language_code=manager.config_cai.cai_language,
                host=manager.config_cai.host,
                port=manager.config_cai.port,
                service_identifier=manager.config_cai.cai_type,
            ),
            stt_config=ServiceConfig(
                language_code=manager.config_audio.s2t_language,
                host=manager.config_audio.s2t_host,
                port=manager.config_audio.s2t_port,
                service_identifier=manager.config_audio.s2t_type,
            ),
            tts_config=ServiceConfig(
                language_code=manager.config_audio.t2s_language,
                host=manager.config_audio.t2s_host,
                port=manager.config_audio.t2s_port,
                service_identifier=manager.config_audio.t2s_type,
            ),
        )


@dataclass
class Manifest:
    manifest_id: str
    contexts: List[context_pb2.Context]
    calles: List[voip_pb2.StartCallInstanceRequest]
