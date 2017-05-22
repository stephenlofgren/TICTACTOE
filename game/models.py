"""defines models used in the squares app"""
from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return "pk={0}".format(self.pk)

    @classmethod
    def create_if_new(cls, newName):
        queryset = Player.objects.all()
        filtered = queryset.filter(name=newName)
        if len(filtered) == 0:
            return cls.objects.create(name=newName)
        return filtered[0]


class Game(models.Model):
    """defines a game"""
    player_choices = (
        (0, 'player1'),
        (1, 'player2')
    )
    move_count = models.BigIntegerField(default=0)
    first_player = models.ForeignKey(
        Player, null=True, related_name='first_player')
    second_player = models.ForeignKey(
        Player, null=True, related_name='second_player')
    state_sequence = models.CharField(default='---------', max_length=9)
    active_player_num = models.SmallIntegerField(
        default=0, choices=player_choices)

    def __str__(self):
        return "pk={0}".format(self.pk)

    @classmethod
    def create(cls, firstPlayerName, secondPlayerName):
        firstPlayer = Player.create_if_new(newName=firstPlayerName)
        firstPlayer.save()
        secondPlayer = Player.create_if_new(newName=secondPlayerName)
        secondPlayer.save()
        return cls(first_player=firstPlayer, second_player=secondPlayer)

    @property
    def active_player(self):
        """returns the active player"""
        if self.active_player_num == 0:
            return self.first_player
        return self.second_player

    def make_move(self, position_index):
        pass
