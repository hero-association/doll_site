# Generated by Django 2.1.3 on 2019-01-29 19:27

from django.db import migrations, models
import doll_sites.models


class Migration(migrations.Migration):

    dependencies = [
        ('doll_sites', '0021_auto_20190130_0325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidebanner',
            name='banner_pic',
            field=models.ImageField(upload_to=doll_sites.models.banner_upload_location),
        ),
    ]
