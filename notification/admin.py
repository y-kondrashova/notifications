from django.contrib import admin
from notification import models

admin.site.register(models.NotificationCategory)
admin.site.register(models.NotificationTemplate)
admin.site.register(models.UserNotification)
admin.site.register(models.UserNotificationOption)
admin.site.register(models.UserNotificationSetting)
