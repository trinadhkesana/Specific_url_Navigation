from django.urls import path
from app1.views import *
app_name='application1'
urlpatterns=[
    path('firstpage/',firstpage,name='firstpage'),
]