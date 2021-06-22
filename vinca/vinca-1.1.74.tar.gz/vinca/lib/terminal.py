from vinca.lib.ansi import ansi
import shutil

COLUMNS, LINES = shutil.get_terminal_size()
TAB_WIDTH = 8

# A Context Manager for the terminal's alternate screen
class AlternateScreen:

	def __init__(self):
		pass

	def __enter__(self):
		print(ansi['save_cursor'] + ansi['hide_cursor'], end='')
		print(ansi['save_screen'] + ansi['clear'] + ansi['move_to_top'], end='')

	def __exit__(self, *exception_args):
		print(ansi['restore_screen'],end='')
		print(ansi['show_cursor'] + ansi['restore_cursor'],end='')
