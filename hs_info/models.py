# encoding: utf-8
from django.db import models
from users_manage.models import Users

# Create your models here.

class  HsInfo(models.Model):
	##任务发布人
	user = models.ForeignKey(Users)
	#小号要求
	week_limited = models.IntegerField(max_length=256, null=True, blank=True) 
	month_limited = models.IntegerField(max_length=256,null=True, blank=True)
	#是否接受卖家号
	is_seller = models.BooleanField()
	#是否签收
	sign_required = models.BooleanField()
	#店铺类型
	shop_type = models.CharField(max_length=256,null=True, blank=True)
	##信誉大于多少？通过表单定义多个字段给用户选择，models只保留最后结果
	reputation_gt = models.CharField(max_length=256,null=True, blank=True) 
	#不刷信用卡等等
	not_do = models.CharField(max_length=512,null=True, blank=True)
	#城市-行业 , 
	city_and_sector = models.CharField(max_length=128,null=True, blank=True)
	#是否假聊 
	chat_required = models.BooleanField()
	#其他注意
	other_info = models.CharField(max_length=512,null=True, blank=True)
	#价格
	min_payment = models.IntegerField(max_length=128) 
	max_payment  = models.IntegerField(max_length=128) 








    # name = models.CharField(max_length=100, null=True, blank=True)
    # email = models.EmailField(max_length=100, null=True, blank=True)
    # password = models.CharField(max_length=8, null=True, blank=True)