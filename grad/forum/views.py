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
    posts = Post.objects.order_by('date').filter(report = (0 or 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10)).reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

    
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

def full_post(request,id):
	post= get_object_or_404(Post, id=id)
	return render(request, 'forum/post.html', {'post':post})


def tech_post(request):
    form = PostForm()
    posts = Post.objects.all().filter(category='Tech',).order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

def news_post(request):
    form = PostForm()
    posts = Post.objects.all().filter(category='News').order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

def music_post(request):
    form = PostForm()
    posts = Post.objects.all().filter(category='Music').order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

def food_post(request):
    form = PostForm()
    posts = Post.objects.all().filter(category='Food').order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

def envi_post(request):
    form = PostForm()
    posts = Post.objects.all().filter(category='Environment').order_by('date').reverse()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

@login_required
def report_post(request):
    if request.method == "POST":
        posts = Post.objects.all().filter(title=request.title)
