from django.conf.urls import patterns, url
from users_manage import views

urlpatterns = patterns('',
	# url(r'^$', views.login, name='login'),
    url(r'^user_add(\.(?P<response_format>\w+))?/?$', views.user_add, name='user_add'),
    # url(r'^login/$', views.login, name='login'),
	# url(r'^accounts/login/$', views.login, name='login'),
    


)