import os
from laipvt.sysutil.gvalue import LAIPVT_BASE_DIR, CHECK_FILE, PRE_CHECK_RESULT_FILE
from laipvt.sysutil.util import get_yaml_config

def is_pre_check():
    try:
        if os.path.exists(LAIPVT_BASE_DIR) and os.path.exists(CHECK_FILE) and os.path.exists(PRE_CHECK_RESULT_FILE):
            check_context = get_yaml_config(PRE_CHECK_RESULT_FILE)
            # print(check_context)
            if check_context["total"]:
                return True
    except Exception as e:
        return False
    return False

