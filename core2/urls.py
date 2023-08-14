from django.urls import path
from . import views

urlpatterns = [
    path('getConnectivity/',views.getConnectivitySurveyData),
    path('postConnectivity/',views.postConnectivitySurveyData),
    path('getConnectivityUsers/',views.getUserData),

    # path('<int:id>/generateCSV',views.generateCSV, name='generateCSV'),
]