import os

try:
    from celery import Celery
    enabled = True
except ImportError:
    app = None
    enabled = False
else:
    app = Celery(os.getenv('CELERY_APP_NAME') or 'unimatrix')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()


    @app.task(bind=True)
    def debug_task(self):
        print('Request: {0!r}'.format(self.request))
