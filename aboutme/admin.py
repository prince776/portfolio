from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Project)
admin.site.register(models.Skill)
admin.site.register(models.Experience)
admin.site.register(models.Me)
admin.site.register(models.Certificate)
