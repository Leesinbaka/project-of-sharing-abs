# Generated by Django 2.0.5 on 2019-05-05 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20190505_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mission',
            name='Mvideo',
            field=models.FileField(blank=True, default='haha.png', upload_to='imageformission'),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='image',
            field=models.ImageField(default='haha.png', upload_to='imageforcase'),
        ),
    ]
