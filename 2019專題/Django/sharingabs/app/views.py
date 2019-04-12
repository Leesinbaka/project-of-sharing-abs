from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import math

from django.shortcuts import render,redirect
from app.models import mission
#words = ["cat","dog","hello world"]#用來測試
page1 = 1
def firstpage(request,pageindex = None):
    now = datetime.now()
    #haha ={'title':words[1]}
    global page1 # 重新頁面保留page 1
    PageConstraints = 8 # 每頁顯示數
    missions = mission.objects.all().order_by('-id')#FILO First In Last Out
    datasize = len(missions)
    totalpage = math.ceil(datasize/PageConstraints)
#       math.ceil(-45.17) :  -45.0
#       math.ceil(100.12) :  101.0
#       math.ceil(100.72) :  101.0
#       math.ceil(119L) :  119.0
#       math.ceil(math.pi) : 4.0
    if pageindex == None: #無參數首頁
        page1 = 1
        units = mission.objects.order_by('-id')[0:PageConstraints] #0到8顯示 [0:8]顯示0,1,2,3,4,5,6,7
    elif pageindex == '1': #上一頁
        start = (page1-2)*PageConstraints
        if start >= 0:
            units = mission.objects.order_by('-id')[start:(start+PageConstraints)]
            page1 -= 1 
        else:
            units = mission.objects.order_by('-id')[start+8:(start+PageConstraints+8)]
    elif pageindex == '2':#下一頁
        start = page1*PageConstraints
        if start < datasize:
            units = mission.objects.order_by('-id')[start:(start+PageConstraints)]
            page1 +=1
        else:
            units = mission.objects.order_by('-id')[start-8:(start+PageConstraints-8)]
    elif pageindex == '3':
        start = (page1-1)*PageConstraints
        units = mission.objects.order_by('-id')[start:(start+PageConstraints)]
    currentpage = page1
    return render(request,"firstpage.html",locals())

def detail(request,detailid=None):
    id = mission.objects.get(id = detailid)
    title = id.Mtitle
    post = id.Mpost
    name = id.Mname
    postime = id.postime
    rating = id.Mrating
    count = id.count
    id.count += 1
    id.save()
    return render(request,"detail.html",locals())

def post(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            title = request.POST['title']
            post = request.POST['post']
            name = request.user.get_username()
            deadline = request.POST['deadline']
            money = request.POST['money']
            status1 = request.POST.get('status', '') == 'on'
            if status1 == None:
                status1 = False
            else:
                status1 = True
            rating1 = request.POST['rating']
            save = mission.objects.create(Mtitle = title,Mpost = post,Mname = name,deadline=deadline,status=status1,money=money,Mrating=rating1)
            save.save()
            mess ="input succeeded"
            return redirect('/firstpage/')
    else:
        mess ="error"
    return render(request,"post.html",locals())
from django.core.exceptions import PermissionDenied
from django.contrib.auth.admin import UserAdmin
def delpost(request,detailid=None):
    if detailid != None:
        id = mission.objects.get(id = detailid)
        id.delete()
    return redirect("/firstpage/")

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
            return redirect('/firstpage/')
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
                return redirect('/firstpage/')
            else:
                message='nothing here'
        else:
            message='failed'
    return render(request,"login.html",locals())
def logout(request):
    auth.logout(request)
    return redirect('/firstpage/')
from app.models import userdata

def addcase(request,detailid=None):
    name = request.user.get_username()
    caseid = mission.objects.get(id = detailid)
    id = caseid.id
    case = caseid.Mtitle
    sta = caseid.status
    deadline = caseid.deadline
    caseid.numofworker += 1
    caseid.nameofaccept += (name+',')
    caseid.save()
    save = userdata.objects.create(case = case,username = name,casestatus = sta,casetime = deadline,caseid = id)
    save.save()
    return redirect('/firstpage/3')

def case(request):
    n = request.user.get_username()
    data1 = userdata.objects.order_by('username')[:]
    return render(request,'mycase.html',locals())

def mypost(request):
    n = request.user.get_username()
    units = mission.objects.order_by('Mname')[:]
    return render(request,'mypost.html',locals())