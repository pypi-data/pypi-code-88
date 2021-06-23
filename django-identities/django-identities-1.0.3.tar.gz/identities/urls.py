from django.urls import re_path
from django.conf.urls import include
from rest_framework.routers import DefaultRouter

from . import views, oidc
from .apps import APP_NAME


router = DefaultRouter()
router.register(r"users", views.UserViewSet, "user")
router.register(r"permission", views.PermissionViewSet, "permission")
router.register(
    r"object_by_permission", views.ObjectByPermissionViewSet, "object_by_permission"
)
router.register(r"group", views.GroupViewSet, "group")


# The API URLs are now determined automatically by the router.
app_name = APP_NAME
urlpatterns = [
    re_path(r"", include(router.urls)),
    re_path("^auth/oidc/authenticate/", oidc.authenticate, name="oidc-authenticate"),
    re_path("^auth/oidc/callback/", oidc.callback, name="oidc-callback"),
    re_path("^auth/oidc/logout/", oidc.logout, name="oidc-logout"),
    re_path(r"^userinfo/$", views.UserinfoView.as_view(), name="userinfo"),
]
