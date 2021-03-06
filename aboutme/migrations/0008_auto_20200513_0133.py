# Generated by Django 3.0.6 on 2020-05-12 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0007_job_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='me',
            name='address',
            field=models.CharField(default='none', max_length=80),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='me',
            name='email',
            field=models.EmailField(default='none', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='me',
            name='phone_number',
            field=models.CharField(default='example@example.com', max_length=15),
            preserve_default=False,
        ),
    ]
