from django.contrib.auth.models import AbstractUser
from django.db import models

from translation.models import Language


class User(AbstractUser):
    role_id = models.ForeignKey(
        "UserRole",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="users",
    )
    active = models.IntegerField(blank=True, null=True)
    verified = models.IntegerField(blank=True, null=True)
    language = models.ForeignKey(
        Language,
        models.CASCADE,
        null=True,
        blank=True,
        related_name="users"
    )

    class Meta:
        db_table = "user"


class UserRole(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "user_role"
