# Generated by Django 2.1.3 on 2019-02-13 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doll_sites', '0026_auto_20190213_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='actress',
            name='count_album',
            field=models.IntegerField(default=0, max_length=9999),
        ),
    ]
