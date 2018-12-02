"""videolearn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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

from django.conf.urls import url,include
from django.contrib import admin
from django.urls import path
from video import views
from django.views.static import serve


urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^video/(?P<vid>\d+)/$', views.videoDetail, name='videoDetail'),
    url(r'^history/$', views.viewHistory, name="viewHistory"),
    url(r'^cate/(?P<cateid>\d+)/$', views.videoCate, name='videoCate'),
    url(r'^login/$', views.logIn, name="login"),
    url(r'^register/$', views.register, name="register"),
    url(r'^logout/$', views.logOut, name="logout"),
    url(r'^like/$', views.like, name='like'),
    url(r'^check_code', views.check_code, name='check_code'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }, name='media'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }, name='static'),
    url(r'^admin/', admin.site.urls),

]