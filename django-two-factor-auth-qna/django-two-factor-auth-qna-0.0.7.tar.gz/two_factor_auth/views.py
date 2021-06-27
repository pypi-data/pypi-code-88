from hashlib import md5

from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from two_factor_auth.serializers import CreateUserSerializer, CreateUserAnswerSerializer
from two_factor_auth.models import Question, UserAnswer
from two_factor_auth.serializers import (
    QuestionSerializer,
    LoginSerializer,
    UserAuthInputSerializer,
    VerifyAnswerInputSerializer,
    VerifyAnswerSerializer,
)
from two_factor_auth.utils import (
    check_2fa_login_attempt,
    update_2fa_session,
    invalid_attempt_limit,
    registration_questions_count,
    registration_min_answer_count,
    retry_in_seconds,
)

User = get_user_model()


class UserLogin(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserAuthInputSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            return Response(
                {"user": self.get_serializer(user).data}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


class QuestionViewSet(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (AllowAny,)


class VerifyAnswerViewSet(GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = VerifyAnswerSerializer

    def post(self, request):
        serializer = VerifyAnswerInputSerializer(data=request.data)
        if serializer.is_valid():
            answer_count_temp = 0
            user_id = request.user.id

            check_2fa_login_attempt(user_id)

            for rq in request.data.get("requests"):
                question_id = rq.get("question_id")
                answer_encode = md5(rq.get("answer").encode()).hexdigest()

                answer = UserAnswer.objects.filter(
                    django_user_id=user_id,
                    question_id=question_id,
                    answer__exact=answer_encode,
                )

                if answer.count() > 0:
                    answer_count_temp += 1

            if answer_count_temp >= invalid_attempt_limit:
                data = dict()
                user = User.objects.get(id=user_id)
                refresh = RefreshToken.for_user(user)
                data["refresh"] = str(refresh)
                data["access"] = str(refresh.access_token)
                return Response(
                    {"token": self.get_serializer(data).data}, status=status.HTTP_200_OK
                )
            else:
                update_2fa_session(user_id, True)
                msg = dict()
                msg["error"] = "Invalid Answers"
                return Response(msg, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserRegistrationViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    permission_classes = (AllowAny,)


class UserAuthAnswerView(GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        requests_data = data.get("requests")
        print(requests_data)
        # TODO: add auth token for this user validation

        try:
            user_obj = User.objects.get(id=request.user.id, is_active=True)
        except User.DoesNotExist:
            return Response("User does not exist")
        # allowed_answer = 1
        # if allowed_answer > len(auth_answer):
        #     return Response(
        #         f'Please answer question at least {allowed_answer}',
        #         status=status.HTTP_400_BAD_REQUEST)

        with transaction.atomic():
            user_answer_serializer = CreateUserAnswerSerializer(
                data=requests_data, many=True, context={"django_user": user_obj}
            )
            if not user_answer_serializer.is_valid():
                transaction.set_rollback(True)
                return Response(
                    user_answer_serializer.errors, status=status.HTTP_400_BAD_REQUEST
                )
            user_answer_serializer.save()

        return Response("success", status=status.HTTP_200_OK)


class Config(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        return Response(
            {
                "Config": {
                    "registration_questions_count": registration_questions_count,
                    "registration_min_answer_count": registration_min_answer_count,
                    "retry_in_seconds": retry_in_seconds,
                    "invalid_attempt_limit": invalid_attempt_limit,
                }
            }
        )
