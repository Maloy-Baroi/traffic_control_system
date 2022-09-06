# Generated by Django 4.0.4 on 2022-08-24 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App_driver', '0001_initial'),
        ('App_main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=50)),
                ('offence_happens_in_place', models.CharField(max_length=200)),
                ('caseType', models.CharField(blank=True, max_length=50)),
                ('occurance_happend_time', models.DateTimeField()),
                ('registered_time', models.DateTimeField(auto_now_add=True)),
                ('accused', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_on_driver', to='App_driver.drivermodel')),
                ('offence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offence_of_driver', to='App_main.penaltymodel')),
            ],
        ),
    ]
