from django.shortcuts import render
from django.http import HttpResponse
from .forms import TagsForm
from .models import Game


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = TagsForm(request.POST or None)
        return render(request, 'main/index.html')

    games = Game.objects.all()
    return render(request, 'main/index.html', {'games': games})
