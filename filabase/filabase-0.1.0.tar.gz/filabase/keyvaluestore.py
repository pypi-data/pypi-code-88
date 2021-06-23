import re
from filabase import storage


class KeyValueStore(object):
    """A Key-Value Store"""
    def __init__(self):
        super(KeyValueStore, self).__init__()
        self.store = {}
        self.io = storage.Storage('~/.filabase')

    def put(self, key, value):
        """
            inserts a key-value pair into the store
        """
        self.store[key] = value

    def persist(self):
        """
            writes the key-value store into a file
        """
        self.io.persist("keyvaluepairs", [self.store])

    def give(self, key):
        """
            Gives back the value stored against the key.
            If there is no such key, a None value is returned.
        """
        return self.store.get(key)

    def seive(self, key_regex):
        """
            returns a dict of all key-value pairs which key matches
            the key_regex
        """
        mask = re.compile(key_regex)
        return dict(filter(lambda pair: mask.match(pair[0]) is not None,
                    self.store.items()))

    def load(self):
        """
            Reads the contents of the file used for persisting the store
            and loads its contents into the store
        """
        media_result_array = self.io.extract('keyvaluepairs')
        self.store |= self.construct_store(media_result_array)

    # Not part of an API / Private

    def construct_store(self, records):
        """
            given a list of store records, construct a dictionary where latest
            record overrides previous ones
        """
        result = {}
        for record in records:
            result |= record
        return result
