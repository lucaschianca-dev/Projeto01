from django.db import models

# Create your models here.
class ToDo(models.Model):
    activate = models.CharField(max_length=120)
    status = models.BooleanField(default=False)