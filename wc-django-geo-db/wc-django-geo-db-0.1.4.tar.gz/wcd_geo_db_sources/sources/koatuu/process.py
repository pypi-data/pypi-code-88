import os
import requests
from wcd_geo_db_sources.modules.process import (
    ProcessRunner, stage, ProcessFinished, ProcessCantProceed
)
import tempfile

from .parsers import registry
from .const import SOURCE, ImportStage


UPLOAD_URL = (
    'https://data.gov.ua/dataset/d945de87-539c-45b4-932a-7dda57daf8d9/'
    'resource/296adb7a-476a-40c8-9de6-211327cb3aa1/download/koatuu.json'
)
PARSER_VERSION = 'v1'



# FIXME: Outdated API
class KOATUUImportRunner(ProcessRunner):
    source: str = SOURCE
    Stage: ImportStage = ImportStage
    default_config: dict = {
        'url': UPLOAD_URL,
        'version': PARSER_VERSION,
    }
    parser_registry: dict = registry

    @stage(Stage.INITIAL)
    def run_initial(self):
        self.update_state(stage=self.Stage.UPLOADING, partial_state={
            'url': self.config['url'],
            'version': self.config['version'],
        })

    @stage(Stage.UPLOADING)
    def run_uploading(self):
        state = self.state.state
        r = requests.get(state['url'], allow_redirects=True)

        if r.status_code // 100 != 2:
            raise ProcessCantProceed(r.reason)

        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(r.content)
            self.update_state(stage=self.Stage.PARSING, partial_state={
                'source_file': tmp.name
            })

    @stage(Stage.PARSING)
    def run_parsing(self):
        state = self.state.state
        parse = self.parser_registry[state['version']]

        with open(state['source_file'], 'r') as file:
            parsed_file = parse(self, file=file)

        self.update_state(stage=self.Stage.MERGE, partial_state={
            'parsed_file': parsed_file
        })

    @stage(Stage.MERGE)
    def run_merge(self):
        self.update_state(stage=self.Stage.CLEANUP)

    @stage(Stage.CLEANUP)
    def run_cleanup(self):
        state = self.state.state

        # for key in ('source_file', 'parsed_file'):
        #     if state.get(key):
        #         os.unlink(state[key])

        raise ProcessFinished()
