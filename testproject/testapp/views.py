# -*- coding: utf-8 -*-
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import ViewSetMixin

from session_filtering.backends import SessionFilterBackend

from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from .session_filtering.models import (
    BookFilterSessionModel,
)
from .session_filtering.serializers import (
    BookFilterSerializer,
)


class BooksViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    ViewSetMixin,
    GenericAPIView,
):
    serializer_class = BookSerializer
    filter_backends = [SessionFilterBackend]
    filter_class = BookFilter
    filter_session_model = BookFilterSessionModel
    filter_serializer_class = BookFilterSerializer
    filter_lookup_field = 'filterset_id'
    queryset = Book.objects.all()
