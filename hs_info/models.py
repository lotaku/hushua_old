# encoding: utf-8
from django.db import models
from users_manage.models import MyUser
from django.contrib.auth.models import User

from django.contrib import admin
from django.contrib.contenttypes.generic import GenericTabularInline

# from myproject.myapp.models import Image, Product
import json
# Create your models here.

class Notdo(models.Model):
	choice = models.CharField(max_length=100)
	# notdos = models.ManyToManyField(HsInfo,related_name='hsinfo_set')
	# hsinfo = models.ForeignKey(HsInfo, null=True)

	def __unicode__(self):
		return unicode(self.choice)

class HsInfo(models.Model):
	# #任务发布人
	user = models.ForeignKey(User)
	# 小号要求
	week_limited = models.IntegerField(max_length=256, null=True, blank=True)
	month_limited = models.IntegerField(max_length=256, null=True, blank=True)
	# 是否接受卖家号
	is_seller = models.BooleanField()
	# 是否签收
	sign_required = models.BooleanField()
	#店铺类型
	# shop_type_dict = (
	# 	('天猫', '天猫'),
	# 	('C店', 'C店'),
	# )

	shop_type = models.CharField(max_length=10, null=True, blank=True)
	#信誉大于多少？通过表单定义多个字段给用户选择，models只保留最后结果
	# reputation = (
	# ('不做要求', '不做要求'),
	# ('1心以上', '1心以上'),
	# ('2心以上', '2心以上'),
	# ('3心以上', '3心以上'),
	# ('4心以上', '4心以上'),
	# ('5心以上', '5心以上'),
	# ('黄钻以上', '黄钻以上'),
	# )
	reputation_gt = models.CharField(max_length=100, null=True, blank=True)

	#不刷信用卡等等
	# not_do = models.NullBooleanField()
	not_dos = models.ManyToManyField(Notdo)
	#城市-行业 ,
	city_and_sector = models.CharField(max_length=8, null=True, blank=True)
	#是否假聊
	chat_required = models.BooleanField(default=True)
	#其他注意
	other_info = models.CharField(max_length=512, null=True, blank=True)
	#价格
	min_payment = models.IntegerField(max_length=128, default=1)
	max_payment = models.IntegerField(max_length=128, default=999)






