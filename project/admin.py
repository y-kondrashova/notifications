from django.contrib import admin

from project import models

admin.site.register(models.Project)
admin.site.register(models.Country)
