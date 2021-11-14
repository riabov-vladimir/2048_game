import random
from os import system, name
from time import sleep

# C1, C2, C3 = 0, 0, 0
# B1, B2, B3 = 0, 0, 0
# A1, A2, A3 = 0, 0, 0
C1, C2, C3 = 2, 4, 8
B1, B2, B3 = 2, 4, 8
A1, A2, A3 = 4, 0, 0

pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]

score = 0

action = ''


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
    pattern = forward_movement(pattern)
    generate_tile_on_move(pattern)
    return pattern


def action_left(pattern: list) -> list:
    pattern = backward_movement(pattern)
    generate_tile_on_move(pattern)
    return pattern


def action_up(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    pattern = forward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = generate_tile_on_move(pattern)
    return pattern


def action_down(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    pattern = backward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    generate_tile_on_move(pattern)
    return pattern

# auto game
# while game_active:
#     if not game_active:
#         break
#     action_right(pattern)
#     for row in pattern:
#         print(row)
#     if not game_active:
#         break
#     action_left(pattern)
#     for row in pattern:
#         print(row)
#     if not game_active:
#         break
#     action_up(pattern)
#     for row in pattern:
#         print(row)
#     if not game_active:
#         break
#     action_down(pattern)
#     for row in pattern:
#         print(row)
#
# print(f"""
# GAME OVER :(
#
# Your final score: {score} pts
# """)
#
# quit()

# manual game beginning

# pattern = generate_tile_on_move(pattern)
# pattern = generate_tile_on_move(pattern)
game_active = True
while game_active:
    if action == '1':
        pattern = action_right(pattern)
    if action == '2':
        pattern = action_left(pattern)
    if action == '3':
        pattern = action_up(pattern)
    if action == '4':
        pattern = action_down(pattern)

    for row in pattern:
        print(row)

    print(f"""
Your score: {score} pts

Use arrow keys and ur brain to play!

""")
    zeros_numbers = []
    for row in pattern:
        for tile in row:
            if tile == 0:
                zeros_numbers.append(1)

    if not zeros_numbers:
        clear_console()
        break

    action = input()
    clear_console()

print(f"""
GAME OVER :-(

Your final score: {score} pts
""")

quit()
