from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout

urlpatterns=[
    url(r'^$', views.home),
    url(r'^login/$',login,{'template_name':'accounts/login.html'}),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}),
    url(r'^register/$', views.register,name='register'),
    url(r'^profile/$', views.create_note, name='profile'),
    url(r'^notes/$', views.notes_view, name='note_view'),
    url(r'^shared_notes/$', views.shared_view, name='note_view'),

    url(r'^home/$',views.home, name='home'),
]