# Generated by Django 2.0.5 on 2019-05-07 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_merge_20190507_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='deadline',
            field=models.DateField(),
        ),
    ]
