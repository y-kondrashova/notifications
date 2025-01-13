from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = "language"
