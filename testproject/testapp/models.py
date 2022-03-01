from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    issue_year = models.IntegerField()
    publisher = models.TextField()
    price = models.FloatField()

    def __str__(self):
        return self.title
