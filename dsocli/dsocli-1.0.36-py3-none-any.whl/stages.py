
import re
from .config import Config
from .providers import ProviderManager
from .constants import *
from .exceptions import DSOException

class Stages():
    # @staticmethod
    # def list(stage):
    #     pass
    
    # @staticmethod
    # def create(stage):
    #     m = re.match(REGEX_PATTERNS['stage'], stage)
    #     stage = m.groups()[0]
    #     stage = m.groups()[1] if len(m.groups()) > 1 else 'default'
    #     # contexts = Config.app_spec['contexts']
    #     # if contexts is None:
    #     #     Config.app_spec['contexts'] = {}
    #     #     contexts = {}
    #     # contexts[stage][stage] = 1
    #     Config.app_spec['contexts'][stage][stage] = 1
    # @staticmethod
    # def download(stage):
    #     pass
    # @staticmethod
    # def delete(stage):
    #     pass


    @staticmethod
    def default_stage():
        return 'default/0'

    @staticmethod
    def raw_parse(stage):
        if not stage: return None, None
        m = re.match(REGEX_PATTERNS['stage'], stage)
        if m is None:
            raise DSOException(MESSAGES['InvalidStage'].format(stage, REGEX_PATTERNS['stage']))
        stage = m.groups()[0]
        env = m.groups()[1] if len(m.groups()) > 1 else ''
        return stage, env

    @staticmethod
    def normalize(stage):
        stage, env = Stages.raw_parse(stage)
        stage = stage or 'default'
        ### force dafault env if stage is default: default/env not allowed
        env = env if env and not stage == 'default' else '0'
        return f"{stage}/{env}"

    def parse_normalized(stage):
        stage = Stages.normalize(stage)
        return Stages.raw_parse(stage)

    @staticmethod
    def get_stage_default_env(stage):
        stage = Stages.parse_normalized(stage)[0]
        return f"{stage}/0"

    @staticmethod
    def get_stage_env(stage):
        return Stages.parse_normalized(stage)[1]

    @staticmethod
    def shorten(stage):
        stage, env = Stages.parse_normalized(stage)
        if env == '0':
            return stage
        else:
            return f"{stage}/{env}"

    @staticmethod
    def is_default(stage):
        return stage in ['default', 'default/0']

    @staticmethod
    def is_stage_default_env(stage):
        env = Stages.parse_normalized(stage)[1]
        return env == '0'
