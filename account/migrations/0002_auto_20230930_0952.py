# Generated by Django 3.2 on 2023-09-30 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='on_trial',
        ),
        migrations.RemoveField(
            model_name='client',
            name='paid_until',
        ),
    ]