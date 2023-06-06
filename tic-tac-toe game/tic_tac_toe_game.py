board_size = 3
board = [1,2,3,4,5,6,7,8,9]

def draw_board():
	print (('_' * 4 * board_size ))
	for i in range(board_size):
		print ((' ' * 3 + '|') * 3)
		print ('',board[i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
		print (('_' * 3 + '|') * 3)

def check_win():
	win = False
	win_combination = (
		(0,1,2), (3,4,5), (6,7,8),	
		(0,3,6), (1,4,7), (2,5,8),	
		(0,4,8), (2,4,6) 			
	)
	for pos in win_combination:
		if (board[pos[0]] == board[pos[1]] and board[pos[1]] == board[pos[2]] and board[pos[1]] in ('X','O')):
			win = board[pos[0]]
	return win

def game_step(index, char):
	if (index > 10 or index < 1 or board[index-1] in ('X','O')):
		return False

	board[index-1] = char
	return True

def start_game():
	current_player = 'X'
	step = 1

	draw_board()
	while (step < 9) and (check_win() == False):
		index = input('Sext player ' + current_player + '. Select a field :')


		if (game_step(int(index), current_player)):
			print('Good move')

			if (current_player == 'X'):
				current_player = 'O'
			else:
				current_player = 'X'

			draw_board()
			step += 1
		else:
			print('Incorrect number! Please repeat!')

	if (step == 9):
		print('Game Over. Draw')
	else:
		print('Won ' + check_win())

print('Rules: \n Players take turns putting 3x3 signs on the free cells of the field (one is always crosses, the other is always zeros). The first player to line up three of their pieces vertically, horizontally, or diagonally wins the game. The first player to make a move is the one who places crosses. Usually, at the end of the game, the winner crosses out his three marks, which form a continuous row.')
start_game()
