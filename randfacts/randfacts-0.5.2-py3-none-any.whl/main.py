from random import choice
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'safe.txt')) as f:
	safeFacts = [fact.rstrip('\r\n ') for fact in f.readlines() if fact.rstrip('\r\n ') != '']
with open(os.path.join(dir_path, 'unsafe.txt')) as f:
	unsafeFacts = [fact.rstrip('\r\n ') for fact in f.readlines() if fact.rstrip('\r\n ') != '']

allFacts = safeFacts + unsafeFacts

def getFact(filter_enabled: bool=True) -> str:
	"""This function returns a random fact.

	Parameters
	----------
	filter_enabled : bool
		The `filter_enabled` parameter determines if the function will filter
		out potentially inappropriate facts. Defaults to True.

	Returns
	------
	str
		A random fact.

	"""
	if filter_enabled is False:
		return choice(allFacts)
	return choice(safeFacts)

if __name__ == '__main__':
	if '--mixed' in sys.argv:
		print(getFact(False))
	elif '--unsafe' in sys.argv:
		print(getFact())
	else:
		print(getFact())
