from fractions import Fraction
from typing import List
import math


class RatioBasedMusicSystem:
    def __init__(
        self, base_frequency: float, ratios: List[Fraction], equivalence_ratio: float
    ):
        self.base_frequency = base_frequency
        self.ratios = ratios
        self.equivalence_ratio = equivalence_ratio
        self.num_notes = len(ratios)
        self.interval_to_ratio = {i: ratios[i] for i in range(self.num_notes)}
        self.ratio_to_interval = {v: k for k, v in self.interval_to_ratio.items()}
        # self.ratios_to_complexity = {ratio: math.lcm(ratio.numerator, ratio.denominator)/math.gcd(ratio.numerator, ratio.denominator) for ratio in self.ratios}
        hand_sorted_intervals = [0, 7, 5, 9, 4, 3, 8, 10, 2, 11, 1, 6]
        self.interval_to_complexity = {
            hand_sorted_intervals[i]: i for i in hand_sorted_intervals
        }


class RBMS_Approximation(RatioBasedMusicSystem):
    def __init__(
        self,
        base_frequency: float,
        ratios: List[Fraction],
        equivalence_ratio: float,
        multiplier: float,
        num_notes: int,
    ):
        super().__init__(base_frequency, ratios, equivalence_ratio)
        self.multiplier = multiplier
        self.fundamental_notes = [
            base_frequency * (multiplier ** i) for i in range(num_notes)
        ]
        self.ratios_to_approximations = {
            ratio: (multiplier ** i) for i, ratio in enumerate(self.ratios)
        }
        self.approximations_to_ratios = {
            v: k for k, v in self.ratios_to_approximations.items()
        }
