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

import os
from dataclasses import dataclass
from typing import List, Optional, Dict, Any

import grpc

from ondewo.nlu import context_pb2
from ondewo.vtsi import call_log_pb2, call_log_pb2_grpc, voip_pb2, voip_pb2_grpc
from ondewo.vtsi.dataclasses.server_configurations_dataclasses import (
    CaiConfiguration,
    VtsiConfiguration,
    AudioConfiguration,
    AsteriskConfiguration,
    CallConfig,
)


def create_parameter_dict(my_dict: Dict) -> Optional[Dict[str, context_pb2.Context.Parameter]]:
    assert isinstance(my_dict, dict) or my_dict is None, "parameter must be a dict or None"
    if my_dict is not None:
        return {
            key: context_pb2.Context.Parameter(
                display_name=key,
                value=my_dict[key]
            )
            for key in my_dict
        }
    return None


@dataclass
class ConfigManager:
    """
    stores all configurations and provides access to the .client

    the helper functions in utils.py and functions defined in /dataclasses/server_configurations_dataclasses.py
        use the manager to extract information when constructing requests
    this means a separate manager instance should be used for different deployments (for example a separate instance for
    each cai project, language, etc.)
    """

    def __init__(
        self,
        config_voip: VtsiConfiguration,
        config_cai: CaiConfiguration,
        config_audio: AudioConfiguration,
        config_asterisk: AsteriskConfiguration,
    ):
        self.config_voip = config_voip
        self.config_cai = config_cai
        self.config_audio = config_audio
        self.config_asterisk = config_asterisk

        self.client = VtsiClient(manager=self)


class VtsiClient:
    """
    exposes the endpoints of the ondewo voip-server in a user-friendly way
    """

    def __init__(self, manager: ConfigManager) -> None:
        self.manager: ConfigManager = manager

        target = f"{self.manager.config_voip.host}:{self.manager.config_voip.port}"

        # create grpc service stub
        if self.manager.config_voip.secure:

            if os.path.exists(self.manager.config_voip.cert_path):
                with open(self.manager.config_voip.cert_path, "rb") as fi:
                    grpc_cert = fi.read()

            credentials = grpc.ssl_channel_credentials(root_certificates=grpc_cert)
            channel = grpc.secure_channel(target, credentials)
            print(f'Creating a secure channel to {target}')
        else:
            channel = grpc.insecure_channel(target=target)
            print(f'Creating an insecure channel to {target}')
        self.voip_stub = voip_pb2_grpc.VoipSessionsStub(channel=channel)
        self.call_log_stub = call_log_pb2_grpc.VoipCallLogsStub(channel=channel)

    @staticmethod
    def get_minimal_client(vtsi_host: str = "grpc-vtsi.ondewo.com", vtsi_port: str = 443, secure: bool = True, cert_path: Optional[str] = './grpc_cert') -> 'VtsiClient':
        if secure and not os.path.exists(cert_path):
            raise Exception("Secure connection requested, but no grpc certificate provided!")

        manager: ConfigManager = ConfigManager(
            config_voip=VtsiConfiguration(
                host=vtsi_host,
                port=int(vtsi_port),
                secure=secure,
                cert_path=cert_path,
            ),
            config_cai=CaiConfiguration(
                cai_project_id="[PLACEHOLDER]",
                cai_type="mirror"
            ),
            config_audio=AudioConfiguration(
                language_code="[PLACEHOLDER]",
                t2s_language="thorsten",
                s2t_language="german_general",
            ),
            config_asterisk=AsteriskConfiguration(),
        )
        return VtsiClient(manager=manager)

    def load_manifest(self, request: voip_pb2.VoipManifest,) -> bool:
        """
        hand a list of callers and listeners (manifest) to the voip server
        context information can be provided for the full manifest
        the voip server will load the list into its memory and wait for further instructions (like run_manifest)
        """
        print("loading manifest")
        response: voip_pb2.VoipManifestResponse = self.voip_stub.LoadManifest(request=request)
        return response.success  # type: ignore

    def run_manifest(self, manifest_id: str,) -> bool:
        """
        deploy a loaded manifest - perform the defined calls and set up the defined number of listeners
        """
        request = voip_pb2.ManifestRequest(manifest_id=manifest_id)
        print("running manifest")
        response: voip_pb2.RunManifestResponse = self.voip_stub.RunManifest(request=request)
        return response.started  # type: ignore

    def remove_manifest(self, manifest_id: str,) -> voip_pb2.RemoveManifestResponse:
        """
        remove a loaded manifest - stop any running calls, stop listeners
        """
        request = voip_pb2.ManifestRequest(manifest_id=manifest_id)
        print("removing manifest")
        response: voip_pb2.RemoveManifestResponse = self.voip_stub.RemoveManifest(request=request)
        return response

    def start_caller(self,
                     phone_number: str,
                     call_id: str,
                     sip_sim_version: str,
                     project_id: str,
                     init_text: Optional[str] = None,
                     initial_intent: Optional[str] = None,
                     contexts: Optional[List[context_pb2.Context]] = None,
                     sip_name: Optional[str] = None,
                     sip_prefix: Optional[str] = None,
                     password_dictionary: Optional[Dict] = None,
                     ) -> voip_pb2.StartCallInstanceResponse:
        """
        perform a single call
        """
        contexts = contexts if contexts else self.manager.config_cai.cai_contexts
        request = CallConfig.get_call_proto_request(
            manager=self.manager,
            call_id=call_id,
            sip_sim_version=sip_sim_version,
            phone_number=phone_number,
            project_id=project_id,
            init_text=init_text,
            initial_intent=initial_intent,
            contexts=contexts,
            sip_name=sip_name,
            sip_prefix=sip_prefix,
            password_dictionary=password_dictionary,
        )
        print("performing call")
        response: voip_pb2.StartCallInstanceResponse = self.voip_stub.StartCallInstance(request=request)
        return response

    def stop_caller(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop an ongoing caller instance
        """
        return self._stop_call(call_id=call_id, sip_id=sip_id)

    def stop_call(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop an ongoing call
        """
        return self._stop_call(call_id=call_id, sip_id=sip_id)

    def start_listener(self,
                       project_id: str,
                       call_id: str,
                       sip_sim_version: str,
                       init_text: Optional[str] = None,
                       initial_intent: Optional[str] = None,
                       contexts: Optional[List[context_pb2.Context]] = None,
                       sip_name: Optional[str] = None,
                       ) -> voip_pb2.StartCallInstanceResponse:
        """
        start an ondewo-sip-sim instance to listen for calls
        """
        contexts = contexts if contexts else self.manager.config_cai.cai_contexts
        request = CallConfig.get_call_proto_request(
            manager=self.manager,
            call_id=call_id,
            sip_sim_version=sip_sim_version,
            project_id=project_id,
            init_text=init_text,
            initial_intent=initial_intent,
            contexts=contexts,
            sip_name=sip_name,
        )
        print("starting listener")
        response: voip_pb2.StartCallInstanceResponse = self.voip_stub.StartCallInstance(request=request)
        return response

    def stop_listener(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop a listener instance
        """
        return self._stop_call(call_id=call_id, sip_id=sip_id)

    def _stop_call(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None,
    ) -> bool:
        """
        stop a call instance
        """
        if call_id:
            request = voip_pb2.StopCallInstanceRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.StopCallInstanceRequest(sip_id=sip_id)
        else:
            raise ValueError("either call_id or sip_id needs to be specified!")
        print("stopping call")
        response: voip_pb2.StopCallInstanceResponse = self.voip_stub.StopCallInstance(request=request)
        return response.success  # type: ignore

    def start_multiple_call_instances(
            self,
            phone_numbers_by_call_ids: Dict[str, str],
            call_ids: List[str],
            sip_sim_version: str,
            project_id: str,
            init_text: Optional[str] = None,
            initial_intent: Optional[str] = None,
            contexts: Optional[List[context_pb2.Context]] = None,
            sip_names_by_call_ids: Optional[Dict[str, str]] = None,
            sip_prefix: Optional[str] = None,
            password_dictionary: Optional[Dict] = None,
    ) -> voip_pb2.StartMultipleCallInstancesResponse:
        call_request_list: List[Any] = []
        for call_id in call_ids:
            sip_name = sip_names_by_call_ids[
                call_id] if sip_names_by_call_ids and call_id in sip_names_by_call_ids else None
            if call_id in phone_numbers_by_call_ids:
                request = CallConfig.get_call_proto_request(
                    manager=self.manager,
                    call_id=call_id,
                    sip_sim_version=sip_sim_version,
                    phone_number=phone_numbers_by_call_ids[call_id],
                    project_id=project_id,
                    init_text=init_text,
                    initial_intent=initial_intent,
                    contexts=contexts or self.manager.config_cai.cai_contexts,
                    sip_name=sip_name,
                    sip_prefix=sip_prefix,
                    password_dictionary=password_dictionary,
                )
                print(f"start caller request added for sip_name {sip_name} to call "
                      f"phone number {phone_numbers_by_call_ids[call_id]}")
            else:
                request = CallConfig.get_call_proto_request(
                    manager=self.manager,
                    call_id=call_id,
                    sip_sim_version=sip_sim_version,
                    project_id=project_id,
                    init_text=init_text,
                    initial_intent=initial_intent,
                    contexts=contexts or self.manager.config_cai.cai_contexts,
                    sip_name=sip_name,
                    password_dictionary=password_dictionary,
                )
                print(f"start listener request added for sip_name {sip_name}")
            call_request_list.append(request)

        print("performing multiple calls")
        request_to_pass = voip_pb2.StartMultipleCallInstancesRequest(
            requests=call_request_list
        )
        response: voip_pb2.StartMultipleCallInstancesResponse = \
            self.voip_stub.StartMultipleCallInstances(request=request_to_pass)

        return response

    def get_instance_status(self, call_id: Optional[str] = None, sip_id: Optional[str] = None,) -> voip_pb2.VoipStatus:
        """
        stop a listener instance
        """
        if call_id:
            request = voip_pb2.GetVoipStatusRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.GetVoipStatusRequest(sip_id=sip_id)
        else:
            raise ValueError("either call_id or sip_id needs to be specified!")
        print("getting instance status")
        response: voip_pb2.VoipStatus = self.voip_stub.GetInstanceStatus(request=request)
        return response

    def update_services_status(
        self, call_id: Optional[str] = None, sip_id: Optional[str] = None, manifest_id: Optional[str] = None,
    ) -> voip_pb2.UpdateServicesStatusResponse:
        """
        send update requests to speech-to-text, asterisk, text-to-speech and cai, which can then be retrieved by
            get_instance_status() or
            get_manifest_status()
        """
        if call_id:
            request = voip_pb2.UpdateServicesStatusRequest(call_id=call_id)
        elif sip_id:
            request = voip_pb2.UpdateServicesStatusRequest(sip_id=sip_id)
        elif manifest_id:
            request = voip_pb2.UpdateServicesStatusRequest(manifest_id=manifest_id)
        else:
            raise ValueError("either call_id, sip_id or manifest_id needs to be specified!")
        print("updating services' status")
        response: voip_pb2.UpdateServicesStatusResponse = self.voip_stub.UpdateServicesStatus(request=request)
        return response

    def get_call_ids(self) -> List[str]:
        """
        get all call_ids known to the voip manager
        """
        request = voip_pb2.GetCallIDsRequest()
        response: voip_pb2.GetCallIDsResponse = self.voip_stub.GetCallIDs(request=request)
        call_ids = []
        for call_id in response.call_ids:
            call_ids.append(call_id)
        return call_ids

    def get_session_id(self, call_id: str) -> str:
        """
        get session id by call id
        """
        request = voip_pb2.GetSessionIDRequest(
            call_id=call_id
        )
        response: voip_pb2.GetSessionIDResponse = self.voip_stub.GetSessionID(request=request)
        return response.session_id

    def shutdown_unhealthy_calls(self) -> bool:
        """
        shutdown any deployed call instances with unhealthy overall voip status
        """
        request = voip_pb2.ShutdownUnhealthyCallsRequest()
        response: voip_pb2.ShutdownUnhealthyCallsResponse = self.voip_stub.ShutdownUnhealthyCalls(request=request)
        return response.success     # type: ignore

    def activate_call_logs(self) -> call_log_pb2.SaveCallLogsResponse:
        """
        activate call logs globally for the voip manager
        """
        request = call_log_pb2.SaveCallLogsRequest()
        response: call_log_pb2.SaveCallLogsResponse = self.call_log_stub.ActivateSaveCallLogs(request=request)
        return response

    def get_voip_log(self, call_id: str) -> call_log_pb2.GetVoipLogResponse:
        """
        get the call log of a sip-sim instance
        """
        request = call_log_pb2.GetVoipLogRequest(call_id=call_id)
        response: call_log_pb2.GetVoipLogResponse = self.call_log_stub.GetVoipLog(request=request)
        return response

    def deploy_precondition_image(
        self, sip_sim_version: str, asterisk_host: str, asterisk_port: Optional[int] = None,
    ) -> bool:
        """
        deploy the 'precondition-for-working-setup' sip image
        """
        request = voip_pb2.DeployPreconditionRequest(
            sip_sim_version=sip_sim_version,
            asterisk_config=voip_pb2.ServiceConfig(
                host=asterisk_host,
                port=asterisk_port,
            )
        )
        response: voip_pb2.DeployPreconditionResponse = self.voip_stub.DeployPreconditionForWorkingSetup(
            request=request
        )
        return response.success  # type: ignore
