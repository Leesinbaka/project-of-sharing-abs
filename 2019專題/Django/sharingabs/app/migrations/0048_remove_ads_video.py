# Generated by Django 2.0.5 on 2019-05-24 07:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_mission_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ads',
            name='video',
        ),
    ]
