"""integration tests"""
from django.test import TestCase
from game.models import Game
from game.models import Player


class GameTestCase(TestCase):
    """Test the general game crud operations"""
