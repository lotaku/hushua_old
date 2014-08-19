# encoding: utf-8
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator
from hs_info.forms import HsInfoForm
from hs_info.models import HsInfo
# Create your views here.


def index(request):
	page = 1
	# page = request.GET.get('page', 1)

	paginate_by = 1
	task_list = HsInfo.objects.all()
	paginator = Paginator(task_list, paginate_by)
	page_obj = paginator.page(page)

	# print page_obj
	print "^&"*45
	# print dir(Paginator.num_pages)
	# previous_list
	# for i in range(0, page_obj.page_)

	num_pages = paginator.num_pages
	pagination_list =[]
	pagination_list.append(page)

	i = 0
	for _ in range(0,page):
		i += 1 
		page_num = page-i
		if page_num >0:
			pagination_list.insert(0,page_num)
		else:
			break
		if i==5:
			break
	i = 0
	for _ in range(page,num_pages):
		i += 1 
		page_num = page+i
		if page_num <num_pages:
			pagination_list.append(page_num)
		else:
			break
		if i==5:
			break
	print pagination_list
	context= {
			'page_obj':page_obj,
			'paginator': paginator,
			'pagination_list': pagination_list,
        		}


	return render_to_response('index.html',context,
			 context_instance=RequestContext(request))	


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