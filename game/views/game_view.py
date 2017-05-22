"""defines X10View"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.shortcuts import render
from game.models import Game
from game.serializers import GameSerializer


class GameView(APIView):
    """defines views for each of the http verbs"""

    @staticmethod
    @permission_classes((permissions.AllowAny,))
    def Show(request, pk=None):
        """returns the status"""
        context_dict = {'id': 1, 'player_count': 3}
        return render(request, 'game/test_view.html', context_dict)

    @staticmethod
    @api_view(['POST'])
    @permission_classes((permissions.AllowAny,))
    def start_game(request):
        data = request.data
        new_game = Game.create(data["first_player"], data["second_player"])
        new_game.save()
        serializer_class = GameSerializer(new_game, many=False,
                                          context={'request': request})
        return Response(data=serializer_class.data, template_name=None)


class GameViewSet(viewsets.ModelViewSet):
    """defines rest api"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
