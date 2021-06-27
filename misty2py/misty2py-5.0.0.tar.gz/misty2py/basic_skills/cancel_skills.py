"""This module enables cancellation of all currently running skills."""
from misty2py.utils.utils import get_misty
from typing import Dict
from misty2py.robot import Misty
from misty2py.utils.status import ActionLog
from misty2py.response import success_of_action_list


def cancel_skills(misty: Misty) -> Dict:
    """Cancels all skills currently running on Misty.

    Args:
        misty (Misty): The Misty on which to cancel running skills.

    Returns:
        Dict: a dictionary with the key `overall_success` specifying whether all actions were successful and a key for every action containing the dictionarised Misty2pyResponse.
    """
    actions = ActionLog()
    data = misty.get_info("skills_running").parse_to_dict()
    actions.append_({"get_running_skills": data})

    data = data.get("rest_response", {})
    result = data.get("result", [])
    to_cancel = []
    for dct in result:
        uid = dct.get("uniqueId", "")
        if len(uid) > 0:
            to_cancel.append(uid)

    for skill in to_cancel:
        data = misty.perform_action(
            "skill_cancel", data={"Skill": skill}
        ).parse_to_dict()
        actions.append_({"cancel_%s" % skill: data})

    return success_of_action_list(actions.get_())
