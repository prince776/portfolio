# Generated by Django 3.0.6 on 2020-05-12 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_priority',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_priority',
            field=models.IntegerField(default=0),
        ),
    ]
