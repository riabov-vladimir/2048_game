from actions3x3 import *
import os

C1, C2, C3 = 0, 0, 0
B1, B2, B3 = 0, 0, 0
A1, A2, A3 = 0, 0, 0

pattern = [
    [C1, C2, C3],
    [B1, B2, B3],
    [A1, A2, A3]
]


generate_tile_on_move(pattern)
generate_tile_on_move(pattern)
action = ''


while game_active:
	if action == '1':
		action_right(pattern)

	for row in pattern:
		print(row)

	# os.system('cls' if os.name == 'nt' else 'clear')

	action = input(f"""
Your score: {score} pts 
	
Use arrow keys and ur brains to play!

	""")