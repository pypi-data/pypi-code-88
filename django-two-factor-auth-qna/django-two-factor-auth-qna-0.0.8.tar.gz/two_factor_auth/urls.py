from django.urls import path

import two_factor_auth.views as view


urlpatterns = [
    path(r"2fa-config/", view.Config.as_view(), name="2fa-config"),
    path(r"login/", view.UserLogin.as_view(), name="login"),
    path(r"register/", view.UserRegistrationViewSet.as_view(), name="register"),
    path(r"questions/", view.QuestionViewSet.as_view(), name="questions"),
    path(
        r"2fa-verify-answer/",
        view.VerifyAnswerViewSet.as_view(),
        name="2fa-verify-answer",
    ),
    path(r"auth-questions/", view.UserAuthAnswerView.as_view(), name="auth-questions"),
]
