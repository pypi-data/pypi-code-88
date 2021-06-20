from django.conf.urls import include, url

from rest_framework.urlpatterns import format_suffix_patterns

from views import (
    IndexPage,
    DuplicateProject,
    DuplicateCategory,
    DuplicateGetProjectCategories,
    GetAllProject,
    GetAllProjectXLSX,
    GetAllProjectDuplications,
    GetAllCategoryDuplications
)

urlpatterns = [
    url(
        r'^admin/duplicate/$',
        IndexPage.as_view(),
        name='index'),
    url(
        r'^admin/duplicate_project/$',
        DuplicateProject.as_view(),
        name='duplicate_project'),
    url(
        r'^admin/duplicate_category/$',
        DuplicateCategory.as_view(),
        name='duplicate_category'),

    url(
        r'^admin/duplicate_categories/projects/(?P<project_id>[0-9]+)/categories/$',
        DuplicateGetProjectCategories.as_view(),
        name='duplicate_get_project_categories'),

    url(
        r'^admin/duplicate/getallproject/$',
        GetAllProject.as_view(),
        name='get_all_project'),
    url(
        r'^admin/duplicate/getallprojectxlsx/$',
        GetAllProjectXLSX.as_view(),
        name='get_all_project_xlsx'),
    url(
        r'^admin/duplicate/getallprojectduplications/$',
        GetAllProjectDuplications.as_view(),
        name='get_all_project_duplications'),
    url(
        r'^admin/duplicate/getallcategoryduplications/$',
        GetAllCategoryDuplications.as_view(),
        name='get_all_category_duplications'),
]
