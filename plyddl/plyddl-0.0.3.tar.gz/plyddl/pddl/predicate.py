import copy
from enum import Enum


class Predicate:

    #def __init__(self, name, vars, params, consts=[]):
    def __init__(self, name, params):
        self.name = name
        self.params = params
        #self.vars = vars
        #self.consts = consts
        self.negation = False

    def __str__(self):
        negation = ''
        if self.negation:
            negation = 'not'

        return f'{negation}({self.name} {" ".join(self.params)})'

    def update_params(self, param, _):
        for i in range(len(self.params)):
            p = self.params[i]
            if p in param:
                self.params[i] = param[p]

    def add(self, var):
        self.vars.insert(0, var)

    def add_const(self, const):
        self.consts.insert(0, const)

    def get_vars(self):
        vars = []
        for p in self.params:
            if p[0] == '?':
                vars.append(p)
        return vars


class GroupType(Enum):
    AND = 0
    OR = 1
    FORALL = 2
    EXISTS = 3
    WHEN = 4
    NUMERIC = 5


class PredicateGroup:

    def __init__(self, type, predicate):
        self.type = type
        self.predicate = predicate
        pass

    def update_params(self, params, p_obs):
        pred = self.predicate
        if type(pred) == list:
            for p in pred:
                p.update_params(params, p_obs)
        else:
            self.predicate.update_params(params, p_obs)


class QuantifyGroup(PredicateGroup):

    def __init__(self, type, predicate, params):
        super().__init__(type, predicate)
        self.params = params

    def update_params(self, params, p_obs):
        super().update_params(params, p_obs)
        type = []
        for sp in self.params:

            type = next((x for x in p_obs if x.type == sp.type),None)
            if not type:
                raise Exception('Object of type' + sp.type + ' not defined')

        if self.type == GroupType.FORALL:
            self.type = GroupType.AND
        else:
            self.type = GroupType.OR

        vars = self.predicate.get_vars()

        preds = []

        for t in type.instances:
            pred = copy.deepcopy(self.predicate)
            p = {vars[0]: t}
            pred.update_params(p,[])
            preds.append(pred)
        self.predicate = preds


class ConditionGroup(PredicateGroup):

    def __init__(self, type, predicate, antecedent):
        super().__init__(type, predicate)
        self.antecedent = antecedent

    def update_params(self, params, p_obs):
        super().update_params(params, p_obs)
        self.antecedent.update_params(params, p_obs)



class NumericGroup(PredicateGroup):

    def __init__(self, type, predicate, operator, value):
        super().__init__(type, predicate)
        self.operator = operator
        self.value = value
        self.negation = False
