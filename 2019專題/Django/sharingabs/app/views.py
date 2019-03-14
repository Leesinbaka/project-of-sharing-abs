from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
def index(request):
    return HttpResponse("Hello")



from django.shortcuts import render,redirect
from app.models import mission
#words = ["cat","dog","hello world"]#用來測試
def firsthtml(request):
    now = datetime.now()
    #haha ={'title':words[1]}
    missions = mission.objects.all()
    return render(request,"firstpage.html",locals())



from app.models import user
def modelstest(request):
    try:
        data = user.objects.get(Uname="李浚謙")#read aa 的資料
        success = "(讀取成功)"
    except:
        errormessage = "(Error)"
    return render(request,"testdata.html",locals())


def post(request):
    if request.method == "POST":
        title = request.POST['title']
        post = request.POST['post']
        save = mission.objects.create(Mtitle = title,Mpost = post)
        save.save()
        mess ="input succeeded"
        return redirect('/firstpage/')
    else:
        mess ="error"
    return render(request,"post.html",locals())
