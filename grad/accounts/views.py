from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from accounts.forms import RegistrationForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/account/')
    else:
        form = RegistrationForm()
    return render(request,'accounts/reg_form.html',{'form': form})

@login_required
def profile(request):
    args = {'user': request.user}
    return render(request,'accounts/profile.html', args)

@login_required
def edit_profile(request):
    if request.method == "POST":
        form = UserUpdateForm(request.POST,instance=request.user)
        form_user = ProfileUpdateForm(request.POST,\
                                    request.FILES,\
                                    instance = request.user.userprofile)
        if form.is_valid() and form_user.is_valid:
            form.save()
            form_user.save()
            return redirect('/account/')
    else:
        form = UserUpdateForm(instance=request.user)
        form_user = ProfileUpdateForm(instance = request.user.userprofile)
    args = {'form': form,'form_user': form_user}
    return render(request,'accounts/edit_profile.html',args)

@login_required   
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('/account/profile/')
        else:
            return redirect('/account/change-password/')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request,'accounts/change_password.html',args)  

def test_view(request):
    return render(request,'accounts/base.html')