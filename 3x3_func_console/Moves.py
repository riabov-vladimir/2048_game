from actions3x3 import *
import random


class Move:

    pattern = None
    prev_pattern = None
    score = 0
    game_active = True

    def __init__(self):

        self.pattern = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.prev_pattern = [[
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]]

        self.generate_tile_on_move()
        self.generate_tile_on_move()

    def action_right(self):
        self.pattern = forward_movement(self.pattern)
        self.generate_tile_on_move()

    def action_left(self):
        self.pattern = backward_movement(self.pattern)
        self.generate_tile_on_move()

    def action_up(self):
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = forward_movement(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.generate_tile_on_move()

    def action_down(self):
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = backward_movement(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.pattern = rotate_pattern(self.pattern)
        self.generate_tile_on_move()

    def __str__(self):
        temp = self.prev_pattern[-1]
        return f"""{self.pattern[0]}
{self.pattern[1]}
{self.pattern[2]}
{self.prev_pattern}
"""

    def generate_tile_on_move(self, max_tile_value: int = 2):
        """
        Replaces a random zero with a provided number.
        Works with a square 2D arrays.
        :param max_tile_value:
        :return:
        """

        zeros_numbers = []
        step_counter = 0
        for row in self.pattern:
            for tile in row:
                step_counter += 1
                if tile == 0:
                    zeros_numbers.append(step_counter)

        if not zeros_numbers:
            self.game_active = False

        target_tile = random.choice(zeros_numbers)

        # print(f'random tile: {target_tile}')

        y = (target_tile - 1) // len(self.pattern)

        while target_tile > len(self.pattern):
            target_tile -= len(self.pattern)
        x = target_tile - 1

        self.pattern[y][x] = max_tile_value


    # def rotate_pattern(pattern: list) -> list:
    #     """
    #     Rotating 2D-pattern clockwise
    #     Solved @ https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    #     :param pattern:
    #     :return:
    #     """
    #     rotated_pattern = list(zip(*pattern[::-1]))
    #     result = []
    #     for n in rotated_pattern:
    #         result.append(list(n))
    #     return result
    #
    # def forward_movement(pattern: list) -> list:
    #     """
    #     Adapts common_move to work with a list of lists frontwards.
    #     :param pattern:
    #     :return:
    #     """
    #     for row in pattern:
    #         common_move(row)
    #     return pattern
    #
    # def backward_movement(pattern: list) -> list:
    #     """
    #     Adapts common_move to work with a list of lists backwards.
    #     :param pattern:
    #     :return:
    #     """
    #     for row in pattern:
    #         row.reverse()
    #         common_move(row)
    #         row.reverse()
    #     return pattern
    #
    # def action_up(pattern: list) -> list:
    #     pattern = rotate_pattern(pattern)
    #     pattern = forward_movement(pattern)
    #     pattern = rotate_pattern(pattern)
    #     pattern = rotate_pattern(pattern)
    #     pattern = rotate_pattern(pattern)
    #     return pattern
    #
    # def action_down(pattern: list) -> list:
    #     pattern = rotate_pattern(pattern)
    #     pattern = backward_movement(pattern)
    #     pattern = rotate_pattern(pattern)
    #     pattern = rotate_pattern(pattern)
    #     pattern = rotate_pattern(pattern)
    #     return pattern