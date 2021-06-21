from ply import lex


tokens = (
    'NUMBER',
    'STRING',
    'PLUS',
    'MINUS',
    'LPAREN',
    'RPAREN',
    'EQUALS',
    'GREATER',
    'LESSER',
    'NAME',
    'VARIABLE',
    'COMMENT'
)

t_PLUS = r'\+'
t_MINUS = r'\-'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ignore = ' \t'
t_EQUALS = r'='
t_GREATER = '>'
t_LESSER = '<'

reserved = {
    'define'       :   'DEFINE',
 'domain'       :   'DOMAIN',
 ':extends'     :   'EXTENDS',
 ':requirements':   'REQS',
 ':strips'      :   'REQ_STRIPS',
 ':typing'      :   'REQ_TYPING',
 ':disjunctive-preconditions' : 'REQ_DISJUNC_PREC',
 ':equality'    :   'REQ_EQUALITY',
 ':existential-preconditions'  :'REQ_EXIST_PREC',
 ':universal-preconditions' : 'REQ_UNIV_PREC',
 ':quantified-preconditions' : 'REQ_QUANTIF_PREC',
 ':conditional-effects' : 'REQ_COND_EFF',
 ':fluents'             : 'REQ_FLUENTS',
 ':numeric-fluents'     : 'REQ_NUMERIC_FLUENTS',
 ':adl'                 : 'REQ_ADL',
 ':functions'           : 'FUNCTIONS',
 ':metric'             : 'METRIC',
 ':types'       :   'TYPES',
 ':constants'   :   'CONST',
 ':predicates'  :   'PREDICATES',
 ':timeless'    :   'TIMELESS',
 ':action'      :   'ACTION',
 ':parameters'  :   'ACT_PARAM',
 ':precondition':   'ACT_PRE',
 ':effect'      :   'ACT_EFF',
 'problem'      :   'PROBLEM',
 ':domain'      :   'PB_DOMAIN',
 ':objects'     :   'OBJECTS',
 ':init'        :   'INIT',
 ':goal'        :   'GOAL',
 'and'          :   'AND',
 'not'          :   'NOT',
 'or'           :   'OR',
 'forall'       :   'FORALL',
 'exists'       :   'EXISTS',
 'when'         :   'WHEN',
 'increase'     :    'INCREASE',
 'decrease'     :   'DECREASE',
 'assign'       :   'ASSIGN',
 'maximize'     :   'MAXIMIZE'
}

tokens += tuple(reserved.values())

def t_KEYWORD(t):
    r':?[a-zA-z_][a-zA-Z_0-9\-]*'
    t.type = reserved.get(t.value, "NAME")
    return t

def t_VARIABLE(t):
    r'\?[a-zA-Z_][a-zA-Z_0-9\-]*'
    t.value = str(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r';.*'

def t_error(t):
    print("Illegal character '%s'" % t.value)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


lexer = lex.lex()
if __name__ == '__main__':
    data = ''' 
           (define
        (domain construction)
        (:extends building)
        (:requirements :strips :typing)
        (:types
            site material - object
            bricks cables windows - material
        )
        (:constants mainsite - site)

        ;(:domain-variables ) ;deprecated

        (:predicates
            (walls-built ?s - site)
            (windows-fitted ?s - site)
            (foundations-set ?s - site)
            (cables-installed ?s - site)
            (site-built ?s - site)
            (on-site ?m - material ?s - site)
            (material-used ?m - material)
        )

        (:timeless (foundations-set mainsite))

        ;(:safety
            ;(forall
            ;    (?s - site) (walls-built ?s)))
            ;deprecated

        (:action BUILD-WALL
            :parameters (?s - site ?b - bricks)
            :precondition (and
                (on-site ?b ?s)
                (foundations-set ?s)
                (not (walls-built ?s))
                (not (material-used ?b))
            )
            :effect (and
                (walls-built ?s)
                (material-used ?b)
            )
            ; :expansion ;deprecated
        )

        (:axiom
            :vars (?s - site)
            :context (and
                (walls-built ?s)
                (windows-fitted ?s)
                (cables-installed ?s)
            )
            :implies (site-built ?s)
        )

        ;Actions omitted for brevity
    )

           '''

    lexer.input(data)
    while True:
         tok = lexer.token()
         if not tok:
             break      # No more input
         print(tok)