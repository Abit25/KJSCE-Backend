"""backend2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls import url, include
from social_auth.views import logout_view, checkLogin, ResumeSubmit

urlpatterns = [
    path("checkLogin/", checkLogin),
    path('admin/', admin.site.urls),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout_view, name='logout'),
    url('', include('social_django.urls', namespace='social')),
<<<<<<< HEAD
    path('demo/', ResumeSubmit.as_view(), name="resume")
=======
>>>>>>> 701ff3b68a6b83eadf1700b4a931f509e8701287
]
