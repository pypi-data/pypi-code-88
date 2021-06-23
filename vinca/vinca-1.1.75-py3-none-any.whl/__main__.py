from vinca import parsing, functions
from vinca.lib.classes import Card
from vinca.lib.ansi import ansi
import sys
from pathlib import Path

vinca_path = Path(__file__).parent 
cards_path = vinca_path / 'cards'

# parse the command line arguments
parser = parsing.parser
args = parser.parse_args()

# accept a file of newline separated card ids
if not sys.stdin.isatty():
	for line in sys.stdin:
		id = line.strip().split()[0]  # first field
		assert id.isdigit(), f'Bad card id {id}'
		args.cards.append(Card(id))
	# reconnect stdin to tty in case we used a pipe
	sys.stdin = open('/dev/tty')  
# operate on all the cards by default
if not args.cards:
	args.cards = [Card(int(id.name)) for id in cards_path.iterdir()]

	
# run the specified function
print(ansi['line_wrap_off'],end='')
print(ansi['hide_cursor'],end='')
func = args.func
func = getattr(functions, func)
func(args)
print(ansi['show_cursor'],end='')
print(ansi['line_wrap_on'], end='')
