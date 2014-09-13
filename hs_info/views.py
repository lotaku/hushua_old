# encoding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from hs_info.forms import HsInfoForm,NotdoForm
from hs_info.models import HsInfo,Notdo
import json
from django.forms.models import inlineformset_factory
# Create your views here.


def index(request):
	page = int(request.GET.get('page', 1))

	paginate_by = 1
	task_list = HsInfo.objects.all()
	paginator = Paginator(task_list, paginate_by)
	page_obj = paginator.page(page)


	num_pages = paginator.num_pages
	pagination_list = []
	pagination_list.append(page)

	if num_pages <= 10:
		print num_pages
		pagination_list = [item for item in range(1, num_pages + 1)]

	elif page < 10:
		pagination_list = [item for item in range(1, 11)]

	else:
		list_right = []

		for idx, item in enumerate(range(page, num_pages + 1)):
			list_right.append(item)
			if idx == 5:
				break
		left_len = 10 - len(list_right)

		left_len = 0 if left_len < 0 else left_len
		list_left = [item for item in range(page - left_len, page)]
		pagination_list = list_left + list_right

	context = {
		'page_obj': page_obj,
		'paginator': paginator,
		'pagination_list': pagination_list,
	}

	return render_to_response('index.html', context,
							  context_instance=RequestContext(request))


@login_required
def add_task(request):
	# NotdoInlineFormSet = inlineformset_factory(HsInfo, Notdo, form=NotdoForm)
	if request.method == 'POST':

		form = HsInfoForm(request.POST)

		if form.is_valid():

			task = form.save(commit=False)
			task.user = request.user
			form.save()


			tasks = HsInfo.objects.all()
			for t in tasks:
				print t.not_dos.all()

			return render_to_response('users_manage/user_all.html',
									  {'users': tasks},
									  context_instance=RequestContext(request))

	else:

		# form = NotdoInlineFormSet()
		form = HsInfoForm()
	return render_to_response('hs_info/add_task.html',
							  {'form': form,
							   'user': request.user},
							  context_instance=RequestContext(request),
	)


	# def create_org(request, response_format='html'):
	# if request.method == 'POST':
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