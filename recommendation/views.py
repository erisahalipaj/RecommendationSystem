from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Count, Avg
from recommendation.forms import UserIDForm
from recommendation.models import User, Rating, Movie


# Welcome page view with the user input form
def welcome_view(request):
    if request.method == 'POST':
        form = UserIDForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            try:
                # Verify the user exists
                user = User.objects.get(user_id=user_id)
                return redirect('recommendations', user_id=user_id)
            except User.DoesNotExist:
                messages.error(request, 'User not found. Please enter a valid user ID.')
    else:
        form = UserIDForm()

    return render(request, 'recommendation/welcome.html', {'form': form})


# Recommendations page view based on selected user
def recommendations_view(request, user_id):
    user = get_object_or_404(User, user_id=user_id)

    # Retrieve all ratings given by this user
    user_ratings = Rating.objects.filter(user=user)

    # Find similar users based on common movies rated
    similar_users = Rating.objects.filter(movie__in=[r.movie for r in user_ratings]) \
                        .exclude(user=user) \
                        .values('user') \
                        .annotate(similarity=Count('movie')) \
                        .order_by('-similarity')[:10]  # top 10 similar users

    similar_user_ids = [s['user'] for s in similar_users]

    # Find movies that these similar users rated highly
    recommended_movies = Rating.objects.filter(user__in=similar_user_ids) \
                             .exclude(movie__in=[r.movie for r in user_ratings]) \
                             .values('movie') \
                             .annotate(avg_rating=Avg('rating')) \
                             .order_by('-avg_rating')[:20]  # top 20 movies

    # Fetch detailed movie info
    top_movies = Movie.objects.filter(pk__in=[r['movie'] for r in recommended_movies])

    return render(request, 'recommendation/recommendations.html', {'user': user, 'top_movies': top_movies})
