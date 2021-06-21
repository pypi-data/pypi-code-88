from ply import yacc
from plyddl.pddllex import tokens
from plyddl.pddl.domain.domain import Domain
from plyddl.pddl.domain.requirements import Requirements
from plyddl.pddl.domain.types import Type, Variables
from plyddl.pddl.predicate import Predicate, PredicateGroup, ConditionGroup, QuantifyGroup, NumericGroup, GroupType
from plyddl.pddl.domain.action import *

from plyddl.pddl.problem.problem import Problem
from plyddl.pddl.problem.objects import ProblemObjects
from plyddl.pddl.problem.init import Init
from plyddl.pddl.problem.goal import Goal

#print(tokens)


def p_pddl(p):
    """pddl : LPAREN DEFINE domain RPAREN
            | LPAREN DEFINE problem RPAREN"""
    p[0] = p[3]


def p_domain(p):
    """domain :  domain_def requirements_def types_def predicates_def action_def
              |  domain_def requirements_def types_def predicates_def function_def action_def"""
    if len(p) == 6:
        p[0] = Domain(p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = Domain(p[1], p[2], p[3], p[4], p[6], p[5])


def p_domain_def(p):
    """domain_def : LPAREN DOMAIN NAME  RPAREN"""
    p[0] = p[3]


def p_requirements_def(p):
    """requirements_def : LPAREN REQS requirement_list RPAREN"""
    p[0] = Requirements(p[2])


def p_requirement_list(p):
    """requirement_list : requirement
                        | requirement requirement_list"""

    if len(p) == 2:
        p[0] = [p[1]]
    else:
        r_l = p[2]
        r_l.insert(0, p[1])
        p[0] = r_l


def p_requirement(p):
    """
     requirement :  REQ_STRIPS
                   | REQ_TYPING
                   | REQ_DISJUNC_PREC
                   | REQ_EQUALITY
                   | REQ_EXIST_PREC
                   | REQ_UNIV_PREC
                   | REQ_QUANTIF_PREC
                   | REQ_COND_EFF
                   | REQ_FLUENTS
                   | REQ_NUMERIC_FLUENTS
                   | REQ_ADL
    """
    p[0] = p[1]


def p_types_def(p):
    """types_def : LPAREN  TYPES type_list  RPAREN"""
    p[0] = p[3]


def p_function_def(p):
    """function_def : LPAREN FUNCTIONS predicate_list RPAREN"""
    if len(p) == 5:
        p[0] = p[3]


def p_type_list(p):
    """type_list : NAME
                 | NAME type_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        lst = p[2]
        lst.insert(0, p[1])
        p[0] = lst


def p_predicates_def(p):
    """predicates_def : LPAREN PREDICATES predicate_list RPAREN"""
    p[0] = p[3]


def p_predicate_list(p):
    """predicate_list : predicate
                      | predicate  predicate_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        preds = p[2]
        preds.insert(0, p[1])
        p[0] = preds


def p_predicate(p):
    """predicate : LPAREN NAME param_list RPAREN
                 | LPAREN NAME RPAREN
                 | LPAREN NOT predicate RPAREN"""

    if p[2] == '-':
        pred = p[3]
        p[3].negation = True
    else:
        pred = Predicate(p[2], p[3])
    p[0] = pred


def p_precond_predicate_list(p):
    """precond_predicate_list : mixed_predicate_list"""
    p[0] = p[1]


def p_mixed_predicate_list(p):
    """mixed_predicate_list : mixed_predicate
                            | mixed_predicate mixed_predicate_list
                      """
    if len(p) == 2:
        p[0] = [p[1]]
    elif len(p) == 3:
        m_p = p[2]
        m_p.insert(0, p[1])
        p[0] = m_p


def p_predicate_group(p):
    """predicate_group :  LPAREN OR mixed_predicate_list RPAREN
                        | LPAREN AND mixed_predicate_list RPAREN
                        | LPAREN WHEN mixed_predicate mixed_predicate RPAREN
                        """
    spec = p[2]
    if spec in ['and', 'or']:
        if spec == 'and':
            type = GroupType.AND
        elif spec == 'or':
            type = GroupType.OR
        m_p = p[3]
        p[0] = PredicateGroup(type, m_p)
    elif spec == 'when':
        p[0] = ConditionGroup(GroupType.WHEN, p[4], p[3])


def p_quantify_group(p):
    """quantify_group :  LPAREN FORALL LPAREN param_list RPAREN mixed_predicate RPAREN
                       | LPAREN EXISTS LPAREN param_list RPAREN mixed_predicate RPAREN"""

    spec = p[2]
    if spec in ['forall', 'exists']:
        params = p[4]
        if spec == 'forall':
            type = GroupType.FORALL
        else:
            type = GroupType.EXISTS
        p[0] = QuantifyGroup(type, p[6], params)


def p_simple_mixed_predicate(p):
    """simple_mixed_predicate : LPAREN NAME mixed_list RPAREN
                              | LPAREN NAME RPAREN
                              | LPAREN EQUALS mixed_list RPAREN
                              | LPAREN NOT simple_mixed_predicate RPAREN
                              """

    if len(p) == 4:
        p[0] = Predicate(p[2],[])
    else:
        if p[2] == 'not':
            pred = p[3]
            pred.negation = True
            p[0] = pred
        elif p[2] == '+':
            p[0] = Predicate('=', p[3]) #p[3]['var'], p[3]['const'])
        else:
            p[0] = Predicate(p[2], p[3])#['var'], p[3]['const'])


def p_mixed_predicate(p):
    """mixed_predicate : simple_mixed_predicate
                       | predicate_group
                       | quantify_group
                       | numeric_predicate
                       """
    if len(p) == 2:
        p[0] = p[1]


def p_numeric_predicate(p):
    """numeric_predicate : LPAREN NOT numeric_predicate RPAREN
                         | LPAREN EQUALS simple_mixed_predicate NUMBER RPAREN
                         | LPAREN LESSER simple_mixed_predicate NUMBER RPAREN
                         | LPAREN GREATER simple_mixed_predicate NUMBER RPAREN
                         | LPAREN INCREASE simple_mixed_predicate NUMBER RPAREN
                         | LPAREN DECREASE simple_mixed_predicate NUMBER RPAREN
                         | LPAREN ASSIGN simple_mixed_predicate NUMBER RPAREN
                         """
    if len(p) == 5:
        num = p[3]
        num.negation = True
        p[0] = num
    else:
        p[0] = NumericGroup(GroupType.NUMERIC, p[3], p[2], p[4])


def p_param_list(p):
    """param_list : VARIABLE MINUS NAME
                | VARIABLE param_list
                | VARIABLE MINUS NAME param_list"""
    if len(p) == 4:
        p[0] = [Variables([p[1]], p[3])]
    elif len(p) == 3:
        t = p[2]
        t[0].add(p[1])
        p[0] = t
    elif len(p) == 5:
        t = p[4]
        t.insert(0, Variables([p[1]], p[3]))
        p[0] = t


def p_action_def(p):
    """action_def : action_list"""
    p[0] = p[1]


def p_action_list(p):
    """action_list : action
                   | action action_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        a_l = p[2]
        a_l.insert(0, p[1])
        p[0] = a_l


def p_action(p):
    """action : LPAREN ACTION NAME parameter_def precondition_def effect_def RPAREN"""
    p[0] = Action(p[3], p[4], p[5], p[6])


def p_parameter_def(p):
    """parameter_def : ACT_PARAM LPAREN param_list RPAREN"""
    p[0] = p[3]


def p_precondition_def(p):
    """precondition_def :  ACT_PRE mixed_predicate_list"""
    p[0] = p[2]


def p_effect_def(p):
    """effect_def : ACT_EFF mixed_predicate_list"""
    p[0] = p[2]


###############
####PROBLEM####
###############


def p_problem(p):
    """problem : problem_def pb_domain_def objects_def init_def goal_def
                | problem_def pb_domain_def objects_def init_def goal_def metric_def
    """
    if len(p) == 6:
        p[0] = Problem(p[1], p[2], p[3], p[4], p[5])
    else:
        p[0] = Problem(p[1], p[2], p[3], p[4], p[5], p[6])


def p_problem_def(p):
    """problem_def : LPAREN PROBLEM NAME RPAREN"""
    p[0] = p[3]


def p_pb_domain_def(p):
    """pb_domain_def : LPAREN PB_DOMAIN NAME RPAREN"""
    p[0] = p[3]


def p_objects_def(p):
    """objects_def : LPAREN OBJECTS object_list RPAREN """
    p[0] = p[3]


def p_object_list(p):
    """object_list : NAME MINUS NAME
                 | NAME object_list
                 | NAME MINUS NAME object_list"""
    if len(p) == 4:
        p[0] = [Type([p[1]], p[3])]
    elif len(p) == 3:
        t = p[2]
        t[0].add(p[1])
        p[0] = t
    elif len(p) == 5:
        t = p[4]
        t.insert(0, Type([p[1]], p[3]))
        p[0] = t


def p_init_def(p):
    """init_def : LPAREN INIT mixed_predicate_list RPAREN"""
    p[0] = p[3]


def p_goal_def(p):
    """goal_def :  LPAREN GOAL precond_predicate_list RPAREN"""
    p[0] = p[3]


def p_metric_def(p):
    """metric_def : LPAREN METRIC metric RPAREN"""
    p[0] = p[3]


def p_metric(p):
    """metric : MAXIMIZE precond_predicate_list"""
    p[0] = p[2]

###############
#####UTILS#####
###############

def p_constant_list(p):
    """constant_list : NAME
                     | NAME constant_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        consts = p[2]
        consts.insert(0, p[1])
        p[0] = consts


def p_mixed_list(p):
    """mixed_list : VARIABLE
                  | NAME
                  | VARIABLE mixed_list
                  | NAME mixed_list"""
    m_l = []
    if len(p) == 2:
        m_l = [] #{'var': [], 'const': []}
    else:
        m_l = p[2]
    #if p[1][0] == '?':
    #    m_l['var'].insert(0, p[1])
    #else:
    #    m_l['const'].insert(0, p[1])
    m_l.insert(0,p[1])
    p[0] = m_l


def p_var_list(p):
    """var_list : VARIABLE
                | VARIABLE var_list"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        vars = p[2]
        vars.insert(0, p[1])
        p[0] = vars


def p_error(p):
    print(f'Syntax error in input {p}')


parser = yacc.yacc()
