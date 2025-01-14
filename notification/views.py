from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from notification import models, serializers


class NotificationCategoryListCreateView(generics.ListCreateAPIView):
    queryset = models.NotificationCategory.objects.all()
    serializer_class = serializers.NotificationCategorySerializer
    permission_classes = [IsAuthenticated]


class NotificationTemplateListCreateView(generics.ListCreateAPIView):
    queryset = models.NotificationTemplate.objects.all()
    serializer_class = serializers.NotificationTemplateSerializer
    permission_classes = [IsAuthenticated]


class UserNotificationListCreateView(generics.ListCreateAPIView):
    serializer_class = serializers.UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        status = self.request.query_params.get("status")
        notification_type = self.request.query_params.get("notification_type")
        queryset = models.UserNotification.objects.filter(user=user)
        if status is not None:
            queryset = queryset.filter(status=status)
        if notification_type is not None:
            queryset = queryset.filter(notification_type=notification_type)

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class UserNotificationDetailView(generics.RetrieveAPIView):
    serializer_class = serializers.UserNotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        queryset = models.UserNotification.objects.filter(user=user)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == 0:
            instance.status = 1
            instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class UserNotificationSettingListUpdateView(generics.ListCreateAPIView):
    serializer_class = serializers.UserNotificationSettingSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return models.UserNotificationSetting.objects.filter(
            user=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
