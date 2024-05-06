from django.db import models

class Movie(models.Model):
    movie_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    genres = models.CharField(max_length=255)
    synopsis = models.TextField(null=True, blank=True)
    cover_image = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class User(models.Model):
    user_id = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.user_id)

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField()