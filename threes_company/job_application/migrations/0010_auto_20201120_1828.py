# Generated by Django 3.1.2 on 2020-11-20 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('job_application', '0009_auto_20201120_1822'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobapplication',
            old_name='company',
            new_name='submitted_to_company',
        ),
    ]
