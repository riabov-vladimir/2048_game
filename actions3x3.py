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
    else:
        return False


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


# def action_right(pattern: list) -> list:
#     reserve_pattern = pattern.copy()
#     reserve_pattern = reserve_pattern.copy()
#     pattern = forward_movement(pattern)
#     print('pattern input')
#     for row in reserve_pattern:
#         print(row)
#     print('pattern mod')
#     for row in pattern:
#         print(row)
#     print(patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern))
#     if patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern):
#         print('equal')
#         result = pattern
#     else:
#         print('not equal')
#         result = generate_tile_on_move(pattern)
#     return result
#
#
# def action_left(pattern: list) -> list:
#     reserve_pattern = pattern.copy()
#     reserve_pattern = reserve_pattern
#     pattern = backward_movement(pattern)
#     print('pattern input')
#     for row in reserve_pattern:
#         print(row)
#     print('pattern mod')
#     for row in pattern:
#         print(row)
#     print(patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern))
#     if patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern):
#         print('equal')
#         result = pattern
#     else:
#         print('not equal')
#         result = generate_tile_on_move(pattern)
#     return result


def action_up(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    reserve_pattern = reserve_pattern
    pattern = rotate_pattern(pattern)
    pattern = forward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    print('pattern input')
    for row in reserve_pattern:
        print(row)
    print('pattern mod')
    for row in pattern:
        print(row)
    print(patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern))
    if patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern):
        print('equal')
        result = pattern
    else:
        print('not equal')
        result = generate_tile_on_move(pattern)
    return result


def action_down(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    reserve_pattern = reserve_pattern
    pattern = rotate_pattern(pattern)
    pattern = backward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    print('pattern input')
    for row in reserve_pattern:
        print(row)
    print('pattern mod')
    for row in pattern:
        print(row)

    print(patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern))
    if patterns_are_equal(pattern1=pattern, pattern2=reserve_pattern):
        print('equal')
        result = pattern
    else:
        print('not equal')
        result = generate_tile_on_move(pattern)
    return result


def action_right(pattern: list) -> list:
    # reserve_pattern = pattern.copy()
    result = action_right(pattern=pattern)
    return result


def action_left(pattern: list) -> list:
    reserve_pattern = pattern.copy()
    patternA = backward_movement(pattern=pattern)
    if patterns_are_equal(pattern1=patternA, pattern2=reserve_pattern):
        print('equal')
        return patternA
    print('not equal')
    result = generate_tile_on_move(patternA)
    return result