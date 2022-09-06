from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TrafficOfficerModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="traffic")
    fullname = models.CharField(max_length=200)
    designation = models.CharField(max_length=50)
    employee_id = models.IntegerField()
    thana = models.CharField(max_length=50)
    duty_place = models.CharField(max_length=50)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to='traffic_officer/profile_picture/', blank=True)
    joining_date = models.DateTimeField(auto_now_add=True)
