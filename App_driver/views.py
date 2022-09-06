from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from App_driver.forms import *
from App_main.models import *
from App_Login.models import *
from App_traffic.models import *


# Create your views here.
def profile_setup(request):
    profileForm = DriverModelForm()
    if request.method == 'POST':
        profileForm = DriverModelForm(request.POST)
        if profileForm.is_valid():
            thisProfile = profileForm.save(commit=False)
            thisProfile.user = request.user
            thisProfile.save()
            return redirect('App_main:index')
        else:
            return render(request, "profile_setup.html")
    content = {
        'form': profileForm,
    }
    return render(request, "App_driver/profile_setup.html", context=content)


def newCases(request):
    driver = DriverModel.objects.get(user=request.user)
    all_case = CaseModel.objects.filter(accused=driver)
    content = {
        'all_case': all_case
    }
    return render(request, 'App_driver/all_cases.html', context=content)


def license_and_validation(request):
    driver = DriverModel.objects.get(user=request.user)
    content = {
        'driver': driver
    }
    return render(request, 'App_driver/my_license.html', context=content)


def traffic_rules(request):
    all_offences = PenaltyModel.objects.all()
    content = {
        'all_offences': all_offences
    }
    return render(request, 'App_driver/traffic_rules.html', context=content)


def license_renew(request):
    driver = DriverModel.objects.get(user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name')
        sendingNumber = request.POST.get('sending_number')
        uploadedScreenShot = request.FILES.get('screenshot')
        transactionID = request.POST.get('transactionID')
        upload = TransactionModel(name=name, sending_number=sendingNumber, upload_screenshot=uploadedScreenShot,
                                  transaction_id=transactionID)
        upload.user = driver
        upload.save()
        return HttpResponseRedirect(reverse('App_driver:license-renew'))
    return render(request, 'App_driver/license_renew.html')
