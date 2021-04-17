from django.shortcuts import render
from django.http import HttpResponse
from .models import Game


# Create your views here.
def index(request):
    if request.method == 'POST':
        return render(request, 'main/index.html')

    games = Game.objects.all()
    return render(request, 'main/index.html', {'games': games})


def game_view(request, name):
    game = Game.objects.get(name=name)
    game.current_players = 2
    return render(request, 'main/game.html')

