# Generated by Django 4.1.1 on 2023-02-23 13:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core2', '0006_alter_connectivitysurveydata_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.IntegerField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
