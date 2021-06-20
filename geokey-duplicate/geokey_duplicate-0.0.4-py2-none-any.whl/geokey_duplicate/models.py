from django.dispatch import receiver
from django.utils import timezone
from django.db import models
from django.conf import settings
from django.contrib.gis.db import models as gis
from model_utils import Choices


from geokey.projects.models import Project


class ProjectDuplication(models.Model):
    """
    Project duplication log
    """

    project_source = models.ForeignKey(
            'projects.Project',
            on_delete=models.DO_NOTHING,
            related_name='%(class)s_project_source')
    project_destination = models.ForeignKey(
            'projects.Project',
            on_delete=models.DO_NOTHING,
            related_name='%(class)s_project_destination')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    def create(cls, id_source, id_destination, creator):
        """
        Creates a project duplication logentry in the database.

        project_source : project
            project source
        project_destination : project
            project destination

        Return
        ------
        the model
        """

        duplication = cls(
            project_source=project_source,
            project_destination=project_destination,
            creator=creator
        )

        duplication.save()
        return duplication

    def save(self, *args, **kwargs):
        super(ProjectDuplication, self).save(*args, **kwargs)


class CategoryDuplication(models.Model):
    """
    Category duplication log
    """

    category_source = models.ForeignKey(
            'categories.Category',
            on_delete=models.DO_NOTHING,
            related_name='%(class)s_category_source')
    category_destination = models.ForeignKey(
            'categories.Category',
            on_delete=models.DO_NOTHING,
            related_name='%(class)s_category_destination')
    creator = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    def create(cls, id_source, id_destination, creator):
        """
        Creates a category duplication logentry in the database.

        category_source : integer
            category source
        category_destination : integer
            category destination
        Return
        ------
        the model
        """

        duplication = cls(
            category_source=category_source,
            category_destination=category_destination,
            creator=creator
        )

        duplication.save()
        return duplication

    def save(self, *args, **kwargs):
        super(CategoryDuplication, self).save(*args, **kwargs)
