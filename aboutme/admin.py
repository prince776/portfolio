from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Project)
admin.site.register(models.Skill)
admin.site.register(models.Job)
admin.site.register(models.Me)
