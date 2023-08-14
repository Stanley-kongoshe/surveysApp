from django.contrib import admin
from .models import AccessSurveyData, Profile, AccessNewSiteSurveyData

# Register your models here.

admin.site.register(AccessSurveyData)
admin.site.register(Profile)
admin.site.register(AccessNewSiteSurveyData)

