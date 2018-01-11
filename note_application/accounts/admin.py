from django.contrib import admin
from django_messages.models import Message
from .models import UserProf,Noteclass



# Register your models here.
admin.site.register(UserProf)
admin.site.register(Noteclass)
