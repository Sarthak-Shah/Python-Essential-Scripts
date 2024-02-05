from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.utils import timezone, formats
import datetime


def index(request):
    return render(request, 'session_app/index.html')


def anonymous_view(request):
    # Get the session key
    session_key = request.session.session_key

    if not session_key:
        # Create a new session if it does not exist
        request.session.create()
        session_key = request.session.session_key
        # Set the session expiry time to 10 minutes
        request.session.set_expiry(10 * 60)

    # Store language preference in the session
    if 'language_preference' not in request.session:
        request.session['language_preference'] = 'en'  # Default to English

    # Track the time spent on the app
    if 'session_start_time' not in request.session:
        request.session['session_start_time'] = formats.date_format(timezone.now(), 'DATETIME_FORMAT')

    # Session expiry time
    session_end_time = formats.date_format(timezone.now() + datetime.timedelta(seconds=request.session.get_expiry_age()), 'DATETIME_FORMAT')

    return render(request, 'session_app/anonymus_view.html', {'session_key': session_key,
                                                              'language_preference': request.session['language_preference'],
                                                              'session_start_time': request.session['session_start_time'],
                                                              'session_end_time': session_end_time})


@login_required
def logged_in_view(request):
    # Get the session key
    session_key = request.session.session_key
    return render(request, 'session_app/logged_in_view.html', {'session_key': session_key})