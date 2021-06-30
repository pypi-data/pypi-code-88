import subprocess
from pathlib import Path
import shutil

vinca_path = Path(__file__).parent.parent.parent

path = Path(__file__).parent
vimrc_path = path / 'vimrc'
# we create a few files to store file paths
# The user will specify media file paths in these files
# then the we will copy the specified file into the card
path_spec_image_front = path / 'image_front'
path_spec_image_back = path / 'image_back'
path_spec_audio_front = path / 'audio_front'
path_spec_audio_back = path / 'audio_back'
# create these temp files and delete previous contents
path_spec_image_front.open('w').close
path_spec_image_back.open('w').close
path_spec_audio_front.open('w').close
path_spec_audio_back.open('w').close

def edit(card):
	# we are going to run vim...
	vim_cmd = ['vim']
	vim_cmd += [card.path/'front']

	# we are going to open each file window
	# one by one so that we can specify things well
	# this tells vim that we do not want to automatically
	# resize/equalize windows each time we open one
	# l will store a list of commands to open the window splits
	l = ['set noequalalways']
	# when we open a window split below we move focus to that window
	l += ['set splitbelow']

	# open the back
	l += [f'split {card.path / "back"}']

	l += [f'3 split {path_spec_image_back}']
	l += [f'1 split {path_spec_audio_back}']
	# vsplit stands for vertical split
	l += [f'vsplit {path_spec_audio_front}']
	# move up one window to draw the image_front split
	l += ['wincmd k']
	l += [f'vsplit {path_spec_image_front}']
	# bring focus back up to the top
	l += ['1 wincmd W']
	vim_cmd += ['-c',' | '.join(l)]  # vim uses | to join commands

	# using a vimrc file to make a few custom bindings...
	vim_cmd += ['-Nu', vimrc_path]
	# launch
	subprocess.run(vim_cmd)

	# finally process the media references
	for ref in ['image_front','image_back','audio_front','audio_back']:
		media_ref = (path / ref).read_text().strip()
		card_media = card.path / ref
		if media_ref == 'none' and card_media.exists():
			card_media.unlink()
		elif media_ref:
			source_file = Path( Path.cwd(), media_ref )
			assert source_file.exists(), f"{source_file} not found"
			shutil.copy( media_ref, card_media )
