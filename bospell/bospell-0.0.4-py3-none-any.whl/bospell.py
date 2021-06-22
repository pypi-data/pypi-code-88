from botok import Token as BotokToken

from bospell.error import ErrorModelBase

from . import utils
from .candidates import CandidateModelBase
from .config import Config, DefaultConfig


class BoSpell:
    """
    The BoSpell class encapsulates the basics needed to accomplish a
    spell checking algorithm.

    Args:
        config (bospell.Config): Configuration class for bospell
    """

    def __init__(self, config: Config = DefaultConfig()):
        self.config = config
        self.candidates_model: CandidateModelBase = utils.load_class(
            config.candidates_model_class
        )(config=config)
        self.error_model: ErrorModelBase = utils.load_class(config.error_model_class)()

    def candidates(self, word, n=5):
        return self.candidates_model.get_candidates(word, n)

    def correction(self, word):
        candidates = self.candidates(word, n=1)
        return candidates[0]

    def is_error(self, token: BotokToken):
        return self.error_model.is_error(token)
