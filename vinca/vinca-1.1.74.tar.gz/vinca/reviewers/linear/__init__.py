from vinca.lib.terminal import AlternateScreen
import readchar

def review(card,mode):

	with AlternateScreen():

		lines = (card.path / 'lines').read_text().splitlines()
		print(lines.pop(0))  # print the first line
		for line in lines:
			if mode == 'review':
				readchar.readchar()  # press any key to continue
			print(line)
		print('\n(end)')

		# grade the card
		char = readchar.readchar()
	
	return char

def make_string(card):
	return (card.path / 'lines').read_text().replace('\n',' / ')
