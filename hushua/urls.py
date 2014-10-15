from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hushua.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/$', include(admin.site.urls)),
    url(r'^polls/$', include('polls.urls', namespace='polls')),
    url(r'^users_manage/', include('users_manage.urls', namespace='users_manage')),
    url(r'^hs_info/$', include('hs_info.urls', namespace='hs_info')),
	url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'users_manage/login.html'}),
	# url(r'^accounts/login/$', include('users_manage.urls', namespace='users_manage')),
	url(r'^accounts/profile/$', 'hs_info.views.index'),
	url(r'^ajax_test/$', 'users_manage.views.ajax_test'),




   

)
# if settings.DEBUG:  
#     urlpatterns += patterns('', 
#         url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),
#         url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), )
urlpatterns += patterns('', 
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT } ,name = 'media'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT},name = 'static'), )   