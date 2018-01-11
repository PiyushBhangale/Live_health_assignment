from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# Create your models here.
from django.dispatch import receiver


class UserProf(models.Model):
    user=models.OneToOneField(User)
    title=models.TextField(max_length=100,default=None )
    note=models.TextField(max_length=1000,default=None)

class Noteclass(models.Model):
    user = models.ForeignKey(User)
    completed=models.BooleanField(default=False)
    shared=models.BooleanField(default=False)
    title=models.TextField(max_length=100,default=None )
    note=models.TextField(max_length=1000,default=None)

# class Sharednotes(models.Model):
#     shared_to=models.ForeignKey(User,related_name='shared_to')
#     shared_by=models.ForeignKey(User,related_name='shared_by')
#     note_id=models.ForeignKey(Noteclass)




# def create_profile(sender,**kwargs):
#     if kwargs['created']:
#         user_profile=UserProf.object.create(user= kwargs['instance'])
#
# post_save.connect(create_profile, sender=User)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProf.objects.create(user=instance)




