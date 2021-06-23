import unittest
from unittest.mock import patch

import palaestrai.core.protocol
from palaestrai.store.receiver import StoreReceiver


class TestReceiver(unittest.TestCase):
    @patch("palaestrai.core.RuntimeConfig")
    def test_handles_all_protocol_messages(self, _):
        # Ideally, we should explicitly handle *all* message types in the
        # store receiver. I.e., everything that is defined in the module:
        # all_message_types = [
        #    t for t in palaestrai.core.protocol.__dir__()
        #    if t.endswith("Request") or t.endswith("Response")
        # ]
        # ...but until we do, we need to go with a curated list instead.
        # Simply setting all hitherto unknown types to "None" in the
        # receiver is *not* an option, as it will never indicate that there
        # are still sime types not considered.
        all_message_types = [
            palaestrai.core.protocol.ExperimentRunStartRequest,
            palaestrai.core.protocol.ExperimentRunStartResponse,
            palaestrai.core.protocol.ExperimentRunShutdownRequest,
            palaestrai.core.protocol.ExperimentRunShutdownResponse,
            palaestrai.core.protocol.SimulationStartRequest,
            palaestrai.core.protocol.SimulationStartResponse,
            palaestrai.core.protocol.SimulationControllerTerminationRequest,
            palaestrai.core.protocol.SimulationControllerTerminationResponse,
            palaestrai.core.protocol.SimulationStopRequest,
            palaestrai.core.protocol.SimulationStopResponse,
            palaestrai.core.protocol.EnvironmentSetupRequest,
            palaestrai.core.protocol.EnvironmentSetupResponse,
            palaestrai.core.protocol.EnvironmentStartRequest,
            palaestrai.core.protocol.EnvironmentStartResponse,
            palaestrai.core.protocol.EnvironmentUpdateRequest,
            palaestrai.core.protocol.EnvironmentUpdateResponse,
            palaestrai.core.protocol.EnvironmentResetRequest,
            palaestrai.core.protocol.EnvironmentResetResponse,
            palaestrai.core.protocol.EnvironmentResetNotificationRequest,
            palaestrai.core.protocol.EnvironmentResetNotificationResponse,
            palaestrai.core.protocol.EnvironmentShutdownRequest,
            palaestrai.core.protocol.EnvironmentShutdownResponse,
            palaestrai.core.protocol.AgentSetupRequest,
            palaestrai.core.protocol.AgentSetupResponse,
            palaestrai.core.protocol.AgentUpdateRequest,
            palaestrai.core.protocol.AgentUpdateResponse,
            palaestrai.core.protocol.AgentShutdownRequest,
            palaestrai.core.protocol.AgentShutdownResponse,
            palaestrai.core.protocol.MuscleUpdateRequest,
            palaestrai.core.protocol.MuscleUpdateResponse,
            palaestrai.core.protocol.ShutdownRequest,
            palaestrai.core.protocol.ShutdownResponse,
            palaestrai.core.protocol.NextPhaseRequest,
            palaestrai.core.protocol.NextPhaseResponse,
        ]
        receiver = StoreReceiver(queue=None)
        for t in all_message_types:
            try:
                _ = receiver._message_dispatch[t]
            except KeyError:
                self.fail(
                    f"Message type {t} raises key error known to the store "
                    f"dispatcher."
                )


if __name__ == "__main__":
    unittest.main()
