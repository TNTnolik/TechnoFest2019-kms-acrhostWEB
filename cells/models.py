from django.db import models
from django.contrib.auth.models import User

class mind(models.Model):
    other = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    codeAuth = models.CharField(max_length=10)
    token = models.CharField(max_length=32, null=True, blank=True)

class cell(models.Model):
    mind = models.ForeignKey(mind, on_delete=models.CASCADE)
    numbers = models.PositiveIntegerField()

class arrow(models.Model):
    cell = models.ForeignKey(cell, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    humidity = models.SmallIntegerField()
    height_type=(
        (1, 'Не вырасло'),
        (2, 'Вырасло')
        )
    height = models.PositiveIntegerField(default=1, choices=height_type)
    temperature = models.SmallIntegerField()

