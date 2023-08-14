from rest_framework import serializers
from .models import ConnectivitySurveyData, Profile
from django.contrib.auth.models import User, auth
from drf_extra_fields.fields import Base64ImageField


class ConnectivitySurveyDataSerializer(serializers.ModelSerializer):
    # image0 = Base64ImageField()
    # image1 = Base64ImageField()
    # image2 = Base64ImageField()
    # image3 = Base64ImageField()
    # image4 = Base64ImageField()
    class Meta:
        model=ConnectivitySurveyData
        fields=('image0','image1','image2','image3','image4','projectName','sitename','sitecode','lit_fibre_pop', 'atn_type', 'atn_location', 'free_atn_electrical_ports',
                'free_atn_electrical_ports', 'free_atn_optical_ports', 'cable_length', 'idu_type', 'microwave_location', 
                'microwave_location', 'free_microwave_electrical_ports', 'free_microwave_optical_ports', 'microwave_cable_length',
                'move_atn_or_mw_to_cabinet', 'duct_cable_required', 'duct_length_required', 'comments', 'author',
            
         )
        # def create(self, validated_data):
        #     image0=validated_data.pop('image0')
        #     image1=validated_data.pop('image1')
        #     image2=validated_data.pop('image2')
        #     image3=validated_data.pop('image3')
        #     image4=validated_data.pop('image4')
           
        #     return ConnectivitySurveyData.objects.create(image0=image0,image1=image1,image2=image2,image3=image3,image4=image4)
        
        

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=('name','department', 'email', 'password' )

    

       