from django.db import models

# Create your models here.
class  Users(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=8, null=True, blank=True)


