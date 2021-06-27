import logging
from django.http import HttpResponse, JsonResponse
from django.template import loader

from .plugins import Plugins
import json


# Module logger
mogger = logging.getLogger("pza.views")


###############################################################################
###############################################################################

def index(request):
    """
    """
    template = loader.get_template('index.html')
    # print(Plugins.GetStatus())
    return HttpResponse(template.render(
        {
            "plugin_status": Plugins.GetStatus()
        },
        request=request))

###############################################################################
###############################################################################

def interfaces(request):
    """
    """
    print(">>>", request, request.method)

    return JsonResponse( Plugins.GetInterfaces() )

###############################################################################
###############################################################################
    
def interfaces_ui(request):
    html = "<html><body>Panduza Server</body></html>"
    return HttpResponse(html)

###############################################################################
###############################################################################

def plugins_ui(request):

    template = loader.get_template('plugins.html')

    plugin_names = Plugins.GetNames()

    return HttpResponse(template.render({"plugin_names": plugin_names}, request))    


###############################################################################
###############################################################################

def plugins(request):
    """
    Return the list of plugins
    """
    if request.method == "GET":
        plugins_status = Plugins.GetStatus()
        mogger.debug("Request GET on plugins %s [%s]", plugins_status, type(plugins_status))
        return JsonResponse( plugins_status )
    else:
        return HttpResponse( status=405 ) # Method not allowed
