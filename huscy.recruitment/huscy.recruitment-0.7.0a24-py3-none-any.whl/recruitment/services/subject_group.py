from django.db.models import F

from huscy.recruitment.models import SubjectGroup
from huscy.recruitment.services.attribute_filtersets import create_attribute_filterset


def create_subject_group(experiment, name, description):
    subject_group = SubjectGroup.objects.create(
        experiment=experiment,
        name=name,
        description=description,
        order=SubjectGroup.objects.filter(experiment=experiment).count(),
    )
    create_attribute_filterset(subject_group)
    return subject_group


def delete_subject_group(subject_group):
    subject_groups_qs = SubjectGroup.objects.filter(experiment=subject_group.experiment)

    if subject_groups_qs.count() == 1:
        raise ValueError('Cannot delete subject group. At least one subject group must remain for '
                         'the experiment.')

    subject_groups_qs.filter(order__gt=subject_group.order).update(order=F('order') - 1)

    subject_group.delete()


def get_or_create_subject_groups(experiment):
    subject_groups_qs = experiment.subject_groups.all()

    if subject_groups_qs.exists():
        return subject_groups_qs

    create_subject_group(experiment, name='SubjectGroup1', description='')

    return subject_groups_qs


def update_subject_group(subject_group, name='', description=''):
    subject_group.name = name or subject_group.name
    subject_group.description = description or subject_group.description
    subject_group.save()
    return subject_group
