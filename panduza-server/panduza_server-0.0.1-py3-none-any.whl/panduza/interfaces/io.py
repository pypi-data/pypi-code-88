import json
import logging
from django.http import HttpResponse, JsonResponse
from django.template import loader

from ..plugins import Plugins


# Module logger
mogger = logging.getLogger("pza.interfaces.io")



###############################################################################
###############################################################################

def ui_multi_control(request):
    """
    """
    template = loader.get_template('io_multi_control.html')
    
    io_interfaces = []

    adapters = Plugins.GetAdapters()
    for a in adapters:
        for i in adapters[a]:
            if adapters[a][i]["type"] == "io":
                io_interfaces.append(str(a) + "/" + str(i))

    return HttpResponse(template.render(
        {
            "io_interfaces": io_interfaces
        },
        request=request))



###############################################################################
###############################################################################

def ui_single_control(request, adapter, interface):
    """
    """
    template = loader.get_template('io_single_control.html')
    
    return HttpResponse(template.render(
        {
            "target_interface": str(adapter) + "/" + str(interface),
            "plugin_status": Plugins.GetStatus()
        },
        request=request))

###############################################################################
###############################################################################

def value(request, adapter, interface):
    """
    """
    # Debug
    mogger.debug("[%s] io.value %s %s", request.method, adapter, interface)
    
    try:
        # Find plugin
        plugin = Plugins.FindPluginFromAdapter(adapter_name=adapter)
        mogger.debug("Plugin found for adapter [%s] => [%s] ", adapter, plugin.Name )

        # Manage the GET method
        if request.method == "GET":
            mogger.debug("GET method")
            return JsonResponse( { 'value': plugin.IoValueRead(adapter, interface) } )

        # Manage the PUT method
        elif request.method == "PUT":
            body_unicode = request.body.decode('utf-8')
            mogger.debug("PUT method %s", body_unicode)
            body = json.loads(body_unicode)
            plugin.IoValueWrite(adapter, interface, body["value"])
            return HttpResponse(status=200)

        # Others are errors
        else:
            mogger.warning("Unknown method %s", request.method)
            return HttpResponse(status=405)

    except Exception as e:
        mogger.error(repr(e))

###############################################################################
###############################################################################

def direction(request, adapter, interface):
    """
    """
    # Debug
    mogger.debug("[%s] io.direction %s %s", request.method, adapter, interface)
    
    try:
        # Find plugin
        plugin = Plugins.FindPluginFromAdapter(adapter_name=adapter)
        mogger.debug("Plugin found for adapter [%s] => [%s] ", adapter, plugin.Name )
        
        # Manage the GET method
        if request.method == "GET":
            mogger.debug("GET method")
            return JsonResponse( { "direction": plugin.IoDirectionRead(adapter, interface) } )

        # Manage the PUT method
        elif request.method == "PUT":
            body_unicode = request.body.decode('utf-8')
            mogger.debug("PUT method %s", body_unicode)
            body = json.loads(body_unicode)
            plugin.IoDirectionWrite(adapter, interface, body["direction"])
            return HttpResponse(status=200)

        # Others are errors
        else:
            mogger.warning("Unknown method %s", request.method)
            return HttpResponse(status=405)

    except Exception as e:
        mogger.error(repr(e))
        return HttpResponse(repr(e), status=500)

###############################################################################
###############################################################################

def active_low(request, adapter, interface):
    # print(">>>", request, request.method)

    return JsonResponse( Plugins.GetInterfaces() )



