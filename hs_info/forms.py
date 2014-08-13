# encoding: utf-8
from django import forms
from django.utils.translation import ugettext as _
from django.forms.extras.widgets import SelectDateWidget
from hs_info.models import HsInfo


REPUTATION = (('1心','1心'),
	('2心','2心'),
	('3心','3心'),
	('4心','4心'),
	('5心','5心'),
	('钻号','钻号')
	)


class HsInfoForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(HsInfoForm, self).__init__(*args, **kwargs)
		self.fields['reputation_gt'].label = "信誉大于"
		self.fields['shop_type'].label = "店铺类型"
		self.fields['sign_required'].label = "是否签收"
		
		# self.fields['new_password'].label = _("New Password")
		# self.fields['new_password_again'].label = _("Confirm Password")

	class Meta:
		model = HsInfo
		# fields = ('user','week_limited', 'reputation_gt', 'shop_type')
		# self.fields = fields	