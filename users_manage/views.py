from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponseRedirect
# from forms import UsersForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Choice, Poll
# from models import Users
from users_manage.forms import UserCreationForm,UserAuthForm
from users_manage.models import MyUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

# class AddView(generic.ListView):
#     template_name = 'users_manage/user_add.html'
#     # context_object_name = 'latest_poll_list'
#     def get_queryset(self):
#     """Return the last five published polls."""
#     return Poll.objects.order_by('-pub_date')[:5]
def user_add(request):
	users=MyUser.objects.all()
	# print users
	print "^"*99
	if request.method == 'POST': 
		
		f = UserCreationForm(request.POST)
		
		if f.is_valid(): 

			email = f.cleaned_data['email']
			password1 = f.cleaned_data['password1']
			user = User.objects.create_user(email, password=password1)
			user.save()

			
			# print "*"*99
			# return render(request, 'users_manage/user_all.html', {'users':users })
			
			return render_to_response('users_manage/user_all.html',
																	 {'users':users },
																	 context_instance=RequestContext(request))
		else:
			# print dir(f)
			print f.errors
			return render_to_response('users_manage/user_all.html',
																	 {'users':users },
																	 context_instance=RequestContext(request))

	else:
		f = UserCreationForm() # An unbound form
		# return render(request, 'users_manage/user_add.html', {'form':f, })
		return render(request, 'users_manage/user_add.html', {'form':f, })

def login(request):
	users=MyUser.objects.all()
	# print users
	if request.method == 'POST': 		
		f = UserCreationForm(request.POST)		
		if f.is_valid(): 
			email = f.cleaned_data['email']
			password = f.cleaned_data['password1']
			user = authenticate(username=email, password=password)
			print "^"*99
			if user is not None:
				# the password verified for the user
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
			# print dir(f)
			print "@@"*99
			print f.errors
			return render_to_response('users_manage/user_all.html',
			 		{'users':users },
 					context_instance=RequestContext(request))

	else:
		f = UserAuthForm() # An unbound form
		# return render(request, 'users_manage/user_add.html', {'form':f, })
		return render(request, 'users_manage/user_add.html', {'form':f, })


	

def two(request):
		return render_to_response('users_manage/2.html',
																	 {'users':'users' },
																	 context_instance=RequestContext(request))

def datatables(request): 
		return render_to_response('users_manage/datatables.html',
																	 {'users':'users' },
																	 context_instance=RequestContext(request))
def validation(request): 
		return render_to_response('users_manage/validation.html',
																	 {'users':'users' },
																	 context_instance=RequestContext(request))
def bootstrapForms(request): 
		return render_to_response('users_manage/bootstrap-forms.html',
																	 {'users':'users' },
																	 context_instance=RequestContext(request))
