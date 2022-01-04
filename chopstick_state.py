""" Subtract square game state"""
from typing import Any, List
from game_state import GameState


class ChopstickState(GameState):
    """ The state of the game substract square
    """

    def __init__(self, current_player_p1: bool, p1_p2_hands: List[int]) -> None:
        """ To initialize the chopstick state with current_player_p1 and the
        list for p1_p2_hands.
        >>> p1 = ChopstickState(True, [1, 2, 3, 4])
        >>> p1.get_current_player_name()
        'p1'
        >>> p1.get_p1_left()
        1
        >>> p1.get_p1_right()
        2
        >>> p1.get_p2_left()
        3
        >>> p1.get_p2_right()
        4
        """
        GameState.__init__(self, current_player_p1, [], '')
        self._p1_left = p1_p2_hands[0]
        self._p1_right = p1_p2_hands[1]
        self._p2_left = p1_p2_hands[2]
        self._p2_right = p1_p2_hands[3]
        self._moves = self.create_moves(current_player_p1, p1_p2_hands)

    def __eq__(self, other: Any) -> bool:
        """ To return True or False when compared to other
        >>> p1 = ChopstickState(True, [1, 1, 1, 1])
        >>> p2 = ChopstickState(True, [1, 1, 1, 1])
        >>> p3 = ChopstickState(False, [1, 2, 1, 1])
        >>> p4 = GameState(False, [], '')
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

    def __str__(self) -> str:
        """ To return a string representation
         >>> p1_state = ChopstickState(True, [1, 2, 3, 4])
         >>> print(p1_state)
         Player 1: 1 - 2; Player 2: 3 - 4
        """
        return "Player 1: {} - {}; Player 2: {} - {}".format(
            str(self._p1_left), str(self._p1_right),
            str(self._p2_left), str(self._p2_right))

    def create_moves(self, current_player_p1: bool, p1_p2_hands: list) -> list:
        """
        To generate a p1_p2_hands list of moves in the condition of
        current_player_p1.
        >>> p_chopstick = ChopstickState(True,[1, 1, 1, 1] )
        >>> p_chopstick.create_moves(True,[1, 1, 1, 1])
        ['ll', 'lr', 'rl', 'rr']
        >>> p2_chopstick = ChopstickState(True,[0, 2, 3, 1 ])
        >>> p2_chopstick.create_moves(True, [0, 2, 3, 1])
        ['rl', 'rr']
        >>> p3_chopstick = ChopstickState(True,[0, 0, 0, 0 ])
        >>> p3_chopstick.create_moves(True, [0, 0, 0,0])
        []
        >>> p4_chopstick = ChopstickState( False,[1, 1, 1, 1 ])
        >>> p4_chopstick.create_moves(False, [1, 1, 1,1])
        ['ll', 'lr', 'rl', 'rr']
        >>> p5_chopstick = ChopstickState(False,[0, 0, 0, 0 ])
        >>> p5_chopstick.create_moves(False, [0, 0, 0,0])
        []
        """
        new_moves = []
        p1_left = p1_p2_hands[0]
        p1_right = p1_p2_hands[1]
        p2_left = p1_p2_hands[2]
        p2_right = p1_p2_hands[3]
        if current_player_p1:
            if p1_left > 0 and p2_left > 0:
                new_moves.append('ll')
            if p1_left > 0 and p2_right > 0:
                new_moves.append('lr')
            if p1_right > 0 and p2_left > 0:
                new_moves.append('rl')
            if p1_right > 0 and p2_right > 0:
                new_moves.append('rr')
        else:
            if p2_left > 0 and p1_left > 0:
                new_moves.append('ll')
            if p2_left > 0 and p1_right > 0:
                new_moves.append('lr')
            if p2_right > 0 and p1_left > 0:
                new_moves.append('rl')
            if p2_right > 0 and p1_right > 0:
                new_moves.append('rr')

        return new_moves

    def is_valid_move(self, move_to_make: str) -> bool:
        """ To return True or False to see whether move_to_make
        is valid or not.
        >>> p1 = ChopstickState(True, [1, 1, 1, 1] )
        >>> p1.is_valid_move('ll')
        True

        """
        return move_to_make in self._moves

    def make_move(self, move_to_make: str) -> "ChopstickState":
        """ Return the new ChopstickState when applying the move_to_make
        >>> p1_game = ChopstickState(True, [1, 1, 1, 1])
        >>> new_state = p1_game.make_move('ll')
        >>> new_state.get_current_player_name()
        'p2'
        >>> new_state.get_possible_moves()
        ['ll', 'lr', 'rl', 'rr']
        >>> new_state.get_winner()
        ''
        """
        if self._current_player_name == 'p1':
            # next player is p2
            new_player_p1 = False
            if move_to_make == 'll':
                new_p1_left = self._p1_left
                new_p1_right = self._p1_right
                new_p2_left = (self._p1_left + self._p2_left) % 5
                new_p2_right = self._p2_right
            elif move_to_make == 'lr':
                new_p1_left = self._p1_left
                new_p1_right = self._p1_right
                new_p2_left = self._p2_left
                new_p2_right = (self._p1_left + self._p2_right) % 5
            elif move_to_make == 'rl':
                new_p1_left = self._p1_left
                new_p1_right = self._p1_right
                new_p2_left = (self._p1_right + self._p2_left) % 5
                new_p2_right = self._p2_right
            else:
                # moves_to_makes == 'rr'
                new_p1_left = self._p1_left
                new_p1_right = self._p1_right
                new_p2_left = self._p2_left
                new_p2_right = (self._p1_right + self._p2_right) % 5
        else:
            # next player is p1
            new_player_p1 = True
            if move_to_make == 'll':
                new_p2_left = self._p2_left
                new_p2_right = self._p2_right
                new_p1_left = (self._p2_left + self._p1_left) % 5
                new_p1_right = self._p1_right
            elif move_to_make == 'lr':
                new_p2_left = self._p2_left
                new_p2_right = self._p2_right
                new_p1_left = self._p1_left
                new_p1_right = (self._p2_left + self._p1_right) % 5
            elif move_to_make == 'rl':
                new_p2_left = self._p2_left
                new_p2_right = self._p2_right
                new_p1_left = (self._p2_right + self._p1_left) % 5
                new_p1_right = self._p1_right
            else:
                # moves_to_makes == 'rr'
                new_p2_left = self._p2_left
                new_p2_right = self._p2_right
                new_p1_left = self._p1_left
                new_p1_right = (self._p2_right + self._p1_right) % 5

        new_chopstick_state = ChopstickState(new_player_p1,
                                             [new_p1_left, new_p1_right,
                                              new_p2_left, new_p2_right])

        if new_p1_left == 0 and new_p1_right == 0:
            new_chopstick_state._winner = 'p2'
        if new_p2_left == 0 and new_p2_right == 0:
            new_chopstick_state._winner = 'p1'

        return new_chopstick_state

    def get_p1_left(self) -> int:
        """" To return _get_p1_left
        >>> p1 = ChopstickState(True, [1, 2, 3, 4])
        >>> p1.get_p1_left()
        1
        """
        return self._p1_left

    def get_p1_right(self) -> int:
        """" To return _get_p1_right
         >>> p1 = ChopstickState(True, [1, 2, 3, 4])
        >>> p1.get_p1_right()
        2
        """
        return self._p1_right

    def get_p2_left(self) -> int:
        """" To return _get_p2_left
        >>> p1 = ChopstickState(True, [1, 2, 3, 4])
        >>> p1.get_p2_left()
        3
        """
        return self._p2_left

    def get_p2_right(self) -> int:
        """" To return _get_p2_right
        >>> p1 = ChopstickState(True, [1, 2, 3, 4])
        >>> p1.get_p2_right()
        4
        """
        return self._p2_right


if __name__ == '__main__':
    import python_ta
    import doctest

    python_ta.check_all(config="a1_pyta.txt")
    doctest.testmod()
