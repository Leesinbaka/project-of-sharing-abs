from django.db import models
# Create your models here.
class mission(models.Model):
    Mtitle = models.CharField(max_length=40,null=False,default="no title") #connect case
    Mpost = models.TextField(max_length=400,null=False)
    Mname = models.CharField(max_length=40,null=False,default="anonymous")
    Rating_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'))
    Mrating = models.IntegerField(choices=Rating_CHOICES, default=5)
    postime = models.DateField(auto_now=True)
    count = models.IntegerField(default=0)
    company = models.CharField(max_length=40,null=False,default="company")
    money = models.CharField(max_length=400,null=False)
    numofworker = models.IntegerField(default=0)
    Mimage = models.ImageField(upload_to='imageformission',default="/image/haha.png")
    Mvideo = models.FileField(upload_to='imageformission',default="/image/haha.png",blank=True)
    status = models.CharField(max_length=20,null=False,default="可") #connect casestatus
    deadline = models.DateField() #connect casetime
    nameofaccept = models.CharField(max_length=400)
    address = models.CharField(max_length=100,default="some error here")
    def __str__(self):
        return self.Mtitle
class userdata(models.Model):
    username = models.CharField(max_length=40,null=False)
    case = models.CharField(max_length=100,null=False,default="maybe something wrong here")
    casestatus = models.CharField(max_length=20,default=False)
    casetime = models.DateField(auto_now=True)
    daysremain = models.IntegerField(null=False,default=0)
    caseid = models.IntegerField(default=0)
    def __str__(self):
        return self.username
# Mtitle
# Mpost
# Mname
# Mrating
# postime
# count
class comments(models.Model):
    caseid = models.IntegerField(null=False)
    usericon = models.CharField(max_length=400,null=False,default='something worng here')
    comment = models.CharField(max_length=100)
    user = models.CharField(max_length=40,null=False)
    uid = models.IntegerField(null=False,default=1)
    like = models.IntegerField(null=False,default=0)
    def __str__(self):
        return self.comment
class usersave(models.Model):
    username = models.CharField(max_length=40,null=False,default="no one !! wtf")
    address = models.CharField(max_length=40,null=False)
    position = models.CharField(max_length=40,null=False)
    userimage = models.ImageField(upload_to='imageforuser',default="no image here")
    userstatus = models.CharField(max_length=20,null=False,default="普通用戶")
    money = models.FloatField(default=0)
    def __str__(self):
        return self.username

class ads(models.Model):
    username = models.CharField(max_length=40,null=False,default="some error here")
    title = models.CharField(max_length=40,null=False,default="some error here")
    content = models.CharField(max_length=400,null=False,default="some error here")
    clickrate = models.IntegerField(default=0)
    image = models.ImageField(upload_to="imageforads",default="no image here")
    def __str__(self):
        return self.username

class care(models.Model):
    username = models.CharField(max_length=40,null=False,default="some error here")
    carenum = models.IntegerField(default=0)
    carename = models.CharField(max_length=40,null=False,default="some error here")
    careid = models.IntegerField(null=False,default=1)
    carebyid = models.IntegerField(null=False,default=1)
    def __str__(self):
        return self.username