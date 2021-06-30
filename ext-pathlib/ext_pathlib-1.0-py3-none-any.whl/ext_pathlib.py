import GroovyFunc as grvy
import shutil
from os import makedirs
from pathlib import Path
from time import sleep as wait

def _copy(self, target):
	assert self.is_file()
	target = Path(target)
	makedirs(target.parent, exist_ok=True)
	shutil.copy(str(self), str(target))

cp_count = 2
def _copy2(self, target):
	assert self.is_file()
	target = Path(target)
	makedirs(target.parent, exist_ok=True)
	while target.exists():
		global cp_count
		# target = Path( target.parent, target.stem+f'_{cp_count}'+target.suffix )
		target = Path( grvy.replace('(_\d+)?(\..*?)$', f'_{cp_count}\\2', str(target)) )
		cp_count += 1
	shutil.copy(str(self), str(target))

def _move(self, dst):
	target = Path(dst)
	makedirs(target.parent, exist_ok=True)
	shutil.move(str(self), str(target))

mv_count = 2
def _move2(self, dst):
	target = Path(dst)
	makedirs(target.parent, exist_ok=True)
	while target.exists():
		global mv_count
		# target = Path( target.parent, target.stem+f'_{mv_count}'+target.suffix )
		target = Path( grvy.replace('(_\d+)?(\..*?)$', f'_{mv_count}\\2', str(target)) )
		mv_count += 1
	shutil.move(str(self), str(target))

def move_helper(dst):
	mv_count = 2
	target = Path(dst)
	makedirs(target.parent, exist_ok=True)
	while target.exists():
		target = Path( grvy.replace('(_\d+)?(\..*?)$', f'_{mv_count}\\2', str(target)) )
		mv_count += 1
	return target

def _mkdirs(self):
	makedirs(self, exist_ok=True)

def _b(self):
	assert self.is_file()
	return self.stat().st_size

def _kb(self):
	assert self.is_file()
	return self.stat().st_size // 1024

def _mb(self):
	assert self.is_file()
	return round(self.stat().st_size / 1024 / 1024, 2)

def _iglob(self, search):
	assert self.is_dir()
	import itertools
	if isinstance(search, str):
		return self.glob(search)
	if isinstance(search, tuple):
		output = itertools.chain()
		for x in search:
			output = itertools.chain(output, self.glob(x))
		return (x for x in output)

def _rglob(self, search):
	assert self.is_dir()
	import itertools
	if isinstance(search, str):
		return self.rglob(search)
	if isinstance(search, tuple):
		output = itertools.chain()
		for x in search:
			output = itertools.chain(output, self.rglob(x))
		return (x for x in output)

def _scan(self, wildcards='*'):
	import itertools, os
	from fnmatch import fnmatch
	path = self.resolve()
	if path == '.':
		path = os.getcwd()
	if isinstance(wildcards, str):
		return (Path(x.path) for x in os.scandir(path) if fnmatch(x.path, wildcards))
	if isinstance(wildcards, tuple):
		output = itertools.chain()
		for w in wildcards:
			output = itertools.chain( output, [x for x in os.scandir(path) if fnmatch(x.path, w)] )
		return (Path(x.path) for x in output)

def _scanr(self, wildcards='*'):
	import itertools, os
	from fnmatch import fnmatch
	path = self.resolve()
	if path == '.':
		path = os.getcwd()
	if isinstance(wildcards, str):
		lst_out = []
		for root, dirs, files in os.walk(path):
			for file in files:
				lst_out.append( Path(os.path.join(root, file)) )
		return (x for x in lst_out if fnmatch(x, wildcards))
	if isinstance(wildcards, tuple):
		output = itertools.chain()
		for w in wildcards:
			lst_out = []
			for root, dirs, files in os.walk(path):
				for file in files:
					lst_out.append( Path(os.path.join(root, file)) )
			lst_out = [x for x in lst_out if fnmatch(x, w)]
			output = itertools.chain( output, lst_out )
		return (x for x in output)

def _write(self, data, mode='w', encoding=None):
	with self.open(mode, encoding=encoding) as fwrite:
		fwrite.write(data)

def _readlines(self, encoding=None):
	with self.open('r', encoding=encoding) as fread:
		return fread.readlines()

def _str_is_file(self):
	import os.path
	ext = os.path.splitext(str(self))[1]
	if self.is_dir():
		return False
	elif ext:
		return True
	else:
		return False

def _exists(self):
	import os.path
	return os.path.exists(self)

def _splitext(self):
	import os.path
	return os.path.splitext(self)

def _getatime(self):
	import os.path
	return os.path.getatime(self)

def _getmtime(self):
	import os.path
	return os.path.getmtime(self)

def _getctime(self):
	import os.path
	return os.path.getctime(self)

def _mkdir(self, mode=0o777, parents=True, exist_ok=True):
	self.mkdir(mode=mode, parents=parents, exist_ok=exist_ok)
	# print(type(self))
	# raise Exception
	pass

help_str = 'Added Functions:\ncopy, copy2, move, move2, mkdirs, b, kb, mb, iglob, riglob, scan, scanr, write, readlines, str_is_file, exists, splitext, getatime, getmctime, getctime'

# Function renaming

Path.copy = _copy
Path.copy2 = _copy2
Path.move = _move
Path.move2 = _move2
Path.mkdirs = _mkdirs
Path.b = _b
Path.kb = _kb
Path.mb = _mb
Path.iglob = _iglob
Path.riglob = _rglob
Path.scan = _scan
Path.scanr = _scanr
Path.write = _write
Path.readlines = _readlines
Path.str_is_file = _str_is_file
Path.exists = _exists
Path.splitext = _splitext
Path.getatime = _getatime
Path.getmtime = _getmtime
Path.getctime = _getctime
master = Path
Path.help = help_str
