from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,HttpResponse,redirect
from forum.forms import PostForm
from .models import Post
# Create your views here.
def view_post(request):
    form = PostForm()
    posts = Post.objects.all()
    args = {'form':form,'posts':posts}
    return render(request,'forum/view.html',args)

@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('/forum/')
    else:
        form = PostForm(instance=request.user)
    args = {'form': form}
    return render(request,'forum/create.html',args)