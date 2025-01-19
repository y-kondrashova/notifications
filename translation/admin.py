from django.contrib import admin
from translation import models

admin.site.register(models.Language)
admin.site.register(models.TranslationString)
