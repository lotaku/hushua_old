# encoding: utf-8
from django import forms
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
	# birth_year = forms.DateField(widget=SelectDateWidget(years=BIRTH_YEAR_CHOICES))
	# favorite_colors = forms.MultipleChoiceField(required=False,
	# 	widget=forms.CheckboxSelectMultiple, choices=FAVORITE_COLORS_CHOICES)
	reputation_gt = forms.MultipleChoiceField(required=False,
		widget=forms.CheckboxSelectMultiple, choices=REPUTATION)

	class Meta:
	        model = HsInfo
	        # fields = ('user','week_limited')