# Generated by Django 5.0.8 on 2024-09-10 09:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_jobposting_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employer',
            name='location',
        ),
    ]
