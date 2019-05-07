from django.contrib import admin
from app.models import userdata,mission,comments,usersave,ads
# Register your models here.
admin.site.register(mission)
admin.site.register(userdata)
admin.site.register(comments)
admin.site.register(usersave)
admin.site.register(ads)