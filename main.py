import os

import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "notifications_project.settings"
)
django.setup()

from notification.models import (
    UserNotification,
    UserNotificationOption,
    UserNotificationSetting,
)


class NotificationService:
    def __init__(self, notification_id):
        self.notification_id = notification_id

    def _get_user(self):
        try:
            notification = UserNotification.objects.select_related("user").get(
                id=self.notification_id
            )
            return notification.user
        except UserNotification.DoesNotExist:
            return None


    def _get_notification_template_text(self):
        try:
            notification = UserNotification.objects.select_related(
                "notification_template"
            ).get(id=self.notification_id)
            notification_text = notification.notification_template.txt
            return notification_text
        except UserNotification.DoesNotExist:
            return None

    def _get_notification(self):
        try:
            return UserNotification.objects.get(id=self.notification_id)
        except UserNotification.DoesNotExist:
            return None


    def _get_notification_options(self):
        try:
            options = UserNotificationOption.objects.select_related(
                "user_notification"
            ).filter(user_notification=self._get_notification())
            return {option.field_id: option.txt for option in options}
        except UserNotificationOption.DoesNotExist:
            return None

    def _get_notification_settings(self, user):
        try:
            settings_queryset = UserNotificationSetting.objects.filter(
                user=user
            ).select_related("notification_template")
            return settings_queryset
        except UserNotificationSetting.DoesNotExist:
            return None


    def _generate_notification_text(self):
        try:
            template_text = self._get_notification_template_text()
            if template_text:
                options = [""] + list(self._get_notification_options().values())
                if options:
                    return template_text.format(*options)
            return None
        except UserNotification.DoesNotExist:
            return None

    def _should_show_notification(self, user):
        """
        Checks if the notification should be displayed based on user settings.
        """
        notification = self._get_notification()
        if not notification:
            return False

        user_settings = self._get_notification_settings(user)
        if not user_settings:
            return True

        for setting in user_settings:
            if setting.notification_template == notification.notification_template:
                if (
                    notification.notification_type == 1
                    and setting.system_notification == 0
                ):
                    return False
                if (
                    notification.notification_type == 2
                    and setting.push_notification == 0
                ):
                    return False

        return True

    def display_notifications(self):
        user = self._get_user()
        if not user:
            return None

        if self._should_show_notification(user):
            return self._generate_notification_text()
        else:
            return None


if __name__ == "__main__":
    service = NotificationService(
        notification_id=4,
    )
    print(service.display_notifications())
