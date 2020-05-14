from django.db import models

# Create your models here.


class Skill(models.Model):
    skill_title = models.CharField(max_length=80)
    skill_description = models.TextField()
    skill_priority = models.IntegerField(default=0)

    skill_category = models.CharField(max_length=20,
                                      choices=(
                                          ("Programming Language",
                                           "Programming Language"),
                                          ("Tools & Technologies",
                                           "Tools & Technologies"),
                                          ("Other Skills", "Other Skills")
                                      ), default="Other Skills")

    def __str__(self):
        return self.skill_title


class Project(models.Model):
    project_title = models.CharField(max_length=80)
    project_description = models.TextField()
    project_priority = models.IntegerField(default=0)

    def __str__(self):
        return self.project_title


class Experience(models.Model):
    exp_title = models.CharField(max_length=80)
    exp_description = models.TextField()
    exp_priority = models.IntegerField()
    completed = models.BooleanField()

    start_date = models.DateTimeField('Start date')
    end_date = models.DateTimeField('End date', blank=True, null=True)

    def __str__(self):
        return self.exp_title


class Certificate(models.Model):
    certificate_title = models.CharField(max_length=100)
    certificate_priority = models.IntegerField(default=0)

    certificate_issuer = models.CharField(max_length=80)
    certificate_credential_id = models.CharField(max_length=100)
    certificate_credential_url = models.CharField(max_length=150)

    issue_date = models.DateTimeField('Issue date')
    expires = models.BooleanField()
    expiration_date = models.DateTimeField(
        'Expiration Date', blank=True, null=True)

    def __str__(self):
        return self.certificate_title


class Me(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    about_me_brief = models.CharField(max_length=100)
    about_me = models.TextField()
    active = models.BooleanField()

    address = models.CharField(max_length=80)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    link_linkedin = models.CharField(max_length=200, null=True, blank=True)
    link_github = models.CharField(max_length=200, null=True, blank=True)
    link_twitter = models.CharField(max_length=200, null=True, blank=True)
    link_instagram = models.CharField(max_length=200, null=True, blank=True)
    link_facebook = models.CharField(max_length=200, null=True, blank=True)

    image = models.ImageField(blank=True, null=True, upload_to='myImages')

    cv = models.FileField(blank=True, null=True, upload_to='myFiles')
    resume = models.FileField(blank=True, null=True, upload_to='myFiles')

    class Meta:
        verbose_name_plural = 'me'

    def __str__(self):
        return self.first_name
