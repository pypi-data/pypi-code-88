from onvif_utilities.decorator import Registry

PARSERS = Registry()

@PARSERS.register("tns1:RuleEngine/CellMotionDetector/Motion")
async def parse_motion_detector(msg):
    try:
        return {
            "motion" : msg.Message._value_1.Data.SimpleItem[0].Value,
        }
    except (AttributeError, KeyError):
        return None

@PARSERS.register("tns1:RuleEngine/TamperDetector/Tamper")
async def parse_tamper_detector(msg):
    try:
        return {
            "tamper" : msg.Message._value_1.Data.SimpleItem[0].Value == "true",
        }
    except (AttributeError, KeyError):
        return None