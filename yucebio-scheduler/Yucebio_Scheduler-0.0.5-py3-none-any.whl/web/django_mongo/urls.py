from django.urls import path
from yucebio_scheduler.web.django_mongo import views


urlpatterns = [
    path('', views.get_info),
    path('get_scheduler_info', views.get_info),
    path('jobs', views.get_jobs),

    path('add_job', views.add_job),
    path('show/<jobid>', views.get_job),
    path('delete/<jobid>', views.delete_job),
    # path('update_job', ''),
    path('pause/<jobid>', views.pause_job),
    path('resume/<jobid>', views.resume_job),
    path('run/<jobid>', views.run_job)
]


