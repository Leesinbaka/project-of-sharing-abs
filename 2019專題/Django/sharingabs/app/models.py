from django.db import models

# Create your models here.
class mission(models.Model):
    Mtitle = models.CharField(max_length=40,null=False,default="no title") #connect case
    Mpost = models.CharField(max_length=400,null=False)
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
    money = models.IntegerField(default=0)
    numofworker = models.IntegerField(default=0)
    Mimage = models.ImageField(upload_to='imageformission',default="haha")
    status = models.BooleanField(null=False,default=False) #connect casestatus
    deadline = models.DateField(auto_now=True) #connect casetime
    nameofaccept = models.CharField(max_length=400)
    def __str__(self):
        return self.Mtitle
class userdata(models.Model):
    username = models.CharField(max_length=40,null=False)
    case = models.CharField(max_length=100,null=False,default="maybe something wrong here")
    casestatus = models.BooleanField(default=False)
    casetime = models.DateField(auto_now=True)
    daysremain = models.IntegerField(null=False,default=0)
    caseid = models.IntegerField(default=0)
    image = models.ImageField(upload_to='imageforcase',default="haha")
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
    like = models.IntegerField(null=False,default=0)
    def __str__(self):
        return self.comment
class usersave(models.Model):
    username = models.CharField(max_length=40,null=False,default="no one !! wtf")
    address = models.CharField(max_length=40,null=False)
    position = models.CharField(max_length=40,null=False)
    userimage = models.ImageField(upload_to='imageforuser',default="no image here")
    def __str__(self):
        return self.username