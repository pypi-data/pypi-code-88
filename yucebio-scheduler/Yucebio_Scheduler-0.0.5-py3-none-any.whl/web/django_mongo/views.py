from yucebio_scheduler.web.django_mongo.utils import create_scheduler
from yucebio_scheduler.web.api import API
from yucebio_scheduler.utils import Job
from django.http import JsonResponse, HttpRequest
from apscheduler.jobstores.base import ConflictingIdError, JobLookupError


def get_api():
    scheduler = create_scheduler()
    api = API(scheduler)
    return api

def get_info(request: HttpRequest):
    api = get_api()

    return JsonResponse({
        "data": api.get_scheduler_info()
    }, status=200)

def add_job(request: HttpRequest):
    return JsonResponse({"error": "不支持添加作业"})

def get_jobs(request: HttpRequest):
    api = get_api()

    jobs = []
    for job in api.get_jobs():
        jobs.append(api.job_to_dict(job))
    return JsonResponse({"data": jobs})

def get_job(request: HttpRequest, jobid: str):
    api = get_api()
    job = api.get_job(jobid)

    if not job:
        return JsonResponse({"error": f"Job {jobid} not found"}, status=404)
    return JsonResponse({"data": api.job_to_dict(job)})

def delete_job(request: HttpRequest, jobid: str):
    return _manage_job(request, jobid, action='delete')

def pause_job(request: HttpRequest, jobid: str):
    return _manage_job(request, jobid, action='pause')

def resume_job(request: HttpRequest, jobid: str):
    return _manage_job(request, jobid, action='resume')

def run_job(request: HttpRequest, jobid: str):
    return _manage_job(request, jobid, action='run')

def _manage_job(request: HttpRequest, jobid: str, action='get'):
    api = get_api()

    try:
        func = getattr(api, f'{action}_job', None)
        func(jobid)
        if not func:
            return JsonResponse({"error": f"not supported action [{action}]"}, status=500)
        job = api.get_job(jobid)
        return JsonResponse({"data": api.job_to_dict(job)})
    except JobLookupError:
        return JsonResponse({"error": f"Job {jobid} not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)