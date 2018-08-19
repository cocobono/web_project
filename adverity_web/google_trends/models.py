from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    signup_stamp = models.DateTimeField(auto_now=True)


class Request(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)
    search_term = models.CharField(max_length=100)


class TimeStamp(models.Model):
    request = models.ForeignKey("Request", on_delete=models.CASCADE)
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now=True)
