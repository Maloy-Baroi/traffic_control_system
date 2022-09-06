from django.urls import path
from App_main.views import *

app_name = 'App_main'

urlpatterns = [
    path('', index, name='index'),
    path('case-register/', caseRegister, name='case-register'),
    path('check-driving-license/', checkValidDrivingLicense, name='check-driving-license'),
    path('traffic-sign-book/', trafficSignBook, name='traffic-sign-book'),
    path('traffic-rules-showcase/', trafficRulesShowcase, name='traffic-rules-showcase'),
]
