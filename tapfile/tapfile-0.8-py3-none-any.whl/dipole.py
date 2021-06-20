from .profile import Profile


class Dipole:
    def __init__(self, profile=None):
        if profile is None:
            profile = Profile()
        self.profile = profile
        self.scaling = [1]*profile.buckets

    def classify(self, dur):
        """Translate a pulse duration in to S, M, L or X."""
        if dur is None:
            return 'X'

        scaled_dur = dur * (sum(self.scaling) / len(self.scaling))

        if scaled_dur < self.profile.low or scaled_dur > self.profile.hi:
            return 'X'

        if scaled_dur < self.profile.hi_s:
            # short
            ret = 'S'
            ideal = self.profile.ideal_s
        elif scaled_dur < self.profile.hi_m:
            # medium
            ret = 'M'
            ideal = self.profile.ideal_m
        else:
            # long
            ret = 'L'
            ideal = self.profile.ideal_l

        self.scaling.pop(0)
        val = ideal/dur
        val = max(val, 0.9) if val < 1 else min(val, 1.1)
        self.scaling.append(val)

        return ret
