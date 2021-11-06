# D1, D2, D3, D4 = None, None, None, None
# C1, C2, C3, C4 = None, None, None, None
# B1, B2, B3, B4 = None, None, None, None
# A1, A2, A3, A4 = None, None, None, None

# original test pattern
# C1, C2, C3 = 8, 2, 8
# B1, B2, B3 = 4, 4, 0
# A1, A2, A3 = 4, 2, 2


C1, C2, C3 = 8, 0, 8
B1, B2, B3 = 4, 4, 0
A1, A2, A3 = 4, 2, 2

# C1, C2, C3 = 0, 0, 0
# B1, B2, B3 = 4, 4, 0
# A1, A2, A3 = 4, 2, 2

# print(f"""input pattern:
# {C1}, {C2}, {C3}
# {B1}, {B2}, {B3}
# {A1}, {A2}, {A3}
# """)

input_pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]
print('input pattern:')
for row in input_pattern:
    print(row)


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


def action_right(pattern: list) -> list:
    for row in pattern:
        if row[2] == row[1]:
            row[2] = row[2] + row[1]
            row[1] = row[0]
            row[0] = 0
        if row[0] == row[1]:
            row[1] = row[1] + row[0]
            row[0] = 0
        if row[2] == 0:
            row[2] = row[1]
            row[1] = row[0]
        if row[1] == 0:
            row[1] = row[0]
            row[0] = 0
    return pattern


def action_left(pattern: list) -> list:
    for row in pattern:
        row.reverse()
        if row[2] == row[1]:
            row[2] = row[2] + row[1]
            row[1] = row[0]
            row[0] = 0
        if row[0] == row[1]:
            row[1] = row[1] + row[0]
            row[0] = 0
        if row[2] == 0:
            row[2] = row[1]
            row[1] = row[0]
        if row[1] == 0:
            row[1] = row[0]
            row[0] = 0
        row.reverse()
    return pattern


def action_up(pattern: list) -> list:
    pattern = rotate_pattern(pattern)
    for row in pattern:
        if row[2] == 0:
            row[2] = row[1]
            row[1] = row[0]
            row[0] = 0
        if row[2] == row[1]:
            row[2] = row[2] + row[1]
            row[1] = row[0]
            row[0] = 0
        if row[0] == row[1]:
            row[1] = row[1] + row[0]
            row[0] = 0
        if row[2] == 0:
            row[2] = row[1]
            row[1] = row[0]
        if row[1] == 0:
            row[1] = row[0]
            row[0] = 0
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    pattern = rotate_pattern(pattern)
    return pattern


def action_down(pattern: list) -> list:
    for row in pattern:
        row.reverse()
        if row[2] == row[1]:
            row[2] = row[2] + row[1]
            row[1] = row[0]
            row[0] = 0
        if row[0] == row[1]:
            row[1] = row[1] + row[0]
            row[0] = 0
        if row[2] == 0:
            row[2] = row[1]
            row[1] = row[0]
        if row[1] == 0:
            row[1] = row[0]
            row[0] = 0
        row.reverse()
    return pattern


# output_pattern = action_right(input_pattern)
# output_pattern = action_left(input_pattern)
output_pattern = action_up(input_pattern)

print('output pattern:')
for row in output_pattern:
    print(row)
