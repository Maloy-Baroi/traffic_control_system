# Generated by Django 4.0.4 on 2022-08-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_main', '0005_alter_penaltymodel_penalty_imposed_on_1st_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='casemodel',
            name='cost_of_penalty',
            field=models.IntegerField(default=0),
        ),
    ]
