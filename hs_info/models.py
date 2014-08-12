# encoding: utf-8
from django.db import models

# Create your models here.

class  HsInfo(models.Model):
	#小号要求
	week_limited = IntegerField(null=True, blank=True)
	month_limited = IntegerField(null=True, blank=True)
	is_seller = BooleanField()

    # name = models.CharField(max_length=100, null=True, blank=True)
    # email = models.EmailField(max_length=100, null=True, blank=True)
    # password = models.CharField(max_length=8, null=True, blank=True)