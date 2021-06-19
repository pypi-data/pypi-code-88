"""
	This module contains a method that checks if some hash is part of a key that is a tuple of two hashes.
"""

from typing import Tuple


def isHashInKey(key: Tuple[str, str], sequenceHash: str) -> bool:
	"""
		This method checks if some hash is part of a key that is a tuple of two hashes.

		:param key: A key that is a tuple of two hashes.
		:param sequenceHash: The hash that needs to be compared to the key.
		:return: A boolean value indicating whether or not the incoming hash is part of the key.
	"""
	hashOne, hashTwo = key
	return hashOne == sequenceHash or hashTwo == sequenceHash
