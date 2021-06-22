import json
import os
import sqlite3
import urllib

from datasette import hookimpl
from datasette.database import Database
from datasette.utils.asgi import Response, NotFound, Forbidden
import sqlite_utils
import uuid


DB_NAME="surveys"
DEFAULT_DBPATH="."
TABLE_NAME="surveys"


@hookimpl
def menu_links(datasette, actor):
    async def inner():
        # right now if you have surveys-list permission, we'll show you
        # the menu link which also leads to survey creation (a separate
        # permission
        allowed = await datasette.permission_allowed(
            actor, "surveys-list", default=False
        )
        if allowed:
            return [{
                "href": datasette.urls.path("/-/surveys"),
                "label": "Surveys"
            }]
    return inner


@hookimpl
def register_routes():
    return [
        # we could use normal datasette list view, but it doesn't provide
        # editing capabilities so it would be just as much work
        (r"^/-/surveys/?$", surveys_list),
        # link to the specific survey for users to fill (GET & POST)
        (r"^/-/surveys/form/(?P<id>.*)/?$", survey_form),
        (r"^/-/surveys/new/?$", surveys_new),
        # CRUD on surveys
        (r"^/-/surveys/(?P<id>[0-9a-zA-Z\-]+)/?$", surveys_update),
    ]


def perm_check_maker(datasette, request):
    async def inner_perm_check(*args):
        a_id = (request.actor or {}).get("id")
        action = args[0]
        if action.startswith("surveys-") and a_id == "root":
            return True
        if not await datasette.permission_allowed(
            request.actor, *args, default=False
        ):
            raise Forbidden("Permission denied")
    return inner_perm_check


def get_db(datasette=None):
    database_path = os.path.join(DEFAULT_DBPATH, f"{DB_NAME}.db")
    # this will create the DB if not exists
    conn = sqlite3.connect(database_path)
    db = sqlite_utils.Database(conn)
    if datasette and not (DB_NAME in datasette.databases):
        datasette.add_database(
            Database(datasette, path=database_path, is_mutable=True),
            name=DB_NAME,
        )
    return db


def get_surveys():
    db = get_db()
    try:
        for survey in db[TABLE_NAME].rows:
            survey["name"] = urllib.parse.unquote(survey["survey_name"])
            yield survey
    except Exception as e:
        print(f"Exception while reading table {TABLE_NAME}: {e}")


async def surveys_new(scope, receive, datasette, request):
    perm_check = perm_check_maker(datasette, request)
    await perm_check('surveys-create')

    if request.method == "POST":
        formdata = await request.post_vars()
        assert "survey_name" in formdata, "survey name required"
        assert "schema" in formdata, "Invalid POST data"
        assert "options" in formdata, "Invalid POST data"
        schema = formdata["schema"]
        options = formdata["options"]
        survey_name = urllib.parse.quote(formdata["survey_name"])
        # submitted_message = formdata.get("submitted_message")
        survey_id = str(uuid.uuid4())
        db = get_db(datasette=datasette)

        if survey_name in db.table_names():
            raise Exception(f"Survey name '{survey_name}' is already taken!")

        surveys_table = db[TABLE_NAME]
        surveys_table.insert({
            "id": survey_id,
            "survey_name": survey_name,
            # "submitted_message": submitted_message,
            "schema": schema,
            "options": options,
        }, pk="id", replace=True)
        return Response.redirect(
            f"/-/surveys/{survey_id}"
        )

    return Response.html(
        await datasette.render_template(
            "form-builder.html", {
                "id": "new",
            }, request=request
        )
    )


async def surveys_update(scope, receive, datasette, request):
    perm_check = perm_check_maker(datasette, request)
    survey_id = request.url_vars["id"]
    assert survey_id, "Survey ID missing"

    db = get_db(datasette=datasette)
    surveys_table = db[TABLE_NAME]

    if request.method == "DELETE":
        await perm_check('surveys-delete', survey_id)
        surveys_table.delete(survey_id)
        return Response.redirect(
            f"/-/surveys"
        )

    # SECURITY CHECK - everything from here out rides on this perm
    await perm_check('surveys-edit', survey_id)
    survey_data = surveys_table.get(survey_id)

    # update exiting survey
    if request.method == "POST":
        formdata = await request.post_vars()
        assert "schema" in formdata, "Invalid POST data"
        assert "options" in formdata, "Invalid POST data"
        schema = formdata["schema"]
        options = formdata["options"]
        surveys_table.insert({
            "id": survey_id,
            # No updating survey names!
            "survey_name": survey_data["survey_name"],
            "schema": schema,
            "options": options,
        }, pk="id", replace=True)
        # TODO: generate save message?
        # TODO: create empty form responses table
        return Response.redirect(
            f"/-/surveys/{survey_id}"
        )

    # show editor
    assert survey_data, "Survey not found."
    return Response.html(
        await datasette.render_template(
            "form-builder.html", {
                "id": survey_id,
                "survey_name": urllib.parse.unquote(survey_data["survey_name"]),
                "schema": survey_data["schema"],
                "options": survey_data["options"],
            }, request=request
        )
    )


async def surveys_list(scope, receive, datasette, request):
    perm_check = perm_check_maker(datasette, request)
    await perm_check('surveys-list')

    return Response.html(
        await datasette.render_template(
            "surveys-list.html", {
                "surveys": get_surveys()
            }, request=request
        )
    )


async def survey_form(scope, receive, datasette, request):
    survey_id = request.url_vars["id"]

    perm_check = perm_check_maker(datasette, request)
    await perm_check('surveys-view', survey_id)

    db = get_db(datasette=datasette)
    surveys_table = db[TABLE_NAME]
    survey = surveys_table.get(survey_id)
    if not survey:
        raise NotFound(f"Form not found: {survey_id}")

    if request.method == "POST":
        await perm_check('surveys-respond', survey_id)

        formdata = await request.post_vars()
        if "csrftoken" in formdata:
            del formdata["csrftoken"]

        survey_name = survey["survey_name"]
        db[survey_name].insert(formdata, alter=True)
        return Response.html(
            await datasette.render_template(
                "generic-message.html", {
                    "title": urllib.parse.unquote(survey["survey_name"]),
                    "message": survey.get(
                        "submitted_message",
                        "Your response has been collected!"
                    ),
                }, request=request
            )
        )

    assert request.method == "GET", f"Invalid method: {request.method}"
    return Response.html(
        await datasette.render_template(
            "form.html", {
                "survey_name": urllib.parse.unquote(survey["survey_name"]),
                "schema": survey["schema"],
                "options": survey["options"],
                "id": survey_id,
            }, request=request
        )
    )

