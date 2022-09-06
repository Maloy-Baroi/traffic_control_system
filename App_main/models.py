from django.db import models
from App_driver.models import *
from App_traffic.models import *


# Create your models here.
class PenaltyModel(models.Model):
    in_section = models.CharField(max_length=50)
    description = models.TextField()
    penalty_imposed_on_1st_time = models.CharField(max_length=250)
    penalty_imposed_on_2nd_time = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return f"{self.in_section}-{self.description}-(প্রথমবার ধার্যকৃতঃ{self.penalty_imposed_on_1st_time})-(২য়বার ধার্যকৃতঃ {self.penalty_imposed_on_2nd_time})"


class CaseModel(models.Model):
    registered_by = models.ForeignKey(TrafficOfficerModel, on_delete=models.CASCADE, related_name='case_registered_by')
    accused = models.ForeignKey(DriverModel, on_delete=models.CASCADE, related_name='case_on_driver')
    vehicle_number = models.CharField(max_length=50, blank=False)
    offence = models.ForeignKey(PenaltyModel, on_delete=models.CASCADE, related_name='offence_of_driver')
    offence_happens_in_place = models.CharField(max_length=200)
    cost_of_penalty = models.IntegerField(default=0)
    caseType = models.CharField(max_length=50, blank=True)
    occurrence_happened_time = models.DateTimeField()
    registered_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"A Case registerd on {self.registered_time} for {self.accused}"
