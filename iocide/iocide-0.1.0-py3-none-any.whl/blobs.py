"""
Embedded binary detection
"""
from iocide import deobfuscate
from logging import getLogger

import chardet

from . import rfc_3548


logger = getLogger(name=__name__)


def decode(data, required_confidence=0.0, fallback='utf_8'):
	"""
	Detect the encoding of the supplied data and decode it as text
	"""
	encoding_detection = chardet.detect(data)
	encoding = encoding_detection['encoding']
	try:
		if encoding is None:
			raise UnicodeDecodeError(
				str(None), data, 0, 0, 'Failed to detect encoding')

		confidence = encoding_detection['confidence']
		if confidence <= required_confidence:
			raise UnicodeDecodeError(
				encoding,
				data,
				0,
				0,
				(
					'Insufficient confidence in detected encoding:'
					f' {confidence} < {required_confidence}'
				),
			)

		return data.decode(encoding)
	except UnicodeDecodeError as error:
		if fallback is None:
			raise

		logger.debug(error, exc_info=error)

	logger.debug('Falling back to %r encoding', fallback)
	return data.decode(fallback)


def extract(text, refang=False):
	"""
	Generate detected binary blobs
	"""
	yield from rfc_3548.extract(text, refang=refang)


def extract_text(
		text, skip_failures=True, depth=1, normalise=True,  **decode_kwargs):
	"""
	Generate decoded text from detected binary blobs
	"""
	if depth is not None and depth <= 0:
		return

	for blob in extract(text=text, refang=True):
		try:
			blob_text = decode(data=blob, **decode_kwargs)
		except UnicodeDecodeError as error:
			if not skip_failures:
				raise

			logger.debug(error, exc_info=error)
			logger.debug('Skipping failure')
			continue

		yield blob_text
		if normalise:
			searchable_text = deobfuscate.normalise(blob_text)
		else:
			searchable_text = blob_text

		next_depth = None if depth is None else depth - 1

		yield from extract_text(
			text=searchable_text,
			skip_failures=True,
			depth=next_depth,
			normalise=normalise,
			**decode_kwargs,
		)
