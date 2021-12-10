from time import sleep
from Moves import Move
from actions3x3 import *
from pynput import keyboard


action = None  # initial var for keyboard input

# manual game beginning
move = Move()

while True:
    if action == '1':
        move.action_right()
    elif action == '2':
        move.action_left()
    elif action == '3':
        move.action_up()
    elif action == '4':
        move.action_down()
    elif action == '5':
        break

    print(move)

    print(f"""
Your score: {move.score} pts

Use arrow keys and ur brain to play!

""")
    zeros_numbers = []
    for row in move.pattern:
        for tile in row:
            if tile == 0:
                zeros_numbers.append(1)

    if not zeros_numbers:
        clear_console()
        break

    # action = input()

    with keyboard.Events() as events:
        event = events.get()
    sleep(0.1)
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

    clear_console()

# game over block

print(move)
print(f"""
GAME OVER :-(

Your final score: {move.score} pts
""")

quit()
