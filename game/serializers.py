"""defines serializers for data models"""
from django.contrib.auth.models import User
from rest_framework import serializers
from game.models import Game, Player


# Serializers define the API representation.
class GameSerializer(serializers.HyperlinkedModelSerializer):
    """defines the fields that will be serialized into json"""
    active_player_name = serializers.SerializerMethodField(
        'player_name')

    @staticmethod
    def player_name(game):
        """used when serializing"""
        return game.active_player.name

    class Meta:
        model = Game
        fields = ('url', 'pk', 'first_player', 'second_player',
                  'active_player_num', 'active_player_name',
                  'state_sequence')


# Serializers define the API representation.
class PlayerSerializer(serializers.HyperlinkedModelSerializer):
    """defines the fields that will be serialized into json"""
    class Meta:
        model = Player
        fields = ("url", "pk", "name")


class PlayerNameField(serializers.Field):
    def get_attribute(self, obj):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.
        return obj

    def to_representation(self, obj):
        """
        Serialize the object's class name.
        """
        return obj.__class__.__name__
