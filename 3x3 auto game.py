import actions3x3
from actions3x3 import *

C1, C2, C3 = 2, 4, 8
B1, B2, B3 = 2, 4, 8
A1, A2, A3 = 4, 0, 0

pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]

action = None

# manual game beginning

# pattern = generate_tile_on_move(pattern)
# pattern = generate_tile_on_move(pattern)


while actions3x3.game_active:
    if not actions3x3.game_active:
        break
    action_right(pattern)
    for row in pattern:
        print(row)
    if not actions3x3.game_active:
        break
    action_left(pattern)
    for row in pattern:
        print(row)
    if not actions3x3.game_active:
        break
    action_up(pattern)
    for row in pattern:
        print(row)
    if not actions3x3.game_active:
        break
    action_down(pattern)
    for row in pattern:
        print(row)

print(f"""
GAME OVER :(
""")

quit()