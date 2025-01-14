from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "language"
