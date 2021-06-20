import datetime
import string
import random
import json
import xlsxwriter
import glob
import csv
import io
import tempfile
import fileinput
import os

from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.views.generic import View, TemplateView
from django.shortcuts import redirect
from django.contrib import messages
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.gis.geos import GEOSGeometry
from django.core import serializers
from django.http import FileResponse
from django.db.models import F


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from braces.views import LoginRequiredMixin

from geokey import version
from geokey.core.decorators import handle_exceptions_for_ajax
from geokey.projects.models import Project, Admins
from geokey.categories.models import Category, Field
from geokey.users.models import User
from geokey.contributions.models import MediaFile, Comment
from geokey.contributions.serializers import (
    ContributionSerializer,
    FileSerializer,
    CommentSerializer
)
from geokey.categories.models import (
    Category, Field, TextField, NumericField, LookupField, LookupValue,
    MultipleLookupField, MultipleLookupValue
)
from geokey.contributions.views.observations import GZipView, GeoJsonView
from geokey.contributions.renderers.geojson import GeoJsonRenderer
from geokey.contributions.renderers.kml import KmlRenderer

from .models import ProjectDuplication, CategoryDuplication
from renderers import CSVRenderer


class IndexPage(LoginRequiredMixin, TemplateView):
    template_name = 'duplicate_index.html'

    def get_context_data(self, *args, **kwargs):
        projects = Project.objects.all()

        return super(IndexPage, self).get_context_data(
            projects=projects,
            *args,
            **kwargs
        )


class DuplicateProject(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def post(self, request):

        if Project.objects.filter(name=self.request.POST.get('pproject_destination_name')).exists():
            return JsonResponse(
                {"error": "project destination name already exists"},
                status=status.HTTP_403_FORBIDDEN)
        # We get project_id
        project_id = self.request.POST.get('pproject_origin')

        # Now we get all categories that belongs to this project
        duplicated_categories = Category.objects.filter(project__id=project_id)

        # Here we are duplicating the project
        dup_project = Project.objects.get(pk=project_id)
        dup_project.pk = None
        dup_project.name = self.request.POST.get('pproject_destination_name')
        dup_project.save()
        user = User.objects.get(pk=self.request.user.id)
        Admins.objects.create(project=dup_project, user=user)

        # Here we are duplication the categories
        for duplicated_category in duplicated_categories:
            duplicated_fields = Field.objects.filter(category__id=duplicated_category.id)
            duplicated_category.pk = None
            duplicated_category.project_id = dup_project.id
            duplicated_category.save()
            # And for each category, we need to duplicate fields
            for duplicated_field in duplicated_fields:
                old_field_id = duplicated_field.pk
                duplicated_field.pk = None
                duplicated_field.category = duplicated_category
                field = Field.create(
                    duplicated_field.name,
                    duplicated_field.key,
                    duplicated_field.description,
                    duplicated_field.required,
                    duplicated_field.category,
                    duplicated_field._meta.model.__name__)

                if isinstance(field, TextField):
                    field.textarea = duplicated_field.textarea
                    field.maxlength = duplicated_field.maxlength
                if isinstance(field, NumericField):
                    field.minval = duplicated_field.minval
                    field.maxval = duplicated_field.maxval
                field.save()
                # If the field es LookupField o MultipleLookupField, we need to duplicate options
                if isinstance(field, LookupField):
                    lookupvalues_to_duplicate = LookupValue.objects.filter(field__id=old_field_id)
                    for lookupvalue_to_duplicate in lookupvalues_to_duplicate:
                        lookupvalue_to_duplicate.pk = None
                        lookupvalue_to_duplicate.field_id = field.pk
                        lookupvalue_to_duplicate.save()
                if isinstance(field, MultipleLookupField):
                    multiple_lookupvalues_to_duplicate = MultipleLookupValue.objects.filter(field__id=old_field_id)
                    for multiple_lookupvalue_to_duplicate in multiple_lookupvalues_to_duplicate:
                        multiple_lookupvalue_to_duplicate.pk = None
                        multiple_lookupvalue_to_duplicate.field_id = field.pk
                        multiple_lookupvalue_to_duplicate.save()

        # Insert duplication
        duplication = ProjectDuplication.objects.create(
                project_source=Project.objects.get(pk=project_id),
                project_destination=dup_project,
                creator=self.request.user)

        serialized_project = serializers.serialize('json', [dup_project])
        return JsonResponse({"project": serialized_project}, status=status.HTTP_200_OK)


class DuplicateCategory(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def post(self, request):

        if Category.objects.filter(
                name=self.request.POST.get('destcategoryname'),
                project_id=self.request.POST.get('project_destination')
                ).exists():
            return JsonResponse(
                    {"error": "Category destination name inside project destination already exists"},
                    status=status.HTTP_403_FORBIDDEN)

        # We get category_origin_id
        category_id = self.request.POST.get('category_origin')
        category_to_duplicate = Category.objects.get(pk=category_id)

        # Here we are duplication the categories
        fields_to_duplicate = Field.objects.filter(category__id=category_id)
        category_to_duplicate.pk = None
        category_to_duplicate.name = self.request.POST.get('destcategoryname')
        category_to_duplicate.project_id = self.request.POST.get('project_destination')
        category_to_duplicate.save()
        # And for each category, we need to duplicate fields
        for duplicated_field in fields_to_duplicate:
            old_field_id = duplicated_field.pk
            duplicated_field.pk = None
            duplicated_field.category = category_to_duplicate
            field = Field.create(
                duplicated_field.name,
                duplicated_field.key,
                duplicated_field.description,
                duplicated_field.required,
                duplicated_field.category,
                duplicated_field._meta.model.__name__)

            if isinstance(field, TextField):
                field.textarea = duplicated_field.textarea
                field.maxlength = duplicated_field.maxlength
            if isinstance(field, NumericField):
                field.minval = duplicated_field.minval
                field.maxval = duplicated_field.maxval
            field.save()
            # If the field es LookupField o MultipleLookupField, we need to duplicate options
            if isinstance(field, LookupField):
                lookupvalues_to_duplicate = LookupValue.objects.filter(field__id=old_field_id)
                for lookupvalue_to_duplicate in lookupvalues_to_duplicate:
                    lookupvalue_to_duplicate.pk = None
                    lookupvalue_to_duplicate.field_id = field.pk
                    lookupvalue_to_duplicate.save()
            if isinstance(field, MultipleLookupField):
                multiple_lookupvalues_to_duplicate = MultipleLookupValue.objects.filter(field__id=old_field_id)
                for multiple_lookupvalue_to_duplicate in multiple_lookupvalues_to_duplicate:
                    multiple_lookupvalue_to_duplicate.pk = None
                    multiple_lookupvalue_to_duplicate.field_id = field.pk
                    multiple_lookupvalue_to_duplicate.save()

                # Insert duplication
        duplication = CategoryDuplication.objects.create(
            category_source=Category.objects.get(pk=category_id),
            category_destination=category_to_duplicate,
            creator=self.request.user)

        serialized_category = serializers.serialize('json', [category_to_duplicate])
        return JsonResponse({"serialized_category": serialized_category}, status=status.HTTP_200_OK)


class DuplicateGetProjectCategories(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def get(self, request, project_id):
        categories = Category.objects.get_list(self.request.user, project_id)
        categories_dict = {}

        for category in categories:
            categories_dict[category.id] = category.name

        return Response(categories_dict, status=status.HTTP_200_OK)


class GetAllProject(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def post(self, request):
        project_id = self.request.POST.get('project_id')
        comments = False
        mediafiles = False
        format = self.request.POST.get('format')
        if format == 'kml':
            renderer = KmlRenderer()
        else:
            renderer = GeoJsonRenderer()
        try:
            project = Project.objects.get_single(self.request.user, project_id)
        except:
            return JsonResponse({"error": "403"}, status=status.HTTP_403_FORBIDDEN)

        contributions = project.get_all_contributions(self.request.user)

        serializer = ContributionSerializer(
            contributions,
            many=True,
            context={'user': self.request.user, 'project': project}
        )
        protocol = 'https' if request.is_secure() else 'http'
        url = '%s://%s' % (protocol, request.get_host())

        for contribution in serializer.data:
            media = FileSerializer(
                MediaFile.objects.filter(
                    contribution__id=contribution['id']
                ),
                many=True,
                context={'user': self.request.user, 'project': project}
            ).data

            for file in media:
                if not file['url'].startswith('http'):
                    file['url'] = url + file['url']
                if not file['thumbnail_url'].startswith('http'):
                    file['thumbnail_url'] = url + file['thumbnail_url']

            contribution['media'] = media

            contribution['comments'] = CommentSerializer(
                Comment.objects.filter(
                    commentto__id=contribution['id'],
                    respondsto=None
                ),
                many=True,
                context={'user': self.request.user, 'project': project}
            ).data

        if comments:
            content = renderer.render_comments(serializer.data)
        elif mediafiles:
            content = renderer.render_mediafiles(serializer.data)
        else:
            content = renderer.render(serializer.data)

        return Response(content, content_type="text/json", status=status.HTTP_200_OK)


class GetAllProjectXLSX(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def post(self, request):
        project_id = self.request.data['project_id']
        renderer = CSVRenderer()
        try:
            project = Project.objects.get_single(self.request.user, project_id)
        except:
            return JsonResponse({"error": "403"}, status=status.HTTP_403_FORBIDDEN)

        categories = Category.objects.get_list(self.request.user, project_id)
        # Check if we need to send mediafiles and or comments
        if self.request.POST.get('media_xlsx') == "true":
            mediafiles = True
        else:
            mediafiles = False
        if self.request.POST.get('comments_xlsx') == "true":
            comments = True
        else:
            comments = False

        try:
            os.makedirs('/tmp/geokey_duplicate_excelfiles/')
        except OSError:
            if not os.path.isdir('/tmp/geokey_duplicate_excelfiles'):
                return JsonResponse({"error": "403"}, status=status.HTTP_403_FORBIDDEN)

        dest_file = '/tmp/geokey_duplicate_excelfiles/%s.xlsx' % project.name
        workbook = xlsxwriter.Workbook(dest_file)
        csv_data = io.BytesIO()
        csv_writer = csv.writer(csv_data)

        for catnumber, category in enumerate(categories):
            contributions = project.get_all_contributions(self.request.user).filter(category=category)

            serializer = ContributionSerializer(
                contributions,
                many=True,
                context={'user': self.request.user, 'project': project}
            )
            protocol = 'https' if request.is_secure() else 'http'
            url = '%s://%s' % (protocol, request.get_host())

            for contribution in serializer.data:
                media = FileSerializer(
                    MediaFile.objects.filter(
                        contribution__id=contribution['id']
                    ),
                    many=True,
                    context={'user': self.request.user, 'project': project}
                ).data

                for file in media:
                    if not file['url'].startswith('http'):
                        file['url'] = url + file['url']
                    if not file['thumbnail_url'].startswith('http'):
                        file['thumbnail_url'] = url + file['thumbnail_url']

                contribution['media'] = media

                contribution['comments'] = CommentSerializer(
                    Comment.objects.filter(
                        commentto__id=contribution['id'],
                        respondsto=None
                    ),
                    many=True,
                    context={'user': self.request.user, 'project': project}
                ).data

            if comments:
                content = renderer.render_comments(serializer.data)
            elif mediafiles:
                content = renderer.render_mediafiles(serializer.data)
            else:
                content = renderer.render(serializer.data)

            content = content.splitlines()
            worksheetname = '%s_%s' % (
                catnumber, category.name[:22].decode('utf-8')+'..' if len(category.name) > 24 else category.name.decode('utf-8'))
            worksheet = workbook.add_worksheet(worksheetname)
            for r, row in enumerate(content):
                lst = row.split(',')
                for c, item in enumerate(lst):
                    worksheet.write(r, c, item.decode('utf-8'))

        workbook.close()
        file = open(dest_file, 'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="filename.xlsx"'

        return response


class GetAllProjectDuplications(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def get(self, request):
        project_duplications = serializers.serialize(
                'json',
                ProjectDuplication.objects.all().order_by('-created_at'),
                use_natural_foreign_keys=True)
        return JsonResponse({"project_duplications": project_duplications})


class GetAllCategoryDuplications(LoginRequiredMixin, APIView):

    @handle_exceptions_for_ajax
    def get(self, request):
        category_duplications = serializers.serialize(
                'json',
                CategoryDuplication.objects.all().order_by('-created_at'),
                use_natural_foreign_keys=True)
        return JsonResponse({"category_duplications": category_duplications})
