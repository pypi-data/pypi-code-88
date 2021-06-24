from dynamod.segop import *
import pandas as pd

class History:
    def __init__(self, model):
        self.model = model
        self.matrix = []
        self.results = {}
        for name in self.model.results:
            self.results[name] = []

    def store(self):
        self.matrix.append(self.model.matrix.copy())
        for name, expr in self.model.results.items():
            self.results[name].append (self.model.evalExpr(expr, Segop(self.model)))

    def get_attribute(self, axis, value, start=None, stop=None):
        segment = axval_segment(self.model, axis, value)
        return [m[segment].sum() for m in self.matrix[slice(start,stop,None)]]

    def get_attributes(self, axis, start=None, stop=None):
        att = self.model.attSystem.attr_map[axis]
        axl = axis_exclude(self.model, axis)
        data = [m.sum(axis=axl) for m in self.matrix[slice(start,stop,None)]]
        return pd.DataFrame(data, columns=att.values)

    def get_result(self, name, start=None, stop=None):
        pair = name.split('=')
        if len(pair) == 2:
            return self.get_attribute(pair[0], pair[1], start, stop)
        return self.results[name][slice(start,stop,None)]

    def get_results(self, names, start=None, stop=None):
        data = {name:(self.get_result(name, start, stop)) for name in names}
        return pd.DataFrame(data)

    def get_all_results(self, start=None, stop=None):
        data = {name:(hist[slice(start,stop,None)]) for (name,hist) in self.results.items()}
        return pd.DataFrame(data)
