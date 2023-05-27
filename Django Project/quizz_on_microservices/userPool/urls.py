from django.urls import path
from .views import register_user, home, login, logout
from quizzDataPool.views import quizz_view


urlpatterns = [
    path('register/', register_user, name='register'),
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('microservices-quizz/', quizz_view, name='microservices_quizz'),
    # Add any additional URL patterns for your app here
]
