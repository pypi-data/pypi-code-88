import re

# ansi codes let us control the terminal just
# by printing special escape sequences
esc = '\033['
ansi = {'reset': esc+'0m',
        'bold': esc+'1m', 'b': esc+'1m',
        'bold_off': esc+'22m', 'b': esc+'1m',
        'light': esc+'2m', 'dim': esc+'2m',
        'italic': esc+'3m', 'it': esc+'3m',
        'underlined': esc+'4m', 'u': esc+'4m',
        'blink': esc+'5m', 'flash': esc+'5m', 'f': esc+'5m',
        'highlight': esc+'7m', 'hi': esc+'7m', 'reverse': esc+'7m',  'mark': esc+'7m',
        'hidden': esc+'8m', 'invisible': esc+'8m',
        'red': esc+'31m', 'r': esc+'31m',
        'green': esc+'32m', 'g': esc+'32m',
        'yellow': esc+'33m',
	'blue': esc+'34m',
	'reset_color': esc+'39m',
	# the next escape codes are more powerful
	'clear': esc+'2J',
	'clear_to_bottom': esc+'J',
	'move_to_top': esc+'H',  # home
	'hide_cursor': esc+'?25l',
	'show_cursor': esc+'?25h',
	'save_cursor': esc+'s',
	'restore_cursor': esc+'u',
	'save_screen': esc+'?47h',
	'restore_screen': esc+'?47l',
	'move_up_line': esc+'F',
	'clear_line': esc+'K',
	'line_wrap_off': esc+'?7l',
	'line_wrap_on': esc+'?7h',
	}

# we define a subclass of string
# ANSI codes count as characters normally.
# We want want to be able to subscript the string
# so that the length of the slice will be the number of LETTERS
# not the number of characters (which would include the ansi codes)
class AnsiStr(str):

	def __getitem__(self, subscript):
		# we want to split on ansi codes
		# and keep the ansi codes as members of the returned list
		codes = [c.replace('[','\[').replace('?','\?') for c in ansi.values()]
		split_pattern = '(' + '|'.join(codes) + ')'
		words_and_codes = re.split(split_pattern, self)

		# now we construct a list in which each element contains
		# exactly one letter and any number of ansi codes
		l=['']
		for wc in words_and_codes:
			if wc in ansi.values(): # append codes to preceding letter
				l[-1] += wc
			else: # add the letters as individual elements
				l += list(wc)
		# the first entry does not contain a letter so
		# we combine the first and second entries
		l = [l[0]+l[1]] + l[2:]

		if type(subscript) is int:
			return l[subscript] 
		elif type(subscript) is slice:
			return ''.join(l[subscript])
