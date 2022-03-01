from rest_framework.serializers import ModelSerializer

from testapp.models import Book


class BookSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = [
            'title',
            'issue_year',
            'price',
            'publisher',
        ]
