from rest_framework import serializers
from .models import AccessSurveyData, Profile, AccessNewSiteSurveyData
from django.contrib.auth.models import User, auth
from drf_extra_fields.fields import Base64ImageField


class AccessSurveyDataSerializer(serializers.ModelSerializer):

    # creator = serializers.ReadOnlyField(source='creator.username')
    # creator_id = serializers.ReadOnlyField(source='creator.id')
    # image = serializers.ImageField(required=False)
    image0 = Base64ImageField()
    image1 = Base64ImageField()
    image2 = Base64ImageField()
    image3 = Base64ImageField()
    image4 = Base64ImageField()
    # image5 = Base64ImageField()

    class Meta:
        model=AccessSurveyData
        fields=('image0','image1','image2', 'image3','image4', 'projectName','sitename','sitecode','longitude','latitude','cabinetLocation',
            'siteType','plinthRequired', 'infrastructureType', 'infrastructureOwner', 'infrastructureHeight',
            'spaceAntennaRequirement', 'lte2600AntennaHeightS1', 'lte2600AntennaHeightS2', 'lte2600AntennaHeightS3',
            'lte2600AntennaHeightS4', 'lte2600AntennaAzimuthS1', 'lte2600AntennaAzimuthS2', 'lte2600AntennaAzimuthS3',
            'lte2600AntennaAzimuthS4',
            'gsm1800AntennaHeightS1', 'gsm1800AntennaHeightS2', 'gsm1800AntennaHeightS3',
            'gsm1800AntennaHeightS4', 'gsm1800AntennaAzimuthS1', 'gsm1800AntennaAzimuthS2', 'gsm1800AntennaAzimuthS3',
            'gsm1800AntennaAzimuthS4',
            'lte1800AntennaHeightS1', 'lte1800AntennaHeightS2', 'lte1800AntennaHeightS3',
            'lte1800AntennaHeightS4', 'lte1800AntennaAzimuthS1', 'lte1800AntennaAzimuthS2', 'lte1800AntennaAzimuthS3',
            'lte1800AntennaAzimuthS4',
            'u2100AntennaHeightS1', 'u2100AntennaHeightS2', 'u2100AntennaHeightS3',
            'u2100AntennaHeightS4', 'u2100AntennaAzimuthS1', 'u2100AntennaAzimuthS2', 'u2100AntennaAzimuthS3',
            'u2100AntennaAzimuthS4',
            'lte2600AntennaHeightS1', 'lte2600AntennaHeightS2', 'lte2600AntennaHeightS3',
            'lte2600AntennaHeightS4', 'lte2600AntennaAzimuthS1', 'lte2600AntennaAzimuthS2', 'lte2600AntennaAzimuthS3',
            'lte2600AntennaAzimuthS4',
            'gsm900AntennaHeightS1', 'gsm900AntennaHeightS2', 'gsm900AntennaHeightS3',
            'gsm900AntennaHeightS4', 'gsm900AntennaAzimuthS1', 'gsm900AntennaAzimuthS2', 'gsm900AntennaAzimuthS3',
            'gsm900AntennaAzimuthS4',
            'groundSpaceComment','author',
            
        
         )
        
        def create(self, validated_data):
            image0=validated_data.pop('image0')
            image1=validated_data.pop('image1')
            image2=validated_data.pop('image2')
            image3=validated_data.pop('image3')
            image4=validated_data.pop('image4')

                       
            # image1=validated_data.pop('image1')
            # image2=validated_data.pop('image2')
            # image3=validated_data.pop('image3')
            # image4=validated_data.pop('image4')
            # image5=validated_data.pop('image5')
            return AccessSurveyData.objects.create(image0=image0,image1=image1,image2=image2, image3=image3, image4=image4)
        
        
class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('name','department', 'email', 'password' )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('username','password','department','email')

class AccessNewSiteSurveyDataSerializer(serializers.ModelSerializer):
    image0 = Base64ImageField()
    image1 = Base64ImageField()
    image2 = Base64ImageField()
    image3 = Base64ImageField()
    image4 = Base64ImageField()
    image5 = Base64ImageField()
    image6 = Base64ImageField()
    image7 = Base64ImageField()
    image8 = Base64ImageField()

    class Meta:
        model=AccessNewSiteSurveyData
        fields=( 'image0','image1','image2','image3','image4','image5','image6','image7','image8','projectName',
    'sitename',
    'sitecode',
    'surveyDate',
    'siteDescription',
    'connectivityRep',
    'saqRep',

    'opt1LocationController',
    'opt1TowerController',
    'opt1ownerName',
    'opt1AccessController',
    'opt1PowerController',
    'opt1LongitudeController',
    'opt1LatitudeController',
    'opt1equipmentComment',

    # Option 2 Fields
    'opt2LocationController',
    'opt2TowerController',
    'opt2ownerName',
    'opt2AccessController',
    'opt2PowerController',
    'opt2LongitudeController',
    'opt2LatitudeController',
    'opt2equipmentComment',


    # // Option 3 Fields
    'opt3LocationController',
    'opt3ownerName',
    'opt3TowerController',
    'opt3AccessController',
    'opt3PowerController',
    'opt3LongitudeController',
    'opt3LatitudeController',
    'opt3equipmentComment',
    'author', )
        
        def create(self, validated_data):
            image0=validated_data.pop('image0')
            image1=validated_data.pop('image1')
            image2=validated_data.pop('image2')
            image3=validated_data.pop('image3')
            image4=validated_data.pop('image4')
            image5=validated_data.pop('image5')
            image6=validated_data.pop('image6')
            image7=validated_data.pop('image7')
            image8=validated_data.pop('image8')
            return AccessSurveyData.objects.create(image0=image0,image1=image1,image2=image2,image3=image3,image4=image4,image5=image5,image6=image6,image7=image7,image8=image8)
        

 

       