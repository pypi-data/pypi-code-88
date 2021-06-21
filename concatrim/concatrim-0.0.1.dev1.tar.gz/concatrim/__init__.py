import bisect
from typing import Sequence, Tuple


class MultiFilePruner(object):
    def __init__(self, gap=0):
        self.files = {}
        self.gap = gap
    
    def add_file(self, filename):
        self.files[filename] = Pruner(filename, self.gap)
    
    def prune_all(self):
        for filename, pruner in self.files.items():
            pruner.prune()

class Pruner(object):
    
    def __init__(self, source_filename, gap=0):
        """
        Initialize a Pruner object with configuration given as arguments.
        
        :param gap: milliseconds to insert between trimmed pieces when joining them back.
        """
        self.sourcefile = source_filename
        self.gap = gap
        self._empty_spans()
    
    def add_spans(self, *spans: Sequence[Tuple[int, int]]) -> None:
        for span in spans:
            for existing_span in self.spans():
                print(existing_span, span)
                if self.is_overlapping(span, existing_span):
                    raise ValueError(f"Found an overlapping span: trying to add \"{list(span)}\", "
                                     f"but it overlaps with \"{list([existing_span])}\".")
            bisect.insort(self.span_starts, span[0])
            bisect.insort(self.span_ends, span[1])
    
    def _empty_spans(self):
        self.span_starts = []
        self.span_ends = []
            
    def spans(self):
        return zip(self.span_starts, self.span_ends)
    
    @classmethod
    def is_overlapping(cls, span1, spane2):
        s1, e1 = span1
        s2, e2 = spane2
        return s1 <= e2 and s2 <= e1
        

if __name__ == '__main__':
    p = Pruner(1)
    p.add_spans( (1,2), (5,6) , [1,3])
