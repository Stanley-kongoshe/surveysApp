# Generated by Django 4.1.1 on 2023-03-15 10:40

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_accesssurveydata_image3'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesssurveydata',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=core.models.upload_to),
        ),
    ]
