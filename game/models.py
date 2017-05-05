"""defines models used in the squares app"""
from django.db import models


class PlayerModel(models.Model):
    name = models.CharField(max_length=200)


class Game(models.Model):
    """defines a game"""
    player_choices = (
        (0, 'player1'),
        (1, 'player2')
    )
    start_date = models.DateTimeField(blank=True, null=True)
    move_count = models.BigIntegerField(default=0)
    player1 = models.ForeignKey(PlayerModel, null=true)
    player2 = models.ForeignKey(PlayerModel, null=true)
    state_sequence = models.CharField(default='---------')
    active_player_num =
    models.SmallIntegerField(default=0, choices=player_choices)

    def active_player:
        if(active_player_num == 0):
            return player1
        else:
            return player2

    def make_move(self, position_index):
        self.move_count += 1
            
        this_move = Move.objects.create(
            move_number=self.move_count,
            game=self,
            move_player=self.active_player)
        this_move.save()
        return this_move

    def init_board(self, game):
        line_width=15
        square_width=90
        columns=0
        rows=0
        square_on_left=None
        square_above=None
        while columns < 10:
            while rows < 10:

                x_coord=columns * (line_width + square_width)
                y_coord=rows * (line_width + square_width)
                coord=Coordinate(x_coord,
                                   y_coord)
                square=GameSquare(game,
                                    coord,
                                    15,
                                    90)
                if square_above is not None:
                    square.top=square_above.bottom
                if square_on_left is not None:
                    square.left=square_on_left.right

                square_above=square
                rows=rows + 1
                square_on_left=square
        columns=columns + 1




class GameSquare(models.Model):
    game=models.ForeignKey(Game, on_delete=models.CASCADE)
    top=models.ForeignKey(
        LineSegment, on_delete=models.CASCADE, related_name='top_line')
    bottom=models.ForeignKey(
        LineSegment, on_delete=models.CASCADE, related_name='bottom_line')
    left=models.ForeignKey(
        LineSegment, on_delete=models.CASCADE, related_name='left_line')
    right=models.ForeignKey(
        LineSegment, on_delete=models.CASCADE, related_name='right_line')

    @classmethod
    def create_square(cls,
                      game,
                      coordinate,
                      line_width,
                      square_width):
        x_position=coordinate.x_position
        y_position=coordinate.y_position
        top=LineSegment(game=game, is_selected=False)
        top.x_position=x_position + line_width
        top.y_position=y_position
        top.width=square_width
        top.height=line_width
        top.save()
        left=LineSegment(game=game, is_selected=False)
        left.x_position=x_position
        left.y_position=y_position + line_width
        left.width=square_width
        left.height=square_width
        left.save()
        bottom=LineSegment(game=game, is_selected=False)
        bottom.x_position=x_position + line_width
        bottom.y_position=y_position + square_width + line_width
        bottom.width=square_width
        bottom.height=line_width
        bottom.save()
        right=LineSegment(game=game, is_selected=False)
        right.x_position=x_position + square_width + line_width
        right.y_position=y_position + line_width
        right.width=square_width
        right.height=square_width
        right.save()
        square=cls(game=game, top=top, bottom=bottom, left=left, right=right)
        square.save()
        return square


class Square(models.Model):
    """defines a square within a gameboard"""
    game=models.ForeignKey(Game)
    square_x_index=models.IntegerField
    square_y_index=models.IntegerField
    won_by=models.ForeignKey(PlayerModel)
