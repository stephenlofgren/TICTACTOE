"""integration tests"""
from django.test import TestCase
from game.models import Game
from game.models import PlayerModel
from game.models import GameSquare
from game.models import Coordinate


class GameTestCase(TestCase):
    """Test the general game crud operations"""

    def setUp(self):
        self.player1 = PlayerModel.objects.create()
        self.player1.save()
        self.player2 = PlayerModel.objects.create()
        self.player2.save()
        self.player3 = PlayerModel.objects.create()
        self.player3.save()
        self.player4 = PlayerModel.objects.create()
        self.player4.save()

        self.game1 = Game.objects.create()
        self.game1.players.add(self.player1)
        self.game1.players.add(self.player2)
        self.game1.save()
        self.game2 = Game.objects.create()
        self.game2.players.add(self.player3)
        self.game2.players.add(self.player4)
        self.game2.save()

    def test_query_returns_game1(self):
        """Confirm that the game we just created can be queried from the db"""
        queryset = Game.objects.filter(pk=self.game1.pk)
        self.assertEqual(1, len(queryset))

    def test_query_game_has_players(self):
        """Confirm that the game we just created can be queried from the db"""
        game_player_count = len(self.game1.players.all())
        player_count = len(PlayerModel.objects.all())
        assert 2 == game_player_count
        assert player_count > game_player_count

    def test_game_move_count_init_zero(self):
        move_count = self.game1.move_count
        assert move_count == 0

    def test_game_status_init_zero(self):
        status = self.game1.status
        assert status == 0

    def test_game_status_is_mine(self):
        player1_games = PlayerModel.objects.mine(self.player2)
        assert 1 == len(player1_games.all())
        player3_games = PlayerModel.objects.mine(self.player3)
        assert 1 == len(player3_games.all())

    def test_init_square(self):
        coord = Coordinate(0, 0)
        game_square = GameSquare.create_square(self.game1, coord, 15, 90)
        assert game_square.id == 1
        assert game_square.top.id == 1
        assert game_square.bottom.id == 3
        assert game_square.left.id == 2
        assert game_square.right.id == 4

    def test_can_start_game2(self):
        self.game2.start_game()
        assert self.game2.active_player is not None

    def test_make_move(self):
        self.game2.start_game()
        move1 = self.game2.make_move(1, 1)
        assert self.game2.move_count == 1
        move2 = self.game2.make_move(1, 2)
        assert self.game2.move_count == 2
