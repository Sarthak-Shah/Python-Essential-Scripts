from django.db import models

class QuestionAnswerPool(models.Model):
    question = models.CharField(max_length=550)
    choice1 = models.CharField(max_length=150)
    choice2 = models.CharField(max_length=150)
    choice3 = models.CharField(max_length=150)
    choice4 = models.CharField(max_length=150)
    trueAnswer = models.CharField(max_length=150)

#20 questions

# q1 = QuestionAnswerPool.objects.create(
#     question = "What is microservices architecture ?",
#     choice1 = "A way to building software app",
#     choice2 = "A way of building hardware devices",
#     choice3 = "A way of building cars",
#     choice4 = "A way of building bridge connections between app",
#     trueAnswer = "A way of building software applications"
# )
#
# q2 = QuestionAnswerPool.objects.create(
#     question = "Which of the following responses is an advantage of microservices?",
#     choice1 = "Any microservice component can change independently from other components",
#     choice2 = "They don't require a lot of expertise to program",
#     choice3 = "They're so small that developers can typically write very powerful ones with a few lines of text",
#     choice4 = "They are easy to manage",
#     trueAnswer = "Any microservice component can change independently from other components"
# )
