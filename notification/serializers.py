from rest_framework import serializers

from main import NotificationService
from notification.models import (
    NotificationCategory,
    NotificationTemplate,
    UserNotification,
    UserNotificationOption,
    UserNotificationSetting,
)


class NotificationCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationCategory
        fields = "__all__"


class NotificationTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTemplate
        fields = "__all__"


class UserNotificationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationOption
        fields = "__all__"

class UserNotificationSerializer(serializers.ModelSerializer):
    options = UserNotificationOptionSerializer(many=True, write_only=True)
    notification_text = serializers.SerializerMethodField()

    class Meta:
        model = UserNotification
        fields = ["id", "user", "notification_template", "notification_type",
                  "status", "created", "options", "notification_text"]
        read_only_fields = ["user", "status", "created", "notification_text"]

    def create(self, validated_data):
        options_data = validated_data.pop("options", [])
        user_notification = UserNotification.objects.create(**validated_data)
        for option_data in options_data:
            UserNotificationOption.objects.create(
                user_notification=user_notification,
                **option_data
            )
        return user_notification


    def get_notification_text(self, obj):
        service = NotificationService(notification_id=obj.id)
        return service.display_notifications()


class UserNotificationSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserNotificationSetting
        fields = "__all__"
