# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 06:58:13 2016

@author: John Villlavicencio
"""

class Poly_inv(object):
           
    def __init__(self,term_i):  
        coef_i=term_i.split('/')[0] 
        self.term_i=term_i
        self.coef=float(coef_i)
        self.lap_inv=''
        
    def exp(self):
        l=len(self.term_i)-1
        ex=self.term_i[l]
        if ex=='t':
            ex=1          
        #if ex<=0:
            #return "No es valida la expresion"        
        return int(ex)
    
    def coe_inv(self):
        new_exp=self.exp()-1
        new_coef=1
        if new_exp==1 or new_exp==0:
            new_coef=self.coef
        if new_exp>1:
            for i in range(1,new_exp):
                new_coef = new_coef*(i+1)  
            new_coef=self.coef*new_coef    
        return  new_coef
        
    def laplace_inv(self):       
        if self.exp()==1:    #new_expo=0 restornaun numero 1/k
            if self.coe_inv()==1:
                res='1'
            else:
                res= str(self.coe_inv())
        if self.exp()==2:    #new_expo=1  t/k
            res=str(self.coe_inv()) + 't'      
        if self.exp()>2:
            res=str(self.coe_inv())+'t^'+str(self.exp()-1)+str(self.coe_inv())
        #if self.exp()<1:
            #res= 'No se contempla para ese caso'
        return res

"""funcion que calcula laplace inverso usando la clase poly_inv"""

class lapinv_comp(Poly_inv):                     
        #exps son terminos de la forma k/s^
    def __init__(self, exps):
        polinew=exps.replace('-','+-')        
        term=polinew.split('+')   
        if term[0]=='':
            term=term[1:] 
        num_term=len(term)
        resul=''
        for i in range(0,num_term):
            termi=Poly_inv(term[i])    
            resul= str(termi.laplace_inv())+ '+'+ resul
        resul=resul[0:len(resul)-1]
        #resul.replace('++','+')
        self.lap_inv=resul
        
        
        
        
        
        