from isc_common.http.DSResponse import DSResponseUpdate, DSResponseAdd, DSResponse, JsonResponseWithException
from isc_common.http.RPCResponse import RPCResponseConstant
from isc_common.http.response import JsonResponse
from lfl_admin.competitions.models.calendar import Calendar, CalendarManager


@JsonResponseWithException()
def Calendar_Fetch(request):
    return JsonResponse(
        DSResponse(
            request=request,
            data=Calendar.objects.
                select_related().
                get_range_rows1(
                request=request,
                function=CalendarManager.getRecord
            ),
            status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Add(request):
    return JsonResponse(DSResponseAdd(data=Calendar.objects.createFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Update(request):
    return JsonResponse(DSResponseUpdate(data=Calendar.objects.updateFromRequest(request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Remove(request):
    return JsonResponse(DSResponse(request=request, data=Calendar.objects.deleteFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Lookup(request):
    return JsonResponse(DSResponse(request=request, data=Calendar.objects.lookupFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Info(request):
    return JsonResponse(DSResponse(request=request, data=Calendar.objects.get_queryset().get_info(request=request), status=RPCResponseConstant.statusSuccess).response)


@JsonResponseWithException()
def Calendar_Copy(request):
    return JsonResponse(DSResponse(request=request, data=Calendar.objects.copyFromRequest(request=request), status=RPCResponseConstant.statusSuccess).response)
