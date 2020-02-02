from django.contrib import admin
from django.urls import path
from django.contrib.auth import login
from django.conf import settings
from django.conf.urls import url, include
from views import ResumeSubmit, SearchQuery

urlpatterns = [
    url(r'resume/$', ResumeSubmit.as_view(), name='resume'),
    url(r'search/$', SearchQuery.as_view(), name='search'),
]
