from django.db import models

class Table(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    db_table = models.CharField(max_length=255)
    count = models.IntegerField(null=True,blank=True)

    class Meta:
        db_table = 'django_truncate_table'
        ordering = ('app','name',)
        unique_together = [('app','name',)]
