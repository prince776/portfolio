# Generated by Django 3.0.6 on 2020-05-12 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0006_me_about_me_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='completed',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
