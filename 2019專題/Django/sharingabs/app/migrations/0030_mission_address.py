# Generated by Django 2.0.5 on 2019-05-03 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_merge_20190503_1807'),
    ]

    operations = [
        migrations.AddField(
            model_name='mission',
            name='address',
            field=models.CharField(default='some error here', max_length=100),
        ),
    ]
