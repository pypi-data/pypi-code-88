import hashlib
import base64
import base32hex
from .make_hashable import represent_and_encode


def hash_object(obj, n_jobs, base=64):
	"""
	:type obj: Obj
	:type base: int
	:rtype str
	"""
	if hasattr(obj, '__hash64__') and base == 64:
		return obj.__hash64__()
	elif hasattr(obj, '__hash32__') and base == 32:
		return obj.__hash32__()

	hash_maker = hashlib.sha256()
	hash_maker.update(represent_and_encode(obj, n_jobs=n_jobs))
	if base == 64:
		return base64.b64encode(hash_maker.digest()).decode()
	elif base == 32:
		return base32hex.b32encode(hash_maker.digest()).replace('=', '-').replace('----', 'hb32')
	else:
		raise ValueError(f'base{base} is unknown!')


smart_hash = hash_object

hash = hash_object
