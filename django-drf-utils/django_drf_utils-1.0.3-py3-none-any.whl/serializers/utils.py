from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError

User = get_user_model()


def get_request_username(serializer) -> User:
    return serializer.context["request"].user


class DetailedValidationError(ValidationError):
    def __init__(self, detail, field="detail"):
        super().__init__({field: detail}, code="invalid")
