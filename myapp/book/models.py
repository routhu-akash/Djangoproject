from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication = models.CharField(max_length=200)
    year = models.DateField()

    def __str__(self):
        return self.name
