import random
from os import system, name

game_active = True
score = 0


def clear_console():
    # for windows the name is 'nt'
    if name == 'nt':
        _ = system('cls')

    # and for mac and linux, the os.name is 'posix'
    else:
        _ = system('clear')


def common_move(row: list) -> list:
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
    if pattern1 == pattern2:
        return True


def generate_tile_on_move(pattern: list, max_tile_value: int = 2) -> list:
    """

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

    print(f'random tile: {target_tile}')

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
    for row in pattern:
        common_move(row)
    return pattern


def backward_movement(pattern: list) -> list:
    global score
    for row in pattern:
        row.reverse()
        common_move(row)
        row.reverse()
    return pattern


def action_right(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    pattern = forward_movement(pattern)
    if patterns_are_equal(pattern, reserve_pattern):
        print('reserve pattern')
        for row in reserve_pattern:
            print(row)
        print('orig pattern')
        for row in pattern:
            print(row)
        pattern = generate_tile_on_move(pattern)
    return pattern


def action_left(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    pattern = backward_movement(pattern)
    if patterns_are_equal(pattern, reserve_pattern):
        pattern = generate_tile_on_move(pattern)
    return pattern


def action_up(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    pattern = rotate_pattern(pattern)
    pattern = forward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    if patterns_are_equal(pattern, reserve_pattern):
        pattern = generate_tile_on_move(pattern)
    return pattern


def action_down(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    pattern = rotate_pattern(pattern)
    pattern = backward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    if patterns_are_equal(pattern, reserve_pattern):
        pattern = generate_tile_on_move(pattern)
    return pattern
