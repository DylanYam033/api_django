from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    technology = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    