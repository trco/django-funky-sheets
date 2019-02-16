from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=64, null=True)
    genre = models.ManyToManyField(Genre)
    imdb_rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)

    def __str__(self):
        return self.title
