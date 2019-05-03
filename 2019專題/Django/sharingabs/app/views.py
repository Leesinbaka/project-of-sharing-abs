from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
import math
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from app.models import mission,comments
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
    comment = comments.objects.order_by('-id')
    title = id.Mtitle
    post = id.Mpost
    name = id.Mname
    postime = id.postime
    rating = id.Mrating
    numofworker = id.numofworker
    workername = id.nameofaccept
    status = id.status
    img = id.Mimage.url
    count = id.count
    money = id.money
    id.count += 1
    id.save()
    if request.method == "POST":
        c = comments()
        c.user = request.user.get_username()
        u = usersave.objects.get(username = c.user)
        c.uid = u.id
        userimg = u.userimage.url
        c.caseid = detailid
        c.usericon = userimg
        c.comment = request.POST.get('comment')
        c.like = 0
        c.save()
    return render(request,"detail.html",locals())

def post(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            m = mission()
            m.Mtitle = request.POST.get('title')
            m.Mpost = request.POST.get('post')
            m.Mname = request.user.get_username()
            m.deadline = request.POST.get('deadline')
            m.money = request.POST.get('money')
            m.Mimage = request.FILES['picture']#image here
            status1 = request.POST.get('status', '') == 'on'
            if status1 == None:
                status1 = False
            else:
                status1 = True
            m.status = status1
            m.Mrating = request.POST['rating']
            m.save()
            mess ="input succeeded"
            return redirect('/firstpage/')
    else:
        mess =""
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
from app.models import usersave
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            u = usersave()
            u.username = request.POST.get('name')
            u.address = request.POST.get('address')
            u.position = request.POST.get('position')
            u.userimage = request.FILES['pic']
            u.save()
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
from django.contrib import messages
def addcase(request,detailid=None):
    name = request.user.get_username()
    caseid = mission.objects.get(id = detailid)
    id = caseid.id
    case = caseid.Mtitle
    sta = caseid.status
    deadline = caseid.deadline
    caseid.numofworker += 1
    caseid.nameofaccept += (name+' ')
    caseid.save()
    save = userdata.objects.create(case = case,username = name,casestatus = sta,casetime = deadline,caseid = id)
    save.save()
    messages.success(request,"新增了新的任務")
    return redirect('/firstpage/3')

def case(request):
    n = request.user.get_username()
    now = datetime.now()
    data1 = userdata.objects.order_by('username')[:]
    return render(request,'mycase.html',locals())

def mypost(request):
    n = request.user.get_username()
    units = mission.objects.order_by('Mname')[:]
    return render(request,'mypost.html',locals())

def userpage(request,userid=None):
    if userid == None:
        n = request.user.get_username()
        u = usersave.objects.get(username = n)
        name = u.username
        pos = u.position
        add = u.address
        pic = u.userimage.url
    else:
        uid = userid
        u = usersave.objects.get(id = userid)
        name = u.username
        pos = u.position
        add = u.address
        pic = u.userimage.url
    return render(request,'userpage.html',locals())

def like(request,commentid=None,detailid=None):
    if commentid != None:
        c = comments.objects.get(id = commentid)
        c.like += 1
        c.save()
    return redirect("/detail/"+detailid)

def edit(request,detailid = None,mode=None):
    e = mission.objects.get(id = detailid)
    if mode == 'edit':
        e = mission.objects.get(id = detailid)
        title = request.POST['title']
        post = request.POST['post']
        name = request.user.get_username()
        dline = request.POST['deadline']
        money = request.POST['money']
        image = request.FILES['picture']#image here
        rating = request.POST['rating']
        status1 = request.POST.get('status', '') == 'on'
        e.Mtitle = title
        e.Mpost = post
        e.Mname = name
        e.deadline = dline 
        e.money = money
        e.Mimage = image
        if status1 == None:
            status1 = False
        else:
            status1 = True
        e.status = status1
        e.Mrating = rating
        e.save()
        return redirect('/detail/'+detailid)
    else:
        e = mission.objects.get(id = detailid)
    return render(request,"edit.html",locals())