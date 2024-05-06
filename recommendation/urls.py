from django.urls import path
from recommendation import views

urlpatterns = [
    path('', views.welcome_view, name='welcome'),  # Root path will render the welcome form
    path('recommendations/<int:user_id>/', views.recommendations_view, name='recommendations'),  # Recommendations page for the selected user
]