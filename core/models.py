from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
import csv

User = get_user_model()

# Create your models here.

# lets us explicitly set upload path and filename
def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Profile(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    # email = models.TextField()
    # id_user = models.IntegerField()
    department = models.TextField(blank=True)
    email = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class AccessSurveyData(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, blank=True)
    # author = models.ForeignKey(Profile, blank=True)
    image0 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image2 = models.TextField(blank=True, null= True)
    image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    report_type = models.CharField(default="Existing Site", editable=False, blank=True,max_length=100,null=True)
    # image2 = models.ImageField(upload_to=upload_to, blank=True)
    # image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    # image5 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(default= datetime.now, blank=True)
    projectName = models.CharField(max_length=100,blank=True)
    sitename = models.CharField(max_length=100,blank=True)
    sitecode = models.CharField(max_length=100,blank=True)
    longitude = models.CharField(max_length=100,blank=True)
    latitude = models.CharField(max_length=100,blank=True)
    cabinetLocation = models.CharField(max_length=100,blank=True)
    siteType = models.CharField(max_length=100,blank=True)
    plinthRequired = models.CharField(max_length=100,blank=True)


    
    # // Infrastructure Information

    infrastructureType = models.TextField(blank=True)
    infrastructureOwner = models.TextField(blank=True)
    infrastructureHeight = models.TextField(blank=True)
    spaceAntennaRequirement = models.TextField(blank=True)


    # // Antenna Information
    # //GSM900

    gsm900AntennaHeightS1 = models.TextField(blank=True)
    gsm900AntennaHeightS2 = models.TextField(blank=True)
    gsm900AntennaHeightS3 = models.TextField(blank=True)
    gsm900AntennaHeightS4 = models.TextField(blank=True)
    gsm900AntennaAzimuthS1 = models.TextField(blank=True)
    gsm900AntennaAzimuthS2 = models.TextField(blank=True)
    gsm900AntennaAzimuthS3 = models.TextField(blank=True)
    gsm900AntennaAzimuthS4 = models.TextField(blank=True)


    # //GSM1800

    gsm1800AntennaHeightS1 = models.TextField(blank=True)
    gsm1800AntennaHeightS2 = models.TextField(blank=True)
    gsm1800AntennaHeightS3 = models.TextField(blank=True)
    gsm1800AntennaHeightS4 = models.TextField(blank=True)
    gsm1800AntennaAzimuthS1 = models.TextField(blank=True)
    gsm1800AntennaAzimuthS2 = models.TextField(blank=True)
    gsm1800AntennaAzimuthS3 = models.TextField(blank=True)
    gsm1800AntennaAzimuthS4 = models.TextField(blank=True)


    # //LTE1800

    lte1800AntennaHeightS1 = models.TextField(blank=True)
    lte1800AntennaHeightS2 = models.TextField(blank=True)
    lte1800AntennaHeightS3 = models.TextField(blank=True)
    lte1800AntennaHeightS4 = models.TextField(blank=True)
    lte1800AntennaAzimuthS1 = models.TextField(blank=True)
    lte1800AntennaAzimuthS2 = models.TextField(blank=True)
    lte1800AntennaAzimuthS3 = models.TextField(blank=True)
    lte1800AntennaAzimuthS4 = models.TextField(blank=True)

    # //U2100

    u2100AntennaHeightS1 = models.TextField(blank=True)
    u2100AntennaHeightS2 = models.TextField(blank=True)
    u2100AntennaHeightS3 = models.TextField(blank=True)
    u2100AntennaHeightS4 = models.TextField(blank=True)
    u2100AntennaAzimuthS1 = models.TextField(blank=True)
    u2100AntennaAzimuthS2 = models.TextField(blank=True)
    u2100AntennaAzimuthS3 = models.TextField(blank=True)
    u2100AntennaAzimuthS4 = models.TextField(blank=True)

    # //lte2600

    lte2600AntennaHeightS1 = models.TextField(blank=True)
    lte2600AntennaHeightS2 = models.TextField(blank=True)
    lte2600AntennaHeightS3 = models.TextField(blank=True)
    lte2600AntennaHeightS4 = models.TextField(blank=True)
    lte2600AntennaAzimuthS1 = models.TextField(blank=True)
    lte2600AntennaAzimuthS2 = models.TextField(blank=True)
    lte2600AntennaAzimuthS3 = models.TextField(blank=True)
    lte2600AntennaAzimuthS4 = models.TextField(blank=True)

    groundSpaceComment = models.TextField(blank=True)
    author = models.CharField(max_length=100,blank=True)
    


    def __str__(self):
        return f'{self.sitename }-{self.sitecode}' #note it's not self.user.username bcoz user is not a foreign key
        

# def generateCSV(request, id):
#     response = HttpResponse(
#         content_type = 'text/csv',
#         headers={'Content-Disposition':'attachment;filename="example.csv"'},
#     )

#     csvv = csv.writer(response)
#     csvv.writerow(['Diana', 'has', 'a', 'police', 'case' ])
#     csvv.writerow(['Let', 'us', 'get', 'her', 'a', 'lawyer'])
#     csvv.writerow(['shall', 'we', 'now'])

#     return response

class AccessNewSiteSurveyData(models.Model):
    projectName = models.CharField(max_length=200,blank=True)
    sitename = models.CharField(max_length=200,blank=True)
    sitecode = models.CharField(max_length=200,blank=True)
    surveyDate = models.CharField(max_length=100,blank=True)
    siteDescription = models.TextField(blank=True)
    connectivityRep = models.CharField(max_length=100,blank=True)
    saqRep = models.CharField(max_length=100,blank=True)
    report_type = models.CharField(default="New Site", editable=False,blank=True,max_length=100,null= True)

    # Option 1 Fields
    opt1LocationController = models.TextField(blank=True)
    opt1TowerController = models.TextField(blank=True)
    opt1ownerName = models.CharField(max_length=100,blank=True)
    opt1AccessController = models.TextField(blank=True)
    opt1PowerController = models.TextField(blank=True)
    opt1LongitudeController = models.TextField(blank=True)
    opt1LatitudeController = models.TextField(blank=True)
    opt1equipmentComment = models.TextField(blank=True)
    image0 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image1 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    # Option 2 Fields
    opt2LocationController = models.TextField(blank=True)
    opt2TowerController = models.TextField(blank=True)
    opt2ownerName = models.TextField(max_length=100,blank=True)
    opt2AccessController = models.TextField(blank=True)
    opt2PowerController = models.TextField(blank=True)
    opt2LongitudeController = models.TextField(blank=True)
    opt2LatitudeController = models.TextField(blank=True)
    opt2equipmentComment = models.TextField(blank=True)
    image3 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image5 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    # // Option 3 Fields
    opt3LocationController = models.TextField(blank=True)
    opt3ownerName = models.CharField(max_length=100,blank=True)
    opt3TowerController = models.TextField(blank=True)
    opt3AccessController = models.TextField(blank=True)
    opt3PowerController = models.TextField(blank=True)
    opt3LongitudeController = models.TextField(blank=True)
    opt3LatitudeController = models.TextField(blank=True)
    opt3equipmentComment = models.TextField(blank=True)
    author = models.TextField(blank=True)
    image6 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image7 = models.ImageField(upload_to=upload_to, blank=True, null=True)
    image8 = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return f'{self.sitename }-{self.sitecode}'
