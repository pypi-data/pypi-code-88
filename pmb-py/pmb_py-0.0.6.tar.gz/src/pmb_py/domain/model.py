from typing import List, Union
from dataclasses import dataclass
import datetime


@dataclass
class PmbProjectStatus:
    id: int
    name: str
    color: str
    code_name: str
    color_text: str


class Project:

    def __init__(self, id: int = None,
                 name: str = '',
                 type_id: int = None,
                 status_id: int = None,
                 sg_project_id: int = None):
        self.id = id
        self.name = name
        self.type_id = type_id
        self.status_id = status_id
        self.sg_project_id = sg_project_id

    def __eq__(self, obj_b):
        if self.id == obj_b.id:
            return True
        else:
            return False

    def __hash__(self):
        data = 'PmbProject_'+str(self.id)
        return hash(data)

    def __repr__(self):
        class_ = str(type(self)).split("'")[1]
        return f'{class_}({self.id}:{self.name}) at {id(self)}'


@dataclass
class ProjectType:
    id: int
    name: str


@dataclass
class MemberStatus:
    id: int
    name: str
    code_name: str


@dataclass
class Member:
    id: int
    name: str
    e_id: str
    email: str


@dataclass
class Task:
    id: int
    name: str
    gantt_item_id: int


@dataclass
class Block:
    id: int
    date: datetime.date
    duration: int
    task_id: int
    member_id: int
    project_id: int
    type_id: int


@dataclass
class BlockType:
    id: int
    name: str
    color: str
    color_text: str
    text: str


@dataclass
class GanttItem:
    id: int
    name: str
    start_datetime: datetime.datetime
    end_datetime: datetime.datetime
    task_type: int
    parent_id: int
    project_id:int
    sg_task_id: int
    legend: str
    read_only: str
    status: str



@dataclass
class Member:
    id: int
    emp_id: str
    name: str
    email: str

