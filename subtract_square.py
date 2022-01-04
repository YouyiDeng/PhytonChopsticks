"""subtract square game implementation"""
from typing import Any
from game_base import GameBase
from sub_square_state import SubtractSquareState


INSTRUCTION = 'Players take turns subtracting square numbers from the ' \
            + 'starting number. The winner is the person who subtracts ' \
            + 'to 0.'


class SubstractSquare(GameBase):
    """ The subtract sqaure game
    """

    def __init__(self, current_player_p1: bool) -> None:
        """ To initialize SubtractSquare with current_player_p1.
        >>> p1 = SubstractSquare(True)
        >>> p1.current_state.get_current_player_name()
        'p1'
        >>> p2 = SubstractSquare(False)
        >>> p2.current_state.get_current_player_name()
        'p2'
        """
        GameBase.__init__(self, current_player_p1)
        start_value = ''
        while not start_value.isdigit():
            start_value = input("Enter the number to subtract from: ")

        self.current_state = SubtractSquareState(current_player_p1,
                                                 int(start_value))

    def __eq__(self, other: Any) -> bool:
        """To return True or False when compared to other
        >>> p1 = SubstractSquare(True)
        >>> p2 = SubstractSquare(True)
        >>> p1 == p2
        T
        """
        if type(self) != type(other):
            return False
        if self.current_state != other.current_state:
            return False

        return True

    def __str__(self) -> str:
        """ To return a string representation
         >>> p1 = SubstractSquare(True)
         >>> p1_state = SubtractSquareState(True, 20)
         >>> p1.current_state = p1_state
         >>> print(p1)
         The current value is 20
        """
        return self.current_state.__str__()

    def get_instructions(self) -> str:
        """ Return game instructions
        >>> p1 = SubstractSquare(True)
        >>> p1.get_instructions() == INSTRUCTION
        True
        """
        return INSTRUCTION

    def str_to_move(self, move: str) -> int:
        """ To convert str move to int
        >>> p1 = SubstractSquare(True)
        >>> p1.str_to_move('1')
        1
        """
        try:
            move_to_make = int(move)
            return move_to_make
        except ValueError:
            return 0


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
