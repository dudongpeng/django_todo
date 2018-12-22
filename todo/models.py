from django.db import models
from django.utils import timezone
from datetime import timedelta
import datetime


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Todo(models.Model):

    content = models.CharField('内容', max_length=200)
    creat_time = models.DateTimeField('创建时间', default=timezone.now)
    status = models.BooleanField('状态', default=False)

    finish_time = models.DateTimeField('结束时间', auto_now=True)

    qid = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content



