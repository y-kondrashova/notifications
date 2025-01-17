from django.urls import path, include
from rest_framework.routers import DefaultRouter

from notification import views

router = DefaultRouter()

router.register("text", views.UserNotificationViewSet, "notification")
router.register("settings", views.UserNotificationSettingViewSet, "settings")
router.register("categories", views.NotificationCategoryViewSet, "categories")
router.register("templates", views.NotificationTemplateViewSet, "templates")


urlpatterns = [
    path("", include(router.urls)),
]

app_name = "notifications"
