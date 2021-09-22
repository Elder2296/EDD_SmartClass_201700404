
from Analizer.lexico import tokens

# dictionary of names
names = {}
global types 

types = list()


def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')


def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    types.append(t[3])

def p_items(t):
    """items : items item
             | item
    """

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """



def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]
    types.append(t[1])
def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TCORREO
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                """

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()