from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import AccessSurveyDataSerializer, UserDataSerializer, AccessNewSiteSurveyDataSerializer
from .models import AccessSurveyData, Profile, AccessNewSiteSurveyData
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate
from django.contrib import messages
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser
from django.http import HttpResponse
import json
from datetime import date

# class MyModelViewSet(viewsets.ModelViewSet):
#     queryset = AccessSurveyData.objects.order_by('-creation_date')
#     serializer_class = AccessSurveyDataSerializer
#     parser_classes = (MultiPartParser, FormParser)
#     permission_classes = [
#         permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(creator=self.request.user)

# Create your views here.
# @api_view(['GET'])
# def getFood(request):
#     return Response()

@api_view(['POST'])
def postAccessSurveyData(request):
    serializer = AccessSurveyDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def loginUser(request):
    if request.method == 'POST':
        body = (request.body).decode('utf8').replace("'", '"')
        data = json.loads(body)
        print(data)

        username = data["username"]
        password = data['password']
        department = data['department']

        # username = request.POST['username']
        # password = request.POST['password']
        # email = request.POST['email']
        print(username)
        print(password)
        if(department == 'Choose Department.....'):
            return HttpResponse(status=400)
        
        user = authenticate(username=username, password=password)

        if user is not None and password != " ":
            auth.login(request, user)
            return HttpResponse(status=200)
        else:
            #messages.info(request, "Credentials Invalid!")
            return HttpResponse(status=400)

@api_view(['GET'])
def getAccessSurveyData(request):
    Accessdata = AccessSurveyData.objects.all()
    serializer = AccessSurveyDataSerializer(Accessdata, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postAccessNewSiteSurveyData(request):
    serializer = AccessNewSiteSurveyDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    with open('output.txt','w') as f :
        f.write(f'{serializer.data}')
    return Response(serializer.data)


@api_view(['GET'])
def getAccessNewSiteSurveyData(request):
    Accessdata = AccessNewSiteSurveyData.objects.all()
    serializer = AccessNewSiteSurveyDataSerializer(Accessdata, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getUserData(request):
    Userdata = Profile.objects.all()
    serializer = UserDataSerializer(Userdata, many=True)
    return Response(serializer.data)

# excel_app/views.py

from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import openpyxl
import xlwt
from django.http import HttpResponse
import os

# def export_write_xls(request, pk):

#     rows = AccessNewSiteSurveyData.objects.get(id=pk) #.values_list('projectName', 'sitename', 'sitecode', 'surveyDate')

    

#     # EG: path = excel_app/sample.xls
#     path = os.path.dirname(__file__)
#     file = os.path.join(path, 'SAO_For_.xlsx')

#     rb = open_workbook(file, formatting_info=True)
#     r_sheet = rb.sheet_by_index(0)

#     wb = copy(rb)
#     ws = wb.get_sheet(0)

#     row_num = 2 # index start from 0
#     # rows = AccessNewSiteSurveyData.objects.get(id=pk) #.values_list('projectName', 'sitename', 'sitecode', 'surveyDate')
#     # for row in rows:
#     #     row_num += 1
#     #     for col_num in range(len(row)):
#     #         ws.write(row_num, col_num, row[col_num])

#     ws.write(1, 2, rows.sitename)
#     ws.write(3, 2, rows.sitecode)
#     ws.write(3, 5, rows.surveyDate)

#     ws.write(16, 2, rows.opt1LocationController)
#     ws.write(17, 2, rows.sitename)
#     ws.write(18, 2, rows.opt1TowerController)
#     ws.write(19, 2, rows.opt1ownerName)
#     ws.write(20, 2, rows.opt1AccessController)
#     ws.write(21, 2, rows.opt1PowerController)
#     ws.write(22, 2, rows.opt1LongitudeController)
#     ws.write(23, 2, rows.opt1LatitudeController)

#     ws.write(16, 5, rows.opt2LocationController)
#     ws.write(17, 5, rows.sitename)
#     ws.write(18, 5, rows.opt2TowerController)
#     ws.write(19, 5, rows.opt2ownerName)
#     ws.write(20, 5, rows.opt2AccessController)
#     ws.write(21, 5, rows.opt2PowerController)
#     ws.write(22, 5, rows.opt2LongitudeController)
#     ws.write(23, 5, rows.opt2LatitudeController)

#     ws.write(16, 8, rows.opt3LocationController)
#     ws.write(17, 8, rows.sitename)
#     ws.write(18, 8, rows.opt3TowerController)
#     ws.write(19, 8, rows.opt3ownerName)
#     ws.write(20, 8, rows.opt3AccessController)
#     ws.write(21, 8, rows.opt3PowerController)
#     ws.write(22, 8, rows.opt3LongitudeController)
#     ws.write(23, 8, rows.opt3LatitudeController)



    
#     # wb.save(file) # will replace original file
#     # wb.save("SAO_For_" + rows.sitename + rows.sitecode + os.path.splitext(file)[-1]) # will save file where the excel file is
#     response = HttpResponse(content_type='application/ms-excel')
#     filename = "SAO_For_" + rows.sitename + rows.sitecode + os.path.splitext(file)[-1]
#     response['Content-Disposition'] = 'attachment; filename= "{}"'.format(filename)
#     wb.save(response)

#     return response

def write_existing_report(request,pk):
    rows = AccessSurveyData.objects.get(id=pk)
    # EG: get the template for download
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'Modernisation_Report_For_.xlsx')
    # to open theexcel sheet 
    srcfile = openpyxl.load_workbook(file, read_only=False, keep_vba=True)

    #Get the sheet name
    sao_sheet = srcfile.get_sheet_by_name('Report')
    sao_sheet['B10'] = rows.sitename #The site name
    sao_sheet['B11'] = rows.sitecode # The site code
    sao_sheet['B12'] = rows.siteType #Type of the site
    sao_sheet['I10'] = str(f'{rows.latitude}, {rows.longitude}') #Site Coordinates
    sao_sheet['I11'] = rows.cabinetLocation #Site Location Indoor/ Outdoor
    sao_sheet['I12'] = rows.plinthRequired #Plinth requirement
    sao_sheet['B16'] = rows.infrastructureType #Infrastructure Type
    sao_sheet['B17'] = rows.infrastructureOwner #Infrastructure Owner
    sao_sheet['B18'] = rows.infrastructureHeight #Height of the Tower
    sao_sheet['B19'] = rows.spaceAntennaRequirement #Comment on the space of the antennas
    sao_sheet['B24'] = rows.gsm900AntennaHeightS1 #Height of sector 1 Antenna
    sao_sheet['C24'] = rows.gsm900AntennaHeightS2 #Height of sector 2 Antenna
    sao_sheet['D24'] = rows.gsm900AntennaHeightS3 #Height of sector 3 Antenna
    sao_sheet['E24'] = rows.gsm900AntennaHeightS4 #Height of sector 4 Antenna
    sao_sheet['B25'] = rows.gsm900AntennaAzimuthS1 #Azimuth pf Sector 1 Antenna
    sao_sheet['C25'] = rows.gsm900AntennaAzimuthS2 #Azimuth pf Sector 2 Antenna
    sao_sheet['D25'] = rows.gsm900AntennaAzimuthS3 #Azimuth pf Sector 3 Antenna
    sao_sheet['E25'] = rows.gsm900AntennaAzimuthS4 #Azimuth pf Sector 4 Antenna
    #GSM1800
    sao_sheet['B26'] = rows.gsm1800AntennaHeightS1 #Height of sector 1 Antenna
    sao_sheet['C26'] = rows.gsm1800AntennaHeightS2 #Height of sector 2 Antenna
    sao_sheet['D26'] = rows.gsm1800AntennaHeightS3 #Height of sector 3 Antenna
    sao_sheet['E26'] = rows.gsm1800AntennaHeightS4 #Height of sector 4 Antenna
    sao_sheet['B27'] = rows.gsm1800AntennaAzimuthS1 #Azimuth pf Sector 1 Antenna
    sao_sheet['C27'] = rows.gsm1800AntennaAzimuthS2 #Azimuth pf Sector 2 Antenna
    sao_sheet['D27'] = rows.gsm1800AntennaAzimuthS3 #Azimuth pf Sector 3 Antenna
    sao_sheet['E27'] = rows.gsm1800AntennaAzimuthS4 #Azimuth pf Sector 4 Antenna
    #LTE1800
    sao_sheet['B28'] = rows.lte1800AntennaHeightS1 #Height of sector 1 Antenna
    sao_sheet['C28'] = rows.lte1800AntennaHeightS2 #Height of sector 2 Antenna
    sao_sheet['D28'] = rows.lte1800AntennaHeightS3 #Height of sector 3 Antenna
    sao_sheet['E28'] = rows.lte1800AntennaHeightS4 #Height of sector 4 Antenna
    sao_sheet['B29'] = rows.lte1800AntennaAzimuthS1 #Azimuth pf Sector 1 Antenna
    sao_sheet['C29'] = rows.lte1800AntennaAzimuthS2 #Azimuth pf Sector 2 Antenna
    sao_sheet['D29'] = rows.lte1800AntennaAzimuthS3 #Azimuth pf Sector 3 Antenna
    sao_sheet['E29'] = rows.lte1800AntennaAzimuthS4 #Azimuth pf Sector 4 Antenna
    #U2100
    sao_sheet['B30'] = rows.u2100AntennaHeightS1 #Height of sector 1 Antenna
    sao_sheet['C30'] = rows.u2100AntennaHeightS2 #Height of sector 2 Antenna
    sao_sheet['D30'] = rows.u2100AntennaHeightS3 #Height of sector 3 Antenna
    sao_sheet['E30'] = rows.u2100AntennaHeightS4 #Height of sector 4 Antenna
    sao_sheet['B31'] = rows.u2100AntennaAzimuthS1 #Azimuth pf Sector 1 Antenna
    sao_sheet['C31'] = rows.u2100AntennaAzimuthS2 #Azimuth pf Sector 2 Antenna
    sao_sheet['D31'] = rows.u2100AntennaAzimuthS3 #Azimuth pf Sector 3 Antenna
    sao_sheet['E31'] = rows.u2100AntennaAzimuthS4 #Azimuth pf Sector 4 Antenna
    #L2600
    sao_sheet['B36'] = rows.lte2600AntennaHeightS1 #Height of sector 1 Antenna
    sao_sheet['C36'] = rows.lte2600AntennaHeightS2 #Height of sector 2 Antenna
    sao_sheet['D36'] = rows.lte2600AntennaHeightS3 #Height of sector 3 Antenna
    sao_sheet['B37'] = rows.lte2600AntennaAzimuthS1 #Azimuth pf Sector 1 Antenna
    sao_sheet['C37'] = rows.lte2600AntennaAzimuthS2 #Azimuth pf Sector 2 Antenna
    sao_sheet['D37'] = rows.lte2600AntennaAzimuthS3 #Azimuth pf Sector 3 Antenna

    sao_sheet['A43'] = rows.groundSpaceComment #Comment on the ground space 
    #Save the file and provide response for the user
    response = HttpResponse(content_type='application/ms-excel')
    filename = "Modernisation_Report_For_" + rows.sitename + f'({rows.sitecode})' + '.xlsm'# os.path.splitext(file)[-1]
    print(filename)
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format(filename)
    srcfile.save(response)
    return response

    



def write_report(request, pk):
    rows = AccessNewSiteSurveyData.objects.get(id=pk)
    # EG: get the template for download
    path = os.path.dirname(__file__)
    file = os.path.join(path, 'SAO_For_.xlsx')
    # to open theexcel sheet 
    srcfile = openpyxl.load_workbook(file, read_only=False, keep_vba=True)

    #get the sheetname from the file
    sao_sheet = srcfile.get_sheet_by_name('SAO')
    sao_sheet['C2'] = rows.sitename #sitename
    sao_sheet['F2'] = str(date.today())
    sao_sheet['C18'] = rows.sitename #Site Identity Name
    sao_sheet['F18'] = rows.sitename #Site Identity Name
    sao_sheet['I18'] = rows.sitename #Site Identity Name
    sao_sheet['D17'] = rows.sitename #Site Identity Name
    sao_sheet['G17'] = rows.sitename #Site Identity Name
    sao_sheet['A17'] = rows.sitename #Site Identity Name
    sao_sheet['C14'] = rows.sitename #Site Identity Name
    sao_sheet['C4'] = rows.sitecode #sitecode
    sao_sheet['F4'] = rows.surveyDate #Survey Date
    sao_sheet['C17'] = rows.opt1LocationController #Option 1 location name
    sao_sheet['F17'] = rows.opt2LocationController #Option 2 location name
    sao_sheet['I17'] = rows.opt3LocationController #Option 3 location name
    sao_sheet['C19'] = rows.opt1TowerController #Tower Details
    sao_sheet['F19'] = rows.opt2TowerController #Tower Details
    sao_sheet['I19'] = rows.opt3TowerController #Tower Details
    sao_sheet['C20'] = rows.opt1ownerName #Option 1 Owner
    sao_sheet['F20'] = rows.opt2ownerName #Option 2 Owner
    sao_sheet['I20'] = rows.opt3ownerName #Option 3 Owner
    sao_sheet['C21'] = rows.opt1AccessController #Option 1 Access Controller
    sao_sheet['F21'] = rows.opt2AccessController #Option 2 Access Controller
    sao_sheet['I21'] = rows.opt3AccessController #Option 3 Access Controller
    sao_sheet['C22'] = rows.opt1PowerController #Option 1 Power Controller
    sao_sheet['F22'] = rows.opt2PowerController #Option 2 Power Controller
    sao_sheet['I22'] = rows.opt3PowerController #Option 3 Power Controller
    sao_sheet['C23'] = str(f'{rows.opt1LatitudeController}, {rows.opt1LongitudeController}') #Option 1 Coordinates
    sao_sheet['F23'] = str(f'{rows.opt2LatitudeController}, {rows.opt2LongitudeController}') #Option 2 Coordinates
    sao_sheet['I23'] = str(f'{rows.opt3LatitudeController}, {rows.opt3LongitudeController}') #Option 3 Coordinates
    sao_sheet['C28'] = rows.siteDescription #Site Description
    sao_sheet['F28'] = rows.siteDescription #Site Description
    sao_sheet['I28'] = rows.siteDescription #Site Description
    sao_sheet['C29'] = rows.opt1equipmentComment #Eqipment Description
    sao_sheet['F29'] = rows.opt1equipmentComment #Equipment Description
    sao_sheet['I29'] = rows.opt1equipmentComment #Equipment Description
    sao_sheet['B37'] = rows.connectivityRep #Name of Connectivity Rep
    sao_sheet['B40'] = rows.connectivityRep #Name of Site Aquisition Rep

    #Customize the response to give to the User
    response = HttpResponse(content_type='application/ms-excel')
    filename = "SAO_For_" + rows.sitename + f'({rows.sitecode})' + '.xlsm'# os.path.splitext(file)[-1]
    print(filename)
    response['Content-Disposition'] = 'attachment; filename= "{}"'.format(filename)
    srcfile.save(response)
    return response


def Surveys(request):
    
    AccessNewsiteData = AccessNewSiteSurveyData.objects.all()
    AccessExistingData = AccessSurveyData.objects.all()
    

    AuthorSurveys = []

    for i in AccessNewsiteData:

        current_user = request.user
        if i.author == current_user.username:
            AuthorSurveys.append(i)

        else:
            pass
    for i2 in AccessExistingData:

        current_user = request.user
        if i2.author == current_user.username:
            AuthorSurveys.append(i2)

        else:
            pass

    

    print(AuthorSurveys)
    print(request.user)
    name = str(request.user).split('.')
    
    
    
    context = {
        'AccessNewsiteData': AccessNewsiteData,
        'AuthorSurveys': AuthorSurveys,
        'Firstname':name[0],
        'Lastname':name[1]
    }

    return render(request, 'surveyreports.html', context)



# @api_view(['POST'])
# def signup(request):

#     serializer = UserDataSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



    # if request.method == 'POST':
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     password2 = request.POST['password2']

        # if password == password2:
        #     if User.objects.filter(email=email).exists():
        #         messages.info(request, 'Email Taken')
        #         return redirect('signup')

        #     elif User.objects.filter(username=username).exists():
        #         messages.info(request, 'Username Taken')
        #         return redirect('signup')

        #     else:
        #         user = User.objects.create_user(username=username, email=email, password=password)
        #         user.save()

        #         #log user in and redirect to settings page
        #         # user_login = auth.authenticate(username=email, password=password)
        #         # auth.login(request, user_login)



        #         #create a profile object for the new user
        #         user_model = User.objects.get(username=username)
        #         new_profile = Profile.objects.create(user = user_model, id_user =user_model.id, department = 'Access Syatems')
        #         new_profile.save()
        #         # return redirect('settings')
        # else:
        #     messages.info(request, 'Password Not Matching')
        #     # return redirect()  #'signup'

        
    # else:

    #     return render() #request, "signup.html"

    # return render(request, "signup.html")



def signin(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # username = request.POST['username']
        # password = request.POST['password']
        # email = request.POST['email']
        print(username)
        print(password)

        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('surveys')
        else:
            messages.info(request, "Credentials Invalid!")
            return redirect('signin') 
    else:
        return render(request, 'signin.html') 
    
# @login_required(login_url='signin')
def logout(request):
    auth.logout(request)
    return redirect('signin')



# Create your views here.
