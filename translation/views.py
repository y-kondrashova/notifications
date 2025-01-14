from rest_framework import viewsets

from translation.models import Language
from translation.serializers import LanguageSerializer


class LanguageViewSet(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
