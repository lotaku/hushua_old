from django.conf.urls import patterns, url
from users_manage import views

urlpatterns = patterns('',
    url(r'^user_add/$', views.user_add, name='user_add'),
    url(r'^login/$', views.login, name='login'),
    
    url(r'^2/$', views.two, name='two'),
    url(r'^datatables/$', views.datatables, name='datatables'),
    url(r'^validation/$', views.validation, name='validation'),
    url(r'^bootstrapForms/$', views.bootstrapForms, name='bootstrapForms'),
    
  
)