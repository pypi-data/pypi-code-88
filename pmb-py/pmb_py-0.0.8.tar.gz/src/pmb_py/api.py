import pmb_py.core as core
from pmb_py import PMB_MEMBER_STATUS, PmbError
from pmb_py.adapter import pmb_convert


class pmb_mixin:
    creator = None

    @classmethod
    def list(cls, *args, **kwargs) -> list:
        items = cls.get_query(*args, **kwargs)
        if not items:
            return list()
        if cls.creator:
            objects = [cls.creator(item) for item in items]
            return {object.id: object for object in objects}.values()
        else:
            return items

    @classmethod
    def get_query(cls, *args, **kwargs):
        pass

    @classmethod
    def get(cls, **kwargs):
        pass
        # raise PmbError("no support for these keyword")

    @classmethod
    def create_one(cls, *args, **kwargs):
        return dict()

    @classmethod
    def create(cls, *args, **kwargs):
        item = cls.create_one(*args, **kwargs)
        if cls.creator:
            obj = cls.creator(item)
            return obj
        else:
            return item

    @classmethod
    def update_one(cls, obj_id, **kwargs):
        return dict()

    @classmethod
    def update(cls, obj_id, **kwargs):
        try:
            item = cls.update_one(obj_id, **kwargs)
        except Exception as e:
            print(str(e))
            return False
        if cls.creator:
            obj = cls.creator(item)
            return obj
        else:
            return item


class ProjectStatus(pmb_mixin):
    creator = pmb_convert.to_project_status

    @classmethod
    def get_query(cls):
        api = "web_project_status_and_types"
        re = core._session.post(api)
        return re["data"]["projectStatus"]


class ProjectType(pmb_mixin):
    creator = pmb_convert.to_project_type

    @classmethod
    def get_query(cls):
        api = "web_project_status_and_types"
        re = core._session.post(api)
        return re["data"]["projectTypes"]


class MemberStatus(pmb_mixin):
    creator = pmb_convert.to_member_status

    @classmethod
    def get_query(cls):
        status_list = list()
        for k, v in PMB_MEMBER_STATUS.items():
            status_list.append({"id": v[0], "name": v[1], "codeName": k})
        return status_list


class Projects(pmb_mixin):
    creator = pmb_convert.to_project

    @classmethod
    def get_query(cls, *args, **kwargs):
        api = 'projects'
        re = core._session.get(api, params=kwargs)
        return re


class Tasks(pmb_mixin):
    creator = pmb_convert.to_pmb_task

    @classmethod
    def get_query(cls, *args, **kwargs):
        api = "tasks"
        re = core._session.get(api, params=kwargs)
        return re


class Blocks(pmb_mixin):
    creator = pmb_convert.to_pmb_block

    @classmethod
    def list(cls, **kwargs):
        raise PmbError(
            "PmbBlocks is not support list method, instead, use get(id=) or get (task_id=)"
        )

    @classmethod
    def get_query(cls, *args, **kwargs):
        api = "web_tasks_logs_a_day"

    @classmethod
    def get(cls, **kwargs):
        blocks = list()
        task_id = kwargs.get("task_id")
        if not task_id:
            raise PmbError("task_id is require")
        date_ = kwargs.get("task_id")
        if not date_:
            raise PmbError('date is require')
        data = {

        }


class GanttItems(pmb_mixin):
    creator = pmb_convert.to_pmb_gantt_item

    @classmethod
    def get_query(cls, *args, **kwargs):
        api = 'gantt_items'
        re = core._session.get(api, params=kwargs)
        return re

    @classmethod
    def create_one(cls, *args, **kwargs):
        api = 'gantt_items'
        re = core._session.post(api, data=kwargs)
        return re
