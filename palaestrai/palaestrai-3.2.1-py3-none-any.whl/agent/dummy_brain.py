from palaestrai.core.protocol import MuscleUpdateResponse

from .brain import Brain


class DummyBrain(Brain):
    def __init__(
        self,
        muscle_connection: str,
        sensors,
        actuators,
        objective,
        store_path,
        seed: int,
        **params,
    ):
        super().__init__(
            muscle_connection,
            sensors,
            actuators,
            objective,
            store_path,
            seed,
            **params,
        )

    def thinking(self, muscle_id, readings, actions, reward, done):
        response = MuscleUpdateResponse(False, None)
        return response

    def store_model(self, path):
        pass

    def load_model(self, path):
        pass
