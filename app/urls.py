from django.urls import path 
from . import views 


urlpatterns = [
     path('', views.Home ) ,
     path('log/singin/', views.SigIn ) ,
     path('log/in/', views.Login ) ,
     path('log/changepassword/', views.ChangePassword ) ,
     path('mc_info/create/', views.createMC ) ,
     path('mc_info/team_members/create/', views.createMCteamMembers ) ,
     path('event/insert/', views.AddEvent ) ,
]