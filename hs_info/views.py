# encoding: utf-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from hs_info.forms import HsInfoForm
from hs_info.models import HsInfo
import json
# Create your views here.


def index(request):
	page = int(request.GET.get('page', 1))

	paginate_by = 1
	task_list = HsInfo.objects.all()
	paginator = Paginator(task_list, paginate_by)
	page_obj = paginator.page(page)
	# a = u'\u4fe1\u7528\u5361'

	# for t in page_obj.object_list:
	#
	# print t.not_do
	# 	print u'360\u6d4f\u89c8\u5668'
	# 	# l =t.not_do.replace('u\'','').replace('[','').replace(']','').replace('\'','')
	# 	l = [i for i in t.not_do.strip('[]').strip('u\'').replace('\'','').split(',') ]
	# 	# l=l[1:-1]
	# 	# l[-1]
	#
	# 	# l = l.split(',')
	# 	print l
	# 	print type(l)
	# 	b=l[0].replace('\\\\','\\')
	# 	print b

	# print a.encode('utf-8')
	# print t.shop_type


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
		print left_len
		left_len = 0 if left_len < 0 else left_len
		list_left = [item for item in range(page - left_len, page)]
		pagination_list = list_left + list_right
		print pagination_list
	for obj in page_obj:
		print list(json.loads(obj.not_do))
		# print x[1]
	context = {
		'page_obj': page_obj,
		'paginator': paginator,
		'pagination_list': pagination_list,
	}

	return render_to_response('index.html', context,
							  context_instance=RequestContext(request))


@login_required
def add_task(request):
	if request.method == 'POST':
		# request.POST['not_do'] = json.dumps(request.POST['not_do'])
		form = HsInfoForm(request.POST)
		# for fs in request.POST['not_do']:
		# 	print fs
		form.not_do = json.dumps(request.POST['not_do'])

		if form.is_valid():
			# for fs in form.cleaned_data['not_do']:
			# 	print fs
			# list_new = [item.encode('utf-8') for item in form.cleaned_data['not_do'] ]
			# list_test = ['谷歌', '百度']
			# x = json.dumps(list_test)
			# j = json.loads(x)
			z = json.dumps(form.cleaned_data['not_do'])
			j = json.loads(z)

			form.not_do = json.dumps(form.cleaned_data['not_do'])
			form.cleaned_data['not_do'] =json.dumps(form.cleaned_data['not_do'])

			form.save()
			# print form.cleaned_data

			tasks = HsInfo.objects.all()

			return render_to_response('users_manage/user_all.html',
									  {'users': tasks},
									  context_instance=RequestContext(request))

	else:

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