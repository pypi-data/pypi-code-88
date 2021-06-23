import subprocess
import json
import datetime
TODAY = datetime.date.today()
from pathlib import Path

from vinca import reviewers, editors, schedulers 

vinca_path = Path(__file__).parent.parent  # /path/to/vinca
cards_path = vinca_path / 'cards'

class Card:
	# Card class can load without 
	default_metadata = {'editor': 'base', 'reviewer':'base', 'scheduler':'base',
			    'tags': [], 'history': [], 'deleted': False,
			    'due_date': TODAY, 'siblings': [], 'string': '',
			    'editor_config': {}, 'reviewer_config': {}, 'scheduler_config': {}}

	def __init__(self, id=None, create=False):
		assert (id is not None) ^ create
		if not create:  # load an existing card
			assert type(id) is int
			self.id = id
			self.path = cards_path/str(id)
			assert self.path.exists(), f'Bad Card ID {self.id}'
			self.metadata_path = self.path/'metadata.json'
			self.metadata_is_loaded = False
		elif create: # create a new card
			old_cids = [int(x.name) for x in cards_path.iterdir()]
			self.id = max(old_cids) + 1 if old_cids else 100 
			self.path = cards_path/str(self.id)
			self.path.mkdir()
			self.metadata = Card.default_metadata
			self.metadata_path = self.path/'metadata.json'
			self.metadata_is_loaded = True
			self.save_metadata()

	def load_metadata(self):
		self.metadata = json.load(self.metadata_path.open())
		# dates must be serialized into strings for json
		# I unpack them here
		self.metadata['history'] = [[datetime.datetime.strptime(date,'%Y-%m-%d').date(),
				grade, time] for date, grade, time in self.metadata['history']]
		self.metadata_is_loaded = True

	def save_metadata(self):
		json.dump(self.metadata, self.metadata_path.open('w'), default=str, indent=2)

	for m in default_metadata.keys():
		# create getter and setter methods for everything in the metadata dictionary
		exec(f'''
@property
def {m}(self):
	if not self.metadata_is_loaded:
		self.load_metadata()
	return self.metadata["{m}"]''')
		exec(f'''
@{m}.setter
def {m}(self, new_val):
	if not self.metadata_is_loaded:
		self.load_metadata()
	self.metadata["{m}"] = new_val
	self.save_metadata()''')	

	def __str__(self):
		return self.string

	def add_history(self, date, time, grade):
		self.history = self.history + [[date, time, grade]]
	def undo_history(self):
		assert len(self.history) > 1
		self.history = self.history[:-1]
			
	def review(self): reviewers.review(self)
	def make_string(self): self.string = reviewers.make_string(self)
	def edit(self): editors.edit(self) 
	def edit_metadata(self):
		subprocess.run(['vim',self.path/'metadata.json'])
		self.make_string()
	def schedule(self): schedulers.schedule(self) 

	@property
	def create_date(self): return self.history[0][0] if self.history else TODAY
	@property
	def seen_date(self): return self.history[-1][0] if self.history else TODAY
	@property
	def last_grade(self): return self.history[-1][2]
	@property
	def last_interval(self): return self.history[-1][0] - self.history[-2][0]  

	@property
	def new(self): return len(self.history) == 1

