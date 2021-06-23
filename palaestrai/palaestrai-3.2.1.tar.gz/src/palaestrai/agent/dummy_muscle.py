from .muscle import Muscle


class DummyMuscle(Muscle):
    def __init__(self, broker_connection, brain_connection, uid, brain_id):
        super().__init__(broker_connection, brain_connection, uid, brain_id)

    def setup(self):
        pass

    def propose_actions(self, sensors, actuators_available, is_terminal=False):
        for actuator in actuators_available:
            actuator(actuator.action_space.sample())
        return actuators_available, actuators_available

    def update(self, update):
        pass

    @property
    def parameters(self) -> dict:
        params = {
            "Broker_Connection": self.brain_connection,
            "Brain_Connection": self.brain_connection,
            "UID": self.uid,
        }
        return params

    def __repr__(self):
        pass

    def prepare_model(self):
        pass
