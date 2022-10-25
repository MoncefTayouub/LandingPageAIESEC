from django.urls import path 
from . import views 


urlpatterns = [
     path('log/singin/', views.SigIn ) ,
     path('log/in/', views.Login ) ,
]