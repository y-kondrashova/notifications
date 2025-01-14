from django.urls import path, include
from rest_framework.routers import DefaultRouter

from translation.views import LanguageViewSet

router = DefaultRouter()
router.register("languages", LanguageViewSet, basename="languages")

urlpatterns = [path("", include(router.urls))]

app_name = "translation"
