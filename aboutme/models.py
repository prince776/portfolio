from django.db import models

# Create your models here.


class Skill(models.Model):
    skill_title = models.CharField(max_length=80)
    skill_description = models.TextField()
    skill_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.skill_title


class Project(models.Model):
    project_title = models.CharField(max_length=80)
    project_description = models.TextField()
    project_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.project_title


class Job(models.Model):
    job_title = models.CharField(max_length=80)
    job_description = models.TextField()
    job_priority = models.IntegerField()
    completed = models.BooleanField()

    def __str__(self):
        return self.job_title


class Me(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    about_me_brief = models.CharField(max_length=100)
    about_me = models.TextField()
    active = models.BooleanField()

    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    image = models.ImageField(blank=True, null=True, upload_to='myImages')

    cv = models.FileField(blank=True, null=True, upload_to='myFiles')
    resume = models.FileField(blank=True, null=True, upload_to='myFiles')

    class Meta:
        verbose_name_plural = 'me'

    def __str__(self):
        return self.first_name
