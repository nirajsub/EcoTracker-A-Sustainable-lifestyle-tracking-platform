# Generated by Django 3.2 on 2023-06-17 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubActivityChoices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='subactivitycategory',
            name='task_method',
            field=models.CharField(choices=[('Had', 'Had'), ('Prepared', 'Prepared')], default='Employee', max_length=20),
        ),
        migrations.AddField(
            model_name='subactivitycategory',
            name='activity_choices',
            field=models.ManyToManyField(to='api.SubActivityChoices'),
        ),
    ]