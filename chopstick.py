"""subtract square game implementation"""
from typing import Any
from game_base import GameBase
from chopstick_state import ChopstickState


INSTRUCTIONS = 'Players take turns adding the values of one of their'\
            + ' hands to one of their opponents. A hand with a total of 5 ' \
            + '(or 0) is considered \'dead\'.  The first player to have 2 ' \
            + 'dead hands is the loser.'


class Chopstick(GameBase):
    """ The subtract sqaure game
    """

    def __init__(self, current_player_p1: bool) -> None:
        """ To initialize ChopstickState with current_player_p1
        >>> p1 = Chopstick(True)
        >>> p1.current_state.get_current_player_name()
        'p1'
        >>> p2 = Chopstick(False)
        >>> p2.current_state.get_current_player_name()
        'p2'
        """
        GameBase.__init__(self, current_player_p1)
        self.current_state = ChopstickState(current_player_p1, [1, 1, 1, 1])

    def __eq__(self, other: Any) -> bool:
        """To return True or False when compared to other
        >>> p1 = Chopstick(True)
        >>> p2 = Chopstick(True)
        >>> p3 = Chopstick(False)
        >>> p4 = GameBase(True)
        >>> p1 == p2
        True
        >>> p1 == p3
        False
        >>> p3 == p4
        False
        """
        if type(self) != type(other):
            return False
        if self.current_state != other.current_state:
            return False

        return True

    def __str__(self) -> str:
        """ To return a string representation
         >>> p1 = Chopstick(True)
         >>> p1_state = ChopstickState(True, [1, 2, 3, 4])
         >>> p1.current_state = p1_state
         >>> print(p1)
         Player 1: 1 - 2; Player 2: 3 - 4
        """
        return self.current_state.__str__()

    def get_instructions(self) -> str:
        """ Return game INSTRUCTIONS
        >>> p1 = Chopstick(True)
        >>> p1.get_instructions() == INSTRUCTIONS
        True
        """
        return INSTRUCTIONS

    def str_to_move(self, move: str) -> str:
        """ Convert move into a string representation
        >>> p1 = Chopstick(True)
        >>> p1.str_to_move('rr')
        'rr'
        """
        return move


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
