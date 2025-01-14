from django.conf import settings
from django.db import models


class NotificationCategory(models.Model):
    name = models.CharField(max_length=32, blank=True, null=True)
    title = models.CharField(max_length=32, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "notification_category"


class NotificationTemplate(models.Model):
    notification_category = models.ForeignKey(
        NotificationCategory,
        models.CASCADE,
        related_name="notification_templates",
    )
    name = models.CharField(max_length=32, blank=True, null=True)
    txt = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "notification_template"


class UserNotification(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        related_name="user_notifications",
    )
    notification_template = models.ForeignKey(
        NotificationTemplate,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="user_notifications",
    )
    notification_type = models.IntegerField()
    status = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user_notification"


class UserNotificationOption(models.Model):
    user_notification = models.ForeignKey(
        UserNotification,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="user_notification_options",
    )
    field_id = models.IntegerField(blank=True, null=True)
    txt = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        db_table = "user_notification_option"


class UserNotificationSetting(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="user_notification_settings",
    )
    notification_template = models.ForeignKey(
        NotificationTemplate,
        models.CASCADE,
        blank=True,
        null=True,
        related_name="user_notification_settings",
    )
    system_notification = models.IntegerField()
    push_notification = models.IntegerField()

    class Meta:
        db_table = 'user_notification_setting'
