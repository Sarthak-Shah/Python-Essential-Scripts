from django.urls import path
from .views import index, anonymous_view, logged_in_view

urlpatterns = [
    path('', index, name='index'),
    path('anonymous', anonymous_view, name='anonymous_view'),
    path('logged-in/', logged_in_view, name='logged-in'),
]
