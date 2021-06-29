from skud_point.main import SkudPoint


class GBarrier(SkudPoint):
    def __init__(self, point_number, skud_sdk, *args, **kwargs):
        super().__init__(skud_sdk, point_number, *args, **kwargs)

    def open_barrier(self):
        self.skud_sdk.open_gate(self.point_number)

    def close_barrier(self):
        self.skud_sdk.open_gate(self.point_number)
