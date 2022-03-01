from session_filtering.serializers import (
    FilterBaseSerializer,
    SessionSaveFilterMixin,
)

from testapp.filters import BookFilter


class BookFilterSerializer(SessionSaveFilterMixin, FilterBaseSerializer):

    class Meta:
        filter_class = BookFilter
