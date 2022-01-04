"""game module"""
from typing import Any


class GameState:
    """ The state of the game.

    """

    def __init__(self, current_player_p1: bool, moves: list, winner: str) \
            -> None:
        """ To initialize GameState with current_player_p1, moves, and winner.
        >>> p1 = GameState(True, [], 'p1')
        >>> p1.get_current_player_name()
        'p1'
        >>> p1.get_possible_moves()
        []
        >>> p1.get_winner()
        'p1'
        >>> p2 = GameState(False, [], 'p2')
        >>> p2.get_current_player_name()
        'p2'
        >>> p2.get_possible_moves()
        []
        >>> p2.get_winner()
        'p2'
        """
        self._current_player_name = 'p1' if current_player_p1 else 'p2'
        self._moves = moves
        self._winner = winner

    def __str__(self) -> str:
        """ To return a string representation
        """
        raise NotImplementedError("Subclasses should implement this!")

    def get_possible_moves(self) -> list:
        """ To return a list of possible moves
        >>> p1 = GameState(True, [], '')
        >>> p1.get_possible_moves()
        []
        >>> p2 = GameState(True, [1, 4, 9], '')
        >>> p2.get_possible_moves()
        [1, 4, 9]
        >>> p3 = GameState(True, ['rl','rr'], '')
        >>> p3.get_possible_moves()
        ['rl', 'rr']
        """
        return self._moves

    def is_valid_move(self, move_to_make: Any) -> bool:
        """ To return True or False to see whether move_to_make is valid or not
        """
        raise NotImplementedError("Subclasses should implement this!")

    def get_current_player_name(self) -> str:
        """ To return what the player name is in a string format
        >>> p1 = GameState( True, [], '')
        >>> p1.get_current_player_name()
        'p1'
        >>> p2 = GameState(False, [], '')
        >>> p2.get_current_player_name()
        'p2'
        """
        return self._current_player_name

    def make_move(self, move_to_make: Any) -> "GameState":
        """ To change it to GameState
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __eq__(self, other: Any) -> bool:
        """ To return True or False when compared to other
        """
        raise NotImplementedError("Subclasses should implement this!")

    def is_winner(self, player_name: str) -> bool:
        """ To return True or False to see if the player_name is the winner
        >>> p1 = GameState(True, [], 'p1')
        >>> p1.is_winner('p1')
        True
        >>> p1.is_winner('p2')
        False
        >>> p2 = GameState(False, [], 'p2')
        >>> p2.is_winner('p2')
        True
        """
        return self._winner == player_name

    def get_winner(self) -> str:
        """ return the winner of the game
        >>> p1 = GameState(True, [], 'p1')
        >>> p1.get_winner()
        'p1'
        >>> p2 = GameState(False, [], 'p2')
        >>> p2.get_winner()
        'p2'
        >>> p3 = GameState(True, [1, 4], '')
        >>> p3.get_winner()
        ''
        """
        return self._winner


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
