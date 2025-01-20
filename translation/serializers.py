from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from notification.models import UserNotification
from translation.models import Language, TranslationString

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = "__all__"

class TranslationStringSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslationString
        fields = "__all__"
        read_only_fields = ("id", "content_type")

    def create(self, validated_data):
        content_type = ContentType.objects.get_for_model(UserNotification)
        validated_data["content_type"] = content_type
        return super().create(validated_data)
