import readline as rl

from vinca.lib import ansi
from vinca.lib.terminal import COLUMNS

def edit(card, scrollback = True):
	front_path, back_path = (card.path / 'front'), (card.path / 'back')
	front = front_path.read_text()
	front.replace('\n',';')
	rl.set_startup_hook(lambda: rl.insert_text(front))
	new_front = input('Q: ').replace(';','\n')
	front_path.write_text(new_front)
	
	back = back_path.read_text().replace('\n',';')
	rl.set_startup_hook(lambda: rl.insert_text(back))
	new_back = input('A: ').replace(';','\n')
	back_path.write_text(new_back)

	rl.set_startup_hook()
	if scrollback:
		ansi.up_line(2)

