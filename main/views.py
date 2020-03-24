from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from .models import blog
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.

def view_details(request,id):
	if not request.user.is_authenticated:
		return render(request,'login.html',{"message":"You need to login first before posting"})
	context = {
		"blog":blog.objects.get(id=id),
		"user":request.user
		}
	return render(request,"view.html",context=context)

def myblogs(request):
	if not request.user.is_authenticated:
    		return render(request,'login.html',{"message":None})
	user = request.user
	
	MyBlogs = blog.objects.filter(author = user)
	context ={
		"user":user,
		"blogs":MyBlogs,
	}
	return render(request,'myblogs.html',context=context)

def register(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse("index"))
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		email = request.POST["email"]
		name = request.POST["fullname"]
		user = User.objects.create_user(username,email,password)
		user.first_name = name
		user.save()
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,"register.html",{"message":"Unable to register"})
	except Exception as e:
		print(e)
		return render(request,"register.html",{"message":None})


def login(request):
	try:
		username = request.POST["username"]
		password = request.POST["password"]
		user = authenticate(request,username=username,password = password)
		if user is not None:
			auth_login(request,user)
			return HttpResponseRedirect(reverse("index"))
		return render(request,"login.html",{"message":"Invalid Credentials"})
	except Exception as e:
		return render(request,"login.html",{"message":None})

def logout(request):
	auth_logout(request)
	return HttpResponseRedirect(reverse("index"))

def post_blog(request):
	if not request.user.is_authenticated:
		return render(request,'login.html',{"message":"You need to login first before posting"})

	try:
		text = request.POST["content"]
		title=request.POST["title"]
		myblog = blog(author=request.user,title=title,text=text,created_date=timezone.now())
		myblog.publish()
		print(myblog)
		return HttpResponseRedirect(reverse("index"))
	except Exception as e:
		print(e)
		return render(request,'post.html')
	


def index(request):
	if not request.user.is_authenticated:
    		return render(request,'login.html',{"message":None})
	user = request.user
	context={
		'blogs':blog.objects.all(), 
		'user':user,
	}
	return render(request,'index.html',context=context)
	