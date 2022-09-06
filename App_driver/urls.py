from django.urls import path
from . import views

app_name = 'App_driver'

urlpatterns = [
    path('profile-setup/', views.profile_setup, name='profile-setup'),
    path('new-cases/', views.newCases, name='new-cases'),
    path('license-and-validation/', views.license_and_validation, name='license-and-validation'),
    path('traffic-rules/', views.traffic_rules, name='traffic-rules'),
    path('license-renew/', views.license_renew, name='license-renew'),
]

