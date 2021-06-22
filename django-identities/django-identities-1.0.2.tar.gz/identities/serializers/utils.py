from django.contrib.auth import get_user_model

User = get_user_model()


def get_request_username(serializer) -> User:
    return serializer.context["request"].user
