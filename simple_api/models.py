import datetime

from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=160)
    created = models.DateTimeField(default=datetime.datetime.now)


class ViewsCounter(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    ip = models.GenericIPAddressField()