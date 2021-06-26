from rest_framework import serializers

from .elastic_filter import ElasticFilter
from .sub_serializer import generate_sub_serializer
from .utils import get_all_fields, str_to_class


def generate_serializer(class_model,
                        model_fields,
                        rest,
                        request,
                        modules):
    """
    Generate main serializer

    :param class_model: Model name.
    :param model_fields: Fields in Model.
    :param rest: Other fields that there aren't in model_fields.
    :param request: Request from url.
    :param modules: Module's path for Model.
    :return : A serializer.
    """

    class Meta:
        model = class_model
        fields = get_all_fields(model_fields, rest)

    def generate_field_method(key, module_path):
        obj = str_to_class(module_path)
        elastic_filter = ElasticFilter(key, 'user_id', request)
        elastic_filter_fields = elastic_filter.get_scope_other_fields()

        def get_field(self, instance):
            try:
                serializer_context = {'request': request}
                natural = obj.objects.get(user=instance.user)
                g = generate_sub_serializer(obj, elastic_filter_fields['fields'])
                serializer = g(natural, context=serializer_context)
                return serializer.data
            except Exception as e:
                raise ValueError(e)

        return get_field

    attr = {}
    for item in rest:
        # Field
        attr[item] = serializers.SerializerMethodField()
        # Method, get_`field`
        attr['get_' + item] = generate_field_method(item, modules[item])

    attr['Meta'] = Meta
    return type('ElasticSerializer', (serializers.ModelSerializer,), attr)
