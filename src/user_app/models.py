
from django.urls import reverse, reverse_lazy
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model # вместо user

User = get_user_model()

class PersonalAccount(models.Model):
    pass


class HomePage (models.Model):
    pass


class Job(models.Model):
    name = models.CharField(max_length=100, verbose_name='Должность',)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
       return reverse_lazy('user:job-list') 
         









