from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$', views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register,name='register'),
    url(r'^profile/$', views.create_note, name='profile'),
    url(r'^notes/$', views.notes_view, name='note_view'),
    url(r'^shared_notes/$', views.shared_view, name='shared_notes'),
    url(r'^edit/(?P<pk>\d+)$', views.note_update, name='note_edit'),
    url(r'^home/$',views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^delete/(?P<pk>\d+)$', views.note_delete, name='note_delete'),
]