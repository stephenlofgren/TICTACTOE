"""defines X10View"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from game.models import Game
from game.serializers import GameSerializer, PlayerSerializer
from django.template import loader
import json


class GameView(APIView):
    """defines views for each of the http verbs"""

    @staticmethod
    @permission_classes((permissions.AllowAny,))
    def Show(request, pk=None):
        """returns the status"""
        context_dict = {'currentGame': {}, 'activePlayer': {}}
        if pk is not None:
            query_set = Game.objects.all()
            game = query_set.filter(pk=pk)
            if len(game) == 1:
                context_dict = GameView.get_game_context(game[0], request)
        return render(request, 'game/game.html', context_dict)

    @staticmethod
    @api_view(['POST'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def start_game(request):
        data = request.data
        new_game = Game.create(data["first_player"], data["second_player"])
        new_game.save()
        serializer_class = GameSerializer(new_game, many=False,
                                          context={'request': request})
        return Response(data=serializer_class.data, template_name=None)

    @staticmethod
    @api_view(['POST'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def create_game(request):
        data = request.data
        new_game = Game.create(data["first_player"], data["second_player"])
        new_game.save()
        context_dict = GameView.get_game_context(new_game, request)
        return Response(data=context_dict, template_name=None)

    @staticmethod
    @api_view(['POST'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def post_turn(request):
        data = request.data
        query_set = Game.objects.all()
        game = query_set.filter(pk=data["game_id"])[0]
        game.make_move(int(data['col_clicked']), int(data['row_clicked']))
        context_dict = GameView.get_game_context(game, request)
        return Response(data=context_dict, template_name=None)

    @staticmethod
    @api_view(['PUT'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def reset_game(request, pk):
        """resets the game and returns the json representation"""
        query_set = Game.objects.all()
        game = query_set.filter(pk=pk)[0]
        game.reset()
        context_dict = GameView.get_game_context(game, request)
        return Response(data=context_dict, template_name=None)

    @staticmethod
    def get_game_context(game, request):
        currentGame = json.dumps(GameSerializer(
            game, many=False, context={'request': request}).data)
        active_player = json.dumps(PlayerSerializer(
            game.active_player,
            many=False,
            context={'request': request}).data)
        context_dict = {'currentGame': currentGame,
                        'activePlayer': active_player}
        return context_dict

    @staticmethod
    @api_view(['GET'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def game_details(request, pk=None):
        query_set = Game.objects.all()
        game = query_set.filter(pk=pk)[0]
        context_dict = GameView.get_game_context(game, request)
        return Response(data=context_dict)


class GameViewSet(viewsets.ModelViewSet):
    """defines rest api"""
    queryset = Game.objects.all()
    serializer_class = GameSerializer
