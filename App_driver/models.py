from django.db import models
from django.contrib.auth.models import User
from django.core.validators import *
from django.utils.translation import gettext_lazy as _

# Create your models here.
bangladeshi_mobile_number_regex = RegexValidator(regex=r"^\+?(88)01[3-9][0-9]{8}$",
                                                 message=_('Enter Bangladeshi Number with country code'))


class DriverModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='drivers')
    driving_license = models.CharField(max_length=100)
    license_last_validation_date = models.DateField(blank=True, null=True)
    mobile_number = models.CharField(max_length=16, validators=[bangladeshi_mobile_number_regex])
    house = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    zipcode = models.PositiveBigIntegerField()
    validate = models.BooleanField(default=False)
    Profile_photo = models.ImageField(upload_to='Drivers/profile_picture', default=None, null=True)
    created_date = models.DateField(auto_created=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s-{self.driving_license}"


class TransactionModel(models.Model):
    user = models.ForeignKey(DriverModel, on_delete=models.DO_NOTHING, related_name='transaction_driver')
    name = models.CharField(max_length=100)
    sending_number = models.CharField(max_length=100)
    upload_screenshot = models.ImageField(upload_to='upload_screenshot')
    transaction_id = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} sends driving license money with {self.sending_number}, transaction ID: {self.transaction_id}"
