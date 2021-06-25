r"""
Copyright &copy; 2021 NetApp Inc.
All rights reserved.

## Overview
You can use this API to add or delete UNIX users to a UNIX group of an SVM.
## Adding users to a UNIX group
The UNIX group users POST endpoint adds UNIX users to the specified UNIX group and the SVM.
Multiple users can be added in a single call using the "records" parameter.
## Examples
### Adding a single user to the group 'group1'
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import UnixGroupUsers

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = UnixGroupUsers("group1")
    resource.name = "user4"
    resource.post(hydrate=True)
    print(resource)

```

### Adding multiple users to the group 'group1' in a single REST call
```python
from netapp_ontap import HostConnection
from netapp_ontap.resources import UnixGroupUsers

with HostConnection("<mgmt-ip>", username="admin", password="password", verify=False):
    resource = UnixGroupUsers("group1")
    resource.records = [{"name": "user1"}, {"name": "user2"}, {"name": "user3"}]
    resource.post(hydrate=True)
    print(resource)

```

## Deleting a user from a group of a specific SVM
## Example
### Delete the user 'user1' from group 'group1' in SVM 'vs1'
```
# The API:
/api/name-services/unix-groups/{svm.uuid}/{unix_group.name}/users/{name}
# The call:
"""

import asyncio
from datetime import datetime
import inspect
from typing import Callable, Iterable, List, Optional, Union

try:
    CLICHE_INSTALLED = False
    import cliche
    from cliche.arg_types.choices import Choices
    from cliche.commands import ClicheCommandError
    from netapp_ontap.resource_table import ResourceTable
    CLICHE_INSTALLED = True
except ImportError:
    pass

from marshmallow import fields, EXCLUDE  # type: ignore

import netapp_ontap
from netapp_ontap.resource import Resource, ResourceSchema, ImpreciseDateTime, Size
from netapp_ontap import NetAppResponse, HostConnection
from netapp_ontap.validations import enum_validation, len_validation, integer_validation
from netapp_ontap.error import NetAppRestError


__all__ = ["UnixGroupUsers", "UnixGroupUsersSchema"]
__pdoc__ = {
    "UnixGroupUsersSchema.resource": False,
    "UnixGroupUsers.unix_group_users_show": False,
    "UnixGroupUsers.unix_group_users_create": False,
    "UnixGroupUsers.unix_group_users_modify": False,
    "UnixGroupUsers.unix_group_users_delete": False,
}


class UnixGroupUsersSchema(ResourceSchema):
    """The fields of the UnixGroupUsers object"""

    links = fields.Nested("netapp_ontap.models.self_link.SelfLinkSchema", data_key="_links", unknown=EXCLUDE)
    r""" The links field of the unix_group_users. """

    name = fields.Str(
        data_key="name",
    )
    r""" UNIX user who belongs to the specified UNIX group and the SVM. """

    records = fields.List(fields.Nested("netapp_ontap.models.unix_group_users_no_records.UnixGroupUsersNoRecordsSchema", unknown=EXCLUDE), data_key="records")
    r""" An array of UNIX users specified to add multiple users to a UNIX group in a single API call.
Not allowed when the `name` property is used. """

    skip_name_validation = fields.Boolean(
        data_key="skip_name_validation",
    )
    r""" Indicates whether or not the validation for the specified UNIX user names is disabled. """

    @property
    def resource(self):
        return UnixGroupUsers

    gettable_fields = [
        "links",
        "name",
    ]
    """links,name,"""

    patchable_fields = [
        "records",
    ]
    """records,"""

    postable_fields = [
        "name",
        "records",
        "skip_name_validation",
    ]
    """name,records,skip_name_validation,"""

def _get_field_list(field: str) -> Callable[[], List]:
    def getter():
        return [getattr(r, field) for r in UnixGroupUsers.get_collection(fields=field)]
    return getter

async def _wait_for_job(response: NetAppResponse) -> None:
    """Examine the given response. If it is a job, asynchronously wait for it to
    complete. While polling, prints the current status message of the job.
    """

    if not response.is_job:
        return
    from netapp_ontap.resources import Job
    job = Job(**response.http_response.json()["job"])
    while True:
        job.get(fields="state,message")
        if hasattr(job, "message"):
            print("[%s]: %s" % (job.state, job.message))
        if job.state == "failure":
            raise NetAppRestError("UnixGroupUsers modify job failed")
        if job.state == "success":
            break
        await asyncio.sleep(1)

class UnixGroupUsers(Resource):
    """Allows interaction with UnixGroupUsers objects on the host"""

    _schema = UnixGroupUsersSchema
    _path = "/api/name-services/unix-groups/{svm[uuid]}/{unix_group[name]}/users"
    _keys = ["svm.uuid", "unix_group.name", "name"]




    @classmethod
    def delete_collection(
        cls,
        *args,
        body: Union[Resource, dict] = None,
        connection: HostConnection = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a user from the specified UNIX group.
### Related ONTAP commands
* `vserver services name-service unix-group deluser`

### Learn more
* [`DOC /name-services/unix-groups/{svm.uuid}/{unix_group.name}/users`](#docs-name-services-name-services_unix-groups_{svm.uuid}_{unix_group.name}_users)"""
        return super()._delete_collection(*args, body=body, connection=connection, **kwargs)

    delete_collection.__func__.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete_collection.__doc__)



    def post(
        self,
        hydrate: bool = False,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Adds users to the specified UNIX group and SVM.
### Important notes
- Multiple users can be added in a single call using the "records" parameter.
- "records" parameter must not be specified when "name" parameter is specified.
- Specified users are appended to the existing list of users.
- Duplicate users are ignored.
### Related ONTAP commands
* `vserver services name-service unix-group adduser`
* `vserver services name-service unix-group addusers`

### Learn more
* [`DOC /name-services/unix-groups/{svm.uuid}/{unix_group.name}/users`](#docs-name-services-name-services_unix-groups_{svm.uuid}_{unix_group.name}_users)"""
        return super()._post(
            hydrate=hydrate, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    post.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._post.__doc__)

    if CLICHE_INSTALLED:
        @cliche.command(name="unix group users create")
        async def unix_group_users_create(
            unix_group_name,
            svm_uuid,
            links: dict = None,
            name: str = None,
            records: dict = None,
            skip_name_validation: bool = None,
        ) -> ResourceTable:
            """Create an instance of a UnixGroupUsers resource

            Args:
                links: 
                name: UNIX user who belongs to the specified UNIX group and the SVM. 
                records: An array of UNIX users specified to add multiple users to a UNIX group in a single API call. Not allowed when the `name` property is used. 
                skip_name_validation: Indicates whether or not the validation for the specified UNIX user names is disabled.
            """

            kwargs = {}
            if links is not None:
                kwargs["links"] = links
            if name is not None:
                kwargs["name"] = name
            if records is not None:
                kwargs["records"] = records
            if skip_name_validation is not None:
                kwargs["skip_name_validation"] = skip_name_validation

            resource = UnixGroupUsers(
                unix_group_name,
                svm_uuid,
                **kwargs
            )
            try:
                response = resource.post(hydrate=True, poll=False)
                await _wait_for_job(response)
                resource.get()
            except NetAppRestError as err:
                raise ClicheCommandError("Unable to create UnixGroupUsers: %s" % err)
            return [resource]


    def delete(
        self,
        body: Union[Resource, dict] = None,
        poll: bool = True,
        poll_interval: Optional[int] = None,
        poll_timeout: Optional[int] = None,
        **kwargs
    ) -> NetAppResponse:
        r"""Deletes a user from the specified UNIX group.
### Related ONTAP commands
* `vserver services name-service unix-group deluser`

### Learn more
* [`DOC /name-services/unix-groups/{svm.uuid}/{unix_group.name}/users`](#docs-name-services-name-services_unix-groups_{svm.uuid}_{unix_group.name}_users)"""
        return super()._delete(
            body=body, poll=poll, poll_interval=poll_interval,
            poll_timeout=poll_timeout, **kwargs
        )

    delete.__doc__ += "\n\n---\n" + inspect.cleandoc(Resource._delete.__doc__)

    if CLICHE_INSTALLED:
        @cliche.command(name="unix group users delete")
        async def unix_group_users_delete(
            unix_group_name,
            svm_uuid,
            name: str = None,
            skip_name_validation: bool = None,
        ) -> None:
            """Delete an instance of a UnixGroupUsers resource

            Args:
                name: UNIX user who belongs to the specified UNIX group and the SVM. 
                skip_name_validation: Indicates whether or not the validation for the specified UNIX user names is disabled.
            """

            kwargs = {}
            if name is not None:
                kwargs["name"] = name
            if skip_name_validation is not None:
                kwargs["skip_name_validation"] = skip_name_validation

            if hasattr(UnixGroupUsers, "find"):
                resource = UnixGroupUsers.find(
                    unix_group_name,
                    svm_uuid,
                    **kwargs
                )
            else:
                resource = UnixGroupUsers(unix_group_name,svm_uuid,)
            try:
                response = resource.delete(poll=False)
                await _wait_for_job(response)
            except NetAppRestError as err:
                raise ClicheCommandError("Unable to delete UnixGroupUsers: %s" % err)


