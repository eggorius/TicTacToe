from django.db import models
from django_tagify.fields import TagsInput
import string
import random


def generate_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Game.objects.filter(code=code).count() == 0:
            break
    return code


class Game(models.Model):
    code = models.CharField(max_length=6, default=generate_code, unique=True)
    current_players = models.IntegerField(default=1, null=False)




