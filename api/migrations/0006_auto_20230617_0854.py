# Generated by Django 3.2 on 2023-06-17 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_subactivitycategory_task_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subactivitycategory',
            name='task_method',
        ),
        migrations.AddField(
            model_name='activitypost',
            name='task_method',
            field=models.CharField(blank=True, choices=[('Had', 'Had'), ('Prepared', 'Prepared')], max_length=20, null=True),
        ),
    ]
