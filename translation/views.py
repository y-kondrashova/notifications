from django.contrib.contenttypes.models import ContentType
from rest_framework import viewsets

from notification.models import UserNotification
from translation.models import Language, TranslationString
from translation.serializers import (
    LanguageSerializer,
    TranslationStringSerializer,
)


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class TranslationStringViewSet(viewsets.ModelViewSet):
    queryset = TranslationString.objects.all()
    serializer_class = TranslationStringSerializer

    def perform_create(self, serializer):
        content_type = ContentType.objects.get_for_model(UserNotification)

        if "content_type" not in serializer.validated_data:
            serializer.validated_data["content_type"] = content_type

        serializer.save()
