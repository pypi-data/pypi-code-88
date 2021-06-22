
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.views import redirect_to_login

from flatpages.models import FlatPage


def flatpage(request, url):

    obj = get_object_or_404(FlatPage, url=url)

    if obj.registration_required and not request.user.is_authenticated():
        return redirect_to_login(request.path)

    template_name = obj.template_name or 'flatpages/default.html'

    return render(request, template_name, {'flatpage': obj})
