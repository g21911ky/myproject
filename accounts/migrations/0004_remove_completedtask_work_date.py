# Generated by Django 4.2.16 on 2024-12-01 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_completedtask_work_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtask',
            name='work_date',
        ),
    ]
