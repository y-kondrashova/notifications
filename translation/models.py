from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Language(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "language"


FIELD_CHOICES = [
    (1, "name"),
    (2, "title"),
    (3, "description"),
    (4, "text"),
    (5, "question"),
    (6, "answer"),
    (7, "additional"),
]

class TranslationString(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING)
    object_id = models.IntegerField()
    related_item = GenericForeignKey("content_type", "object_id")
    translation_field_id = models.IntegerField(
        choices=FIELD_CHOICES,
        default=1,
    )
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=255)

    class Meta:
        unique_together = ("content_type", "object_id", "translation_field_id", "language")
        db_table = "translation_string"

