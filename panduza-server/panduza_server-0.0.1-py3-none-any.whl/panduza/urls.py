"""panduza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path


from panduza.views import plugins, index, interfaces, interfaces_ui

from .interfaces import io


urlpatterns = [
    path('', index),
    path('ui/interfaces', interfaces_ui),
    # path('ui/plugins', plugins_ui),

    path('ui/io', io.ui_multi_control),
    path('ui/io/<str:adapter>/<str:interface>', io.ui_single_control),

    path('plugins', plugins),
    # path('plugin/<str:name>/conf', plugins),

    path('interfaces', interfaces),
    
    path('io/<str:adapter>/<str:interface>/value', io.value),
    path('io/<str:adapter>/<str:interface>/direction', io.direction),
    # path('io/<str:adapter>/<str:interface>/active_low', io.active_low),
]


