"""This module enables speech with an extended return message.
"""
from typing import Dict

from misty2py.robot import Misty
from misty2py.utils.generators import get_random_string
from misty2py.response import compose_custom_response


def speak(misty: Misty, utterance: str) -> Dict:
    """Speaks an utterance and returns descriptive message.

    Args:
        misty (Misty): The Misty that speaks the utterance.
        utterance (str): The utterance to speak.

    Returns:
        Dict: the enhanced dictionarised Misty2pyResponse.
    """
    result = misty.perform_action(
        "speak",
        data={"Text": utterance, "UtteranceId": "utterance_" + get_random_string(6)},
    ).parse_to_dict()
    return compose_custom_response(
        result,
        success_message="Talking successful. Utterance: `%s`." % utterance,
        fail_message="Talking failed. Utterance: `%s`." % utterance,
    )
