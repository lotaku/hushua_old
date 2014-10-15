# -*- coding:utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from django.forms.extras.widgets import SelectDateWidget
from hs_info.models import HsInfo,Notdo


REPUTATION = (
	(u'1心','1心'),
	(u'2心','2心'),
	(u'3心','3心'),
	(u'4心','4心'),
	(u'5心','5心'),
	(u'钻号','钻号')
	)
class NotdoForm(forms.ModelForm):
		#不刷

	# NOT_DO_LIST = (
	# 	('信用卡','信用卡'),
	# 	('360浏览器','360浏览器'),
	# 	('淘宝浏览器','淘宝浏览器'),
	# 	('代付', '代付'),
	# 	)
	# LIST = ['信用卡', '360浏览器']
	# not_do = forms.MultipleChoiceField(choices=NOT_DO_LIST)
	class Meta:
		model = Notdo

class HsInfoForm(forms.ModelForm):
	#user


	#不刷

	# NOT_DO_LIST = (
	# 	('信用卡','信用卡'),
	# 	('360浏览器','360浏览器'),
	# 	('淘宝浏览器','淘宝浏览器'),
	# 	('代付', '代付'),
	# 	)
	# LIST = ['信用卡', '360浏览器']
	# not_do = forms.MultipleChoiceField(choices=NOT_DO_LIST)
	#其他信息
	other_info = forms.CharField(max_length=200,widget=forms.Textarea)

	#店铺类型
	SHOP_TYPE_DICT = (

		(u'C店', 'C店'),
		(u'天猫', '天猫'),
	)
	shop_type = forms.ChoiceField(choices=SHOP_TYPE_DICT)

	#信誉大于
	REPUTATION = (
	(u'不做要求', '不做要求'),
	(u'1心以上', '1心以上'),
	(u'2心以上', '2心以上'),
	(u'3心以上', '3心以上'),
	(u'4心以上', '4心以上'),
	(u'5心以上', '5心以上'),
	(u'黄钻以上', '黄钻以上'),


	)
	reputation_gt = forms.ChoiceField(choices=REPUTATION)



	def __init__(self, *args, **kwargs):
		super(HsInfoForm, self).__init__(*args, **kwargs)
		self.fields['reputation_gt'].label = u"信誉大于"
		self.fields['shop_type'].label = u"店铺类型"
		self.fields['sign_required'].label = u"是否签收"
		# self.fields['not_dos'] = forms.CheckboxSelectMultiple() # 也是有效的


	class Meta:
		model = HsInfo
		exclude = ['user','publish_date']
		widgets = {'not_dos': forms.CheckboxSelectMultiple,

		}
		labels = {
			'shop_type': u"店铺类型",
		}
