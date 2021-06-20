"""
	This module contains a method that hashes an incoming sequence using the Python package 'xxhash'.
"""

from numpy import ndarray
import xxhash


def hashSequence(sequence: ndarray) -> str:
	"""
		This method hashes an incoming sequence using the Python package 'xxhash'.

		:param sequence: The incoming sequence that needs to be hashed.
		:return: The hash of the incoming sequence.
	"""
	return xxhash.xxh32(sequence).hexdigest()
