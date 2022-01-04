""" Subtract square game state"""
from typing import Any
from game_state import GameState


class SubtractSquareState(GameState):
    """ The state of the game substract square
    """

    def __init__(self, current_player_p1: bool, start_value: int) -> None:
        """ To initialize the subtract square game state with current_player_p1
        and start_value.
        >>> p1 = SubtractSquareState(True, 30)
        >>> p1.get_current_player_name()
        'p1'
        >>> p1.get_value_remainder()
        30
        >>> p2 = SubtractSquareState(False, 20)
        >>> p2.get_current_player_name()
        'p2'
        >>> p2.get_value_remainder()
        20
        """
        moves = self.create_move_list(start_value)
        GameState.__init__(self, current_player_p1, moves, '')
        self._value_remainder = start_value

    def __eq__(self, other: Any) -> bool:
        """ To return True or False when compared to other
        >>> p1 = SubtractSquareState(True, 30)
        >>> p2 = SubtractSquareState(True, 30)
        >>> p3 = SubtractSquareState(False, 20)
        >>> p4 = GameState(True,[], '')
        >>> p1 == p2
        True
        >>> p1 == p3
        False
        >>> p1 == p4
        False

        """
        if type(self) != type(other):
            return False
        if self.get_current_player_name() != other.get_current_player_name():
            return False
        if self.get_winner() != other.get_winner():
            return False
        for i in range(len(self._moves)):
            if self.get_possible_moves()[i] != other.get_possible_moves()[i]:
                return False
        return True

    def create_move_list(self, start_value: int) -> list:
        """ Generate square less than or equal to start_value
        >>> p1 = SubtractSquareState( True, 20)
        >>> p1.get_possible_moves()
        [1, 4, 9, 16]
        """
        new_moves = []
        for i in range(1, start_value + 1):
            if i * i <= start_value:
                new_moves.append(i * i)
        return new_moves

    def __str__(self) -> str:
        """ To return a string representation
        >>> p1 = SubtractSquareState(True, 20)
        >>> print(p1)
        The current value is 20
        """
        return "The current value is {}".format(self._value_remainder)

    def is_valid_move(self, move_to_make: int) -> bool:
        """ To return True or False to see whether move_to_make is valid or not
        >>> p1 = SubtractSquareState(True, 20)
        >>> p1.is_valid_move(4)
        True
        """
        return move_to_make in self._moves

    def make_move(self, move_to_make: int) -> "SubtractSquareState":
        """ Return the new SubtractSquareState when applied the move_to_make
        >>> p1_game = SubtractSquareState(True, 20)
        >>> new_state = p1_game.make_move(4)
        >>> new_state.get_current_player_name()
        'p2'
        >>> new_state.get_possible_moves()
        [1, 4, 9, 16]
        >>> new_state.get_winner()
        ''
        """
        new_value = self._value_remainder - move_to_make
        new_player_p1 = False if self._current_player_name == 'p1' else True
        new_sub_square_state = SubtractSquareState(new_player_p1, new_value)

        if new_value == 0:
            new_sub_square_state._winner = self._current_player_name
        return new_sub_square_state

    def get_value_remainder(self) -> int:
        """ To return _value_remainder
        >>> p1 = SubtractSquareState(True, 30)
        >>> p1.get_current_player_name()
        'p1'
        >>> p1.get_value_remainder()
        30
        >>> p2 = SubtractSquareState(False, 20)
        >>> p2.get_current_player_name()
        'p2'
        >>> p2.get_value_remainder()
        20
        """
        return self._value_remainder


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
