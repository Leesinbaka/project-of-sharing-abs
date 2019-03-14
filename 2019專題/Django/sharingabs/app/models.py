from django.db import models

# Create your models here.
class user(models.Model):
    Uname = models.CharField(max_length=30,null=False)
    sex = (("Male","M"),("Female","F"))
    Usex = models.CharField(choices=sex,max_length=7,null=False)
    Uphone = models.CharField(max_length=30,null=False)
    Uaddress = models.CharField(max_length=100,null=False)
    UAcname = models.CharField(max_length=20,null=False) # account name ID
    Uemail = models.EmailField(null=False)
    Ubirthday = models.DateField(null=False)
    def __str__(self):
        return self.UAcname

class company(models.Model):
    Cname = models.CharField(max_length=40,null=False)
    Caddress = models.CharField(max_length=100,null=False)
    Cphone = models.CharField(max_length=30,null=False)
    Cemail = models.EmailField(null=False)
    def __str__(self):
        return self.Cname

class mission(models.Model):
    Mtitle = models.CharField(max_length=40,null=False)
    Mpost = models.CharField(max_length=400,null=False)
    Rating_CHOICES = (
    (1, '希望改善'),
    (2, '一般'),
    (3, '不錯'),
    (4, '非常好'),
    (5, '_(:3'))
    Mrating = models.IntegerField(choices=Rating_CHOICES, default=5)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.Mtitle
