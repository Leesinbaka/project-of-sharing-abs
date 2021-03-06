"""sharingabs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url #用這個才可以用來接收
from app import views
from django.conf import settings #media 設定要加
from django.conf.urls.static import static #media 設定要加
urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^firstpage/$', views.firstpage),
    url(r'^firstpage/(\d+)/$',views.firstpage),
    url(r'^detail/(\d+)/$',views.detail),
    path('mycase/',views.case),
    path('mypost/',views.mypost),
    url(r'^like/(\d+)/(\d+)/$',views.like),
    url(r'^delcomment/(\d+)/(\d+)/$',views.delcomment),

    path('post/',views.post),
    url(r'^delete/(\d+)/$',views.delpost),

    path('login/',views.login),
    path('register/',views.register),
    path('logout/',views.logout),
    url(r'^addcase/(\d+)/$',views.addcase),
    path('userpage/',views.userpage),
    url(r'^userpage/(\d+)/$',views.userpage),
    path('gamepage/',views.game),
    url(r'^edit/(\d+)/$',views.edit),
    url(r'^edit/(\d+)/(\w+)/$',views.edit),
    url(r'^care/(\w+)/(\d+)/$',views.cares),

    path('ads/',views.postads),
    url(r'^ads/(\w+)/$',views.postads),
    url(r'^adspage/(\d+)/$',views.adspage),
    url(r'^myads/(\w+)/$',views.myads),
    path('admincheck/',views.admincheck),
    url(r'^joinlist/(\d+)/$',views.joinlist),
    path('error/',views.detail),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # we need to add this to make those image visible