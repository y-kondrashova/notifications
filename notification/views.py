from django_filters import rest_framework as filters
from rest_framework import viewsets, status
from rest_framework.response import Response

from main import NotificationService
from notification import models, serializers


class NotificationCategoryViewSet(viewsets.ModelViewSet):
    queryset = models.NotificationCategory.objects.all()
    serializer_class = serializers.NotificationCategorySerializer


class NotificationTemplateViewSet(viewsets.ModelViewSet):
    queryset = models.NotificationTemplate.objects.all()
    serializer_class = serializers.NotificationTemplateSerializer


class UserNotificationFilter(filters.FilterSet):
    class Meta:
        model = models.UserNotification
        fields = ["status", "notification_type"]

class UserNotificationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserNotificationSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserNotificationFilter

    def get_queryset(self):
        user = self.request.user
        return models.UserNotification.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        service = NotificationService(notification_id=instance.id)
        if instance.status == 0:
            instance.status = 1
            instance.save()
        notification_text = service.display_notifications()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data["notification_text"] = notification_text
        if notification_text:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"error": "Notification not found or not displayable"},
            status=status.HTTP_404_NOT_FOUND
        )


class UserNotificationSettingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserNotificationSettingSerializer

    def get_queryset(self):
        return models.UserNotificationSetting.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
