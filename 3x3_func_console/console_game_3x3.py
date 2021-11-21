from time import sleep

import actions3x3
from actions3x3 import *
from pynput import keyboard

C1, C2, C3 = 0, 0, 0
B1, B2, B3 = 0, 0, 0
A1, A2, A3 = 0, 0, 0

pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]

action = None  # initial var for keyboard input

# manual game beginning

pattern = generate_tile_on_move(pattern)
pattern = generate_tile_on_move(pattern)

while True:
    if action == '1':
        pattern = action_right(pattern)
    elif action == '2':
        pattern = action_left(pattern)
    elif action == '3':
        pattern = action_up(pattern)
    elif action == '4':
        pattern = action_down(pattern)
    elif action == '5':
        break

    for row in pattern:
        print(row)

    print(f"""
Your score: {actions3x3.score} pts

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

    # action = input()

    with keyboard.Events() as events:
        event = events.get()
        if event.key == keyboard.Key.right:
            action = '1'
        elif event.key == keyboard.Key.left:
            action = '2'
        elif event.key == keyboard.Key.up:
            action = '3'
        elif event.key == keyboard.Key.down:
            action = '4'
        elif event.key == keyboard.Key.esc:
            action = '5'
    sleep(0.1)
    clear_console()

# game over block

for row in pattern:
    print(row)
print(f"""
GAME OVER :-(

Your final score: {actions3x3.score} pts
""")

quit()
