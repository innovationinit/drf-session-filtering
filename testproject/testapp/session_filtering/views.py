from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from testapp.filters import BookFilter
from session_filtering.views import BaseFilterMixin
from .models import BookFilterSessionModel

from .serializers import BookFilterSerializer


class BookFilterViewSet(
    BaseFilterMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    filter_class = BookFilter
    serializer_class = BookFilterSerializer
    filter_session_model = BookFilterSessionModel
