# Generated by Django 4.1.1 on 2023-03-15 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_accesssurveydata_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesssurveydata',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='accesssurveydata',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='accesssurveydata',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='accesssurveydata',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='accesssurveydata',
            name='image5',
        ),
    ]
