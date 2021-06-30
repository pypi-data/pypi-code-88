from . import gv
from django.http import JsonResponse


def set_gv():
    gv.model_map = {}
    gv.validator_map = {}
    gv.ajax_form_map = {}
    gv.data_map_for_list_view = {}


def get_kwargs_for_ajax_request(data):
    required_kw = data.pop('r_kwargs', 'id')

    kw_d = {}
    for kw in required_kw.split(';'):
        field_value = kw.split('=')

        if len(field_value) > 1:
            kw_d[field_value[0]] = field_value[1]

    return kw_d


def get_verbose_name(model_name):
    return gv.model_map[model_name]._meta.verbose_name.capitalize()


def get_verbose_name_for_fields(model_name, keys=['id']):
    meta = gv.model_map[model_name]._meta

    return [
        meta.get_field(key).verbose_name.capitalize() for key in keys
    ]


def get_instance_by_kwargs(data, model=None, model_name=None, kwargs=None):
    if not model:
        model = gv.model_map[model_name]
    if not kwargs:
        kwargs = get_kwargs_for_ajax_request(data)

    return model.objects.filter(**kwargs)


def populate_data_from_request(request):
    data = {
        **dict(request.GET),
        **dict(request.POST)
    }
    files = dict(request.FILES)

    return {
        k: v[0] for k, v in data.items()
    }, {
        k: v[0] for k, v in files.items()
    }


def populate_template_context(form, data, class_name):
    return {
        'form': form,
        'data_url': data.get('data-post-url', ''),
        'form_class': class_name,
        'data_props': data.get('model-props', 'rider-add-profile'),
        **data
    }


def model_props(props):
    app_label, action, model_name = props.split('-')

    return app_label, action, model_name


def check_act_perm(request, app_label, action, model_name_actual):
    have_permission = request.user.has_perm(
        app_label + '.' + action + '_' + model_name_actual)

    if not have_permission:
        response = JsonResponse(
            {
                'message': "Don't have enough permission, please try again after getting permission."
            }
        )
        response.status_code = 403
        return response

    else:
        return False


def get_custom_script(class_name):
    return """
        $('.%s').on('submit', function(e) {
            ajaxTwoActHandler($(this), e)
        });
    """ % class_name


def get_form_call_custom_script(class_name):
    return """
        $('.%s').on('click', function(e) {
            ajaxFourActHandler($(this))
        });
    """ % class_name
