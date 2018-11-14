from django.db import models
import time
# Create your models here.


class SysConfig(models.Model):
    ID = models.CharField(max_length=36, primary_key=True)
    Content = models.CharField(max_length=5000)
    ConfigType = models.IntegerField()
    Updated = models.DateTimeField(default=time.time())

    class Meta:
        ordering=('Updated')
