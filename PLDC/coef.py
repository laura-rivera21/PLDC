# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 05:35:24 2016

@author: Velcy
"""
#Recibe el polinom como string devuelve los coeficientes del polinomio
def coefi(poli):
    #poli debe in gresarse en forma descendente
    #-3t^3+2t-2               
    poli=poli.replace('-','+-')        
    term=poli.split('+')   
    coefi=[]
    exps=[]
    if term[0]=='':
        term=term[1:] 
        
    for i in term:
        l=len(i)-1
        coe= i.split('t')[0]
        if coe=='':
           coe=1
        if coe=='-':
           coe=-1
        ex=i[l]
        if ex=='t':
           ex=1          
        if i.find('t')==-1:
           ex=0     
        exps.append(int(ex))           
        coefi.append(float(coe))
        
    newcoef=[0]*(exps[0]+1)      
    p=0
    #Add 0t to missing terms with exponenets
    for c in exps:                 
        newcoef[exps[0]-c]=coefi[p]
        p+=1
    return newcoef
    
  #funcion de asignacion      