"""game module"""
from typing import Any
from game_state import GameState


class GameBase:
    """ The abt of the game.
    === Instance attributes ===
    current_state:
    The snapshot of the current situation in the game.
    """
    current_state: GameState

    def __init__(self, current_player_p1: bool) -> None:
        """ To initialize GameBase and apply current_player_p1 to set the
        current player is p1 or p2.

        >>> p1 = GameBase(True)
        >>> p1.current_state.get_current_player_name()
        'p1'
        >>> p2 = GameBase(False)
        >>> p2.current_state.get_current_player_name()
        'p2'
        """
        self.current_state = GameState(current_player_p1, [], '')

    def get_instructions(self) -> str:
        """ Return game instructions"""
        raise NotImplementedError("Subclasses should implement this!")

    def is_over(self, current_state: GameState) -> bool:
        """ To return True or False by checking current_state.

        >>> p1 = GameBase(True)
        >>> p1_state = GameState(True, [], '')
        >>> p1.is_over(p1_state)
        True
        >>> p1_state._moves = [1, 4, 9]
        >>> p1.is_over(p1_state)
        False
        >>> p1_state._moves = ['rr', 'rl']
        >>> p1.is_over(p1_state)
        False
        """
        return len(current_state.get_possible_moves()) == 0

    def is_winner(self, player_name: str) -> bool:
        """ To return True or False by checking if the player_name is the
        winner.
        >>> p1 = GameBase(True)
        >>> p1.current_state._winner = 'p1'
        >>> p1.is_winner('p1')
        True
        >>> p1.is_winner('p2')
        False
        >>> p2 = GameBase(False)
        >>> p2.is_winner('p1')
        False
        >>> p2.is_winner('p2')
        False
        """
        return self.current_state.is_winner(player_name)

    def __eq__(self, other: Any) -> bool:
        """To return True or False when compared to other
        """
        raise NotImplementedError("Subclasses should implement this!")

    def __str__(self) -> str:
        """ To return a string representation
        """
        raise NotImplementedError("Subclasses should implement this!")

    def str_to_move(self, move: str) -> Any:
        """ To convert str to move
        """
        raise NotImplementedError("Subclasses should implement this!")


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
