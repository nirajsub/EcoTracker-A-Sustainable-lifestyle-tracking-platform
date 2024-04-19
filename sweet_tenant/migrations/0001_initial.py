# Generated by Django 3.2 on 2023-09-30 02:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sweet_shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('sweet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sweet_shared.sweettype')),
            ],
        ),
    ]
