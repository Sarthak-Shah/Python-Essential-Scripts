from django.shortcuts import render, redirect
from django.urls import reverse
from django.forms.utils import ErrorList
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
import logging
logger = logging.getLogger(__name__)

def register_user(request):
    try:
        if request.method == 'POST':
            form = RegisterUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = RegisterUserForm()
        return render(request, 'registration.html', {'form': form})
    except Exception as e:
        print("Error registering user: ", e)
        form = RegisterUserForm()
        form.errors['__all__'] = ErrorList(["There was an error registering your account. Please try again later."])
        return render(request, 'registration.html', {'form': form})

def home(request):
    return render(request, 'home.html')

def login(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            # print(username, password)
            logger.debug(f'Attempting to authenticate user {username}...')
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                request.session['user_name'] = user.username
                auth_login(request, user)
                return redirect(reverse('microservices_quizz'))
            else:
                logger.warning(f'Authentication failed for user {username}.')
                raise ValueError("Invalid username or password.")
        else:
            return render(request, 'login.html')
    except ValueError as e:
        print("Error logging in: ", e)
        error = "Invalid username or password. Please try again."
        return render(request, 'login.html', {'error': error})
    except Exception as e:
        print("Error logging in: ", e)
        error = "There was an error logging you in. Please try again later."
        return render(request, 'login.html', {'error': error})

def logout(request):
    auth_logout(request)
    return redirect('home')
