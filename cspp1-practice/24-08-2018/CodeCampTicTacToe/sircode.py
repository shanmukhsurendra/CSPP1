def taking_tictactoe():
	matrix = []
	for i in range(3):
		matrix.append(input().strip().split())
	return matrix
def is_validinput(matrix):
	for row in matrix:
		for element in row:
			if element not in 'xo.':
				return False
	return True
def is_validgame():
	x_count = 0
	o_count = 0
	for row in matrix:
		x_count += row.count('x')
		o_count += row.count('o')
	if o_count > 5 or x_count > 5 or o_count == x_count:
		return False
	return True

def rows_columns(matrix):
	for row in matrix:
		if len(set(row)) == 1 and row[0] == winner_variable:
			return True
	return False

def decide_winner(matrix, winner_variable):
	


def main():
	matrix = taking_tictactoe()
	check = is_validinput(matrix)
	if check:
		if is_validgame(matrix):
			if decide_winner(matrix, 'x'):
				print('x')
			elif decide_winner(matrix, 'o'):
				print('o')
			else:
				print("draw")
		else:
			print("invalid input")
	else:
		print("invalid input")