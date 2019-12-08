from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    TYPE = (
        ('Юр', 'Юр. лицо'),
        ('Физ', 'Физ. лицо')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    inn = models.IntegerField(max_length=12)
    type = models.CharField(max_length=3, choices=TYPE)