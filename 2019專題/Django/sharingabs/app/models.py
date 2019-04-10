from django.db import models

# Create your models here.
class mission(models.Model):
    Mtitle = models.CharField(max_length=40,null=False,default="no title")
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
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.Mtitle
class userdata(models.Model):
    username = models.CharField(max_length=40,null=False)
    mission = models.CharField(max_length=40,null=False,default="maybe something wrong here")
def __str__(self):
        return self.username
# Mtitle
# Mpost
# Mname
# Mrating
# postime
# count