# encoding: utf-8
from django.shortcuts import render,render_to_response
from hs_info.forms import HsInfoForm
from django.template import RequestContext
from hs_info.models import HsInfo
# Create your views here.
def add_task(request):
	if request.method == 'POST':
		form = HsInfoForm(request.POST)
		if form.is_valid():
			form.save()
			print "%"*99
			tasks=HsInfo.objects.all()
			print tasks
			return render_to_response('users_manage/user_all.html',
									{'users':tasks },
									 context_instance=RequestContext(request))
			# return render_to_response('hs_info/add_task.html',
			# {'form': form},
			# context_instance=RequestContext(request),)
	else:
		form = HsInfoForm()

	return render_to_response('hs_info/add_task.html',
		{'form': form},
		context_instance=RequestContext(request),
		)


# def create_org(request, response_format='html'):
# 	if request.method == 'POST':
# 		profile = request.user.get_profile()
# 		if profile.orgnization is not None:
# 			return HttpResponseRedirect(reverse('org:index'))
# 		form = OrgnizationForm(request.POST)
# 		if form.is_valid():
# 			org = form.save(commit = False)
# 			org.creator = profile
# 			org.save()
# 			profile.orgnization = org
# 			profile.save()

# 			Team.objects.create(name = u'默认组', orgnization = org)
# 			#grant_user_terminal(request, ['manage_org_orgs', \
# 			#        'manage_org_invite', 'manage_org_teams'])
# 			return render_to_response('org/create_org_contact', {'org': org},
# 								  context_instance=RequestContext(request),
# 								  response_format=response_format)

# 	return render_to_response('org/create_org',
# 								  context_instance=RequestContext(request),
# 								  response_format=response_format)