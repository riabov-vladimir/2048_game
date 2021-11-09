import random

C1, C2, C3 = 0, 0, 0
B1, B2, B3 = 4, 0, 0
A1, A2, A3 = 0, 2, 2

input_pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]


score = 0


print('input pattern:')
for row in input_pattern:
    print(row)


def generate_tile_on_move(pattern: list, max_tile_value: int = 2) -> list:
    """

    :param pattern:
    :param max_tile_value:
    :return:
    """
    zeros_numbers = []
    step_counter = 0

    for row in pattern:
        for tile in row:
            step_counter += 1
            if tile == 0:
                zeros_numbers.append(step_counter)

    try:
        target_tile = random.choice(zeros_numbers)
    except IndexError:
        return pattern

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
    global score
    for row in pattern:
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
    return pattern


def backward_movement(pattern: list) -> list:
    global score
    for row in pattern:
        row.reverse()
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
    generate_tile_on_move(pattern)
    return pattern


def action_down(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    pattern = backward_movement(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    generate_tile_on_move(pattern)
    return pattern


pattern = action_right(input_pattern)

print('move right:')
for row in pattern:
    print(row)

pattern = action_left(pattern)
print('move left:')
for row in pattern:
    print(row)

pattern = action_up(pattern)
print('move up:')
for row in pattern:
    print(row)

pattern = action_down(pattern)
print('move down:')
for row in pattern:
    print(row)

print(f'Total score - {score} points')

