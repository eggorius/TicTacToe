from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


class Game(models.Model):
    name = models.CharField(unique=True, null=False, max_length=20)
    current_players = models.IntegerField(default=1, null=False)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'name': self.name})





