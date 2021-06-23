from typing import TYPE_CHECKING, Optional

from django.db.models import Count, Q
from django.http import HttpRequest, HttpResponseNotFound
from django.shortcuts import get_object_or_404

from guardian.core import ObjectPermissionChecker

from aleksis.core.models import Group, Person
from aleksis.core.util.predicates import check_global_permission

from ..managers import TimetableType
from ..models import LessonPeriod, LessonSubstitution, Room

if TYPE_CHECKING:
    from django.contrib.auth import get_user_model

    User = get_user_model()  # noqa


def get_el_by_pk(
    request: HttpRequest,
    type_: str,
    pk: int,
    year: Optional[int] = None,
    week: Optional[int] = None,
    regular: Optional[str] = None,
    prefetch: bool = False,
    *args,
    **kwargs,
):
    if type_ == TimetableType.GROUP.value:
        return get_object_or_404(
            Group.objects.prefetch_related("owners", "parent_groups") if prefetch else Group, pk=pk,
        )
    elif type_ == TimetableType.TEACHER.value:
        return get_object_or_404(Person, pk=pk)
    elif type_ == TimetableType.ROOM.value:
        return get_object_or_404(Room, pk=pk)
    else:
        return HttpResponseNotFound()


def get_substitution_by_id(request: HttpRequest, id_: int, week: int):
    lesson_period = get_object_or_404(LessonPeriod, pk=id_)
    wanted_week = lesson_period.lesson.get_calendar_week(week)

    return LessonSubstitution.objects.filter(
        week=wanted_week.week, year=wanted_week.year, lesson_period=lesson_period
    ).first()


def get_teachers(user: "User"):
    """Get the teachers whose timetables are allowed to be seen by current user."""
    checker = ObjectPermissionChecker(user)

    teachers = (
        Person.objects.annotate(lessons_count=Count("lessons_as_teacher"))
        .filter(lessons_count__gt=0)
        .order_by("short_name", "last_name")
    )

    if not check_global_permission(user, "chronos.view_all_person_timetables"):
        checker.prefetch_perms(teachers)

        wanted_teachers = set()

        for teacher in teachers:
            if checker.has_perm("core.view_person_timetable", teacher):
                wanted_teachers.add(teacher.pk)

        teachers = teachers.filter(Q(pk=user.person.pk) | Q(pk__in=wanted_teachers))

    return teachers


def get_classes(user: "User"):
    """Get the classes whose timetables are allowed to be seen by current user."""
    checker = ObjectPermissionChecker(user)

    classes = (
        Group.objects.for_current_school_term_or_all()
        .annotate(
            lessons_count=Count("lessons"), child_lessons_count=Count("child_groups__lessons"),
        )
        .filter(
            Q(lessons_count__gt=0, parent_groups=None)
            | Q(child_lessons_count__gt=0, parent_groups=None)
        )
        .order_by("short_name", "name")
    )

    if not check_global_permission(user, "chronos.view_all_group_timetables"):
        checker.prefetch_perms(classes)

        wanted_classes = set()

        for _class in classes:
            if checker.has_perm("core.view_group_timetable", _class):
                wanted_classes.add(_class.pk)

        classes = classes.filter(
            Q(pk__in=wanted_classes) | Q(members=user.person) | Q(owners=user.person)
        )
        if user.person.primary_group:
            classes = classes.filter(Q(pk=user.person.primary_group.pk))

    return classes


def get_rooms(user: "User"):
    """Get the rooms whose timetables are allowed to be seen by current user."""
    checker = ObjectPermissionChecker(user)

    rooms = (
        Room.objects.annotate(lessons_count=Count("lesson_periods"))
        .filter(lessons_count__gt=0)
        .order_by("short_name", "name")
    )

    if not check_global_permission(user, "chronos.view_all_room_timetables"):
        checker.prefetch_perms(rooms)

        wanted_rooms = set()

        for room in rooms:
            if checker.has_perm("chronos.view_room_timetable", room):
                wanted_rooms.add(room.pk)

        rooms = rooms.filter(Q(pk__in=wanted_rooms))

    return rooms
