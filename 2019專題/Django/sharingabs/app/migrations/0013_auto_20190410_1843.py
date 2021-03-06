# Generated by Django 2.0.5 on 2019-04-10 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20190410_1735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdata',
            old_name='mission',
            new_name='case',
        ),
        migrations.AddField(
            model_name='mission',
            name='deadline',
            field=models.DateField(auto_now=True),
        ),
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
        migrations.AddField(
            model_name='userdata',
            name='casestatus',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userdata',
            name='casetime',
            field=models.DateField(auto_now=True),
        ),
    ]
