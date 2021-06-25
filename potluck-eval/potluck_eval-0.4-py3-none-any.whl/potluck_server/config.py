import os.path

# Various folders and directories
EVALUATION_BASE = '../potluck_testarea'

# Potluck base folder that should have potluck/ module directory plus
# scripts/ directory.
POTLUCK_BASE_DIR = '..'

# Which class ID to use (include semester)
COURSE_NAMES = {
    'test_course': 'TEST COURSE'
}
DEFAULT_COURSE = 'test_course'
DEFAULT_SEMESTER = 'fall2021'

# Where students should direct support requests if things aren't working
SUPPORT_EMAIL = 'username@example.com'
SUPPORT_LINK = f'<a href="mailto:{SUPPORT_EMAIL}">User Name</a>'

# Default timezone for dates
DEFAULT_TZ = "ET"

# Central Authentication Server config
CAS_SERVER = 'https://login.example.com:443'
CAS_AFTER_LOGIN = 'dashboard'
CAS_LOGIN_ROUTE = '/module.php/casserver/cas.php/login'
CAS_LOGOUT_ROUTE = '/module.php/casserver/cas.php/logout'
CAS_AFTER_LOGOUT = 'https://example.com/potluck'
CAS_VALIDATE_ROUTE = '/module.php/casserver/serviceValidate.php'

# Course URLs
PSET_URLS = {
    'test_course': 'https://example.com/archive/test_course_{semester}/public_html/psets/{pset}',
}
TASK_URLS = {
    'test_course': 'https://example.com/archive/test_course_{semester}/public_html/psets/{pset}/{task}',
}

# Where to load task info from:
TASK_INFO_FILE = 'tasks.json'

# Where to load admin info:
ADMIN_INFO_FILE = 'potluck-admin.json'

# Where to load the roster from (used for the gradesheet view and for
# gatekeeping solution files):
ROSTER_FILE = 'roster.csv'

# Where to look for a student-info file
STUDENT_INFO_FILE = 'student-info.tsv'

# Which port to use for manager to synchronize file operations
SYNC_PORT = 51723

# How seconds to give the evaluation process before assuming something
# has gone wrong
FINAL_EVAL_TIMEOUT = 60

# Whether to use xvfb for a virtual framebuffer
USE_XVFB = False
# X-server arguments to use with XVFB
XVFB_SERVER_ARGS = "-screen 0 1024x768x24"
