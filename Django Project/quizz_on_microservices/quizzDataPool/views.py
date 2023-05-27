from django.shortcuts import render, redirect
from .models import QuestionAnswerPool
from userPool.models import UserSpecificQuizzData
from django.utils import timezone
from django.contrib import messages
import random

from django.db.models import Max, Min, Avg

def quizz_view(request):
    quizz_data = QuestionAnswerPool.objects.all()
    random_five_questions = random.sample(list(quizz_data.values()), 5)
    total_marks = 0
    current_user_name = request.session.get('user_name')
    error = None

    if request.method == 'POST':
        try:
            for question in quizz_data:
                selected_answer = request.POST.get(str(question.id))
                if selected_answer == question.trueAnswer:
                    total_marks += 1

            # user = RegisterUser.objects.get(email=current_user_name)
            timestamp = timezone.now()
            total_marks = float(total_marks)

            user_quizz_data = UserSpecificQuizzData()
            # user_quizz_data.email = user
            user_quizz_data.email = current_user_name
            user_quizz_data.marks = total_marks
            user_quizz_data.timestamp = timestamp
            user_quizz_data.save()

            context = {'total_marks': total_marks, 'played_user': current_user_name}
            print(f'User {current_user_name} has scored {total_marks} !')
            return render(request, 'result.html', context)
        except Exception as e:
            error = f"An error occurred while saving user data: {e}"
            print(error)

    if current_user_name is None:
        error = 'Please log in first!'
        return redirect('login')

    context = {'quizz_data': random_five_questions, 'played_user': current_user_name, 'error': error}
    return render(request, 'microservicesQuizz.html', context)


def render_user_stats(request):
    error = None
    try:
        loggedIn_user_email_id = request.session.get('user_name')
        all_makrs = UserSpecificQuizzData.objects.filter(email=loggedIn_user_email_id)
        past_record = {}
        for each_record in all_makrs:
            past_record.update({each_record.timestamp:each_record.marks })
        max_marks = UserSpecificQuizzData.objects.filter(email=loggedIn_user_email_id).aggregate(Max('marks'))['marks__max']
        min_marks = UserSpecificQuizzData.objects.filter(email=loggedIn_user_email_id).aggregate(Min('marks'))['marks__min']
        avg_marks = round(UserSpecificQuizzData.objects.filter(email=loggedIn_user_email_id).aggregate(Avg('marks'))['marks__avg'], 2)
    except Exception as e:
        error = f"An error occurred while fetching user stats: {e}"
        print(error)
        max_marks = None
        min_marks = None
        avg_marks = None
        past_record = None

    context = {'max_marks': max_marks, 'min_marks': min_marks, 'avg_marks': avg_marks, 'error': error, 'past_record': past_record}
    return render(request, 'user_stats.html', context)
