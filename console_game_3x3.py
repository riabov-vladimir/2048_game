from actions3x3 import *
from sys import stdout

C1, C2, C3 = 0, 0, 0
B1, B2, B3 = 0, 0, 0
A1, A2, A3 = 0, 0, 0

pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]

score = score
action = ''
game_active = True

generate_tile_on_move(pattern)
generate_tile_on_move(pattern)

while game_active:
    if action == '1':
        action_right(pattern)
    if action == '2':
        action_left(pattern)
    if action == '3':
        action_up(pattern)
    if action == '4':
        action_down(pattern)

    action = ''
    for row in pattern:
        stdout.write(str(row) + '\n')
    stdout.write(f"""
Your score: {score} pts 

Use arrow keys and ur brains to play!

""")
    action = input()
    stdout.flush()
    stdout.write("\r  \r\n")