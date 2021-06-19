import ply.lex as lex
import ply.yacc as yacc


tokens = (
   'NUMBER',
    'EQUALS',
    'FLOAT',
   'PLUS',
   'MINUS',
   'TIMES',
   'DIVIDE',
   'LPAREN',
   'RPAREN',
   'EXPO'
)
t_EXPO=     r'\^'
t_EQUALS  = r'\='
t_PLUS    = r'\+'
t_MINUS   = r'\-'
t_TIMES   = r'\*'
t_DIVIDE  = r'\/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore  = ' \t'


def t_error(t):
    print("Illegal character")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (  
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'TIMES', 'DIVIDE' ),
    ('left','EXPO')
    )

def p_operations( p ) :
    '''expr :  expr TIMES expr
            | expr DIVIDE expr
            | expr PLUS expr 
            | expr MINUS expr
            | expr EXPO expr'''
    p[0]=(p[1],p[2],p[3])
    print(p[0])
    if(p[2]=="+"):
        p[0]=p[1]+p[3]
    elif(p[2]=="-"):
        p[0]=p[1]-p[3]
    elif(p[2] == '*') :
        p[0] = p[1] * p[3]
    elif(p[2]=="^"):
        p[0]=p[1] ** p[3]
    else :
        if (p[3] == 0) :
            print("Can't divide by 0")
        else:    
            p[0] = p[1] / p[3]
    

def p_expr2NUM( p ) :
    '''expr : NUMBER 
            | FLOAT'''
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = p[2]

def p_error( p ):
    print("Syntax error in input!")

parser = yacc.yacc()
def inp():
    s=input("Enter expression : ")
    print("\nAST ")
    res=parser.parse(s)
    print("Result : ",res)



s=input(" \n\n   Welcome to Calc ! \nEnter expression : ")
print("\nAST ")
res = parser.parse(s)
print("Result : ",res)

while (True):
        a=input("\nWant to continue?(y/n) :")
        if(a=='y'):
            inp()
        else:
            print("Thank you!")
            break
    