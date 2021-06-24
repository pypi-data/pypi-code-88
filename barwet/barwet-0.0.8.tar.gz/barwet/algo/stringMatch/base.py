class MatchBase:
    
    def __init__(self, template: str) -> None:
        self.template = template

    def index(self, probe: str) -> int:
        """
        Exact matching, return the matched index.
        """
        raise Exception('Must be implemented in subclass!')

    def blurry_index(self, probe: str, allowed_mismatches: int):
        """
        Blurry matching, return the matched index.
        """
        raise Exception('Must be implemented in subclass!')

    def has(self, probe: str, allowed_mismatches=0) -> bool:
        if allowed_mismatches == 0:
            return self.index(probe) >= 0
        else:
            return self.blurry_index(probe, allowed_mismatches) >= 0