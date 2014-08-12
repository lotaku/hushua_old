from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponseRedirect
from forms import UsersForm
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from polls.models import Choice, Poll
from models import Users

# class AddView(generic.ListView):
#     template_name = 'users_manage/user_add.html'
#     # context_object_name = 'latest_poll_list'
#     def get_queryset(self):
#     """Return the last five published polls."""
#     return Poll.objects.order_by('-pub_date')[:5]

def user_add(request):
    if request.method == 'POST': 
        f = UsersForm(request.POST)
        if f.is_valid(): 
            f.save()
            users=Users.objects.all()
            print "*"*99
            # return render(request, 'users_manage/user_all.html', {'users':users })
            return render_to_response('users_manage/user_all.html',
                                                                     {'users':users },
                                                                     context_instance=RequestContext(request))
    else:
        f = UsersForm() # An unbound form
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
