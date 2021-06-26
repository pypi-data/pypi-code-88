from rest_framework.serializers import ModelSerializer


def gen_sub_serializer(class_model,
                       model_fields):
    class SubModelSerializer(ModelSerializer):
        def __init__(self, *args, **kwargs):
            request = kwargs.get('context', {}).get('request')
            str_fields = request.GET.get('info', '') if request else None
            fields = str_fields.split(',') if str_fields else None
            super(SubModelSerializer, self).__init__(*args, **kwargs)

            if fields is not None:
                allowed = set(fields)
                existing = set(fields)
                for field_name in existing - allowed:
                    fields.pop(field_name)

        class Meta:
            model = class_model
            fields = model_fields

    return SubModelSerializer
