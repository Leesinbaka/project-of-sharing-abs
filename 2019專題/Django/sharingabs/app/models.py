from django.db import models

# Create your models here.
class mission(models.Model):
    Mtitle = models.CharField(max_length=40,null=False)
    Mpost = models.CharField(max_length=400,null=False)
    Mname = models.CharField(max_length=40,null=False,default="anonymous")
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
