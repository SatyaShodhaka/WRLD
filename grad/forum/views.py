from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from forum.forms import PostForm
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login

# Create your views here.
def view_post(request):
    form = PostForm()
    posts = Post.objects.all()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

"""
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,\
                request.FILES,\
                instance=request.user)
        if form.is_valid():
            form.user = request.user
            form.save()
            return redirect('/forum/')
    else:
        form = PostForm(instance=request.user)
    args = {'form': form}
    return render(request,'forum/create.html',args)
"""
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            p = form.save(commit = False)
            p.user = request.user
            p.save()
            return redirect('/forum/')
    else:
        form = PostForm()
        args = {'form':form}
        return render(request,'forum/create.html',args)

def full_post(request):
    return request