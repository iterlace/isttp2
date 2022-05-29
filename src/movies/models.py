from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.TextField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"


class Director(models.Model):
    name = models.TextField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Director"
        verbose_name_plural = "Directors"
        db_table = "directors"


class Movie(models.Model):
    name = models.TextField(max_length=256)

    director = models.ForeignKey(
        "movies.Director",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Director",
        related_name="movies",
    )

    category = models.ForeignKey(
        "movies.Category",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Petition",
        related_name="movies",
    )

    release_date = models.DateField(null=False)

    created_at = models.DateTimeField(
        verbose_name="Date created",
        default=timezone.now,
        null=False,
    )

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        db_table = "movies"
        constraints = [
            models.UniqueConstraint(
                "name",
                "release_date",
                "director",
                name="unique_movie_name_year_director",
            )
        ]
