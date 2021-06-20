"""This module enables cancellation of all currently running skills."""
from misty2py.robot import Misty


def cancel_skills(misty: Misty):
    """Cancels all skills currently running on Misty."""
    data = misty.get_info("skills_running")
    result = data.get("result", [])
    to_cancel = []
    for dct in result:
        uid = dct.get("uniqueId", "")
        if len(uid) > 0:
            to_cancel.append(uid)
    for skill in to_cancel:
        misty.perform_action("skill_cancel", data={"Skill": skill})
