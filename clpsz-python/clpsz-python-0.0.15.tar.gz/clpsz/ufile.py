import os
import re
import sys


def read_file_as_list(file_path):
	"""
	read_file_as_list(file_path) -> list of string

	read a file and convert to a lis tof string, split the file content by new line,
	remove the last line break.
	"""
	res = []
	with open(file_path, 'r') as f:
		for line in f:
			if line[-1] == os.linesep:
				line = line[:-1]
			res.append(line)
	return res


def write_to_file(file_path, content):
	"""
	write_to_file(file_path, content) -> None
	write content to file
	"""
	with open(file_path, 'w') as f:
		f.write(content)


def read_file_as_list_and_keep_linesep(file_path):
	res = []
	with open(file_path, 'r') as f:
		for line in f:
			res.append(line)
	return res


def get_file_line_count(file_path):
	count = 0
	with open(file_path, 'r') as f:
		for _ in f:
			count += 1
	return count


def file_sub(file_path, old, new):
	file_content_list = read_file_as_list_and_keep_linesep(file_path)
	with open(file_path, 'w') as f:
		for line in file_content_list:
			f.write(line.replace(old, new))


def file_sub_re(file_path, pattern, repl):
	pattern = re.compile(pattern)
	file_content_list = read_file_as_list_and_keep_linesep(file_path)
	with open(file_path, 'w') as f:
		for line in file_content_list:
			f.write(pattern.sub(repl, line))


def yield_stdin_by_line():
	k = 0
	try:
		buff = ''
		while True:
			buff += sys.stdin.read(1)
			if buff.endswith(os.linesep):
				line = buff[:-1]
				yield line
				buff = ''
				k = k + 1
	except KeyboardInterrupt:
		sys.stdout.flush()
		pass


if __name__ == '__main__':
	# file_sub_re('/tmp/aaa.txt', r'w.*r ', 'xixi')
	write_to_file("/tmp/ta", "haha\nxixi\n")
