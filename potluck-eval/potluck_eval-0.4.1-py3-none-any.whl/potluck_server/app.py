#!/usr/local/bin/python
# -*- coding: UTF-8 -*-
"""
potluck_server/app.py

Flask WSGI web app for managing student submissions & grading them w/
potluck. Fork of Ocean server for Codder. Withholds feedback until after
the deadline, so the display of feedback is detached a bit from the
generation of feedback.

Students log in using CAS, select a pset, and submit one file per task
(where the filename is checked against a configurable list), and can view
their most recent submission, see any warnings on it, or even submit a
revision. Once the deadline + review period has passed (modulo
extensions), the full report from each student's last on-time submission
is made available. Main routes:

/ (route_index):
    Checks for CAS authentication and redirects to login page or to
    dashboard.

/dashboard (route_default_dash):
    Auto-redirects to the dashboard for the "current" course/semester
    based on configuration.

/<course>/<semester>/dashboard (route_dash):
    Main interface w/ rows for each pset. Each row has sub-rows for each
    task w/ upload button to submit the task and link to latest feedback
    for that task.

/<course>/<semester>/feedback/<username>/<phase>/<pset>/<task> (route_feedback):
    Displays latest feedback for a given user/phase/pset/task.
    Pre-deadline this just shows any warnings.
    TODO: Add submit/resubmit mechanism to this page!

/<course>/<semester>/submit/<phase>/<pset>/<task> (route_submit):
    Form target for submissions; accepts valid submissions and redirects
    back to feedback page.

/<course>/<semester>/extension/<pset> (route_extension):
    Request an extension for a pset (automatically grants the default
    extension; the extension always applies only to the initial deadline,
    not to revisions; and the extension applies to the whole problem set,
    not per-task).
    # TODO: Allow students to revoke requested extensions if they haven't
    # started using them yet.

/<course>/<semester>/solution/<pset>/<task> (route_solution):
    View the solution code for a particular task. Only available once a
    task is finalized (on a per-student basis to deal with extensions).

/<course>/<semester>/gradesheet/<pset> (route_gradesheet):
    An overview of all grades for a specific problem set, visible only to
    admins.
    # TODO: Make this faster!
"""

# Attempts at 2/3 dual compatibility:
from __future__ import print_function

import sys

# IF we're not in pyhton3:
if sys.version_info[0] < 3:
    reload(sys) # noqa F821
    # Set explicit default encoding
    sys.setdefaultencoding('utf-8')
    # Rename raw_input
    input = raw_input # noqa F821


def ensure_directory(target):
    """
    makedirs 2/3 shim.
    """
    if sys.version_info[0] < 3:
        try:
            os.makedirs(target)
        except OSError:
            pass
    else:
        os.makedirs(target, exist_ok=True)


# Main imports
import flask # noqa E402
import flask_cas # noqa E402
import jinja2 # noqa E402

from flask import json # noqa E402

import os, subprocess, shutil # noqa E402
import datetime, time, random, copy, csv, re # noqa E402

import sync # noqa E402


#-------#
# Setup #
#-------#

# Create our app object:
app = flask.Flask(__name__)

# Enable authentication:
cas = flask_cas.CAS(app)

# Load configuration file config.py (see Makefile):
app.config.from_object('config')

# Load potluck modules:
sys.path.append(app.config["POTLUCK_BASE_DIR"])
import potluck.report # noqa: E402

# Set secret key from secret file (see Makefile):
with open("secret", 'rb') as fin:
    app.secret_key = fin.read()

# Initialize file access synchronization system
sync.init_sync(port=app.config["SYNC_PORT"])


#------------#
# Debug mode #
#------------#

NOAUTH = False
if __name__ == "__main__":

    print("WARNING: Running in debug mode WITHOUT AUTHENTICATION!")
    input("Press enter to continue in debug mode.")
    # Disable login_required
    flask_cas.login_required = lambda f: f
    # Set up username workaround
    NOAUTH = True


#-----------#
# Constants #
#-----------#

# TODO: Move this to config?
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


#---------#
# Helpers #
#---------#

def evaluation_directory(course, semester):
    """
    The evaluation directory for a particular class/semester.
    """
    return os.path.join(app.config["EVALUATION_BASE"], course, semester)


def logs_folder(course, semester):
    """
    The logs folder for a class/semester.
    """
    return os.path.join(evaluation_directory(course, semester), "logs")


def submissions_folder(course, semester):
    """
    The submissions folder for a class/semester.
    """
    return os.path.join(evaluation_directory(course, semester), "submissions")


def reports_folder(course, semester):
    """
    The reports folder for a class/semester.
    """
    return os.path.join(evaluation_directory(course, semester), "reports")


def extensions_folder(course, semester):
    """
    The extensions folder for a class/semester.
    """
    return os.path.join(evaluation_directory(course, semester), "extensions")


def admin_info_file(course, semester):
    """
    The admin info file for a class/semester.
    """
    return os.path.join(
        evaluation_directory(course, semester),
        app.config["ADMIN_INFO_FILE"]
    )


def task_info_file(course, semester):
    """
    The task info file for a class/semester.
    """
    return os.path.join(
        evaluation_directory(course, semester),
        app.config["TASK_INFO_FILE"]
    )


def roster_file(course, semester):
    """
    The roster file for a class/semester.
    """
    return os.path.join(
        evaluation_directory(course, semester),
        app.config["ROSTER_FILE"]
    )


def student_info_file(course, semester):
    """
    The student info file for a class/semester.
    """
    return os.path.join(
        evaluation_directory(course, semester),
        app.config["STUDENT_INFO_FILE"]
    )


def augment_arguments(route_function):
    """
    A decorator that modifies a route function to supply `username`,
    `is_admin`, `masquerade_as`, `effective_user`, and `task_info`
    keyword arguments along with the other arguments the route recieves.
    Must be applied before app.route, and the first two parameters to the
    function must be the course and semester.

    Because flask/werkzeug routing requires funciton signatures to be
    preserved, we do some dirty work with compile and eval... As a
    result, this function can only safely be used to decorate functions
    that don't have any keyword arguments. Furthermore, the 5 augmented
    arguments must be the last 5 arguments that the function accepts.
    """
    def with_extra_arguments(*args, **kwargs):
        """
        A decorated route function which will be supplied with username,
        is_admin, masquerade_as, effective_user, and task_info parameters
        as keyword arguments after other arguments have been supplied.
        """
        # Grabe course + semester values
        course = kwargs.get('course', args[0] if len(args) > 0 else None)
        semester = kwargs.get(
            'semester',
            args[1 if 'course' not in kwargs else 0]
                if len(args) > 0 else None
        )

        if course == None or semester == None:
            flask.flash(
                (
                    "Error: Unable to get course and/or semester. Course"
                    " is {} and semester is {}."
                ).format(repr(course), repr(semester))
            )
            return error_response(
                course,
                semester,
                username,
                (
                    "Failed to access <code>course</code> and/or"
                    " <code>semeser</code> values."
                )
            )

        if NOAUTH:
            username = "test"
        else:
            username = cas.username

        # Get admin info
        admin_info = get_admin_info(course, semester)
        if admin_info is None:
            flask.flash("Error loading admin info!")
            admin_info = {}

        # Check user privileges
        is_admin, masquerade_as = check_user_privileges(admin_info, username)

        # Effective username
        effective_user = masquerade_as or username

        # Get basic info on all psets/tasks
        task_info = get_task_info(course, semester)
        if task_info is None: # error loading task info
            flask.flash("Error loading task info!")
            return error_response(
                course,
                semester,
                username,
                "Failed to load <code>tasks.json</code>."
            )

        # Set pause time for the task info
        set_pause_time(admin_info, task_info, username, masquerade_as)

        # Update the kwargs
        kwargs["username"] = username
        kwargs["is_admin"] = is_admin
        kwargs["masquerade_as"] = masquerade_as
        kwargs["effective_user"] = effective_user
        kwargs["task_info"] = task_info

        # Call the decorated function w/ the extra parmeers we've
        # deduced.
        return route_function(*args, **kwargs)

    # Grab info on original function signature
    fname = route_function.__name__
    nargs = route_function.__code__.co_argcount
    argnames = route_function.__code__.co_varnames[:nargs - 5]

    # Create a function with the same signature:
    code = """\
def {name}({args}):
    return with_extra_arguments({args})
""".format(name=fname, args=', '.join(argnames))
    env = {"with_extra_arguments": with_extra_arguments}
    # 2/3 compatibility attempt...
    if sys.version_info[0] < 3:
        exec (code) in env, env
    else:
        exec(code, env, env) in env, env
    result = env[fname]

    # Return our synthetic function...
    return result


def goback(course, semester):
    """
    Returns a flask redirect aimed at either the page that the user came
    from, or the dashboard if that information isn't available.
    """
    if flask.request.referrer:
        # If we know where you came from, send you back there
        return flask.redirect(flask.request.referrer)
    else:
        # Otherwise back to the dashboard
        return flask.redirect(
            flask.url_for('route_dash', course=course, semester=semester)
        )


#-----------------#
# Route functions #
#-----------------#

@app.route('/')
def route_index():
    """
    Checks authentication and redirects to login page or to dashboard.
    """
    if NOAUTH or cas.username:
        return flask.redirect(flask.url_for('route_default_dash'))
    else:
        return flask.redirect(flask.url_for('cas.login'))


@app.route('/dashboard')
@flask_cas.login_required
def route_default_dash():
    """
    Redirects to dashboard w/ default class/semester.
    """
    return flask.redirect(
        flask.url_for(
            'route_dash',
            course=app.config.get("DEFAULT_COURSE", "unknown"),
            semester=app.config.get("DEFAULT_SEMESTER", "unknown")
        )
    )


@app.route('/<course>/<semester>/dashboard')
@flask_cas.login_required
@augment_arguments
def route_dash(
    course,
    semester,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Displays dashboard w/ links for submitting each pset/task & summary
    information of task grades.
    """

    # Add pset status and task feedback summaries to task info
    amend_task_info(course, semester, task_info, effective_user)

    # Render dashboard template
    return flask.render_template(
        'dashboard.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        is_admin=is_admin,
        masquerade_as=masquerade_as,
        effective_user=effective_user,
        task_info=task_info
    )


@app.route(
    '/<course>/<semester>/feedback/<target_user>/<phase>/<psid>/<taskid>'
)
@flask_cas.login_required
@augment_arguments
def route_feedback(
    course,
    semester,
    target_user,
    phase,
    psid,
    taskid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Displays feedback on a particular task of a particular problem set,
    for either the 'initial' or 'revision' phase.
    """
    if target_user != effective_user and not is_admin:
        return error_response(
            course,
            semester,
            username,
            "You are not allowed to view feedback for {}.".format(target_user)
        )
    elif target_user != effective_user:
        flask.flash("Viewing feedback for {}.".format(target_user))

    # From here on we treat the effective user as the target user
    effective_user = target_user

    try:
        ps = get_ps_obj(task_info, psid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    try:
        task = get_task_obj(ps, taskid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    # Add status & time remaining info to pset and objects
    amend_pset(course, semester, task_info, ps, target_user)
    amend_task(course, semester, task_info, psid, task, target_user, phase)
    # Note: this amended task will always be amended according to the
    # correct phase.

    if task["eval_status"] not in (
        None,
        "initial",
        "in_progress",
        "error",
        "expired",
        "completed"
    ):
        msg = "Invalid evaluation status <code>{}</code>.".format(
            task["eval_status"]
        )
        flask.flash(msg)
        return error_response(course, semester, username, msg)

    # Get full feedback for the task in question if it's available
    task["feedback"] = get_feedback(
        course,
        semester,
        task_info,
        target_user,
        phase,
        ps["id"],
        task["id"]
    )
    fb_css = ""
    fb_js = ""
    if task["feedback"] not in [None, "missing"]:
        task["submitted"] = True
        for taskid in task["feedback"]["tasks"]:
            tasklog = task["feedback"]["tasks"][taskid]
            potluck.report.augment_tasklog(tasklog)
        fb_css = potluck.report.get_css()
        fb_js = potluck.report.get_js()

    return flask.render_template(
        'feedback.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        is_admin=is_admin,
        masquerade_as=masquerade_as,
        effective_user=effective_user,
        target_user=target_user,
        phase=phase,
        ps=ps,
        task=task,
        task_info=task_info,
        fb_css=fb_css,
        fb_js=fb_js,
        support_link=app.config["SUPPORT_LINK"]
    )


@app.route('/<course>/<semester>/submit/<psid>/<taskid>', methods=['POST'])
@flask_cas.login_required
@augment_arguments
def route_submit(
    course,
    semester,
    psid,
    taskid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Accepts a file submission for a task and initiates an evaluation
    process for that file. Figures out submission phase automatically
    based on task info. Redirects to the feedback page for the submitted
    task.

    Note: there are probably some nasty race conditions if the same user
    submits the same task simultaneously via multiple requests. We simply
    hope that that does not happen.
    """
    try:
        ps = get_ps_obj(task_info, psid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    # TODO: Do we need this?
    try:
        # Don't need the object here, just need to be sure the task
        # exists.
        _ = get_task_obj(ps, taskid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    # Add status & time remaining info to pset
    amend_pset(course, semester, task_info, ps, effective_user)

    # Determine the phase from the pset state
    ps_state = ps['status']['state']
    if ps_state == "unknown":
        msg = "{} has no deadline.".format(psid)
        flask.flash(msg)
        return error_response(course, semester, username, msg)
    elif ps_state in ("unreleased", "released"):
        phase = "initial"
    elif ps_state in ("under_review", "revisable"):
        phase = "revision"
        if ps_state == "under_review":
            flask.flash(
                "You should probably wait until the review period is"
              + " over and view feedback on your initial submission"
              + " before submitting a revision."
            )
    elif ps_state == "final":
        flask.flash(
            "We are no longer accepting new submissions for {}.".format(psid)
        )
        phase = "belated"

    # Ensure that there's a file being submitted
    files = flask.request.files
    if ('upload' not in files or files['upload'].filename == ''):
        flask.flash("You must choose a file to submit.")
        return goback(course, semester)
    else:
        uploaded = files['upload']

        # Check for an in-flight grading process for this task
        ts, logfile, status = get_inflight(
            course,
            semester,
            effective_user,
            phase,
            psid,
            taskid
        )

        # If the submission is already being evaluated, or if we couldn't
        # figure out whether that was the case, we can't start another
        # evaluation process!
        if ts == "error":
            flask.flash(
                (
                    "ERROR: Failed to check evaluation status. Try"
                  + " refreshing this page, and if the problem persists,"
                  + " contact {}."
                ).format(app.config["SUPPORT_LINK"])
            )
            return flask.redirect(
                flask.url_for(
                    'route_feedback',
                    course=course,
                    semester=semester,
                    target_user=effective_user,
                    phase=phase,
                    psid=psid,
                    taskid=taskid
                )
            )
        elif status in ("initial", "in_progress"):
            flask.flash(
                (
                    "ERROR: Task {taskid} for pset {psid} is currently being"
                  + " evaluated. You must wait until that process is"
                  + " complete before uploading a revised submission. This"
                  + " should take no longer than"
                  + " {timeout} seconds."
                ).format(
                    taskid=taskid,
                    psid=psid,
                    timeout=app.config['FINAL_EVAL_TIMEOUT']
                )
            )
            return flask.redirect(
                flask.url_for(
                    'route_feedback',
                    course=course,
                    semester=semester,
                    target_user=effective_user,
                    phase=phase,
                    psid=psid,
                    taskid=taskid
                )
            )

        # Record the time spent value
        if (
            'time_spent' not in flask.request.form
         or flask.request.form["time_spent"] == ""
        ):
            flask.flash(
                "You did not give us an estimate of how much time this"
              + " task took you. Please re-submit and enter a time spent"
              + " value so that we can help advise future students about"
              + " how long this task will take them."
            )
            time_spent = ""
        else:
            time_spent = flask.request.form["time_spent"]

        record_time_spent(
            course,
            semester,
            effective_user,
            phase,
            psid,
            taskid,
            time_spent
        )

        # Save the file with the correct filename, ignoring the name that
        # the user uploaded.
        target = get_submission_filename(
            course,
            semester,
            task_info,
            effective_user,
            phase,
            psid,
            taskid
        )
        destdir, reqname = os.path.split(target)
        ensure_directory(destdir)
        backup = unused_filename(target)
        if backup != target:
            shutil.move(target, backup)
        uploaded.save(target)
        # TODO: Flash categories
        if phase == "belated":
            flask.flash(
                (
                    "Uploaded LATE '{filename}' for {psid} {taskid}."
                  + " This submission will not be graded."
                ).format(
                    filename=uploaded.filename,
                    psid=psid,
                    taskid=taskid
                )
            )
        else:
            flask.flash(
                (
                    "Successfully uploaded {phase} submission"
                  + " '{filename}' for {psid} {taskid}."
                ).format(
                    phase=phase,
                    filename=uploaded.filename,
                    psid=psid,
                    taskid=taskid
                )
            )
        # Flash a warning if the uploaded filename seems wrong
        if uploaded.filename != reqname:
            flask.flash(
                (
                    "Warning: you uploaded a file named"
                  + " '{filename}', but {taskid} in"
                  + " {psid} requires a file named '{reqname}'. Are you sure"
                  + " you uploaded the correct file?"
                ).format(
                    filename=uploaded.filename,
                    psid=psid,
                    taskid=taskid,
                    reqname=reqname
                )
            )

        # Log setup
        ts, logfile, _ = put_inflight(
            course,
            semester,
            effective_user,
            phase,
            psid,
            taskid
        )

        if ts == "error":
            flask.flash(
                (
                    "ERROR: Failed to check evaluation status. Try"
                  + " refreshing this page, and if the problem persists,"
                  + " contact {}."
                ).format(app.config["SUPPORT_LINK"])
            )
            return flask.redirect(
                flask.url_for(
                    'route_feedback',
                    course=course,
                    semester=semester,
                    target_user=effective_user,
                    phase=phase,
                    psid=psid,
                    taskid=taskid
                )
            )
        elif ts is None: # another grading process is already in-flight
            flask.flash(
                (
                    "ERROR: Task {taskid} for pset {psid} is currently being"
                  + " evaluated. You must wait until that process is"
                  + " complete before uploading another submission. This"
                  + " should take no longer than {timeout} seconds."
                ).format(
                    psid=psid,
                    taskid=taskid,
                    timeout=app.config['FINAL_EVAL_TIMEOUT']
                )
            )
            return flask.redirect(
                flask.url_for(
                    'route_feedback',
                    course=course,
                    semester=semester,
                    target_user=effective_user,
                    phase=phase,
                    psid=psid,
                    taskid=taskid
                )
            )

        # Start the evaluation process (we don't wait for it)
        launch_potluck(
            course,
            semester,
            effective_user,
            phase,
            psid,
            taskid,
            logfile
        )

    return flask.redirect(
        flask.url_for(
            'route_feedback',
            course=course,
            semester=semester,
            target_user=effective_user,
            # There are no provisions for displaying feedback on late
            # files, so we redirect to the latest revision in that case.
            phase="revision" if phase == "belated" else phase,
            psid=psid,
            taskid=taskid
        )
    )


def launch_potluck(course, semester, username, phase, psid, taskid, logfile):
    """
    Launches the evaluation process. This is fire-and-forget; we'll look
    for the output file to determine whether it's finished or not.
    """
    potluck_exe = flask.safe_join(
        app.config["POTLUCK_BASE_DIR"],
        "scripts",
        "potluck_eval"
    )
    potluck_args = [
        # TODO: Phases?!?
        "-t", taskid,
        "-u", username,
        "--clean",
    ]
    with open(logfile, 'wb') as log:
        if app.config["USE_XVFB"]:
            # Virtualize frame buffer for programs with graphics, so they don't
            # need to create Xwindow windows '--auto-servernum', # create a new
            # server??  '--auto-display', # [2019/02/08] Peter: try this
            # instead per comment in the -h?
            xvfb_err_log = os.path.splitext(logfile)[0] + ".xvfb_errors.log"
            subprocess.Popen(
                (
                    [
                        'xvfb-run',
                        '-d',
                        # [2019/02/11] Lyn: --auto-display doesn't work but -d
                        # does (go figure, since they're supposed to be
                        # synonyms!)
                        '-e', # --error-file doesn't work
                        xvfb_err_log,
                        '--server-args',
                        app.config["XVFB_SERVER_ARGS"], # screen properties
                        '--',
                        potluck_exe,
                    ]
                  + potluck_args
                ),
                cwd=evaluation_directory(course, semester), # working directory
                stdout=log,
                stderr=log,
            )
        else:
            # Raw potluck launch without XVFB
            subprocess.Popen(
                [ potluck_exe ] + potluck_args,
                cwd=evaluation_directory(course, semester), # working directory
                stdout=log,
                stderr=log,
            )


@app.route('/<course>/<semester>/extension/<psid>', methods=['GET'])
@flask_cas.login_required
@augment_arguments
def route_extension(
    course,
    semester,
    psid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Requests (and automatically grants) the default extension on the
    given problem set. The extension is applied to the initial phase
    only. For now, nonstandard extensions and revision extensions must be
    applied by hand-editing JSON files in the `extensions/` directory.
    """
    try:
        ps = get_ps_obj(task_info, psid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    # Add status & time remaining info to pset
    amend_pset(course, semester, task_info, ps, effective_user)
    # TODO: triple-check the possibility of requesting an extension
    # during the period an extension would grant you but after the
    # initial deadline?

    # Grant the extension
    if (
        ps["status"]["state"] in ("unreleased", "released")
    and ps["status"]["initial_extension"] == 0
    ):
        succeeded = set_extension(
            course,
            semester,
            effective_user,
            "initial",
            psid
        )
        if succeeded:
            flask.flash("Extension granted for {}.".format(psid))
        else:
            flask.flash("Failed to grant extension for {}.".format(psid))
    elif ps["status"]["state"] not in ("unreleased", "released"):
        flask.flash(
            (
                "It is too late to request an extension for {}. You must"
                " request extensions before the deadline for each pset."
            ).format(psid)
        )
    elif ps["status"]["initial_extension"] != 0:
        flask.flash(
            "You have already been granted an extension on {}.".format(psid)
        )
    else:
        flask.flash(
            "You cannot take an extension on {}.".format(psid)
        )

    # Send them back to the dashboard or wherever they came from
    return goback(course, semester)


@app.route('/<course>/<semester>/set_extensions/<target_user>/<psid>', methods=['POST'])
@flask_cas.login_required
@augment_arguments
def route_set_extensions(
    course,
    semester,
    target_user,
    psid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Form target for editing extensions for a particular user/pset. Only
    admins can use this route. Can be used to set custom extension values
    for both initial and revised deadlines. Nonstandard extensions and
    revision extensions may be also be applied by hand-editing JSON files
    in the `extensions/` directory.
    """
    try:
        ps = get_ps_obj(task_info, psid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    if not is_admin:
        flask.flash("Only admins can grant extensions.")
        return goback(course, semester)

    # Get initial/revision extension values from submitted form values
    try:
        initial = int(flask.request.form["initial"])
    except:
        initial = None

    try:
        revision = int(flask.request.form["revision"])
    except:
        revision = None

    # At least one or the other needs to be valid
    if initial == None and revision == None:
        flask.flash(
            (
                "To set extensions, you must specify either an initial"
                " or a revision value, and both values must be integers."
            )
        )
        return goback(course, semester)

    # Grant the extension(s)
    if initial != None:
        succeeded = set_extension(
            course,
            semester,
            target_user,
            "initial",
            psid,
            initial
        )
        if succeeded:
            flask.flash(
                "Set {}h initial extension for {} on {}.".format(
                    initial,
                    target_user,
                    psid
                )
            )
        else:
            flask.flash(
                "Failed to grant initial extension for {} on {} (try again?)."
                .format(target_user, psid)
            )

    if revision != None:
        succeeded = set_extension(
            course,
            semester,
            target_user,
            "revision",
            psid,
            revision
        )
        if succeeded:
            flask.flash(
                "Set {}h revision extension for {} on {}.".format(
                    revision,
                    target_user,
                    psid
                )
            )
        else:
            flask.flash(
                "Failed to grant revision extension for {} on {} (try again?)."
                .format(target_user, psid)
            )

    # Send them back to the dashboard or wherever they came from
    return goback(course, semester)


@app.route('/<course>/<semester>/manage_extensions/<target_user>', methods=['GET'])
@flask_cas.login_required
@augment_arguments
def route_manage_extensions(
    course,
    semester,
    target_user,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Admin-only route that displays a list of forms for each pset showing
    current extension values and allowing the user to edit them and press
    a button to update them.
    """
    if not is_admin:
        flask.flash("Only admins can grant extensions.")
        return goback(course, semester)

    # Get extensions info for the target user for all psets
    amend_task_info(course, semester, task_info, target_user)

    return flask.render_template(
        'extension_manager.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        is_admin=is_admin,
        masquerade_as=masquerade_as,
        task_info=task_info,
        target_user=target_user
    )


@app.route('/<course>/<semester>/solution/<psid>/<taskid>', methods=['GET'])
@flask_cas.login_required
@augment_arguments
def route_solution(
    course,
    semester,
    psid,
    taskid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Visible only once a task's status is final, accounting for all
    extensions, and if the active user has a graded submission for the task (or
    if they're an admin). Shows the solution code for a particular task,
    including a formatted version and a link to download the .py file.
    """
    try:
        ps = get_ps_obj(task_info, psid)
    except ValueError as e:
        flask.flash("ValueError: " + str(e))
        return goback(course, semester)

    try:
        task = get_task_obj(ps, taskid)
    except ValueError as e:
        flask.flash("ValueError: " + str(e))
        return goback(course, semester)

    # Add status & time remaining info to pset and objects
    amend_pset(course, semester, task_info, ps, effective_user)

    # Amend the task object so that we know whether they've submitted or not,
    # and check for both initial and revised submissions.
    initial_task = task
    revised_task = copy.deepcopy(task)
    amend_task(
        course,
        semester,
        task_info,
        psid,
        initial_task,
        effective_user,
        "initial"
    )
    amend_task(
        course,
        semester,
        task_info,
        psid,
        revised_task,
        effective_user,
        "revision"
    )

    # Check roster so that only students on the roster can view solutions
    # (we don't want future-semester students viewing previous-semester
    # solutions!).
    try:
        roster = get_roster(course, semester)
    except Exception as e:
        flask.flash(str(e))
        roster = None

    if roster is None:
        msg = "Failed to load <code>roster.csv</code>."
        flask.flash(msg)
        return error_response(course, semester, username, msg)

    if ps["status"]["state"] != "final":
        if is_admin:
            flask.flash(
                "Viewing solution code as admin; solution is not"
              + " visible to students until revision period is over."
            )
        else:
            flask.flash(
                (
                    "You cannot view the solutions for {pset} {task} until the"
                  + " revision period is over."
                ).format(pset=psid, task=taskid)
            )
            return goback(course, semester)

    elif effective_user not in roster: # not on the roster
        if is_admin:
            flask.flash(
                (
                    "Viewing solution code as admin; solution is not"
                  + " visible to user {} as they are not on the roster"
                  + " for this course/semester."
                ).format(effective_user)
            )
        else:
            flask.flash(
                (
                    "You cannot view solutions for {course} {semester}"
                  + " because you are not on the roster for that class."
                ).format(course=course, semester=semester)
            )
            return goback(course, semester)

    elif not (
        app.config.get("DISPLAY_UNSUBMITTED_SOLUTIONS")
     or initial_task.get("submitted")
     or revised_task.get("submitted")
    ):
        # This user hasn't submitted this task, so we'd like to make it
        # possible for them to get an extension later without worrying about
        # whether they've accessed solution code in the mean time.
        if is_admin:
            flask.flash(
                (
                    "Viewing solution code as admin; solution is not"
                  + " visible to user {} as they don't have a submission"
                  + " for this task."
                ).format(effective_user)
            )
        else:
            flask.flash(
                (
                    "You cannot view the solution for {} {} becuase you haven't"
                  + "submitted that task."
                ).format(psid, taskid)
            )
            return goback(course, semester)

    # At this point, we've verified it's okay to display the solution:
    # the pset is finalized, and the user is an admin or at least on the
    # roster for this particular course/semester, and the user has a
    # submission for this task.

    # We'd like the feedback CSS & JS because we're going to render code
    # as HTML using potluck.
    # TODO: THESE THINGS...
    fb_css = potluck.dock.get_css()
    fb_js = potluck.dock.get_js()

    # TODO: This feels a bit hardcoded... can we do better?
    # TODO: Multi-file stuff!
    soln_filename = os.path.join(
        evaluation_directory(course, semester),
        "specs",
        task["id"],
        "soln",
        task["filename"]
    )

    with open(soln_filename, 'r') as fin:
        soln_code = fin.read()

    soln_code_html = potluck.report.render_code(
        taskid,
        soln_filename,
        soln_code
    )

    return flask.render_template(
        'solution.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        is_admin=is_admin,
        masquerade_as=masquerade_as,
        effective_user=effective_user,
        ps=ps,
        task=task,
        task_info=task_info,
        soln_code=soln_code,
        rendered_soln=soln_code_html,
        fb_css=fb_css,
        fb_js=fb_js,
        support_link=app.config["SUPPORT_LINK"]
    )


@app.route('/<course>/<semester>/gradesheet/<psid>', methods=['GET'])
@flask_cas.login_required
@augment_arguments
def route_gradesheet(
    course,
    semester,
    psid,
    # Augmented arguments
    username,
    is_admin,
    masquerade_as,
    effective_user,
    task_info
):
    """
    Visible by admins only, this route displays an overview of the status
    of every student on the roster, with links to the feedback views for
    each student/pset/phase/task.
    """
    if not is_admin:
        flask.flash("You do not have permission to view the gradesheet.")
        return goback(course, semester)

    # Create base task info from logged-in user's perspective
    base_task_info = copy.deepcopy(task_info)
    amend_task_info(course, semester, base_task_info, username)

    try:
        ps = get_ps_obj(base_task_info, psid)
    except ValueError as e:
        flask.flash(str(e))
        return goback(course, semester)

    # Get the roster
    try:
        roster = get_roster(course, semester)
    except Exception as e:
        flask.flash(str(e))
        roster = None

    if roster is None:
        msg = "Failed to load <code>roster.csv</code>."
        flask.flash(msg)
        return error_response(course, semester, username, msg)

    initial_task_times = {}
    revision_task_times = {}
    rows = []
    for stid in sorted(
        roster,
        key=lambda stid: (
            roster[stid]["course_section"],
            roster[stid]["sortname"]
        )
    ):
        row = roster[stid]
        row_info = copy.deepcopy(task_info)
        amend_task_info(course, semester, row_info, row["username"])
        row["task_info"] = row_info
        psobj = get_ps_obj(row_info, psid)
        row["this_pset"] = psobj

        psobj["total_time"] = 0

        for taskobj in psobj["tasks"]:
            taskid = taskobj["id"]
            time_spent = taskobj["time_spent"]
            if time_spent is not None:
                time_val = time_spent["time_spent"]
                if taskid not in initial_task_times:
                    initial_task_times[taskid] = {}

                if isinstance(time_val, (float, int)):
                    initial_task_times[taskid][row["username"]] = time_val
                    taskobj["initial_time_val"] = time_val
                    if isinstance(psobj["total_time"], (int, float)):
                        psobj["total_time"] += time_val
                elif isinstance(time_val, str) and time_val != "":
                    taskobj["initial_time_val"] = time_val
                    psobj["total_time"] = "?"
                else: # empty string or None or the like
                    taskobj["initial_time_val"] = "?"
            else:
                taskobj["initial_time_val"] = 0

            rev_time_spent = taskobj.get("revision", {}).get("time_spent")
            if rev_time_spent is not None:
                rev_time_val = rev_time_spent["time_spent"]
                if taskid not in revision_task_times:
                    revision_task_times[taskid] = {}

                if isinstance(rev_time_val, (float, int)):
                    revision_task_times[taskid][row["username"]] = rev_time_val
                    taskobj["revision_time_val"] = rev_time_val
                    if isinstance(psobj["total_time"], (int, float)):
                        psobj["total_time"] += rev_time_val
                    if isinstance(taskobj["initial_time_val"], (int, float)):
                        taskobj["combined_time_val"] = (
                            taskobj["initial_time_val"]
                          + rev_time_val
                        )
                    elif ( # initial was a non-empty string
                        isinstance(taskobj["initial_time_val"], str)
                    and taskobj["initial_time_val"] not in ("", "?")
                    ):
                        taskobj["combined_time_val"] = "?"
                    else: # empty string or None or the like
                        taskobj["combined_time_val"] = rev_time_val

                elif isinstance(rev_time_val, str) and rev_time_val != "":
                    taskobj["revision_time_val"] = rev_time_val
                    psobj["total_time"] = "?"
                    taskobj["combined_time_val"] = "?"

                else: # empty string or None or the like
                    taskobj["revision_time_val"] = "?"
                    taskobj["combined_time_val"] = taskobj["initial_time_val"]

            else: # no rev time spent
                taskobj["revision_time_val"] = "?"
                taskobj["combined_time_val"] = taskobj["initial_time_val"]

        rows.append(row)

    aggregate_times = {
        phase: {
            "average": { "pset": 0 },
            "median": { "pset": 0 },
            "75th": { "pset": 0 },
        }
        for phase in ("initial", "revision")
    }
    aggregate_times["all"] = {}
    for phase, times_group in [
        ("initial", initial_task_times),
        ("revision", revision_task_times)
    ]:
        for taskid in times_group:
            times = list(times_group[taskid].values())
            if len(times) == 0:
                avg = None
                med = None
                qrt = None
            elif len(times) == 1:
                avg = times[0]
                med = times[0]
                qrt = times[0]
            else:
                avg = sum(times) / len(times)
                med = percentile(times, 50)
                qrt = percentile(times, 75)

            aggregate_times[phase]["average"][taskid] = avg
            aggregate_times[phase]["median"][taskid] = med
            aggregate_times[phase]["75th"][taskid] = qrt

            if avg is not None:
                aggregate_times[phase]["average"]["pset"] += avg
                aggregate_times[phase]["median"]["pset"] += med
                aggregate_times[phase]["75th"]["pset"] += qrt

    # Compute total times taking zero-revision-times into account
    total_timespent_values = []
    for student in [row["username"] for row in roster.values()]:
        total_timespent = 0
        for taskobj in psobj["tasks"]:
            taskid = taskobj["id"]
            this_task_initial_times = initial_task_times.get(taskid, {})
            this_task_revision_times = revision_task_times.get(taskid, {})
            if student in this_task_initial_times:
                total_timespent += this_task_initial_times[student]
            if student in this_task_revision_times:
                total_timespent += this_task_revision_times[student]
        if total_timespent > 0:
            total_timespent_values.append(total_timespent)

    if len(total_timespent_values) == 0:
        avg = 0
        med = 0
        qrt = 0
    elif len(total_timespent_values) == 1:
        avg = total_timespent_values[0]
        med = total_timespent_values[0]
        qrt = total_timespent_values[0]
    else:
        avg = sum(total_timespent_values) / len(total_timespent_values)
        med = percentile(total_timespent_values, 50)
        qrt = percentile(total_timespent_values, 75)

    aggregate_times["all"]["average"] = avg
    aggregate_times["all"]["median"] = med
    aggregate_times["all"]["75th"] = qrt

    # Get the student info
    try:
        student_info = get_student_info(course, semester)
    except Exception as e:
        flask.flash(str(e))
        student_info = None

    return flask.render_template(
        'gradesheet.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        is_admin=is_admin,
        masquerade_as=masquerade_as,
        task_info=task_info,
        ps=ps,
        roster=rows,
        student_info=student_info,
        aggregate_times=aggregate_times
    )


#---------#
# Helpers #
#---------#

def error_response(course, semester, username, cause):
    """
    Shortcut for displaying major errors to the users so that they can
    bug the support line instead of just getting a pure 404.
    """
    return flask.render_template(
        'error.html',
        course_name=app.config.get("COURSE_NAMES", {}).get(course, course),
        course=course,
        semester=semester,
        username=username,
        announcements="Piazza",
        support_link=app.config["SUPPORT_LINK"],
        error=cause,
        task_info={}
    )


def get_ps_obj(task_info, psid):
    """
    Gets the pset object with the given ID. Raises a ValueError if there
    is no such pset object, or if there are multiple matches.
    """
    psmatches = [ps for ps in task_info["psets"] if ps["id"] == psid]
    if len(psmatches) == 0:
        raise ValueError("Unknown problem set '{}'".format(psid))
    elif len(psmatches) > 1:
        raise ValueError("Multiple problem sets with ID '{}'!".format(psid))
    else:
        return psmatches[0]


def get_task_obj(ps_obj, taskid, redirect=Exception):
    """
    Extracts a task object with the given ID from the given pset object,
    or raises a ValueError if there is no matching task object or if
    there are multiple matches.
    """
    taskmatches = [task for task in ps_obj["tasks"] if task["id"] == taskid]
    if len(taskmatches) == 0:
        raise ValueError(
            "Problem set {} has no task '{}'".format(ps_obj["id"], taskid)
        )
    elif len(taskmatches) > 1:
        raise ValueError(
            "Multiple tasks in problem set {} with ID '{}'!".format(
                ps_obj["id"],
                taskid
            )
        )
    else:
        return taskmatches[0]


def check_user_privileges(admin_info, username):
    """
    Returns a pair containing a boolean indicating whether a user is an
    admin or not, and either None, or a string indicating the username
    that the given user is masquerading as.

    Requires admin info as returned by get_admin_info.
    """
    admins = admin_info.get("admins", [])
    is_admin = username in admins

    masquerade_as = None
    # Only admins can possibly masquerade
    if is_admin:
        masquerade_as = admin_info.get("MASQUERADE", {}).get(username)
        # You cannot masquerade as an admin
        if masquerade_as in admins:
            flask.flash("Error: You cannot masquerade as another admin!")
            masquerade_as = None
    elif admin_info.get("MASQUERADE", {}).get(username):
        print(
            (
                "Warning: User '{}' cannot masquerade because they are"
              + "not an admin."
            ).format(username)
        )

    return (is_admin, masquerade_as)


def set_pause_time(admin_info, task_info, username, masquerade_as=None):
    """
    Sets the PAUSE_AT value in the given task_info object based on any
    PAUSE_USERS entries for either the given true username or the given
    masquerade username. The pause value for the username overrides the
    value for the masqueraded user, so that by setting PAUSE_AT for an
    admin account plus creating a masquerade entry, you can act as any
    user at any point in time.
    """
    pu = admin_info.get("PAUSE_USERS", {})
    if username in pu:
        task_info["PAUSE_AT"] = pu[username]
    elif masquerade_as in pu:
        task_info["PAUSE_AT"] = pu[masquerade_as]
    elif "PAUSE_AT" in admin_info:
        task_info["PAUSE_AT"] = admin_info["PAUSE_AT"]
    # else we don't set PAUSE_AT at all


def amend_task_info(course, semester, task_info, username):
    """
    Amends task info object with extra keys in each pset to indicate pset
    state. Also adds summary information to each task of the pset based
    on user feedback generated so far. Also checks potluck inflight
    status and adds a "submitted" key to each task where appropriate.
    Template code should be careful not to reveal feedback info not
    warranted by the current pset state.
    """
    for pset in task_info["psets"]:
        # Add status info to the pset object:
        amend_pset(course, semester, task_info, pset, username)
        # Add summary info to each task, and duplicate for revisions
        for task in pset["tasks"]:
            rev_task = copy.deepcopy(task)
            amend_task(
                course,
                semester,
                task_info,
                pset["id"],
                rev_task,
                username,
                "revision"
            )
            task["revision"] = rev_task
            amend_task(
                course,
                semester,
                task_info,
                pset["id"],
                task,
                username,
                "initial"
            )


def amend_pset(course, semester, task_info, pset_obj, username):
    """
    Adds a "status" key to the given problem set object (which should be
    part of the given task info). The username is used to look up
    extension information.
    """
    ext_info = get_extensions(course, semester, username)
    initial_ext = ext_info.get("initial", {}).get(pset_obj["id"], False)
    revision_ext = ext_info.get("revision", {}).get(pset_obj["id"], False)
    pset_obj["status"] = pset_status_now(
        username,
        task_info,
        pset_obj,
        extensions=[initial_ext, revision_ext]
    )


def amend_task(course, semester, task_info, psid, task, username, phase):
    """
    Adds task-state-related keys to the given task object. The following
    keys are added:

        "feedback_summary": A feedback summary object (see
            `get_feedback_summary`).
        "time_spent": The time spent info that the user entered for time
            spent when submitting the task (see fetch_time_spent for the
            format). Will be None if that info isn't available.
        "submitted": True if the user has attempted submission (even if
            there were problems) or if we have feedback for them
            (regardless of anything else).
        "submitted_at": A `datetime.datetime` object representing when
            the submission was received, or None if there is no recorded
            submission.
        "eval_elapsed": A `datetime.timedelta` that represents the time
            elapsed since evaluation was started for the submission (in
            possibly fractional seconds).
        "eval_timeout": A `datetime.timedelta` representing the number
            of seconds before the evaluation process should time out.
        "eval_status": The status of the evaluation process (see
            `get_inflight`).
        "submission_status": A string representing the status of the
            submission overall. One of:
                "unsubmitted": no submission yet.
                "inflight": has been submitted; still being evaluated.
                "unprocessed": evaluated but there's an issue (evaluation
                    crashed or elsehow failed to generate feedback).
                "issue": evaluated but there's an issue (evaluation
                    warning or 'incomplete' evaluation result.)
                "complete": Evaluated and there's no major issue (grade
                    may or may not be perfect, but it better than
                    "incomplete").
        "submission_icon": A one-character string used to represent the
            submission status.
        "submission_desc": A brief human-readable version of the
            submission status.
    """
    task["feedback_summary"] = get_feedback_summary(
        course,
        semester,
        task_info,
        username,
        phase,
        psid,
        task["id"]
    )

    task["time_spent"] = fetch_time_spent(
        course,
        semester,
        username,
        phase,
        psid,
        task["id"]
    )

    task["submitted"] = task["feedback_summary"].get("submitted")

    ts, logfile, status = get_inflight(
        course,
        semester,
        username,
        phase,
        psid,
        task["id"]
    )

    # Time submitted and time elapsed since submission
    if ts == "error":
        task["submitted_at"] = "unknown"
        task["eval_elapsed"] = "unknown"
    elif ts is not None:
        submit_time = time_from_timestamp(ts)
        task["submitted_at"] = submit_time
        task["eval_elapsed"] = datetime.datetime.now() - submit_time
    else:
        try:
            # TODO: What here?
            submit_time = time_from_potluck_timestamp(
                task["feedback_summary"]["timestamp"]
            )
            task["submitted_at"] = submit_time
            task["eval_elapsed"] = datetime.datetime.now() - submit_time
        except Exception:
            task["submitted_at"] = None
            task["eval_elapsed"] = None

    task["eval_timeout"] = datetime.timedelta(
        seconds=app.config["FINAL_EVAL_TIMEOUT"]
    )

    if ts == "error":
        task["eval_status"] = "unknown"
    else:
        task["eval_status"] = status

    if status is not None:
        task["submitted"] = True

    # Set detailed submission status along with icon and description
    if task["eval_status"] == "unknown":
        task["submission_status"] = "inflight"
        task["submission_icon"] = "‽"
        task["submission_desc"] = "status unknown"
    if task["eval_status"] in ("initial", "in_progress"):
        task["submission_status"] = "inflight"
        task["submission_icon"] = "?"
        task["submission_desc"] = "evaluation in progress"
    elif task["eval_status"] in ("error", "expired"):
        task["submission_status"] = "unprocessed"
        task["submission_icon"] = "☹"
        task["submission_desc"] = "processing error"
    elif task["eval_status"] == "completed" or task["submitted"]:
        report = task["feedback_summary"]["report"]
        if report["warnings"]:
            task["submission_status"] = "issue"
            task["submission_icon"] = "✗"
            task["submission_desc"] = "major issue"
        elif report["evaluation"] == "incomplete":
            task["submission_status"] = "issue"
            task["submission_icon"] = "✗"
            task["submission_desc"] = "incomplete submission"
        elif report["evaluation"] == "not evaluated":
            task["submission_status"] = "unprocessed"
            task["submission_icon"] = "☹"
            task["submission_desc"] = "submission not evaluated"
        else:
            task["submission_status"] = "complete"
            task["submission_icon"] = "✓"
            task["submission_desc"] = "submitted"
    else:
        task["submission_status"] = "unsubmitted"
        task["submission_icon"] = "…"
        task["submission_desc"] = "not yet submitted"


def percentile(dataset, pct):
    """
    Computes the nth percentile of the dataset by a weighted average of
    the two items on either side of that fractional index within the
    dataset. pct must be a number between 0 and 100 (inclusive).

    Returns None when given an empty dataset, and always returns the
    singular item in the dataset when given a dataset of length 1.
    """
    fr = pct / 100.0
    if len(dataset) == 1:
        return dataset[0]
    elif len(dataset) == 0:
        return None
    srt = sorted(dataset)
    fridx = fr * (len(srt) - 1)
    idx = int(fridx)
    if idx == fridx:
        return srt[idx] # integer index -> no averaging
    leftover = fridx - idx
    first = srt[idx]
    second = srt[idx + 1] # legal index because we can't have hit the end
    return first * (1 - leftover) + second * leftover


#----------------#
# Time functions #
#----------------#

ONE_MINUTE = 60
ONE_HOUR = ONE_MINUTE * 60
ONE_DAY = ONE_HOUR * 24
ONE_WEEK = ONE_DAY * 7


def pset_status_now(username, task_info, pset_obj, extensions=(False, False)):
    """
    Returns the current state of the given pset object (also needs the
    task info object and the username). If "PAUSE_AT" is set in the task
    object and non-empty (see set_pause_time), that moment, not the
    current time, will be used. Extensions must contain two values (one
    for the initial phase and one for the revision phase). They may each
    be False for no extension, True for the default extension, or an
    integer number of hours. Those hours will be added to the effective
    initial and revision deadlines.

    Returns a dictionary with 'state', 'initial-extension',
    'revision-extension', 'release', 'due', 'reviewed', and 'finalized',
    keys. Each of the 'release', 'due', 'reviewed', and 'finalized' keys
    will be a sub-dictionary with the following keys:

        'at': A dateimte.datetime object specifying absolute timing.
        'at_str': A string representation of the above.
        'until': A datetime.timedelta representing time until the event (will
            be negative afterwards).
        'until_str': A string representation of the above.

    Each of the sub-values will be none if the pset doesn't have a
    deadline set.

    The 'state' value will be one of:

        "unreleased": This pset hasn't yet been released; don't display
            any info about it.
        "released": This pset has been released and isn't due yet.
        "under_review": This pset's due time has passed, but the feedback
            review period hasn't expired yet.
        "revisable": This pset's due time is past, and the review period has
            expired, so full feedback should be released, but revisions
            may still be submitted.
        "final": This pset's due time is past, the review period has
            expired, and the revision period is also over, so full
            feedback is available, and no more submissions will be
            accepted.
        "unknown": This pset doesn't have a due date. The
            seconds_remaining value will be None.

    The 'initial_extension' and 'revision_extension' will both be numbers
    specifying how many hours of extension were granted (these numbers
    are already factored into the deadline information the status
    contains). These numbers will be 0 for students who don't have
    extensions.
    """
    # Get extension/revision durations and grace period from task info:
    standard_ext_hrs = task_info.get("extension_hours", 24)
    review_hours = task_info.get("review_hours", 24)
    grace_mins = task_info.get("grace_minutes", 0)
    revision_hours = task_info.get("revision_hours", 72)

    # Figure out extension amounts
    initial_extension = 0
    if extensions[0] is True:
        initial_extension = standard_ext_hrs
    elif isinstance(extensions[0], (int, float)):
        initial_extension = extensions[0]
    elif extensions[0] is not False:
        flask.flash(
            "Ignoring invalid initial extension value '{}'".format(
                extensions[0]
            )
        )

    revision_extension = 0
    if extensions[1] is True:
        revision_extension = standard_ext_hrs
    elif isinstance(extensions[1], (int, float)):
        revision_extension = extensions[1]
    elif extensions[1] is not False:
        flask.flash(
            "Ignoring invalid revision extension value '{}'".format(
                extensions[1]
            )
        )

    # The default result
    result = {
        'state': "unknown",
        'release': {
            'at': None,
            'at_str': 'unknown',
            'until': None,
            'until_str': 'at some point (not yet specified)'
        },
        'due': {
            'at': None,
            'at_str': 'unknown',
            'until': None,
            'until_str': 'at some point (not yet specified)'
        },
        'reviewed': {
            'at': None,
            'at_str': 'unknown',
            'until': None,
            'until_str': 'at some point (not yet specified)'
        },
        'finalized': {
            'at': None,
            'at_str': 'unknown',
            'until': None,
            'until_str': 'at some point (not yet specified)'
        },
        'initial_extension': 0,
        'revision_extension': 0,
    }

    # Save extension info
    result['initial_extension'] = initial_extension or 0
    result['revision_extension'] = revision_extension or 0

    # Get current time:
    if "PAUSE_AT" in task_info and task_info["PAUSE_AT"]:
        now = task_time__time(task_info, task_info["PAUSE_AT"])
    else:
        now = datetime.datetime.now()

    # Get release date/time:
    release_at = pset_obj.get("release", None) # if None, we assume release
    if release_at is not None:
        release_at = task_time__time(
            task_info,
            release_at,
            default_time_of_day=task_info.get(
                "default_release_time_of_day",
                "23:59"
            )
        )
        # Fill in release info
        result['release']['at'] = release_at
        result['release']['at_str'] = fmt_datetime(release_at)
        until_release = release_at - now
        result['release']['until'] = until_release
        result['release']['until_str'] = fuzzy_time(
            until_release.total_seconds()
        )

    # Get due date/time:
    due_at = pset_obj.get("due", None)
    if due_at is None:
        # Return empty result
        return result
    else:
        due_at = task_time__time(
            task_info,
            due_at,
            default_time_of_day=task_info.get(
                "default_due_time_of_day",
                "23:59"
            )
        )
        review_end = due_at + datetime.timedelta(hours=review_hours)

    due_string = fmt_datetime(due_at)

    base_deadline = due_at

    # Add extension hours:
    if initial_extension > 0:
        due_at += datetime.timedelta(hours=initial_extension)
        due_string = fmt_datetime(due_at) + (
            ' <span class="extension_taken">'
          + '(after accounting for your {}‑hour extension)'
          + '</span>'
        ).format(initial_extension)

    grace_deadline = due_at + datetime.timedelta(minutes=grace_mins)

    # Fill in due info
    result['due']['at'] = due_at
    result['due']['at_str'] = due_string
    until_due = due_at - now
    result['due']['until'] = until_due
    result['due']['until_str'] = fuzzy_time(until_due.total_seconds())

    # Fill in review info
    result['reviewed']['at'] = review_end
    result['reviewed']['at_str'] = fmt_datetime(review_end)
    until_reviewed = review_end - now
    result['reviewed']['until'] = until_reviewed
    result['reviewed']['until_str'] = fuzzy_time(
        until_reviewed.total_seconds()
    )

    # Get final date/time:
    # Note: any extension to the initial deadline is ignored. A separate
    # revision extension should be issued when an initial extension eats
    # up too much of the revision period.
    final_at = base_deadline + datetime.timedelta(
        hours=review_hours + revision_hours
    )

    final_string = fmt_datetime(final_at)

    # Add extension hours:
    if revision_extension > 0:
        final_at += datetime.timedelta(hours=revision_extension)
        final_string = fmt_datetime(final_at) + (
            ' <span class="extension_taken">'
          + '(after accounting for your {}‑hour extension)'
          + '</span>'
        ).format(revision_extension)

    grace_final = final_at + datetime.timedelta(minutes=grace_mins)

    # Fill in finalization info
    result['finalized']['at'] = final_at
    result['finalized']['at_str'] = final_string
    until_final = final_at - now
    result['finalized']['until'] = until_final
    result['finalized']['until_str'] = fuzzy_time(until_final.total_seconds())

    # Check release time:
    if release_at and now < release_at:
        result['state'] = "unreleased"
    # Passed release_at point: check if it's due or not
    elif now < grace_deadline:
        # Note time-remaining ignores grace period and may be negative
        result['state'] = "released"
    # Passed due_at point; check if it's still under review:
    elif now < review_end:
        result['state'] = "under_review"
    # Passed review period: are revisions still being accepted?
    elif now < grace_final:
        result['state'] = "revisable"
    # Passed review period: it's final
    else:
        result['state'] = "final"

    return result


def task_time__time(task_info, time_string, default_time_of_day=None):
    """
    Converts a time string from task info into a time value. Uses
    str__time with the default hour and minute from the task info.
    """
    if default_time_of_day is None:
        default_time_of_day = task_info.get("default_time_of_day", "23:59")
    hd = int(default_time_of_day.split(':')[0])
    md = int(default_time_of_day.split(':')[1])

    return str__time(time_string, default_hour=hd, default_minute=md)


def str__time(tstr, default_hour=23, default_minute=59, default_second=59):
    """
    Converts a string to a datetime object. Default format is:

    yyyy-mm-dd HH:MM:SS TZ

    The hours, minutes, seconds, and timezone are optional. Timezone must
    be given as +HH:SS or -HH:SS. Hours/minutes/seconds default to the end
    of the given day/hour/minute (i.e., 23:59:59), not to 00:00:00,
    unless alternative defaults are specified.
    """
    formats = [
        ("%Y-%m-%d %H:%M:%S %z", {}),
        ("%Y-%m-%d %H:%M:%S", {}),
        ("%Y-%m-%d %H:%M %z", {"second": default_second}),
        ("%Y-%m-%d %H:%M", {"second": default_second}),
        (
            "%Y-%m-%d",
            {
                "second": default_second,
                "minute": default_minute,
                "hour": default_hour
            }
        )
    ]
    result = None
    for f, defaults in formats:
        try:
            result = datetime.datetime.fromtimestamp(
                time.mktime(time.strptime(tstr, f))
            )
        except Exception:
            pass

        if result is not None:
            result = result.replace(**defaults)
            break

    if result is None:
        raise ValueError("Couldn't parse time data: '{}'".format(tstr))

    return result


TS_FORMAT = "%Y-%m-%d@%H:%M:%S"
POTLUCK_TS_FORMAT = "%Y-%m-%d %H:%M:%S %Z"


def current_timestamp():
    """
    Returns a string based on the current time (down to the second).
    """
    return timestamp_from_time(datetime.datetime.now())


def timestamp_from_time(time):
    """
    Converts a datetime.datetime into a timestamp.
    """
    return time.strftime(TS_FORMAT)


def time_from_timestamp(timestamp):
    """
    Converts a timestamp back into a datetime.datetime.
    """
    return datetime.datetime.strptime(timestamp, TS_FORMAT)


def time_from_potluck_timestamp(timestamp):
    """
    Converts a potluck-style timestamp back into a datetime.datetime.
    """
    filtered = ' '.join(timestamp.split(' ')[:3])
    return datetime.datetime.strptime(filtered, POTLUCK_TS_FORMAT)


#--------------------#
# Filename functions #
#--------------------#

def unused_filename(target):
    """
    Checks whether the target already exists, and if it does, appends _N
    before the file extension, where N is the smallest positive integer
    such that the returned filename is not the name of an existing file.
    If the target does not exists, returns it.
    """
    n = 1
    backup = target
    base, ext = os.path.splitext(target)
    while os.path.exists(backup):
        backup = base + "_" + str(n) + ext
        n += 1

    return backup


def extensions_filename(course, semester, username):
    """
    Craft the filename for the extensions file for a user.
    """
    return flask.safe_join(
        extensions_folder(course, semester),
        username + ".json"
    )


def inflight_filename(course, semester, username):
    """
    Craft the filename where in-flight info should be stored for a user.
    """
    return flask.safe_join(
        logs_folder(course, semester),
        "inflight-{}".format(username)
    )


def time_spent_filename(course, semester, username, phase, psid, taskid):
    """
    Craft the filename where time-spent info should be stored for the
    given user/phase/pset/task.
    """
    return flask.safe_join(
        submissions_folder(course, semester),
        psid + '-' + phase,
        username,
        "{}-info.json".format(taskid)
    )


def get_submission_filename(
    course,
    semester,
    task_info,
    username,
    phase,
    psid,
    taskid
):
    """
    Returns the filename for the user's submission for a given
    phase/pset/task. Raises a ValueError if the pset or task doesn't
    exit.
    """
    ps = get_ps_obj(task_info, psid)
    task = get_task_obj(ps, taskid)

    return flask.safe_join(
        submissions_folder(course, semester),
        psid + '-' + phase,
        username,
        task["filename"]
    )


def get_feedback_filename(
    course,
    semester,
    task_info,
    username,
    phase,
    psid,
    taskid
):
    """
    Returns the filename for the user's feedback file for a given
    phase/pset/task. Raises a ValueError if the pset or task doesn't
    exit.

    Note that unlike normal feedback reports, the web service uses
    per-task report files, because that's how students submit stuff.
    """
    filename = (
        "{course}-{semester}-{username}-{pset}-{task}.json"
    ).format(
        course=course,
        semester=semester,
        pset=psid,
        username=username,
        task=taskid
    )

    return flask.safe_join(
        reports_folder(course, semester),
        psid + '-' + phase,
        filename
    )


#--------------------#
# File I/O functions #
#--------------------#

def get_task_info(course, semester):
    """
    Loads the task info from the JSON file (or returns a cached version
    if the file hasn't been modified since we last loaded it).

    Returns None if the file doesn't exist or can't be parsed.

    Pset and task URLs are added to the information loaded.

    Note: The task info file needs to contain weight values for each task
    that match any custom weights specified in the task spec, or else the
    submission UI will lie to students about the weight of each task!
    TODO: FIX THIS!
    """
    filename = task_info_file(course, semester)
    try:
        result = sync.load_or_get_cached(filename)
    except Exception:
        flask.flash("Failed to read task info file!")
        result = None

    if result is None:
        return None

    psfmt = app.config.get("PSET_URLS", {}).get(course, "#")
    taskfmt = app.config.get("TASK_URLS", {}).get(course, "#")
    for pset in result["psets"]:
        pset["url"] = psfmt.format(
            semester=semester,
            pset=pset["id"]
        )
        for task in pset["tasks"]:
            task["url"] = taskfmt.format(
                semester=semester,
                pset=pset["id"],
                task=task["id"]
            )

    return result


def get_admin_info(course, semester):
    """
    Reads the ocean-admin.json file to get information about which users
    are administrators and various other settings.
    """
    filename = admin_info_file(course, semester)
    try:
        result = sync.load_or_get_cached(filename)
    except Exception:
        flask.flash("Failed to read admin info file '{}'!".format(filename))
        result = None

    return result # might be None


class AsRoster(sync.View):
    """
    Encoding and decoding for CSV rosters, which are cached. The roster
    structure is a dictionary mapping usernames to student info.
    """
    @staticmethod
    def encode(obj):
        """
        A roster *cannot* be encoded, because we are not interested in
        writing it to a file.
        # TODO: Roster editing in-app?
        """
        raise NotImplementedError(
            "Cannot encode a roster: rosters are read-only."
        )

    @staticmethod
    def decode(string):
        """
        A roster is read from a roaster file by extracting the text and
        running it through `load_roster_from_stream`.
        """
        lines = string.strip().split('\n')
        return load_roster_from_stream(lines)


def get_roster(course, semester):
    """
    Loads and returns the roster file. Returns None if the file is
    missing.
    """
    return sync.load_or_get_cached(
        roster_file(course, semester),
        view=AsRoster,
        missing=None
    )


class AsStudentInfo(sync.View):
    """
    Encoding and decoding for TSV student info files, which are cached.
    The student info structure is a dictionary mapping usernames to
    additional student info.
    """
    @staticmethod
    def encode(obj):
        """
        Student info *cannot* be encoded, because we are not interested
        in writing it to a file.
        # TODO: Student info editing in-app?
        """
        raise NotImplementedError(
            "Cannot encode student info: student info is read-only."
        )

    @staticmethod
    def decode(string):
        """
        Extra student info is read from a student info file by extracting
        the text, loading it as Excel-TSV data, and turning it into a
        dictionary where each student ID maps to a dictionary containing
        the columns as keys with values from that column as values.
        """
        reader = csv.DictReader(
            (line for line in string.strip().split('\n')),
            dialect="excel-tab"
        )
        result = {}
        for row in reader:
            entry = {}
            for key in REMAP_STUDENT_INFO:
                entry[REMAP_STUDENT_INFO[key]] = row.get(key)
            entry["username"] = entry["email"].split('@')[0]
            result[entry['username']] = entry
        return result


def get_student_info(course, semester):
    """
    Loads and returns the student info file. Returns None if the file is
    missing.
    """
    return sync.load_or_get_cached(
        student_info_file(course, semester),
        view=AsStudentInfo,
        missing=None
    )


def get_extensions(course, semester, username):
    """
    Gets the extensions dictionary for a user. Returns an empty
    dictionary if the user doesn't have any extensions file.
    """
    # TODO: Handle file read errors better...
    try:
        return sync.read_file(
            extensions_filename(course, semester, username),
            missing={}
        )
    except Exception:
        flask.flash("Failed to read extensions file!")
        return {}


def set_extension(course, semester, username, phase, psid, duration=True):
    """
    Sets an extension value for the given user on the given pset. May be
    an integer number of hours, or just True (the default) for the
    standard extension (whatever is listed in tasks.json). Set to False
    to remove any previously granted extension.

    Note: There's a race condition here if we're setting an extension
    value multiple times simultaneously! TODO: Fix that (requires atomic
    read/write in sync.py).

    Returns True if it succeeds and False if it knows that it failed.
    """
    uext = get_extensions(course, semester, username)

    if phase not in uext:
        uext[phase] = {}

    if duration != uext[phase].get(psid): # skip update if duration is the same
        uext[phase][psid] = duration

        try:
            sync.write_file(
                extensions_filename(course, semester, username),
                uext
            )
        except Exception:
            flask.flash("Failed to write extensions file!")
            return False

    return True


def get_inflight(course, semester, username, phase, psid, taskid):
    """
    Returns a triple containing the timestamp at which processing for the
    given user/phasepset/task was started, the filename of the log file
    for that evaluation run, and a string indicating the status of the
    run. Reads that log file to check whether the process has completed,
    and updates in-flight state accordingly. Returns (None, None, None)
    if no attempts to grade the given task have been made yet.

    The status string will be one of:
        "initial" - evaluation hasn't started yet.
        "in_progress" - evaluation is running.
        "error" - evaluation noted an error in the log.
        "expired" - We didn't hear back from evaluation, but it's been so
            long that we've given up hope.
        "completed" - evaluation finished.

    When status is "error", "expired", or "completed", it's appropriate
    to initiate a new evaluation run for that file, but in other cases,
    the existing run should be allowed to terminate first.

    In rare cases, when an exception is encountered trying to read the
    file even after a second attempt, the timestamp will be set to
    "error" with status and filename values of None.
    """
    iff = inflight_filename(course, semester, username)

    # default view reads file as JSON
    try:
        inflight = sync.read_file(iff, missing={})
    except Exception:
        flask.flash("Failed to read in-flight file!")
        inflight = None

    # try again...
    if inflight is None:
        time.sleep(0.01) # delay a tiny bit
        try:
            inflight = sync.read_file(iff, missing={})
        except Exception:
            flask.flash("Failed to read in-flight file!")
            return ("error", None, None)

    if phase not in inflight:
        return (None, None, None)

    if psid not in inflight[phase]:
        return (None, None, None)

    if taskid not in inflight[phase][psid]:
        return (None, None, None)

    timestamp, log_filename, status = inflight[phase][psid][taskid]

    if status in ("error", "expired", "completed"):
        # No need to check the file text again
        return (timestamp, log_filename, status)

    # Figure out what the new status should be...
    new_status = status

    # Read the log file to see if evaluation has finished yet
    try:
        log_text = sync.read_file(
            log_filename,
            view=sync.AsIs,
            missing="", # file might not yet be created...
            cache=False
            # no point in caching contents of a log that we ignore once it
            # stops updating
        )
    except Exception:
        flask.flash("Failed to read evaluation log file!")
        # Treat as a missing file
        log_text = ""

    # If anything has been written to the log file, we're in progress...
    if status == "initial" and log_text != "":
        new_status = "in_progress"

    # Check for an error
    if potluck.report.ERROR_MSG in log_text:
        new_status = "error"

    # Check absolute timeout
    elapsed = datetime.datetime.now() - time_from_timestamp(timestamp)
    allowed = datetime.timedelta(seconds=app.config["FINAL_EVAL_TIMEOUT"])
    if new_status != "error" and elapsed > allowed:
        new_status = "expired"

    # Check for completion message (ignored if there's an error or timeout)
    if (
        status in ("initial", "in_progress")
    and log_text.endswith(potluck.report.DONE_MSG + '\n')
    ):
        new_status = "completed"

    # Now we've got our result
    result = [timestamp, log_filename, new_status]

    # Write new status if it has changed
    if new_status != status:
        inflight[phase][psid][taskid] = result
        try:
            sync.write_file(iff, inflight)
        except Exception:
            pass

    # Return our result
    return result


def put_inflight(course, semester, username, phase, psid, taskid):
    """
    Picks a new log filename for the given user/phase/pset/task and
    returns a triple containing a string timestamp, the new log filename,
    and the status string "initial", while also writing that information
    into the inflight data for that user so that get_inflight will return
    it until evaluation is finished.

    Returns (None, None, None) if there is already an in-flight log file
    for this user/pset/task that has a status other than "error",
    "expired", or "completed".

    Note: this method is prone to race conditions on the file name! Avoid
    calling put_inflight for the same user/pset/task simultaneously...

    TODO: Provide atomic read+update in sync.py to be able to avoid this
    problem!
    """
    # Check whether there's another log file that's in-flight:
    prev_timestamp, prev_filename, prev_status = get_inflight(
        course,
        semester,
        username,
        phase,
        psid,
        taskid
    )
    if prev_timestamp == "error":
        return ("error", None, None)
    elif (
        (
            prev_timestamp is not None
        and prev_status in ("initial", "in_progress")
        )
    ):
        return (None, None, None)

    # Generate a timestamp for the log file
    timestamp = current_timestamp()

    # We should have per-process different seeds, and since the random
    # module is thread-safe, requests in the same process should still
    # get sequential values from the generator. Since a race condition is
    # only posisble when calling put_inflight very quickly, although this
    # doesn't make that impossible, it should make it vanishingly likely
    # even when put_inflight is called quickly, which it shouldn't be in
    # the first place.
    rand = random.randint(0, 1000)

    # Read in-flight info in preparation for updating it
    # (default view reads file as JSON)
    iff = inflight_filename(course, semester, username)
    try:
        inflight = sync.read_file(iff, missing={})
    except Exception:
        flask.flash("Failed to read in-flight file!")
        return ("error", None, None)

    # Get unused log filename (this part has serious race conditions)
    logfile = unused_filename(
        flask.safe_join(
            logs_folder(course, semester),
            "{username}-{phase}-{psid}-{taskid}-{timestamp}-{rand}.log".format(
                username=username,
                phase=phase,
                psid=psid,
                taskid=taskid,
                timestamp=timestamp,
                rand=rand
            )
        )
    )

    # Update inflight info
    if phase not in inflight:
        inflight[phase] = {}
    if psid not in inflight[phase]:
        inflight[phase][psid] = {}

    inflight[phase][psid][taskid] = [timestamp, logfile, "initial"]

    # Write updated in-flight info
    try:
        sync.write_file(iff, inflight)
    except Exception:
        flask.flash("Failed to write in-flight file!")
        return ("error", None, None)

    # Return the timestamp, filename, and status that we recorded
    return (timestamp, logfile, "initial")


def fetch_time_spent(course, semester, username, phase, psid, taskid):
    """
    Returns a time-spent record for the given user/phase/pset/task. It
    has the following keys:

        "phase": The phase.
        "psid": The problem-set ID.
        "taskid": The task ID.
        "timestamp": Timestamp (see `current_timestamp`) indicating when
            the information was last updated.
        "time_spent": A floating-point number or string describing the
            user's description of the time they spent on the task.
        "old_timestamp": If present, indicates that the time_spent value
            came from a previous entry and was preserved when a newer
            entry would have been empty. Shows the time at which the
            previous entry was entered.
            TODO: preserve across multiple empty entries?

    Returns None if there is no information for that user/pset/task yet,
    or if an error is encountered while trying to access that
    information.

    TODO: More nuanced error reporting.
    """
    # Filename to use
    tsfile = time_spent_filename(
        course,
        semester,
        username,
        phase,
        psid,
        taskid
    )

    # Read the file and return the result
    try:
        return sync.read_file(tsfile, missing=None)
    except Exception:
        return None


def record_time_spent(
    course,
    semester,
    username,
    phase,
    psid,
    taskid,
    time_spent
):
    """
    Inserts a time spent entry into the given user's time spent info.

    Note: This function is vulnerable to a race condition when called
    multiple times with the same user/phase/pset/task, which could result
    in one function call overriding the time spent value set by another.

    Subsequent function calls overwrite the time spent value in any case,
    so this is not necessarily a super-important issue.
    """
    # Filename to use
    tsfile = time_spent_filename(
        course,
        semester,
        username,
        phase,
        psid,
        taskid
    )

    # Generate a timestamp for the log file
    timestamp = current_timestamp()

    # Convert to a number if we can
    try:
        time_spent = float(time_spent)
    except Exception:
        pass

    # Here's the info we store
    info = {
        "phase": phase,
        "psid": psid,
        "taskid": taskid,
        "timestamp": timestamp,
        "time_spent": time_spent
    }

    # Check for old info if the new info is missing
    if time_spent == "":
        try:
            old_info = sync.read_file(tsfile, missing=None)
        except Exception:
            flask.flash("Failed to read time spent file!")
            old_info = None

        if old_info and old_info["time_spent"] != "":
            info["time_spent"] = old_info["time_spent"]
            info["old_timestamp"] = old_info["timestamp"]
            # The presence of old_timestamp indicates that a more-recent
            # empty timestamp was ignored.

    # Create the destination directory if necessary
    destdir, _ = os.path.split(tsfile)
    ensure_directory(destdir)

    # Write the information, and we're done
    try:
        sync.write_file(tsfile, info)
    except Exception:
        flask.flash("Failed to write time spent file!")


def define_summarized_feedback_view(taskid):
    """
    Defines a View class for summarizing feedback on a particular task.
    """
    class AsFeedbackSummary(sync.View):
        """
        Encoding and decoding for feedback summaries, which are cached.
        """
        @staticmethod
        def encode(obj):
            """
            A feedback summary *cannot* be encoded, because it cannot be
            written to a file. Feedback summaries are only read from full
            feedback files, never written.
            """
            raise NotImplementedError(
                "Cannot encode a feedback summary: summaries are read-only."
            )

        @staticmethod
        def decode(string):
            """
            A feedback summary is read from a feedback file by extracting the
            full JSON feedback and then paring it down to just the essential
            information for the dashboard view.
            """
            if string is None: # happens when the target file doesn't exist
                return {
                    "submitted": False,
                    "partner_username": None,
                    "task_time": None,
                    "ps_total_weight": None,
                    "weight": None,
                    "grade": None,
                    "grade_string": None,
                    "review_level": None,
                    "timestamp": None,
                    "report": {
                        "evaluation": "not evaluated",
                        "warnings": [ "We found no submission for this task." ]
                    }
                }
            # Note taskid is nonlocal here
            fbobj = json.loads(string)
            taskobj = fbobj["tasks"][taskid]
            warnings = taskobj["report"].get("warnings", [])
            evaluation = taskobj["report"].get("evaluation", "not evaluated")
            if evaluation == "incomplete" and len(warnings) == 0:
                warnings.append(
                    "Your submission is incomplete"
                  + " (it did not satisfy even half of the core goals)."
                )
            return {
                "submitted": True,
                "partner_username": fbobj.get("partner_username"),
                "task_time": fbobj["task_times"].get(taskid),
                "ps_total_weight": fbobj["total_weight"],
                "weight": taskobj.get("weight", 1),
                "grade": taskobj.get("grade"),
                "grade_string": taskobj.get("grade_string"),
                "review_level": taskobj.get("review_level", "unknown"),
                "timestamp": fbobj.get("timestamp"),
                "report": {
                    "evaluation": evaluation,
                    "warnings": warnings
                    # report summary and table omitted
                }
            }

    AsFeedbackSummary.__name__ = "{}#{}".format(
        AsFeedbackSummary.__name__,
        taskid
    )
    AsFeedbackSummary.__doc__ += "\nSummarizes {}.".format(taskid)
    return AsFeedbackSummary


def feedback_summary_view(taskid):
    """
    Creates or retrieves a feedback summary View for the given task ID.
    """
    result = sync.build_or_get_singleton(
        "AsFBS#{}".format(taskid),
        lambda key: define_summarized_feedback_view(key.split('#')[1])
    )
    return result


def default_feedback_summary(ps, taskid):
    """
    Returns a default summary object for the given problem set object.
    The summary is a pared-down version of the full feedback .json file
    that stores the result of captain.calc_rubric_grades.
    """
    task = get_task_obj(ps, taskid)
    return {
        "submitted": False, # We didn't find any feedback file!
        "partner_username": None,
        "task_time": None,
        "ps_total_weight": sum(task.get("weight", 1) for task in ps["tasks"]),
        "weight": task.get("weight", 1),
        "grade": None,
        "grade_string": "Not Graded",
        "review_level": "unknown",
        "report": {
            "evaluation": "not evaluated",
            "warnings": [],
            # report summary and table omitted
        },
        "is_default": True
    }


def get_feedback_summary(
    course,
    semester,
    task_info,
    username,
    phase,
    psid,
    taskid
):
    """
    This retrieves just the feedback summary information that appears on
    the dashboard for a given user/phase/pset/task. That much info is
    light enough to cache, so we do cache it to prevent hitting the disk
    a lot for each dashboard view.
    """
    ps = get_ps_obj(task_info, psid)
    filename = get_feedback_filename(
        course,
        semester,
        task_info,
        username,
        phase,
        psid,
        taskid
    )
    fallback = default_feedback_summary(ps, taskid)
    try:
        return sync.read_file(
            filename,
            view=feedback_summary_view(taskid),
            missing=fallback,
            cache=True # explicit default
        )
    except Exception:
        flask.flash("Failed to read feedback file for summary.")
        return fallback


def get_feedback(course, semester, task_info, username, phase, psid, taskid):
    """
    Gets feedback for the user's latest pre-deadline submission for the
    given phase/pset/task. Instead of caching these values (which would
    be expensive memory-wise over time) we hit the disk every time.

    Returns the string "missing" if the relevant feedback file does not
    exist, or None if some kind of error occurs trying to access the
    file.
    """
    filename = get_feedback_filename(
        course,
        semester,
        task_info,
        username,
        phase,
        psid,
        taskid
    )
    try:
        result = sync.read_file(
            filename,
            # default view is AsJSON, which we want
            missing="missing", # return a string if there is no such file
            cache=False
            # These include student code, so it would be expensive to
            # cache them.
        )
    except Exception:
        flask.flash("Failed to read feedback file.")
        result = "missing"

    if result != "missing" and "report" in result:
        # Polish up warnings/evaluation a tiny bit
        warnings = result["report"].get("warnings", [])
        evaluation = result["report"].get("evaluation", "not evaluated")
        if evaluation == "incomplete" and len(warnings) == 0:
            warnings.append(
                "Your submission is incomplete"
              + " (it did not satisfy even half of the core goals)."
            )
        result["report"]["evaluation"] = evaluation
        result["report"]["warnings"] = warnings

    return result


# Ensure required folders for the default course/semester
this_course = app.config.get("DEFAULT_COURSE", 'unknown')
this_semester = app.config.get("DEFAULT_SEMESTER", 'unknown')
ensure_directory(evaluation_directory(this_course, this_semester))
ensure_directory(logs_folder(this_course, this_semester))
ensure_directory(submissions_folder(this_course, this_semester))
ensure_directory(reports_folder(this_course, this_semester))
ensure_directory(extensions_folder(this_course, this_semester))


#---------------#
# Jinja support #
#---------------#

_sorted = sorted


@app.template_filter()
def sorted(*args, **kwargs):
    """
    Turn builtin sorted into a template filter...
    """
    return _sorted(*args, **kwargs)


@app.template_filter()
def fuzzy_time(seconds):
    """
    Takes a number of seconds and returns a fuzzy time value that shifts
    units (up to weeks) depending on how many seconds there are. Ignores
    the sign of the value.
    """
    if seconds < 0:
        seconds = -seconds

    weeks = seconds / ONE_WEEK
    seconds %= ONE_WEEK
    days = seconds / ONE_DAY
    seconds %= ONE_DAY
    hours = seconds / ONE_HOUR
    seconds %= ONE_HOUR
    minutes = seconds / ONE_MINUTE
    seconds %= ONE_MINUTE
    if int(weeks) > 1:
        if weeks % 1 > 0.75:
            return "almost {:.0f} weeks".format(weeks + 1)
        else:
            return "{:.0f} weeks".format(weeks)
    elif int(weeks) == 1:
        return "{:.0f} days".format(7 + days)
    elif int(days) > 1:
        if days % 1 > 0.75:
            return "almost {:.0f} days".format(days + 1)
        else:
            return "{:.0f} days".format(days)
    elif int(days) == 1:
        return "{:.0f} hours".format(24 + hours)
    elif hours > 4:
        if hours % 1 > 0.75:
            return "almost {:.0f} hours".format(hours + 1)
        else:
            return "{:.0f} hours".format(hours)
    elif int(hours) > 0:
        return "{:.0f}h {:.0f}m".format(hours, minutes)
    elif minutes > 30:
        return "{:.0f} minutes".format(minutes)
    else:
        return "{:.0f}m {:.0f}s".format(minutes, seconds)


@app.template_filter()
def fmt_datetime(when):
    """
    Formats a datetime using 24-hour notation w/ extra a.m./p.m.
    annotations in the morning for clarity, and a timezone attached.
    """
    # Use a.m. for extra clarity when hour < 12, and p.m. for 12:XX
    am_hint = ''
    if when.hour < 12:
        am_hint = ' a.m.'
    elif when.hour == 12:
        am_hint = ' p.m.'

    tz = when.strftime("%Z")
    if tz == '':
        tz = app.config.get("DEFAULT_TZ", "")
    if tz != '':
        tz = ' ' + tz
    return when.strftime("at %H:%M{}{} on %Y-%m-%d".format(am_hint, tz))


@app.template_filter()
def timestamp(value):
    """
    A filter to display a timestamp.
    """
    dt = time_from_timestamp(value)
    return fmt_datetime(dt)


@app.template_filter()
def seconds(timedelta):
    """
    Converts a timedelta to a floating-point number of seconds.
    """
    return timedelta.total_seconds()


@app.template_filter()
def integer(value):
    """
    A filter to display a number as an integer.
    """
    if isinstance(value, (float, int)):
        return str(round(value))
    else:
        return str(value)


app.add_template_global(min, name='min')
app.add_template_global(max, name='max')
app.add_template_global(round, name='round')
app.add_template_global(sum, name='sum')


@app.template_filter()
def a_an(h):
    """
    Returns the string 'a' or 'an' where the use of 'a/an' depends on the
    first letter of the name of the first digit of the given number, or
    the first letter of the given string.

    Can't handle everything because it doesn't know phonetics (e.g., 'a
    hour' not 'an hour' because 'h' is not a vowel).
    """
    digits = str(h)
    fd = digits[0]
    if fd in "18aeiou":
        return 'an'
    else:
        return 'a'


@app.template_filter()
def pset_combined_grade(pset):
    """
    Extracts a full combined grade value (0-100) from a pset object.
    Fills in zeroes for any missing grades, and grabs the highest score
    from each task pool.
    """
    total_score = 0
    total_weight = 0
    pool_scores = {}
    for task in pset["tasks"]:
        # Get a grade & weight
        cg = task_combined_grade(task)
        tw = task["feedback_summary"]["weight"]
        if cg is None:
            cg = 0

        # Figure out this task's pool
        if "pool" in task:
            pool = task["pool"]
        else:
            pool = task["id"]

        if pool in pool_scores:
            old_score, old_weight = pool_scores[pool]
            if old_weight != tw:
                raise ValueError("Inconsistent weights for pooled tasks!")
            if old_score < cg:
                pool_scores[pool] = [cg, tw]
        else:
            pool_scores[pool] = [cg, tw]

    total_score = sum(pool[0] for pool in pool_scores.values())
    total_weight = sum(pool[1] for pool in pool_scores.values())

    return total_score / float(total_weight)


@app.template_filter()
def uses_pools(pset):
    """
    Returns True if the pset has at least two tasks that are in the same
    pool, and False otherwise.
    """
    pools = set(task_pool(task) for task in pset["tasks"])
    return len(pools) < len(pset["tasks"])


@app.template_filter()
def task_pool(task):
    """
    Grabs the pool for a task, which defaults to the task ID.
    """
    return task.get("pool", task["id"])


@app.template_filter()
def pset_pools(pset):
    """
    Returns a list of pairs, each containing a pool ID and a colspan
    integer for that pool.
    """
    seen = set()
    result = []
    for task in pset["tasks"]:
        pool = task_pool(task)
        if pool in seen:
            continue
        else:
            seen.add(pool)
            result.append((pool, pool_colspan(pset, task["id"])))
    return result


@app.template_filter()
def pool_colspan(pset, taskid):
    """
    Returns the column span for the pool of the given task in the given
    pset, assuming that the tasks of the pset are displayed in order.
    """
    start_at = None
    this_task = None
    for i in range(len(pset["tasks"])):
        if pset["tasks"][i]["id"] == taskid:
            start_at = i
            this_task = pset["tasks"][i]
            break

    if start_at is None:
        raise ValueError(
            "Pset '{}' does not contain a task '{}'.".format(
                pset["id"],
                taskid
            )
        )

    this_pool = task_pool(this_task)
    span = 1
    for task in pset["tasks"][i + 1:]:
        if task_pool(task) == this_pool:
            span += 1
        else:
            break # span is over

    return span


@app.template_filter()
def task_combined_grade(task):
    """
    Extracts the combined grade value between initial and revised
    submissions for the given task. Returns a floating point number
    between 0 and 100, or None if there is not enough information to
    establish a grade.
    """
    base_grade = task["feedback_summary"].get("grade", -111)
    if base_grade is None:
        base_grade = -111

    rev_task = task.get("revision")
    if (
        rev_task
    and "grade" in rev_task["feedback_summary"]
    and rev_task["feedback_summary"]["grade"]
    ):
        rev_grade = min(95, rev_task["feedback_summary"]["grade"])
        full_grade = max(base_grade, rev_grade)
    else:
        rev_grade = None
        full_grade = base_grade

    if full_grade == -111:
        return None
    else:
        return full_grade


@app.template_filter()
def grade_string(grade_value):
    """
    Turns a grade value (None, or a number between 0 and 100) into a
    grade string (an HTML string w/ a denominator, or 'unknown').
    """
    if grade_value is None:
        return "unknown"
    else:
        rounded = round(grade_value, 2)
        if int(rounded) == rounded:
            rounded = int(rounded)
        return "{}&nbsp;/&nbsp;100".format(rounded)


@app.template_filter()
def shorter_grade(grade_string):
    """
    Shortens a grade string.
    """
    denom = "&nbsp;/&nbsp;100"
    if denom in grade_string:
        return grade_string[:-len(denom)]
    elif grade_string == "unknown":
        return "?"
    else:
        return "!"


@app.template_filter()
def grade_category(grade_value):
    """
    Categorizes a grade value (0-100 or None).
    """
    if grade_value is None:
        return "missing"
    elif grade_value < 75:
        return "low"
    elif grade_value < 90:
        return "mid"
    else:
        return "high"


@app.template_filter()
def timespent(time_spent):
    """
    Handles numerical-or-string-or-None time spent values.
    """
    if isinstance(time_spent, (int, float)):
        if time_spent == 0:
            return '-'
        elif int(time_spent) == time_spent:
            return "{}h".format(int(time_spent))
        else:
            return "{}h".format(round(time_spent, 2))
    elif isinstance(time_spent, str):
        return time_spent
    else:
        return "?"


@app.template_filter()
def initials(full_section_title):
    """
    Reduces a full section title potentially including time information
    to just first initials.
    """
    words = full_section_title.split()
    if len(words) > 1:
        return words[0][0] + words[1][0]
    else:
        return full_section_title


@app.template_filter()
def pronoun(pronouns):
    """
    Reduces pronoun info to a single pronoun.
    """
    test = '/'.join(re.split(r"[^A-Za-z]+", pronouns.lower()))
    if test in (
        "she",
        "she/her",
        "she/hers",
        "she/her/hers"
    ):
        return "she"
    elif test in (
        "he",
        "he/him",
        "he/his",
        "he/him/his"
    ):
        return "he"
    elif test in (
        "they",
        "they/them",
        "them/them/their"
    ):
        return "they"
    else:
        return pronouns


# Characters that need replacing to avoid breaking strings in JS script
# tags
_JS_ESCAPES = [ # all characters with ord() < 32
    chr(z) for z in range(32)
] + [
    '\\',
    "'",
    '"',
    '>',
    '<',
    '&',
    '=',
    '-',
    ';',
    u'\u2028', # LINE_SEPARATOR
    u'\u2029', # PARAGRAPH_SEPARATOR
]


@app.template_filter()
def escapejs(value):
    """
    Modified from:

    https://stackoverflow.com/questions/12339806/escape-strings-for-javascript-using-jinja2

    Escapes string values so that they can appear inside of quotes in a
    <script> tag and they won't end the quotes or cause any other
    trouble.
    """
    retval = []
    for char in value:
        if char in _JS_ESCAPES:
            retval.append(r'\u{:04X}'.format(ord(char)))
        else:
            retval.append(char)

    return jinja2.Markup(u"".join(retval))


#----------------#
# Roster loading #
#----------------#

def load_roster_from_stream(iterable_of_strings):
    """
    Implements the roster-loading logic given an iterable of strings,
    like an open file or a list of strings. See `load_roster`.
    """
    reader = csv.reader(iterable_of_strings)

    students = {}
    # [2018/09/16, lyn] Change to handle roster with titles
    # [2019/09/13, peter] Change to use standard Registrar roster columns
    # by default
    titles = next(reader) # Read first title line of roster
    titles = [x.lower() for x in titles] # convert columns to lower-case
    emailIndex = titles.index('email')

    if 'student name' in titles:
        nameIndex = titles.index('student name')

        def get_name(row):
            return row[nameIndex]

    else:
        firstIndex = titles.index('first')
        lastIndex = titles.index('last')

        def get_name(row):
            return "{} {}".format(row[firstIndex], row[lastIndex])

    if 'section' in titles:
        lecIndex = titles.index('section')
    elif 'lec' in titles:
        lecIndex = titles.index('lec')
    else:
        lecIndex = titles.index('course title')

    if "sort name" in titles:
        sortnameIndex = titles.index('sort name')
    elif "sortname" in titles:
        sortnameIndex = titles.index('sortname')
    else:
        sortnameIndex = None

    for row in reader:
        username = row[emailIndex].split('@')[0]
        if 0 < len(username):
            name = get_name(row)
            namebits = name.split()
            if sortnameIndex is not None:
                sort_by = row[sortnameIndex]
            else:
                sort_by = ' '.join(
                    [row[lecIndex], namebits[-1]]
                    + namebits[:-1]
                )
            students[username] = {
                'username': username,
                'fullname': get_name(row),
                'sortname': sort_by,
                'course_section': row[lecIndex]
            }
        pass
    pass
    return students


#-----------#
# Main code #
#-----------#

if __name__ == "__main__":
    app.run('localhost', 8787)
