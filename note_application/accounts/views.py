from account.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.generic import TemplateView
from django_messages.admin import User
from .models import Noteclass

from .forms import RegistrationForm,NoteForm


# Create your views here.

def home(request):
    number=[1,2,3,4]
    name="Piyush"
    args={'name':name,'number':number}
    return render(request,'accounts/home.html',args)

def register(request):
    print ("insde_reg")
    if request.method =='POST':
        print ("insde_post")
        form=RegistrationForm(request.POST)

        if form.is_valid():
            print ("insde_ifffffff")
            form.save()
            return redirect('/accounts/profile.html')
        else:

            print (form.errors ,"errrorrr") #display errors

            return render(request, 'accounts/reg_form.html', {'form': form})


    else:
        form=RegistrationForm()
        args={'form':form}

        return render(request,'accounts/reg_form.html',args)


def profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

def notes_view(request):
    # current_user=request.user
    all_user=User.objects.all()



    # for n1 in data_shared:
    #     print (n1.title,"aaaaaaaaaaaaaaa")
    note_data= Noteclass.objects.filter(user=request.user.id)
    shared=Noteclass.objects.filter(shared=True)



    all_notes={"note_data":note_data,"all_user":all_user,"shared":shared}
    # args={'user':request.user}
    return render(request,'accounts/notes.html',all_notes)

def shared_view(request):
    all_user = User.objects.all()

    # for n1 in data_shared:
    #     print (n1.title,"aaaaaaaaaaaaaaa")
    note_data = Noteclass.objects.filter(user=request.user.id)
    shared = Noteclass.objects.filter(shared=True)



    all_notes = {"note_data": note_data, "all_user": all_user, "shared": shared}
    # args={'user':request.user}
    return render(request, 'accounts/shared_notes.html', all_notes)



@login_required
def create_note(request):
    print(request.user.id,"#########################3")
    if request.method =='POST':
        form=NoteForm(request.POST)
        form_cont = form.save(commit=False)
        # set attributes not to the form but to the model instance:
        if form.is_valid():
            # form_cont.user = User.objects.get(id=1)
            form_cont.user = request.user
            print(form_cont.user.id,"iddddd")
            form_cont.save()
            return redirect('/accounts/profile')
        else:

            return redirect('/accounts/profile')


    else:
        note_form=NoteForm()
        args={'note_form':note_form}
        # print('Entered else')

        return render(request,'accounts/profile.html',args)

@login_required
def note_update(request, pk, template_name='accounts/edit.html'):
    if request.user.is_superuser:
        note= get_object_or_404(Noteclass, pk=pk)
    else:
        note= get_object_or_404(Noteclass, pk=pk, user=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():

        form.save()

        return redirect('accounts:note_view')
    return render(request, template_name, {'form':form})



@login_required
def note_delete(request, pk, template_name='accounts/note_confirm_delete.html'):
    if request.user.is_superuser:
        note= get_object_or_404(Noteclass, pk=pk)
    else:
        note= get_object_or_404(Noteclass, pk=pk, user=request.user)
    if request.method=='POST':
        note.delete()
        return redirect('accounts:note_view')
    return render(request, template_name, {'object':note})




