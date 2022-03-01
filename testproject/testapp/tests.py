from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from testapp.models import Book


class SessionFilteringTestCase(APITestCase):

    def setUp(self):
        super().setUp()
        Book.objects.create(title='Book 1', issue_year=1999, publisher='Gallimard', price=20.)
        Book.objects.create(title='Book 2', issue_year=2001, publisher='Verso', price=30.)
        Book.objects.create(title='Book 3', issue_year=1982, publisher='Verso', price=25.)

    def test_filter_specific_name(self):
        filter_params = {'title': 'Book 1'}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'title': 'Book 1',
                    'publisher': 'Gallimard',
                    'issue_year': 1999,
                    'price': 20.0,
                },
            ]
        )

    def test_filter_partial_name(self):
        filter_params = {'title__contains': 'Book'}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 3)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'title': 'Book 1',
                    'publisher': 'Gallimard',
                    'issue_year': 1999,
                    'price': 20.0,
                },
                {
                    'title': 'Book 2',
                    'publisher': 'Verso',
                    'issue_year': 2001,
                    'price': 30.0,
                },
                {
                    'title': 'Book 3',
                    'publisher': 'Verso',
                    'issue_year': 1982,
                    'price': 25.0,
                },

            ]
        )

    def test_filter_publisher(self):
        filter_params = {'publisher': 'Verso'}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'title': 'Book 2',
                    'publisher': 'Verso',
                    'issue_year': 2001,
                    'price': 30.0,
                },
                {
                    'title': 'Book 3',
                    'publisher': 'Verso',
                    'issue_year': 1982,
                    'price': 25.0,
                },

            ]
        )

    def test_filter_year(self):
        filter_params = {'issue_year__gt': 2000}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'title': 'Book 2',
                    'publisher': 'Verso',
                    'issue_year': 2001,
                    'price': 30.0,
                },
            ]
        )

    def test_filter_price(self):
        filter_params = {'price__lt': 25}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 1)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            [
                {
                    'title': 'Book 1',
                    'publisher': 'Gallimard',
                    'issue_year': 1999,
                    'price': 20.0,
                },
            ]
        )

    def test_multiple_choice_filter(self):
        filter_params = {'publication_date': [1982, 2001]}

        filter_url = reverse('book-filter-list')
        response = self.client.post(filter_url, data=filter_params, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.json())

        filterset_id = response.data.get('id')

        url = reverse('book-list')

        response = self.client.get(
            url,
            data={'filterset_id': filterset_id},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.json(),
            [
                {
                    'title': 'Book 2',
                    'publisher': 'Verso',
                    'issue_year': 2001,
                    'price': 30.0,
                },
                {
                    'title': 'Book 3',
                    'publisher': 'Verso',
                    'issue_year': 1982,
                    'price': 25.0
                },

            ]
        )
