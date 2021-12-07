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

    def __str__(self):
        return str(self.pattern)


a = Move()

print(a)