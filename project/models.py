from django.conf import settings
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=25, blank=True, null=True)
    code = models.CharField(max_length=5, blank=True, null=True)
    code_exp = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "country"


class Project(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="projects"
    )
    name = models.CharField(max_length=510, blank=True, null=True)
    address = models.CharField(max_length=510, blank=True, null=True)
    started = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    country = models.ForeignKey(Country, models.CASCADE, related_name="projects")
    archived = models.IntegerField(default=0)

    class Meta:
        db_table = "project"
