# Generated by Django 3.0.6 on 2020-05-12 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0010_auto_20200513_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='image_front',
            field=models.ImageField(blank=True, null=True, upload_to='myImages'),
        ),
        migrations.AlterField(
            model_name='me',
            name='image_main',
            field=models.ImageField(blank=True, null=True, upload_to='myImages'),
        ),
    ]