"""This module handles Misty's movement."""
from typing import Dict

from misty2py.robot import Misty


class Movement:
    """Handles Misty's movement."""

    def __init__(
        self,
        max_velocity=100,
        min_velocity=1,
        stagnant_velocity=0,
        max_angle=100,
        min_angle=1,
        stagnant_angle=0,
    ) -> None:
        """Initialises the Movement class.

        Args:
            max_velocity (int, optional): The maximal allowed velocity. Defaults to `100`.
            min_velocity (int, optional): The minimal allowed velocity that is not stagnant. Defaults to `1`.
            stagnant_velocity (int, optional): The stagnant velocity. Defaults to `0`.
            max_angle (int, optional): The maximum turning angle. Defaults to `100`.
            min_angle (int, optional): The minimum turning angle that is not equal to the straight line driving. Defaults to `1`.
            stagnant_angle (int, optional): The angle equal to the straight line driving. Defaults to `0`.
        """
        self.max_velocity = max_velocity
        self.min_velocity = min_velocity
        self.stagnant_velocity = stagnant_velocity
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.stagnant_angle = stagnant_angle

    def _parse_value(
        self,
        value: int,
        max: int,
        min: int,
        negative: bool = False,
        negatives_allowed: bool = False,
    ) -> int:
        """Parses a velocity or angle value based on the minimum / maximum
        values and the stagnant values.

        Args:
            value (int): the input value.
            max (int): the maximal allowed value.
            min (int): the minimal allowed value.
            negative (bool, optional): Whether the input value should be transformed into its negative. Defaults to `False`.
            negatives_allowed (bool, optional): Whether an input value can be negative. Defaults to `False`.

        Returns:
            int: the input value so that it is smaller or equal to the maximum value and higher or equal to the minimum value if negatives are not allowed; transformed to its negative if `negative` is `True` and higher or equal to the negative of the maximal value and lower or equal to the maximal value if negatives are allowed.
        """
        if negatives_allowed:
            if value > max:
                return max
            if value < max * (-1):
                return max * (-1)
            return value

        if negative:
            if value > max:
                # velocity over max
                return max * (-1)
            if value > min:
                # velocity over min below max
                return value * (-1)
            if value > max * (-1):
                # velocity below min, over negative max
                return value
            # velocity over negative max
            return max * (-1)

        if value < min:
            return min
        if value > max:
            return max
        return value

    def _parse_velocity(
        self, velocity: int, negative: bool = False, both: bool = False
    ) -> int:
        """Parses the velocity.

        Args:
            velocity (int): the input value.
            negative (bool, optional): Whether the input value should
            be transformed into its negative. Defaults to `False`.
            both (bool, optional): Whether an input value can be negative.
            Defaults to `False`.

        Returns:
            int: the input value so that it is smaller or equal to the maximum value and higher or equal to the minimum value if negatives are not allowed; transformed to its negative if `negative` is `True` and higher or equal to the negative of the maximal value and lower or equal to the maximal value if negatives are allowed.
        """
        return self._parse_value(
            velocity,
            self.max_velocity,
            self.min_velocity,
            negative=negative,
            negatives_allowed=both,
        )

    def _parse_angle(
        self, angle: int, negative: bool = False, both: bool = False
    ) -> int:
        """Parses the angle.

        Args:
            angle (int): the input value.
            negative (bool, optional): Whether the input value should be transformed into its negative. Defaults to `False`.
            both (bool, optional): Whether an input value can be negative. Defaults to `False`.

        Returns:
            int: the input value so that it is smaller or equal to the maximum value and higher or equal to the minimum value if negatives are not allowed; transformed to its negative if `negative` is `True` and higher or equal to the negative of the maximal value and lower or equal to the maximal value if negatives are allowed.
        """
        return self._parse_value(
            angle,
            self.max_angle,
            self.min_angle,
            negative=negative,
            negatives_allowed=both,
        )

    def drive_forward(self, misty: Misty, velocity: int) -> Dict:
        """Drives forwards with the specified velocity."""
        forw = {
            "LinearVelocity": self._parse_velocity(velocity),
            "AngularVelocity": self.stagnant_angle,
        }
        return misty.perform_action("drive", data=forw)

    def drive_backward(self, misty: Misty, velocity: int):
        """Drives backwards with the specified velocity."""
        back = {
            "LinearVelocity": self._parse_velocity(velocity, negative=True),
            "AngularVelocity": self.stagnant_angle,
        }
        return misty.perform_action("drive", data=back)

    def drive_left(self, misty: Misty, velocity: int, angle: int):
        """Drives left with the specified velocity and angle."""
        left = {
            "LinearVelocity": self._parse_velocity(velocity),
            "AngularVelocity": self._parse_angle(angle),
        }
        return misty.perform_action("drive", data=left)

    def drive_right(self, misty: Misty, velocity: int, angle: int):
        """Drives right with the specified velocity and angle."""
        velocity = self._parse_velocity(velocity)
        right = {
            "LinearVelocity": self._parse_velocity(velocity),
            "AngularVelocity": self._parse_angle(angle, negative=True),
        }
        return misty.perform_action("drive", data=right)

    def stop_driving(self, misty: Misty):
        """Stops driving."""
        return misty.perform_action("drive_stop")
