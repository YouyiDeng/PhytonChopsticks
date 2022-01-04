""" game strategy module"""
from typing import Any
from random import randint
from game_base import GameBase


def interactive_strategy(game: GameBase) -> Any:
    """
    Return a move for game through interactively asking the user for input.
    """
    move = input("Enter a move: ")
    return game.str_to_move(move)


def random_strategy(game: GameBase) -> Any:
    """
    To have a random stratedy when asked for the user's input
    """
    new_count = len(game.current_state.get_possible_moves())
    if new_count == 0:
        return None
    return game.current_state.get_possible_moves()[randint(0, new_count - 1)]


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config="a1_pyta.txt")
