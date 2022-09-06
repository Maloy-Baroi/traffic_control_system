from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from App_driver.models import *
from App_main.forms import *
from App_main.models import *
from App_Login.models import *
from App_traffic.models import *
from App_Login.views import is_traffic_, is_driver_
import datetime


# Create your views here.
@login_required
def index(request):
    if is_traffic_(request.user):
        profile = TrafficOfficerModel.objects.filter(user=request.user)
        if profile.exists():
            traffic = profile[0]
            all_reports = CaseModel.objects.filter(registered_by=traffic)
            total_credits = all_reports.count() * 50
            content = {
                'traffic': traffic,
                'all_reports': all_reports,
            }
            return render(request, 'App_traffic/index.html', context=content)
        else:
            return HttpResponseRedirect(reverse('App_Login:login'))
    else:
        profile = DriverModel.objects.filter(user=request.user)
        driver = profile[0]
        if driver.license_last_validation_date < datetime.date.today():
            driver.validate = False
            driver.save()
        if profile.exists():
            content = {
                'profile': profile[0]
            }
            return render(request, 'App_driver/dashboard.html', context=content)
        else:
            return HttpResponseRedirect(reverse('App_driver:profile-setup'))


def caseRegister(request):
    all_penalty = PenaltyModel.objects.all()
    all_driver = DriverModel.objects.all()
    traffic_police = TrafficOfficerModel.objects.get(user=request.user)
    form = CaseModelForm()
    if request.method == 'POST':
        accused_info = request.POST.get('accused')
        accused = all_driver.get(id=accused_info)
        form = CaseModelForm(request.POST)
        if form.is_valid():
            thisForm = form.save(commit=False)
            thisForm.registered_by = traffic_police
            thisForm.accused = accused
            thisForm.save()
            return HttpResponseRedirect(reverse('App_main:case-register'))
    content = {
        'form': form,
        'all_penalty': all_penalty,
        'all_driver': all_driver,
    }
    return render(request, 'App_main/case_register.html', context=content)


def checkValidDrivingLicense(request):
    all_driver = DriverModel.objects.all()
    content = {
        'all_driver': all_driver
    }
    return render(request, 'App_main/checkDrivingLicense.html', context=content)


def trafficSignBook(request):
    return render(request, 'App_main/rule_book.html')


def trafficRulesShowcase(request):
    all_offences = PenaltyModel.objects.all()
    content = {
        'all_offences': all_offences
    }
    return render(request, 'App_main/traffic_rule.html', context=content)
