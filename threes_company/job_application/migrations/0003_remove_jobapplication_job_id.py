# Generated by Django 3.1.2 on 2020-11-05 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0002_auto_20201105_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job_id',
        ),
    ]