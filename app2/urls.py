from app2.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('karthik/',karthik,name='karthik'),
    path('karthik1/',karthik1,name='karthik1'),
]