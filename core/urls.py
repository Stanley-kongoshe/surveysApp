from django.urls import path
from . import views

urlpatterns = [
    path('getAccess/',views.getAccessSurveyData),
    path('postAccess/',views.postAccessSurveyData),
    path('getAccessNewSite/',views.getAccessNewSiteSurveyData),
    path('getAccessNewSitereport/<int:pk>/',views.write_report, name='download-report'),
    path('getAccessExistingSitereport/<int:pk>/',views.write_existing_report, name='download-existing-report'),
    path('Surveys/', views.Surveys, name="surveys"),
    path('postAccessNewSite/',views.postAccessNewSiteSurveyData),
    path('getAccessUsers/',views.getUserData),
    # path('<int:id>/generateCSV',views.generateCSV, name='generateCSV'),
    path('appSignin',views.loginUser),
    path('signin', views.signin, name="signin"),
    path('logout', views.logout, name="logout"),

]