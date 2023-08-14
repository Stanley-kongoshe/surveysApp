from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ConnectivitySurveyDataSerializer,UserDataSerializer
from .models import ConnectivitySurveyData, Profile

# Create your views here.
# @api_view(['GET'])
# def getFood(request):
#     return Response()

@api_view(['POST'])
def postConnectivitySurveyData(request):
    serializer = ConnectivitySurveyDataSerializer(data=request.data)
    print(request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getConnectivitySurveyData(request):
    Connectivitydata = ConnectivitySurveyData.objects.all()
    serializer = ConnectivitySurveyDataSerializer(Connectivitydata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserData(request):
    Userdata = Profile.objects.all()
    serializer = UserDataSerializer(Userdata, many=True)
    return Response(serializer.data)



# Create your views here.
