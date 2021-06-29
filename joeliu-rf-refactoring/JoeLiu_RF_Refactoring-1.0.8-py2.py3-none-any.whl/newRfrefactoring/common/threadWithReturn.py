import threading
from ..builder.testModelBuilder import TestModelBuilder
from ..common.utility import get_file_extension_from_path


class BuildingModelThread(threading.Thread):
    def __init__(self, _path):
        threading.Thread.__init__(self)
        self._path = _path

    def run(self):
        if(get_file_extension_from_path(self._path) == ''):
            self.buildingResult = TestModelBuilder().get_all_models_in_directory(self._path)
        else:
            self.buildingResult = TestModelBuilder().build(self._path)

    def join(self):
        threading.Thread.join(self)
        return self.buildingResult