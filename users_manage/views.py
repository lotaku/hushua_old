# -*- coding: UTF-8 –*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import  login as django_login

from django.shortcuts import get_object_or_404
# Create your views here.

from django.template import RequestContext
from users_manage.forms import UserCreationForm,UserAuthForm
from users_manage.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
from django.http import HttpResponse
from django.utils import simplejson
import json

def render_json(data):
	return HttpResponse(simplejson.dumps(data, ensure_ascii=False))

def user_add(request,response_format = 'ajax'):
	users=MyUser.objects.all()
	if request.method == "POST" and request.is_ajax():
		print "Right!"
		f = UserCreationForm(request.POST)
		if f.is_valid():
			email = f.cleaned_data['email']
			password1 = f.cleaned_data['password1']
			user = User.objects.create_user(email, password=password1,email=email)
			user.save()

			response_data = {}
			response_data.update({'users':users,})

			return render_to_response('users_manage/user_all.html',
									  json.dumps(response_data),
									  context_instance=RequestContext(request))
		else:
			print "ougoeuogu"
			response_data = json.dumps({'state': False,'errMsg':'错误信息'})

			return HttpResponse(response_data,content_type='application/json')



	else:
		f = UserCreationForm() # An unbound form
		# return render(request, 'users_manage/user_add.html', {'form':f, })
		return render(request, 'users_manage/user_add.html', {'form':f, })

def login(request):
	users=MyUser.objects.all()
	if request.method == 'POST':
		f = UserAuthForm(request, data=request.POST)
		if f.is_valid(): 
			username = f.cleaned_data['username']
			password = f.cleaned_data['password']
			user = authenticate(username=username, password=password)
			request.user = user
			django_login(request,user)

			if user is not None:
				if user.is_active:
					print("User is valid, active and authenticated")
				else:
					print("The password is valid, but the account has been disabled!")
			else:
				# the authentication system was unable to verify the username and password
				print("The username and password were incorrect.")
			return render_to_response('users_manage/user_all.html',
			 {'users':users },
			 context_instance=RequestContext(request))
		else:
			print f.error_messages
			for m in f.error_messages:
				print type(m)
			return render_to_response('users_manage/user_all.html',
			 		{'users':users },
 					context_instance=RequestContext(request))
	else:
		f = UserAuthForm() # An unbound form
		# return render(request, 'users_manage/user_add.html', {'form':f, })
		return render(request, 'users_manage/login.html', {'form':f })


def ajax_test(request):
	print request.is_ajax()
	if request.method == "POST":
		response_data = json.dumps({'state': True,'errMsg':'错误信息'})
		print response_data
		return HttpResponse(response_data,content_type='application/json')

	else:
		print 'not ajax'
		return render(request, 'test.html',{})

