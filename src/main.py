"""
This is your starting point for a Python bot. It will read and store the game information every turn, then responds
with an action. For now, this action is just shooting with a random angle. Write your own logic in game.py.
"""

from game import Game


if __name__ == "__main__":
    game = Game()
    while game.read_next_turn_data():
        game.respond_to_turn()