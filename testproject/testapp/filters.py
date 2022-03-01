from django_filters import MultipleChoiceFilter
from django_filters.rest_framework import FilterSet, NumberFilter

from testapp.models import Book


class BookFilter(FilterSet):

    publication_date = MultipleChoiceFilter(
        label='Pub dates',
        method='filter_by_issue_date',
        choices=lambda: [(year, str(year)) for year in Book.objects.all().values_list('issue_year', flat=True)],
    )

    class Meta:
        model = Book
        fields = {
            'title': ['exact', 'icontains'],
            'issue_year': ['gt'],
            'price': ['lt'],
            'publisher': ['exact', 'contains'],
            'publication_date': ['exact'],
        }

    @staticmethod
    def filter_by_issue_date(queryset, name, value):
        return queryset.filter(issue_year__in=value)
