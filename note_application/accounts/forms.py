from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Noteclass


class RegistrationForm(UserCreationForm):
    email=forms.EmailField(required=True)

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].label = "username_access"
    #     self.fields['first_name'].label = "firstname_access"
    #     self.fields['last_name'].label = "lastname_access"
    #     self.fields['email'].label = "email_access"
    #     self.fields['password1'].label = "password1_access"
    #     self.fields['password2'].label = "password2_access"


    class Meta:
        model= User
        fields =(
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self,commit=True):
        user=super(RegistrationForm,self).save(commit=False)
        user.first_name= self.cleaned_data['first_name']
        user.last_name=self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']



        if commit:
            user.save()

        return user

class NoteForm(forms.ModelForm):



    class Meta:
        model= Noteclass
        fields =(
            'title',
            'note',
            'shared',
            'completed',
        )

    def save(self,commit=True):
        user=super(NoteForm,self).save(commit=False)
        user.title= self.cleaned_data['title']
        user.note=self.cleaned_data['note']


        if commit:
            user.save()

        return user




