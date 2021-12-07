from actions3x3 import *


class Move:

    pattern = []

    def __init__(self):

        self.pattern = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.pattern = generate_tile_on_move(self.pattern)
        self.pattern = generate_tile_on_move(self.pattern)

    def action_right(self):
        self.pattern = action_right(self.pattern)

    def action_left(self):
        self.pattern = action_left(self.pattern)

    def action_up(self):
        self.pattern = action_up(self.pattern)

    def action_down(self):
        self.pattern = action_down(self.pattern)

    def __str__(self):
        return f"""{self.pattern[0]}
{self.pattern[1]}
{self.pattern[2]}
"""
