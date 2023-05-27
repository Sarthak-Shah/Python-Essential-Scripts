from django.db import models
from django.contrib.auth.models import User

class RegisterUser(models.Model):
    class Meta:
        app_label = 'userPool'
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=30)
    username = models.EmailField()
    date_registered = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     created = self.pk is None  # Check if this is a new instance
    #     super().save(*args, **kwargs)
    #     if created:
    #         user = User(
    #             username=self.email,
    #             first_name=self.first_name,
    #             last_name=self.last_name,
    #             email=self.email
    #         )
    #         user.set_password(self.password)
    #         print("storing copy of data to User database !")
    #         user.save()

class UserSpecificQuizzData(models.Model):
    class Meta:
        app_label = 'userPool'
        unique_together = ('email', 'timestamp')
    email = models.EmailField()
    marks = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

