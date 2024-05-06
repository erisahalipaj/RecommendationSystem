# recommendation/management/commands/load_movielens.py
import csv
from django.core.management.base import BaseCommand
from recommendation.models import Movie, User, Rating

class Command(BaseCommand):
    help = 'Load MovieLens dataset into the database'

    def handle(self, *args, **kwargs):
        # Adjust paths as needed
        movie_file = 'C:/Users/user/PycharmProjects/djangoProject1/ml-latest-small/movies.csv'
        ratings_file = 'C:/Users/user/PycharmProjects/djangoProject1/ml-latest-small/ratings.csv'

        # Load movies
        with open(movie_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Skip header
            for row in reader:
                movie_id, title, genres = row
                Movie.objects.create(movie_id=movie_id, title=title, genres=genres)

        # Load users and ratings
        with open(ratings_file, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                user_id, movie_id, rating, _ = row
                user, _ = User.objects.get_or_create(user_id=user_id)
                movie = Movie.objects.get(movie_id=movie_id)
                Rating.objects.create(user=user, movie=movie, rating=rating)

        self.stdout.write(self.style.SUCCESS('Successfully loaded MovieLens dataset'))
