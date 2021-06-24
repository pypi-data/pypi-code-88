from django.db import models

class Model(models.Model):
    app = models.TextField()
    name = models.TextField()
    db_table = models.TextField()
    is_admin = models.BooleanField(null=True,verbose_name='admin')
    is_middleware = models.BooleanField(verbose_name='middleware')
    count = models.IntegerField(null=True)

    class Meta:
        db_table = 'django_objects_count_model'
        indexes = [
           models.Index(fields=['app',]),
           models.Index(fields=['name',]),
           models.Index(fields=['db_table',]),
           models.Index(fields=['is_middleware',]),
        ]
        ordering = ('app','name',)
