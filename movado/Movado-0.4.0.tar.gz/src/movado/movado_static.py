from typing import List, Optional

from movado.meta_controller import MetaController

models: List[str] = [
    model.replace("Model", "")
    for model in globals().keys()
    if ("Model" in model) and len(model) > 5
]
controllers: List[str] = [
    ctrl.replace("Controller", "")
    for ctrl in globals().keys()
    if ("Controller" in ctrl) and len(ctrl) > 10
]
