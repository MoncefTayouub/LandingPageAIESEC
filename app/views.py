
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
from .serializable import *
# Create your views here.

@api_view(['GET','POST'])
def Home(request):    
    if request.method == 'POST':
        rq = FQ.objects.create(Question='AIESEC is the best ?',Answer='yes')
        rq.save()
        tb = FQ.objects.all()
        ser = FQserializers(tb, many=True).data
        return Response({'response':'admit','msg sents':request.POST , 'database':ser})

    return Response('you are home')  
    
@api_view(['GET','POST']) 
def SigIn(request):

    if request.method == "POST":
        print(request.POST)
        if (User.objects.filter(username = request.POST.get('email')).count() > 0 ):
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
        if (authenticate(username= request.POST.get('name') , password = request.POST.get('password')) == None ):
            return Response(0)  
        else : 
            return Response(1)


    return Response('')

# @api_view(['GET','POST']):
@api_view(['GET','POST'])
def createMC (request):
    if request.method == 'POST' :
        tuple = (str(request.POST.get('Date')),str(2),str(2))
        print()
        rq  = MC.objects.create()
        rq.name = request.POST.get('name')
        rq.why = request.POST.get('why')
        rq.how = request.POST.get('how')
        rq.what = request.POST.get('what')
        rq.vision = request.POST.get('vision')
        rq.date = '-'.join(tuple) 
        if (request.FILES != {}) :
            rq.picture = request.FILES['picture']
        rq.save()
        
    table = MC.objects.all()
    ser = MCserializers(table , many=True)
    return Response(ser.data)

@api_view(['GET','POST'])
def createMCteamMembers (request):
    if request.method == 'POST' :
        print(request.POST)
        print(request.FILES)
        if (MCTEAM.objects.all().count() == 0 ):
            rq  = MCTEAM.objects.create()
            rq.name = request.POST.get('name')
            rq.whatsapp = request.POST.get('whatsapp')
            rq.insta = request.POST.get('insta')
            rq.linkedin = request.POST.get('linkedin')
            rq.facebook = request.POST.get('facebook')
            if (request.FILES != {}) :
                rq.picture = request.FILES['picture']
            rq.save()
        else :
            idIndex = 0 
            for s in MCTEAM.objects.all() :
                idIndex = s.id
            update = MCTEAM.objects.get(id = idIndex)  
            update.name = request.POST.get('name')
            update.whatsapp = request.POST.get('whatsapp')
            update.insta = request.POST.get('insta')
            update.linkedin = request.POST.get('linkedin')
            update.facebook = request.POST.get('facebook')
            if (request.FILES != {}) :
                update.picture = request.FILES['picture']
            update.save()
    return Response('')