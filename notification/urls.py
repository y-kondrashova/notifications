from django.urls import path

from notification import views


urlpatterns = [
    path(
        "",
        views.UserNotificationListCreateView.as_view(),
        name="notification_create"
    ),
    path(
        "<int:pk>/",
        views.UserNotificationDetailView.as_view(),
        name="notification_detail"
    ),
    path(
        "categories/",
        views.NotificationCategoryListCreateView.as_view(),
        name="category_list_create"
    ),
    path(
        "templates/",
        views.NotificationTemplateListCreateView.as_view(),
        name="template_list_create"
    ),

    path(
        "settings/",
        views.UserNotificationSettingListUpdateView.as_view(),
        name="settings_list_update"
    )
]

app_name = "notifications"
