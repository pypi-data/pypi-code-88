# The default reviewer
# The parent module (reviewers/__init__.py) contatins some
# generic code used by all of the reviewers.
from vinca.lib.ansi import ansi
import re
import readchar 

from vinca.lib.video import DisplayImage
from vinca.lib.audio import Recording
from vinca.lib.terminal import AlternateScreen

def make_string(card):
	f = ' / '.join((card.path / 'front').read_text().splitlines())
	b = ' / '.join((card.path / 'back').read_text().splitlines())
	return f + ' | ' + b

def review(card):
	global spelltest_words; spelltest_words = []

	with AlternateScreen():
		# front text
		front = (card.path / 'front').read_text()
		print(re.sub(r'\{.*?\}', colorize, front))
		tags_str = '    '.join(['['+t.replace('_',' ')+']' for t in card.tags])  # TODO show tags only if requested
		print(ansi['light'] + tags_str + ansi['reset'])

		# front media
		with DisplayImage(card.path/'image_front'), Recording(card.path/'audio_front'):
			# card flip
			if spelltest_words:
				spelltest(spelltest_words)
			else:
				char = readchar.readchar() # press any key to flip the card
				if char in ['x','a','q']: # immediate exit actions
					return char
		# back text
		back = '\n' + (card.path / 'back').read_text()
		print(re.sub(r'\{.*?\}', colorize, back))

		# front media
		with DisplayImage(card.path/'image_back'), Recording(card.path/'audio_back'):
			key = readchar.readchar()
	
	return key

spelltest_words = []
def spelltest(spelltest_words):
	for word in spelltest_words:
		print(ansi['show_cursor'],end='')
		i = input(f'{ansi["light"]}  spell test:   {ansi["reset"]}')
		print(ansi['hide_cursor'],end='')
		print(ansi['move_up_line'] + ansi['clear_line'],end='')
	
		# evaluate input
		if i.strip().lower() == word.strip().lower():  # right
			print(f'{ansi["green"]} {word} {ansi["reset"]}')
		else:
			print(f'{ansi["red"]} {i} {ansi["reset"]}')  # wrong
			print(f'{ansi["green"]} {word} {ansi["reset"]}')

# WARNING: functional side effect
def colorize(match_obj):
	''' a basic function which uses ansi terminal codes to markup the text
	whose inputs look like {it, b, yellow, spell: word}
	It has the side effect of processing spell: attr into spelltest_words.'''
	# WARNING: functional side effect
	global spelltest_words

	s = match_obj.group()
	s = s[1:-1]  # strip off {braces}
	attrs, word = s.split(':')
	attrs = [attr.strip() for attr in attrs.split(',')]
	
	# add words to the spell test (see warning)
	if 'type' in attrs: spelltest_words.append(word); attrs.remove('type')
	if 'spell' in attrs: spelltest_words.append(word); attrs.remove('spell')

	assert all([a in ansi.keys() for a in attrs]), f'Bad Attribute\n{ansi.keys()}'
	attrs = ''.join([ansi[attr] for attr in attrs])
	return attrs + word + ansi["reset"]

