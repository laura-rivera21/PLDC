#############EXPRESSION NAME###############
def p_expname(p):
    'pol_var : POLT expname'
    p[0] = str(p[1])

#############POLYNOMIAL VARIABLE###############
def p_pol_var_t(p):
    'pol_var : EXPRNAME'
    p[0] = str(p[1])

def p_pol_var_s(p):
    'pol_var : EXPRNAME'
    p[0] = str(p[1])
