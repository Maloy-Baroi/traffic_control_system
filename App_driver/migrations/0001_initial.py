# Generated by Django 4.0.4 on 2022-08-24 15:14

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DriverModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driving_license', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=16, validators=[django.core.validators.RegexValidator(message='Enter Bangladeshi Number with country code', regex='^\\+?(88)01[3-9][0-9]{8}$')])),
                ('house', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('zipcode', models.PositiveBigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='drivers', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
