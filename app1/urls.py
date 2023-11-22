from app1.views import *
from django.urls import path
app_name='spe'
urlpatterns=[
    path('specific/',specific,name='specific'),
    path('specific2/',specific2,name='specific2'),
    
]