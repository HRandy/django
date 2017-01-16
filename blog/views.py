from django.utils import timezone
from .models import Post
from .forms import PostForm
from django import forms
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
me = User.objects.get(username='iii')


post_form = PostForm()



# Create your views here.


def post_list(request):
	
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	
	return render(request,'blog/post_list.html',{'posts':posts,'post_form':post_form})
	
def add_record(request):
	if request.POST:
		title = request.POST['title'].encode('utf-8')
		text = request.POST['text'].encode('utf-8')
		newpost = Post.objects.create(author = me, title = title, text = text)
	return redirect('/blog')
	
	
def post_record(request,id):
	post = Post.objects.get(id = id)
	return render(request, 'blog/post_record.html',locals())
	
	
	