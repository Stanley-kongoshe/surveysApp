from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import csv

User = get_user_model()
# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/connectivity/{filename}'.format(filename=filename)

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(primary_key=True,unique=True,default=uuid.uuid4)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    
    # email = models.TextField()
    # id_user = models.IntegerField()
    department = models.TextField(blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name





class ConnectivitySurveyData(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True)
    author = models.CharField(max_length=200,blank=True)
    image0 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(default= datetime.now, blank=True)
    projectName = models.CharField(max_length=100,blank=True)
    sitename = models.CharField(max_length=100,blank=True)
    sitecode = models.CharField(max_length=100,blank=True)
    lit_fibre_pop = models.TextField(blank=True)
    atn_type = models.CharField(max_length=100,blank=True)
    atn_location = models.CharField(max_length=100,blank=True)
    free_atn_electrical_ports = models.CharField(max_length=100,blank=True)
    free_atn_optical_ports = models.CharField(max_length=100,blank=True)
    cable_length = models.TextField(blank=True)
    idu_type = models.TextField(blank=True)
    microwave_location = models.TextField(blank=True)
    free_microwave_electrical_ports = models.CharField(max_length=100,blank=True)
    free_microwave_optical_ports = models.CharField(max_length=100,blank=True)
    microwave_cable_length = models.CharField(max_length=100,blank=True)
    move_atn_or_mw_to_cabinet = models.CharField(max_length=100,blank=True)
    duct_cable_required = models.TextField(blank=True)
    duct_length_required = models.CharField(max_length=100,blank=True)
    comments = models.TextField(blank=True)
    #author = models.TextField(blank=True)

    #Author author;

    def __str__(self):
        return f'{self.sitename }-{self.sitecode}' #note it's not self.user.username bcoz user is not a foreign key
        

