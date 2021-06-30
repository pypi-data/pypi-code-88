from django.shortcuts import render, HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required

from .utils import *
set_gv()


@login_required()
def ajax_two_act_handler(request):
    data, files = populate_data_from_request(request)
    app_label, action, model_name = model_props(
        data.get('model-props', 'rider-add-profile')
    )

    response = check_act_perm(
        request, app_label, action, model_name
    )

    if response:
        return response

    method = request.method
    data['r_kwargs'] = "id=%s" % data['pk']

    try:
        validator = gv.validator_map.get(data['model-props'], False)
        validate = validator().is_valid()

        if not validate:
            raise Exception('Request not allowed, please check permission.')

        if method == 'POST' and action == 'add':
            form = gv.ajax_form_map[data['model-props']](
                request.POST, request.FILES
            )

            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors.as_text())

        elif method == 'POST' and action == 'change':
            form = gv.ajax_form_map[data['model-props']](
                request.POST, request.FILES, instance=get_instance_by_kwargs(
                    data, model_name=model_name
                ).first())

            if form.is_valid():
                form.save()
            else:
                raise Exception(form.errors.as_text())
        else:
            raise Exception('Request and action is not valid.')

    except Exception as e:
        data['error'] = str(e)

    if request.is_ajax():
        response = JsonResponse(data)

        if data.get('error', False):
            response.status_code = 403

        return response


@login_required()
def ajax_four_act_handler(request, props=None):
    if props is None:
        data, files = populate_data_from_request(request)
    else:
        data = gv.data_map_for_list_view.get(props, False)
        if type(data) is dict:
            data['model-props'] = props
        else:
            return HttpResponse('')

    app_label, action, model_name = model_props(
        data.get('model-props', 'rider-add-profile')
    )

    response = check_act_perm(
        request, app_label, action, model_name
    )

    if response:
        return response

    method = request.method
    data['verbose_name'] = get_verbose_name(model_name)

    if method == 'GET' and action == 'view':
        result = {'action': 'view'}
        keys = data.get('data-keys', 'id').split(',')

        data['data_add_props'] = app_label + '-add-' + model_name
        data['data_change_props'] = app_label + '-change-' + model_name
        data['data_delete_props'] = app_label + '-delete-' + model_name

        data['add_perm'] = request.user.has_perm(
            app_label + '.' + 'add' + '_' + model_name
        )
        data['change_perm'] = request.user.has_perm(
            app_label + '.' + 'change' + '_' + model_name
        )
        data['delete_perm'] = request.user.has_perm(
            app_label + '.' + 'delete' + '_' + model_name
        )

        data['ajax_call_add_change'] = 'ajax-four-act-handler-call-add-change-' + model_name
        data['custom_script'] = get_form_call_custom_script(data['ajax_call_add_change'])

        data['objects'] = list(get_instance_by_kwargs(
            data, model_name=model_name
        ).values(*keys).all())

        data['headers'] = get_verbose_name_for_fields(model_name, keys)

        result['html'] = get_template('onepage/list.html').render(
            data, request=request
        )

        if request.is_ajax():
            return JsonResponse(result)
        else:
            return render(request, 'base.html', {
                'html_body': result['html']
            })

    elif method == 'GET' and action == 'add':
        result = {'action': 'add'}

        form = gv.ajax_form_map[data['model-props']]()

        class_name = 'ajax-four-act-handler-add-' + model_name
        data['custom_script'] = get_custom_script(class_name)
        data['form_props'] = app_label + '-add-' + model_name
        data['method'] = 'POST'

        result['html'] = get_template('onepage/form.html').render(
            populate_template_context(
                form, data, class_name
            ), request=request
        )

        return JsonResponse(result)

    elif method == 'GET' and action == 'change':
        result = {'action': 'change'}
        data['r_kwargs'] = "id=%s" % data['id']

        form = gv.ajax_form_map[data['model-props']](
            instance=get_instance_by_kwargs(
                data, model_name=model_name
            ).first())

        class_name = 'ajax-four-act-handler-change-%s-%s' % (
            model_name, data.get('id', 0)
        )
        data['custom_script'] = get_custom_script(class_name)
        data['form_props'] = app_label + '-change-' + model_name
        data['method'] = 'POST'

        result['html'] = get_template('onepage/form_edit.html').render(
            populate_template_context(
                form, data, class_name
            ), request=request
        )

        return JsonResponse(result)

    elif method == 'GET' and action == 'delete':
        instance = get_instance_by_kwargs(
            data, model_name=model_name
        ).first()

        instance.delete()

        return JsonResponse(data)

    else:
        response = JsonResponse(
            {'message': 'Request and action is not valid.'}
        )
        response.status_code = 403

        return response
