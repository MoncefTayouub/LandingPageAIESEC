
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
from .Manipulation import *
# Create your views here.

@api_view(['GET','POST'])
def Home(request):    
    
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
    
        index =  request.POST.get('parent')

        rqup = MCTEAM.objects.create()
        rqup.name = request.POST.get('name')
        rqup.mcParent = MC.objects.get(id=index)
        rqup.gmail = request.POST.get('whatsapp')
        rqup.insta = request.POST.get('insta')
        rqup.twiter = request.POST.get('linkedin')
        rqup.facebook = request.POST.get('facebook')
        rqup.deparment = request.POST.get('deparment')
        if (request.FILES != {}) :
            rqup.picture = request.FILES['picture']
        rqup.save()
        return Response(1) 
    
    tb = MCTEAM.objects.all()
   
    return Response(MCTEAMser(tb,many=True).data)


@api_view(['GET','POST'])
def AddEvent (request):
    if request.method == 'POST' :
        print(request.POST)
        print(str_bool(request.POST.get('AIESECER')))
        print(str_bool(request.POST.get('eventlimited_places_OR_nonlimited')))
        tm = Event.objects.create()

        tm.name = request.POST.get('name') 
        tm.picture = request.POST.get('eventPic')
        tm.venue_address = request.POST.get('address')

        tm.venue_address_LINK_maps = request.POST.get('maps')
        tm.date = FixdateForma(request.POST.get('date'))
        tm.registration_link_form = request.POST.get('form')
        
        tm.time = float(request.POST.get('time'))
        tm.AIESECERS_or_youth = str_bool(request.POST.get('AIESECER'))
        tm.link_page = request.POST.get('link_page')

        tm.limited_places_OR_nonlimited = str_bool(request.POST.get('eventlimited_places_OR_nonlimited'))
        tm.city_name = request.POST.get('event_city_name')
        tm.description = request.POST.get('event_description')
        tm.save()  
        return Response(1)
    if request.method == 'GET':
        TB = Event.objects.all()
        return Response(Eventserializers(TB,many=True).data)
    return Response('') 

# @api_view(['GET','POST'])
# def AddFQ (request):
#     if request.method == 'POST' :
#         tl = FQ.objects.create()
#         tl.Question = request.POST.get('question')
#         tl.Answer = request.POST.get('Answer')
#         tl.save()   
    
#     if request.method == 'GET' :
#         sr = FQ.objects.all()
#         return Response(FQserializers(sr,many=True).data)
#     return Response('')

@api_view(['GET','POST'])
def AddFQ (request):
    if request.method == 'POST' :
        tl = FQ.objects.create()
        tl.Question = request.POST.get('question')
        tl.Answer = request.POST.get('Answer')
        tl.save()   
    
    if request.method == 'GET' :
        sr = FQ.objects.all()
        return Response(FQserializers(sr,many=True).data)
    return Response('')

@api_view(['GET','POST'])
def AddForms (request):
    if request.method == 'POST' :
        print(request.POST)
        tl = Forms.objects.create()
        tl.joinAIESC = request.POST.get('joinAIESC')
        tl.beApartner = request.POST.get('beApartner')
        tl.EP = request.POST.get('EP')
        tl.save()   
    
    if request.method == 'GET' :
        sr = Forms.objects.all()
        return Response(FormsSerializers(sr,many=True).data)
    return Response('')

@api_view(['GET','POST'])
def createLCembers (request):
    if request.method == 'POST' :
        print(request.POST)
        tl = LCs.objects.create()
        tl.name = request.POST.get('name')
        tl.vision = request.POST.get('vision')
        if (request.FILES != {}) :
            tl.picture = request.FILES['picture']
        tl.save()  
    else : 
        r = LCs.objects.all()
        return Response(LCser(r,many=True).data)

@api_view(['GET','POST'])
def createLCteamMembers (request):
    if request.method == 'POST' :
        print(request.POST)
        tl = LCMembers.objects.create()
        tl.name = request.POST.get('name')
        tl.department = request.POST.get('department')
        tl.role = request.POST.get('role')
        tl.parent = request.POST.get('index')
        tl.save()  
    else : 
        m = LCMembers.objects.all()
        return Response(LCTEAMser(m , many=True).data)
    return Response(1)