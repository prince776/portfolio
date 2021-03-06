# Generated by Django 3.0.6 on 2020-05-12 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0004_job'),
    ]

    operations = [
        migrations.CreateModel(
            name='Me',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('about_me', models.TextField()),
                ('active', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'me',
            },
        ),
    ]
