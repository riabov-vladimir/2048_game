from os import system, name
import random


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


