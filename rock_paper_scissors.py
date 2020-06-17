from random import choice

comp = choice(['rock', 'scissors', 'paper'])

game_mode = input('choose a game mode  1 = two players , 2 = comp vs player:   ')
game_mode = int(game_mode)
player1_score = 0
player2_score = 0
#rules:
#'rock' > 'sicss'
#'rock' < 'papper'
#'papper' < 'scissors'

# methood num 1:

while game_mode == 2:
	name = input('what is your name? ')
    
	print(f'ready for a best of 5 {name} ? \n')

	while player1_score < 5 and player2_score < 5:
		comp = choice(['rock', 'scissors', 'paper'])
		
		player1 = input('rock, scissors or paper?  ').lower()

		if player1 == 'rock' and comp == 'scissors':
			print( name + " wins ")
			player1_score += 1
			print( f"{name}'s score: {player1_score} computer's score: {player2_score}\n")		
		elif player1 =='rock' and comp == 'paper':
			print('computer wins ')
			player2_score += 1
			print( f"{name}'s score: {player1_score} computer's score: {player2_score}\n")	
		elif player1 == 'paper' and comp == 'scissors':
			print('computer wins ')
			player2_score += 1
			print( f"{name}'s score: {player1_score} computer's score: {player2_score}\n")
		elif player1 == comp:
			print('its a tie! ')
			print( f"{name}'s score: {player1_score} computer's score: {player2_score}\n")
		else:
			print(name + ' wins\n')
			print(f"{name}'s score: {player1_score} computer's score: {player2_score}\n")
	if player1_score == 5:
		print( f"{name}'s score: {player1_score}, computer first to reach socre of: {player2_score}\n")		
	elif player2_score == 5:
		print( f"computer wins with {player2_score} points where {name} behind at {player1_score}\n points")


# method num 2
#
# nested if / elif can be used to make the code cleaner;
# 
# if player1 == rock:	
#	if comp == 'scissors':
#		print('player1 wins!')
#	if comp == 'papper'
#		print('comp wins!')

#	game_mode = input('continue against computer(2)? change to 2 player mode(1) or quite(0): ')

while game_mode == 1:

	print('are you ready for a best of 5? \n')

	while player1_score < 5 and player2_score < 5:

		print('are you ready for a best of 5? \n')
		player1 = input('player1 rock, scissors, paper? ').lower()
		print("**** NO CHEATING ****\n" * 25)
		player2 = input('player2 rock, scissors, paper? ').lower()

		if player1 == player2:
			print('its a tie!')
			print( f"player1 score: {player1_score} player2 score: {player2_score}\n")

		if player1 == 'rock':
			if player2 == 'scissors':
				print('player1 wins!')
				player1_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
			elif player2 == 'paper':
				print('player2 wins!')
				player2_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
		elif player1 == 'paper':
			if player2 == 'scissors':
				print('player2 2 wins!')
				player2_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
			elif player2 == 'rock':
				print('player1 wins!')
				player1_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
		elif player1 == 'scissors':
			if player2 == 'paper':
				print('player1 wins!')
				player1_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
			elif player2 == 'rock':
				print('player2 wins!')
				player2_score += 1
				print( f"player1 score: {player1_score} player2 score: {player2_score}\n")
			else:
				print('try again something went wrong!')	
						


#	game_mode = input('continue(1)? change to play against computer(2) or quite(0): ')

