# Generated by Django 4.1.1 on 2023-03-15 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_accesssurveydata_image1'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesssurveydata',
            name='image2',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='accesssurveydata',
            name='image3',
            field=models.TextField(blank=True),
        ),
    ]
