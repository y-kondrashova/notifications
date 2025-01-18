from django.urls import path, include
from rest_framework.routers import DefaultRouter

from project.views import ProjectViewSet

router = DefaultRouter()
router.register("", ProjectViewSet, basename="projects")

urlpatterns = [path("", include(router.urls))]

app_name = "project"
