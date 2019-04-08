from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime


from django.shortcuts import render,redirect
from app.models import mission
#words = ["cat","dog","hello world"]#用來測試
def firstpage(request):
    now = datetime.now()
    #haha ={'title':words[1]}
    missions = mission.objects.all()
    return render(request,"firstpage.html",locals())

def post(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST['title']
            post = request.POST['post']
            name = request.user.get_username()
            save = mission.objects.create(Mtitle = title,Mpost = post,Mname = name)
            save.save()
            mess ="input succeeded"
            return redirect('/')
    else:
        mess ="error"
    return render(request,"post.html",locals())
# login , register , logout 的打法
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request,"register.html",locals())
def login(request):
    if request.method =='POST':
        name = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                message='sucess'
                return redirect('/')
            else:
                message='nothing here'
        else:
            message='failed'
    return render(request,"login.html",locals())
def logout(request):
    auth.logout(request)
    return redirect('/')

