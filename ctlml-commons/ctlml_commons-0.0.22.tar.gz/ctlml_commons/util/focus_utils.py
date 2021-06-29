from typing import Any, Dict

from ctlml_commons.entity.focus import Focus, PercentageFocus, PriceFocus


def str_to_focus(data: Dict[str, Any]) -> Focus:
    try:
        focus_type: str = data["focus_type"]

        if focus_type == "PriceFocus":
            return PriceFocus.deserialize(data)
        elif focus_type == "PercentageFocus":
            return PercentageFocus.deserialize(data)
    except Exception as e:
        raise e


def focus_to_str(focus: Focus) -> Dict[str, Any]:
    try:
        return focus.serialize()
    except Exception as e:
        raise Exception(f"Error serializing: {e}")
