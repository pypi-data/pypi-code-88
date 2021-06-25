# linear editor for lyrics, poetry, oratory, etc.
import subprocess
from pathlib import Path
import shutil

vinca_path = Path(__file__).parent.parent.parent # I counted right
tags_path = vinca_path / 'data' / 'tags.txt'

path = Path(__file__).parent
vimrc_path = path / 'vimrc'

def edit(card):
	# we are going to run vim...
	vim_cmd = ['vim']
	vim_cmd += [card.path/'lines']

	# we are going to open each file window
	# one by one so that we can specify things well
	# this tells vim that we do not want to automatically
	# resize/equalize windows each time we open one
	# l will store a list of commands to open the window splits
	l = ['set noequalalways']
	# when we open a window split below
	# we automatically move focus to that window
	l += ['set splitbelow']
	l += [f'1 split {card.path / "tags"}']
	# bring focus back up to the top
	l += ['1 wincmd W']
	vim_cmd += ['-c',' | '.join(l)]
	# using a vimrc file to make a few custom bindings...
	vim_cmd += ['-Nu', vimrc_path]
	# including tag autocompletion
	vim_cmd += ['-c', f'set dictionary={tags_path}']
	# launch
	subprocess.run(vim_cmd)
