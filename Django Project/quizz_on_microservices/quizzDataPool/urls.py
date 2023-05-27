from django.urls import path
from .views import render_user_stats, quizz_view

urlpatterns = [
    path('quizz/', quizz_view, name='quizz'),
    path('stats/', render_user_stats, name='stats'),
]