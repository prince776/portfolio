# Generated by Django 3.0.6 on 2020-05-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutme', '0014_auto_20200514_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='me',
            name='link_facebook',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='link_github',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='link_instagram',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='me',
            name='link_twitter',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]