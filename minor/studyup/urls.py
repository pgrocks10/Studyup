from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^signup/$', views.userform_view, name='userform_view'),
	url(r'^login/$', views.loginform_view, name='loginform_view'),
]
