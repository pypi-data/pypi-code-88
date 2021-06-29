from skud_point import functions


class SkudPoint:
    def __init__(self, skud_sdk, point_number, request_current_state=None):
        self.skud_sdk = skud_sdk
        self.point_number = point_number
        self.last_states = {'ONLINE_NORMAL': None,
                            'ONLINE_LOCKED': None,
                            'ONLINE_UNLOCKED': None}
        self.current_state = None
        if request_current_state:
            self.request_current_state()

    def set_point_locked(self):
        self.skud_sdk.set_point_locked(self.point_number)
        self.request_current_state()

    def set_point_unlocked(self):
        self.skud_sdk.set_point_unlocked(self.point_number)

    def set_point_normal(self):
        self.skud_sdk.set_point_normal(self.point_number)

    def set_current_state(self, state, *args, **kwargs):
        self.current_state = state

    def get_current_state(self, *args, **kwargs):
        return self.current_state

    def set_state(self, state):
        functions.update_last_state(self.last_states, state)

    def request_current_state(self):
        current_state = self.skud_sdk.get_point_status(self.point_number)
        self.set_current_state(current_state)
        self.set_state(current_state)

