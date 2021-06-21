from typing import Optional

from .pyside import QtCore
from .model import AppData
from .parallel import Worker
from .component import warning_callback
from ..core.crypt import gpg, load_authority_key


def load_authority_key_threaded(app_data: AppData) -> None:
    """Retrieve and refresh the key certification authority's PGP key in
    threaded mode. This avoids freezing the entire application when the
    refresh sometimes takes a couple of seconds.
    """
    # This function is responsible for taking the returned value from
    # load_authority_key() and assign it to the correct attribute of app_data.
    def update_authority_key_in_app_data(key: Optional[gpg.Key]):
        app_data.validation_authority_key = key

    show_warning = warning_callback("Certification Authority Key Loading Error")
    worker = Worker(
        load_authority_key,
        report_config=app_data.config,
        sett_config=app_data.config,
        forward_errors=show_warning,
    )
    worker.signals.warning.connect(show_warning)
    worker.signals.result.connect(update_authority_key_in_app_data)
    QtCore.QThreadPool.globalInstance().start(worker)
