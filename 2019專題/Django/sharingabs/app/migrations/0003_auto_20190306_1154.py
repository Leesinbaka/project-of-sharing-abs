# Generated by Django 2.0.5 on 2019-03-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='UAcname',
            field=models.CharField(max_length=20),
        ),
    ]
