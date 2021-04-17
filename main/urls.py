from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('game/<str:name>', views.game_view, name='game'),
]
