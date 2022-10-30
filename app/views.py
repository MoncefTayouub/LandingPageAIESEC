from ast import Return
from asyncio import constants
from asyncio.windows_events import NULL
from tkinter.messagebox import RETRY
from turtle import title
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import * 
from rest_framework.response import *
from rest_framework.decorators import api_view
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.renderers import * 
from django.core.files.images import ImageFile
from django.core.mail import *
from django.conf import settings
from django.contrib.auth import authenticate
import random
import string
from django.contrib.auth.models import User
from .forms import *
from asyncio.windows_events import NULL
# Create your views here.

@api_view(['GET','POST'])
def Home(request):    
    return Response('')
    
@api_view(['GET','POST'])
def SigIn(request):

    if request.method == "POST":
        print(request.POST)
        if (User.objects.filter(username = request.POST.get('username')).count() > 0 ):
            return Response(-1)
        else :
            form = RegistrationForm(request.POST)
            if (form.is_valid()):
                form.save()
                return Response(1)
            else : 
                return Response(0)
    
    return Response('')

@api_view(['GET','POST'])
def Login(request):

    if request.method == "POST":
        if ( authenticate(username= request.POST.get('username') , password = request.POST.get('password')) == None ):
            return Response(0)
        else : 
            return Response(1)

    return Response('')

@api_view(['GET','POST'])
def ChangePassword(request):

    if request.method == "POST":
        users = User.objects.get(username = request.POST.get('name') )
        users.set_password(request.POST.get('password'))
        users.save()
        if (authenticate(username= request.POST.get('username') , password = request.POST.get('password')) == None ):
            return Response(0)
        else : 
            return Response(1)


    return Response('')