# Generated by Django 3.2 on 2023-06-17 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20230617_0846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subactivitycategorychoices',
            name='sub_activity_category',
        ),
        migrations.AddField(
            model_name='subactivitycategorychoices',
            name='sub_activity_category',
            field=models.ManyToManyField(to='api.SubActivityCategory'),
        ),
    ]
