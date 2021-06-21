from kubehelm.models import apps
from kubehelm.models.objects import ListK8sObjects


def k8s_list(namespace):
    print(ListK8sObjects(namespace).deployments())
    print("="*99)
    print(ListK8sObjects(namespace).pods())


def read_required_context(app_class):
    context = {}
    if hasattr(app_class, "required_context") and app_class.required_context:
        for field in app_class.required_context:
            default = app_class.default_context.get(field) or "-"
            value = input('%s (%s): ' % (field, default))
            context[field] = value or default
    return context


def handle_args(nargs):
    if nargs.action == 'list':
        return k8s_list('default')

    try:
        app_class = getattr(apps, nargs.app_name.capitalize())
    except (IndexError, AttributeError) as err:
        print("="*80)
        raise err
    context = read_required_context(app_class)
    app = app_class(**context)
    results = getattr(app, nargs.action)()
    print(results)
