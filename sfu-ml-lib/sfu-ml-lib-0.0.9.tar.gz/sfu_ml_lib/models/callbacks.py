import json
import os
from typing import Optional, Mapping

import sfu_data_io.helpers as io
from tensorflow.keras.callbacks import Callback

from sfu_ml_lib.base.tracker import Tracker
from sfu_ml_lib.base.metrics import NumericType


class TrackerCallback(Callback):
    def __init__(self, tracker: Tracker, split: Optional[int] = None, save: bool = False) -> None:
        super().__init__()

        self.tracker = tracker
        self.split = split
        self.save = save

    @classmethod
    def to_string(cls, metrics: Mapping[str, NumericType], prefix: Optional[str] = None) -> str:
        string_metrics = [
            f'{key}: {value}'
            for key, value
            in sorted(metrics.items(), key=lambda key_value: key_value[0])
        ]

        string_metrics = [prefix] + string_metrics if prefix is not None else string_metrics

        message = ', '.join(string_metrics)

        return message

    def save_model(self) -> None:
        local_prefix = os.path.join(io.get_temporary_local_directory_path(), 'weights')

        self.model.save_weights(local_prefix)
        self.tracker.save_model(local_prefix)

    def save_config(self) -> None:
        local_file = os.path.join(io.get_temporary_local_directory_path(), 'config.json')

        with io.open(local_file, mode='w') as json_file:
            json.dump(self.model.get_config(), json_file)

        self.tracker.save_model(local_file)

    def on_epoch_end(self, epoch: int, logs: Optional[Mapping[str, NumericType]] = None):
        if logs is not None:
            self.tracker.log_metrics(logs, step=epoch)
            print(self.to_string(logs, f'Finished Epoch: {epoch}'))

    def on_train_end(self, logs: Optional[Mapping[str, NumericType]] = None):
        if self.save and self.model is not None:
            self.save_model()

            try:
                self.save_config()
            except NotImplementedError:
                pass

        if logs is not None:
            self.tracker.log_metrics(logs, step=self.split)
            print(self.to_string(logs, f'Finished Split: {self.split}'))
