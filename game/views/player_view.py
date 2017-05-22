"""defines X10View"""
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework import permissions
from django.template.loader import get_template
from django.template import RequestContext, Template
from django.shortcuts import render
from game.models import Player
from game.serializers import GameSerializer, PlayerSerializer
import json
from django.core.serializers.json import DjangoJSONEncoder


class PlayerViewSet(viewsets.ModelViewSet):
    """defines rest api"""
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
