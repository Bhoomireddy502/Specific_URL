from app1.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('sekhar/',sekhar,name='sekhar'),
    path('sekhar1/',sekhar1,name='sekhar1'),
]