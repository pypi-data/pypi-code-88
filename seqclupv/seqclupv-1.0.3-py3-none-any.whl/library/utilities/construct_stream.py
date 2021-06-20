"""
	This module contains a method that constructs a data stream of sequenceStore
	from a given set of clusters, classes and number of prototypes.
"""
import random
from typing import Tuple, List, Union

from numpy import ndarray

Stream = List[Tuple[ndarray, Union[int, chr]]]


def constructStream(clusters: List[List[Union[ndarray, list]]], classes: List[Union[int, chr]], numPrototypes: int) \
		-> Tuple[Stream, Stream]:
	"""
		This method constructs a data stream of sequenceStore from a
		given set of clusters, classes and number of prototypes.

		:param clusters: The set of clusters that needs to be clustered by some clustering algorithm.
		:param classes: The identifier of the classes that belong to the clusters that were passed to this method.
		:param numPrototypes: The number of prototypes that will be used in the clustering algorithm.
		:return: A two-tuple where the first item is the complete stream and the second item is a stream of sequences
		from any of the clusters that are not prototypes where the order of sequenceStore is randomized.
	"""
	# Preparing input sequence data (Exp with different settings, e.g. randomize, inverted, etc)
	stream = []

	print(f"[SeqCluCLI] The number of sequences per class is {map(len, clusters)}.")

	# Q: How to select initial prototypes?
	for i, cluster in enumerate(clusters):
		stream.extend(list(zip(cluster[:numPrototypes], [classes[i]] * len(cluster))))

	print(f"[SeqCluCLI] The total number of prototypes is {len(stream)}.")

	# randomize incoming sequenceStore so they belong to random classes
	randomizedStream = []
	for i, cluster in enumerate(clusters):
		randomizedStream.extend(list(zip(cluster[numPrototypes:], [classes[i]] * len(cluster))))

	random.shuffle(randomizedStream)

	stream.extend(randomizedStream)

	return stream, randomizedStream
