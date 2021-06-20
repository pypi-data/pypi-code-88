import logging


log = logging.getLogger(__name__)


class TapObject:
    def _init_from_streams(self):
        """Create an object from two data streams."""
        self._data, errors1 = self.primary.payload()
        if errors1:
            # can only perform error correction if stream lengths match
            if len(self.primary) == len(self.secondary):
                data2, errors2 = self.secondary.payload()
                for n in errors1-errors2:
                    self._data[n] = data2[n]
                self.uncorrected_errors = bool(errors1 & errors2)
                if self.uncorrected_errors:
                    log.debug("%d uncorrected errors remain", len(errors1 & errors2))
                else:
                    log.debug("All errors corrected")
            else:
                log.debug("Stream lengths differ, no error correction")
                self.uncorrected_errors = True
        else:
            self.uncorrected_errors = False

    def __str__(self):
        return "<{}: data_len - {}, errors? - {}>".format(type(self).__name__, len(self._data), self.uncorrected_errors)
