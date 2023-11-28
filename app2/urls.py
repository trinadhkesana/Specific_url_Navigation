from django.urls import path
from app2.views import *
app_name='application2'
urlpatterns=[
    path('secondpage/',secondpage,name='secondpage'),
]