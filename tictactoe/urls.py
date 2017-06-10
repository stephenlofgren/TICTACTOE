"""tictactoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from game.models import Game, Player
from rest_framework import routers
from game.views.game_view import GameView, GameViewSet
from game.views.player_view import PlayerViewSet
from django.conf.urls import url, include

admin.site.register(Game)
admin.site.register(Player)

ROUTER = routers.DefaultRouter()
ROUTER.register(r'players', PlayerViewSet)
ROUTER.register(r'games', GameViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(ROUTER.urls)),
    url(r'^play_game/$', GameView.Show),
    url(r'^play_game/([0-9]{1,2})$', GameView.Show),
    url(r'^create_game/$', GameView.create_game),
    url(r'^start_game/$', GameView.start_game),
    url(r'^post_turn/$', GameView.post_turn),
    url(r'^game_details/([0-9]{1,2})$', GameView.game_details),
    url(r'^reset_game/([0-9]{1,2})$', GameView.reset_game),
]
