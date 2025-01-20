from django.urls import path, include
from rest_framework.routers import DefaultRouter

from translation.views import LanguageViewSet, TranslationStringViewSet

router = DefaultRouter()
router.register(r"languages", LanguageViewSet, basename="languages")
router.register(r"translation_strings", TranslationStringViewSet, basename="translations")


urlpatterns = [path("", include(router.urls))]

app_name = "translation"
