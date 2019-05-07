from django.contrib import admin
from app.models import userdata,mission,comments,usersave
# Register your models here.
admin.site.register(mission)
admin.site.register(userdata)
admin.site.register(comments)
admin.site.register(usersave)
