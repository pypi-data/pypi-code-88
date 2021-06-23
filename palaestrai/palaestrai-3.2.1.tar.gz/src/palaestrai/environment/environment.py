"""This module contains the abstract class :class:`Environment` that
is used to implement a new environment.

"""
import signal
from abc import ABC, abstractmethod
from typing import List, Tuple, Union, Sequence

from palaestrai.core import MajorDomoWorker
from palaestrai.core.protocol import (
    EnvironmentResetRequest,
    EnvironmentResetResponse,
    EnvironmentShutdownRequest,
    EnvironmentShutdownResponse,
    EnvironmentStartRequest,
    EnvironmentStartResponse,
    EnvironmentUpdateRequest,
    EnvironmentUpdateResponse,
)

from ..agent import ActuatorInformation, SensorInformation
from . import LOG


class Environment(ABC):
    """Abstract class for environment implementation

    This abstract calls provides all necessary functions needed
    to implement a new environment. The developer only has to
    implement the functions start_environment and update.

    Parameters
    ----------
    connection : str
        URI used to connect to the simulation broker
    uid : uuid4
        Unique identifier to identify an environment
    seed : int
        Seed for recreation
    params : dict
        Dictionary of additional needed parameters
    """

    def __init__(self, connection, uid, reward, seed: int, params=None):
        self._ctx = None
        self.broker_connection = connection
        self.uid = uid
        self.seed = seed
        self.reward = reward
        self._worker = None

        self.params = params
        self.sensors: List[SensorInformation] = []
        self.actuators: List[ActuatorInformation] = []

        if params is not None:
            self.name = params.get("name", uid)
        else:
            self.name = uid

        # Filter lists for incoming actuators
        self._sensor_ids: List[str] = list()
        self._actuator_ids: List[str] = list()

        self.is_terminal = False
        LOG.debug(
            "Environment %s(id=0x%x, uid=%s) created.",
            self.__class__,
            id(self),
            self.uid,
        )

    @property
    def worker(self):
        """Return the major domo worker.

        The worker will be created if necessary.
        """

        if self._worker is None:
            self._worker = MajorDomoWorker(
                self.broker_connection,
                self.uid,
            )
        return self._worker

    def _handle_sigintterm(self, signum, frame):
        LOG.info(
            "Environment %s(id=0x%x, uid=%s) interrupted by signal %s in "
            "frame %s.",
            self.__class__,
            id(self),
            self.uid,
            signum,
            frame,
        )
        raise SystemExit()

    async def run(self):
        """Main function for message handling

        This is the main function of the environment. It receives
        and processes incoming messages and calls the requested functions
        it also returns the responses.
        """
        reply = None
        signal.signal(signal.SIGINT, self._handle_sigintterm)
        signal.signal(signal.SIGTERM, self._handle_sigintterm)

        LOG.info(
            "Environment %s(id=0x%x, uid=%s) commencing run.",
            self.__class__,
            id(self),
            self.uid,
        )
        while not self.is_terminal:
            try:
                request = await self.worker.transceive(reply)
            except SystemExit:
                LOG.critical(
                    "Environment %s(id=0x%x, uid=%s) "
                    "interrupted in transceive by SIGINT/SIGTERM, "
                    "existing run loop",
                    self.__class__,
                    id(self),
                    self.uid,
                )
                break

            LOG.debug(
                "Environment %s(id=0x%x, uid=%s) received message: %s",
                self.__class__,
                id(self),
                self.uid,
                request,
            )
            if request is None:
                break
            elif isinstance(request, EnvironmentStartRequest):
                reply = self._handle_setup(request)
            elif isinstance(request, EnvironmentUpdateRequest):
                reply = self._handle_update(request)
            elif isinstance(request, EnvironmentResetRequest):
                reply = self._handle_reset(request)
            elif isinstance(request, EnvironmentShutdownRequest):
                reply = self._handle_shutdown(request)

        await self.worker.transceive(reply, skip_recv=True)
        LOG.info(
            "Environment %s(id=0x%x, uid=%s) completed shutdown: "
            "so much fun we had.",
            self.__class__,
            id(self),
            self.uid,
        )

    def _handle_setup(
        self, request: EnvironmentStartRequest
    ) -> EnvironmentStartResponse:
        """Handle an environment start request.

        The :meth:`start_environment` is called that can be used by
        environments for setup purposes and that should provide the
        available sensors and actuators.

        Finally, an start response is prepared.

        Parameters
        ----------
        request: EnvironmentStartRequest
            The start request from the simulation controller.

        Returns
        -------
        EnvironmentStartResponse
            The answer from the environment, contains the available
            sensors and actuators.

        """
        LOG.info(
            "Environment %s(id=0x%x, uid=%s) received "
            "EnvironmentStartRequest("
            "experiment_run_id=%s, environment_id=%s).",
            self.__class__,
            id(self),
            self.uid,
            request.run_id,
            request.environment_id,
        )
        # TODO: self.sensors?
        sensors, actuators = self.prepend_identifier(*self.start_environment())
        self._sensor_ids = [sen.sensor_id for sen in sensors]
        self._actuator_ids = [act.actuator_id for act in actuators]

        msg = EnvironmentStartResponse(
            request.run_id, self.uid, sensors, actuators
        )
        LOG.debug(
            "Environment %s(id=0x%x, uid=%s) sending "
            "EnvironmentStartResponse(experiment_run_id=%s, "
            "environment_id=%s, sensors=%s, actuators=%s)",
            self.__class__,
            id(self),
            self.uid,
            msg.run_id,
            msg.environment_id,
            sensors,
            actuators,
        )
        return msg

    def _handle_update(
        self, request: EnvironmentUpdateRequest
    ) -> EnvironmentUpdateResponse:
        """Handle an environment update request.

        The request contains current actuator values and the
        environment receives the actuator values in the update method.
        The environment answers with updated sensor readings, an
        environment reward, and the done flag, whether the
        environment has finished or not.

        Finally, an update response is prepared.

        Parameters
        ----------
        request: EnvironmentUpdateRequest
            The update request from the simulation controller, contains
            the current actuator values from one or more agent.

        Returns
        -------
        EnvironmentUpdateResponse
            The response for the simulation controller, containing the
            updated sensor values, a reward, and the done flag.

        """

        sensors, done = self.update(
            [
                act
                for act in request.actuators
                if act.actuator_id in self._actuator_ids
            ]
        )

        (sensors,) = self.prepend_identifier(sensors)

        reward = self.reward(state=sensors)

        return EnvironmentUpdateResponse(
            sender_environment_id=self.uid,
            receiver_simulation_controller_id=request.sender,
            experiment_run_id=request.experiment_run_id,
            environment_conductor_id=request.environment_conductor_id,
            sensors=sensors,
            reward=reward,
            is_terminal=done,
        )

    def _handle_reset(
        self, request: EnvironmentResetRequest
    ) -> EnvironmentResetResponse:
        """Handle an environment reset request.

        The actual behavior of the restart is delegated to the method
        :meth:`reset`.

        Parameters
        ----------
        request: EnvironmentResetRequest
            The reset request send by the simulation controller.

        Returns
        -------
        EnvironmentResetResponse
            The response for the simulation controller.

        """
        LOG.info(
            "Environment %s(id=0x%x, uid=%s) performing a reset due to "
            "EnvironmentResetRequest(simulation_controller_id=%s, "
            "environment_id=%s).",
            self.__class__,
            id(self),
            self.uid,
            request.sender,
            request.receiver,
        )
        return self.reset(request)

    def _handle_shutdown(
        self, request: EnvironmentShutdownRequest
    ) -> EnvironmentShutdownResponse:
        """Handle an environment shutdown request.

        The :meth:`shutdown` is called that handles the shutdown of the
        environment. Finally, a shutdown response is prepared.

        Parameters
        ----------
        request: EnvironmentShutdownRequest
            The shutdown request from the simulation controller.

        Returns
        -------
        EnvironmentShutdownResponse
            The shutdown response for the simulation controller.

        """
        LOG.info(
            "Environment %s(id=0x%x, uid=%s) now handling shutdown.",
            self.__class__,
            id(self),
            self.uid,
        )
        _ = self.shutdown()
        return EnvironmentShutdownResponse(request.run_id, self.uid, True)

    @abstractmethod
    def start_environment(
        self,
    ) -> Tuple[List[SensorInformation], List[ActuatorInformation]]:
        """Function to start the environment

        If the environment uses a simulation tool, this function
        can be used to initiate the simulation tool. Otherwise this
        function is used to prepare the environment for the simulation.
        It must be able to provide initial sensor information.

        On a reset, this method is called to restart a new environment
        run. Therefore, it also must provide initial values for all
        variables used!

        Returns
        -------
        tuple(List[SensorInformation], List[ActuatorInformation])
            A tuple containing a list of available sensors and a list
            of available actuators.

        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self, actuators: List[ActuatorInformation]
    ) -> Tuple[List[SensorInformation], bool]:
        """Function to update the environment

        This function receives the agent's actions and has to respond
        with new sensor information. This function should create a
        new simulation step.

        Parameters
        ----------
        actuators : list[ActuatorInformation]
            List of actuators with setpoints

        Returns
        -------
        tuple[list[SensorInformation], bool]
            A tuple containing a list of SensorInformation and a flag
            whether the environment has terminated.

        """
        raise NotImplementedError

    def reset(
        self, request: EnvironmentResetRequest
    ) -> EnvironmentResetResponse:
        """Reset the environment (in process).

        The default behavior for a reset comprises:

            * calling shutdown to allow a graceful shutdown of
              environment simulation processes
            * calling start_environment again
            * preparing the EnvironmentResetResponse

        If an environment requires a more special reset procedure,
        this method can be overwritten.

        Parameters
        ----------
        request: EnvironmentResetRequest
            The reset request send by the simulation controller.

        Returns
        -------
        EnvironmentResetResponse
            The response for the simulation controller.

        """
        # Allow graceful shutdown ...
        self.shutdown(reset=True)
        LOG.debug(
            "Environment %s(id=0x%x, uid=%s) stopped the leftovers "
            "of the previous run. Initiating a new run now.",
            self.__class__,
            id(self),
            self.uid,
        )
        # ... but do not break the main loop
        self.is_terminal = False
        sensors, actuators = self.prepend_identifier(*self.start_environment())

        LOG.debug(
            "Environment %s(id=0x%x, uid=%s) restarted successfully.",
            self.__class__,
            id(self),
            self.uid,
        )

        return EnvironmentResetResponse(
            receiver_simulation_controller_id=request.sender,
            sender_environment_id=self.uid,
            create_new_instance=False,
            sensors=sensors,
            actuators=actuators,
        )

    def shutdown(self, reset: bool = False) -> bool:
        """Initiate the environment shutdown.

        In this function the :attr:`.is_terminal` is set to True, which
        leads to a break of the main loop in the :meth:`.run` method.

        Parameters
        ----------
        reset: bool, optional
            Is set to True when only a reset is required. A concrete
            environment may distinguish between reset and shutdown.

        Returns
        -------
        bool
            *True* if the shutdown was successful, *False* otherwise.

        """
        self.is_terminal = not reset
        return True

    def prepend_identifier(
        self,
        *information: Sequence[Union[SensorInformation, ActuatorInformation]],
    ):
        """Append the environment identifier to the ids of a list of information objects

        :param information: a list of lists of SensorInformation or ActuatorInformation
        :return: the altered list(s)
        """

        for inf_list in information:
            for i in inf_list:
                i.id = f"{self.params['identifier']}.{i.id}"
        return information
