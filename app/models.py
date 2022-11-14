from django.db import models
import datetime
# Create your models here.
def upload_path(instance , filename):
    path = '/'.join(['covers',filename])
    # path = 'frontend/src' + path + '.jpg'
    path = ''.join([ path , '.jpg'])
    return path


class LCs(models.Model):
    name = models.TextField()
    vision = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)

class MC(models.Model):
    name = models.TextField()
    why = models.TextField()
    how = models.TextField()
    what = models.TextField()
    vision = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)

class social_media_link (models.Model):
    whatsapp = models.TextField()
    insta = models.TextField()
    linkedin = models.TextField()
    facebook = models.TextField()
    departents = models.TextField() 

class MCTEAM (models.Model):
    name  = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)
    whatsapp = models.TextField()
    insta = models.TextField()
    linkedin = models.TextField()
    facebook = models.TextField() 


class Event (models.Model):
    name  = models.TextField()
    picture = models.ImageField(upload_to=upload_path, blank=True)
    venue_address = models.TextField()
    venue_address_LINK_maps = models.TextField()
    date =  models.DateField(("Date"), default=datetime.date.today)
    registration_link_form = models.TextField()
    time =  models.IntegerField()
    AIESECERS_or_youth = models.BooleanField() # true if for AIESECER 
    link_page =  models.TextField()
    limited_places_OR_nonlimited = models.BooleanField()
    city_name = models.TextField()
    description = models.TextField()

class FQ (models.Model):
    Question = models.TextField()
    Answer = models.TextField()

class Forms (models.Model):
    joinAIESC =  models.TextField()
    beApartner =  models.TextField()
    EP =  models.TextField()  