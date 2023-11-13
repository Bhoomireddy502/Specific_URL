from app3.views import *
from django.urls import path
app_name='no nothing'
urlpatterns=[
    path('raja/',raja,name='raja'),
    path('raja1/',raja1,name='raja1'),
]