from .views import *
from django.urls import path, re_path
from .validator import BasicValidator


def add_pattern(model, form, form_update=False, validator=False):
    meta = model._meta
    app_label = meta.app_label
    model_name = meta.model_name

    gv.model_map[model_name] = model
    gv.validator_map[model_name] = validator or BasicValidator

    gv.ajax_form_map[app_label + '-' + 'add' + '-' + model_name] = form
    gv.ajax_form_map[app_label + '-' + 'change' + '-' + model_name] = form_update if form_update else form

    gv.data_map_for_list_view[app_label + '-' + 'view' + '-' + model_name] = {
        'r_kwargs': '',
        'data-keys': ",".join(f.name for f in model._meta.get_fields()),
        'data-post-url': '/ajax/two-act-handler/'
    }


patterns = [
    path('ajax/four-act-handler/', ajax_four_act_handler, name='ajax-four-act-handler'),
    path('ajax/two-act-handler/', ajax_two_act_handler, name='ajax-two-act-handler'),
    re_path(r'^(?P<props>[\w-]+)/', ajax_four_act_handler, name="ajax-one-page-view")
]
