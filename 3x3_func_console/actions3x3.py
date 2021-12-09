import random
from os import system, name

game_active = True  # A flag to continue auto-game
score = 0  # Game score


def clear_console():
    """
    Clears console output for 3 main OS types
    :return:
    """
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def common_move(row: list) -> list:
    """
    A basic 2048 game mechanics. Moves and sums numbers in a list with len=3.
    Broadcasts game score through global var.
    :param row:
    :return:
    """
    global score
    if row[2] == 0:
        row[2] = row[1]
        row[1] = row[0]
        row[0] = 0
    if row[1] == 0:
        row[1] = row[0]
        row[0] = 0
    if row[2] == row[1]:
        row[2] = row[2] + row[1]
        row[1] = row[0]
        row[0] = 0
        score += row[2] * 2
    if row[0] == row[1]:
        row[1] = row[1] + row[0]
        row[0] = 0
        score += row[1] * 2
    if row[2] == 0:
        row[2] = row[1]
        row[1] = row[0]
    return row


def patterns_are_equal(pattern1: list, pattern2: list) -> bool:
    """
    Compares two lists, returns bool.
    :param pattern1:
    :param pattern2:
    :return:
    """
    if pattern1 == pattern2:
        return True
    else:
        return False

def generate_tile_on_move(pattern: list, max_tile_value: int = 2) -> list:
    """
    Replaces a random zero with a provided number.
    Works with a square 2D arrays.
    :param pattern:
    :param max_tile_value:
    :return:
    """
    global game_active

    zeros_numbers = []
    step_counter = 0
    for row in pattern:
        for tile in row:
            step_counter += 1
            if tile == 0:
                zeros_numbers.append(step_counter)

    if not zeros_numbers:
        game_active = False
        return pattern
    target_tile = random.choice(zeros_numbers)

    # print(f'random tile: {target_tile}')

    y = (target_tile - 1) // len(pattern)

    while target_tile > len(pattern):
        target_tile -= len(pattern)
    x = target_tile - 1

    pattern[y][x] = max_tile_value
    return pattern


def rotate_pattern(pattern: list) -> list:
    """
    Rotating 2D-pattern clockwise
    Solved @ https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
    :param pattern:
    :return:
    """
    rotated_pattern = list(zip(*pattern[::-1]))
    result = []
    for n in rotated_pattern:
        result.append(list(n))
    return result


def forward_movement(pattern: list) -> list:
    """
    Adapts common_move to work with a list of lists frontwards.
    :param pattern:
    :return:
    """
    for row in pattern:
        common_move(row)
    return pattern


def backward_movement(pattern: list) -> list:
    """
    Adapts common_move to work with a list of lists backwards.
    :param pattern:
    :return:
    """
    for row in pattern:
        row.reverse()
        common_move(row)
        row.reverse()
    return pattern


def action_right(pattern: list) -> list:
    pattern = forward_movement(pattern)
    return pattern


def action_left(pattern: list) -> list:
    pattern = backward_movement(pattern)
    return pattern


def action_up(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    pattern = forward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    return pattern


def action_down(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    pattern = backward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    return pattern
