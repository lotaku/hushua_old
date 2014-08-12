from django import forms
from models import Users

class UsersForm(forms.ModelForm):
    # name = forms.CharField(max_length=100)
    class Meta:
        model = Users
        # fields = ['name', 'email', 'password']
    # message = forms.CharField()
    # sender = forms.EmailField()
    # cc_myself = forms.BooleanField(required=False)