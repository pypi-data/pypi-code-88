


def hash_int(x):
	s = represent_and_encode(x)
	_hash_maker = hashlib.sha256()

	encoded = to_bytes(s)  # instead of x.encode()
	_hash_maker.update(encoded)
	return hash(base64.b64encode(_hash_maker.digest()).decode())
