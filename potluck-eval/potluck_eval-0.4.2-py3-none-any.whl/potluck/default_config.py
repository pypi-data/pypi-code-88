BASE_DIR = "."
"""
Base directory to use to look for things like task info, task specs, and
submitted files.
"""

TEMPLATES_DIRECTORY = "templates"
"""
Templates directory for Jinja2 templates. If it's not an absolute path,
it will be relative to the potluck package directory.
"""

RESOURCES_DIRECTORY = "resources"
"""
Resources directory for css and js files. If it's not an absolute path,
it will be relative to the potluck package directory.
"""

TASKS_FILENAME = "tasks.json"
"""
The file name of the tasks meta-data file, relative to BASE_DIR. May be
an absolute path instead.
"""

SUBMISSIONS_DIR = "submissions"
"""
Directory to find submissions in, relative to BASE_DIR (or not, if an
absolute path is provided). The submissions directory must have a
directory for each username, within which must be directories for each
submitted task named by the task ID. Submitted files for each task should
be placed in these task directories.
"""

REPORTS_DIR = "reports"
"""
Directory to write reports into, relative to BASE_DIR (or not, if an
absolute path is provided). Per-user sub-directories will be created,
where timestamped reports will be written.
"""

RUBRICS_DIRECTORY = "rubrics"
"""
Directory to write blank rubrics into, relative to BASE_DIR (or not, if
an absolute path is provided).
"""
