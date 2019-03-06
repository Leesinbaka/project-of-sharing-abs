from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from datetime import datetime
def index(request):
    return HttpResponse("Hello")



from django.shortcuts import render
words = ["cat","dog","hello world"]#用來測試
def firsthtml(request):
    now = datetime.now()
    haha ={'title':words[1]}
    return render(request,"firstpage.html",locals())

from app.models import user
def modelstest(request):
    try:
        data = user.objects.get(Uname="李浚謙")#read aa 的資料
        success = "(讀取成功)"
    except:
        errormessage = "(Error)"
    return render(request,"testdata.html",locals())