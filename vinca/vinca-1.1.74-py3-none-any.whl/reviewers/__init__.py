# The metareviewer which implements specific reviewers
import time, datetime
today = datetime.date.today()
import importlib
	
grade_dict = {'x': -1,
	      'd': -1,
	      'q': 0,
	      'e': 0,
	      '\x1b': 0, # <ESC>
	      '1': 1,
	      '2': 2,
	      '3': 3,
	      '4': 4,
	      ' ': 3,
	      '\r': 3,
	      '\n': 3}
def review(card, mode='review'):
	assert mode in ['review','preview']

	start = time.time()

	# dynamically import the required reviewer module
	# a specifc reviewer is responsible for returning a key to the generic reviewer
	m = importlib.import_module('.'+card.reviewer, package = 'vinca.reviewers')
	key = m.review(card, mode)  # the reviewer gives back the key

	stop = time.time()
	elapsed = int(stop - start)

	grade = grade_dict[key] if key in grade_dict else 0
	grade = grade if mode=='review' or grade<0 else 0

	card.add_history(today, elapsed_time, grade)

def make_string(card):
	m = importlib.import_module('.'+card.reviewer, package = 'vinca.reviewers')
	assert hasattr(m, 'make_string'), f'{card.reviewer} must implement \
		the make_string method to represent this card on the command line'
	return m.make_string(card)
	
