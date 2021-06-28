import json
from ..utils.utils import Decoder
from importlib import import_module


def selectloss(
    lossname, parameter={}, config_file="defaults/loss_definition.json"
):
    if isinstance(parameter, str):
        parameter = json.loads(
            parameter.replace("'", '"'),
            cls=Decoder,
        )
    loss_func = get_loss_path(lossname, config_file)
    loss_func.pop("name", None)

    if "module" in loss_func:
        module = loss_func.pop("module", "nn.")
        lmod = import_module(module)
        loss_func["criterion"] = "lmod." + loss_func["criterion"]
    else:
        loss_func["criterion"] = "nn." + loss_func["criterion"]

    param = loss_func.pop("initparam", {})
    if isinstance(param, str):
        param = json.loads(
            param.replace("'", '"'),
            cls=Decoder,
        )
    for key, val in parameter.items():
        param[key] = val

    criterion = eval(loss_func["criterion"] + "(**param)")
    criterionparam = loss_func["criterionparam"]

    return criterion, criterionparam


def get_metric_path(config_file="defaults/metrics.json"):
    metrics = json.load(open(config_file), cls=Decoder)
    return metrics


def get_loss_path(name, config_file="defaults/loss_definition.json"):
    loss_func = json.load(open(config_file), cls=Decoder)
    if name == "":
        name = list(loss_func.keys())[0]
    if name not in loss_func:
        raise "Function " + name + " not found in " + config_file
    print(name)
    return loss_func[name]