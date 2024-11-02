import functions as f

if __name__ == '__main__':
	board = f.start()
	while(True):
		f.show(board)
		x = input('Enter a direction: ')
		f.move(board, x)
		status = f.status(board)
		if status == 0:
			f.spawn(board)
			continue
		if status == 1:
			print('You win!')
		else:
			print('You lose!')
		x = input('Play again? (y/n): ')
		if x == 'y':
			board = f.start()
		else:
			break