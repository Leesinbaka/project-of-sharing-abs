# Generated by Django 2.0.5 on 2019-04-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190410_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='money',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mission',
            name='numofworker',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mission',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
