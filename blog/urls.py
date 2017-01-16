from django.conf.urls import url
from . import views
from django.conf.urls import include, url
from . import views



urlpatterns = [
	url(r'^add_record', views.add_record, name = 'add_record'),
	url(r'(?P<id>^\d+)', views.post_record, name = 'post_record'),
	url(r'^$',views.post_list,name='post_list'),
	
]