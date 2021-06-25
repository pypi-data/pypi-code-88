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
_archive_base = 'https://example.com/archive/test_course_{semester}/'
PSET_URLS = {
    'test_course': _archive_base + 'public_html/psets/{pset}'
}
TASK_URLS = {
    'test_course': _archive_base + + 'public_html/psets/{pset}/{task}'
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

# Mapping from student_info.tsv header values to student info items
REMAP_STUDENT_INFO = {
    "What is your name?": "full_name",
    "What would you like us to call you?": "nonce",
    "Any pronunciation tips that you'd like to share?": "pronunciation",
    "What are your preferred pronouns?": "pronouns",
    "What is one of your favorite things?": "favorite_thing",
    (
        "What are your personal expectations for this class? What would"
      + " you love to take away from it?"
    ): "expectations",
    "Please indicate your lab instructor:": "lab_instructor",
    "Please indicate your lecturer:": "lecture_instructor",
    "Email Address": "email",
    (
        "CS111 has no prerequisites and we do *not* expect students to"
      + " have any previous programming background.  However, if you have"
      + " done some programming before, we are interested to know about"
      + " that. How much programming experience have you had?"
    ): "experience_amount",
    (
        "In a general sense, how would you describe your previous"
      + " programming experience"
    ): "experience_description",
}

# Basis value for numeric scores
SCORE_BASIS = 100

# Mapping from evaluations to points
EVALUATION_SCORES = {
    "excellent": 100,
    "complete": 95,
    "almost complete": 85,
    "partially complete": 75,
    "incomplete": 0,
}

# Max point score on revisions
REVISION_MAX_SCORE = 95
