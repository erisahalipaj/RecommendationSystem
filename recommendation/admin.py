from django.contrib import admin
from .models import Movie, User, Rating

admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Rating)
