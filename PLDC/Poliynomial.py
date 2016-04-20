# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 08:19:37 2016

@author: Velcy Palomino

"""

class Polynomial(object):
                    
    def __init__(self,coefi):
        #coefi est en forma descendente
        coefi.reverse()
        self.coef=coefi
        #coef retorna en forma ascendente
       
    def degree(self):
        return len(self.coef)-1        
                
    #muestra el polinomio en t     
    def showPolt(self):
        if self.degree() == 0:
            return "" + str(self.coef[0])
        if self.degree() == 1:
            return str(self.coef[1]) + "t + " + str(self.coef[0])
        polit = str(self.coef[self.degree()]) + "t^" + str(self.degree())
        for i in range(self.degree()-1, -1, -1):
            if self.coef[i] == 0:
                continue
            elif self.coef[i] > 0:
                polit = polit + " + " + str(self.coef[i])
            elif self.coef[i] < 0:
                polit = polit + " - " + str(-1*(self.coef[i]))
            if i == 1:
                polit = polit + "t"
            elif i > 1:
                polit = polit + "t^" + str(i)
        return polit
    #encuentra los coeficientes de la transformada de lapalce
    def laplace(self):
        list=[]
        for i in range(0, self.degree()+1):
            list.append(0)
        c = Polynomial(list)
        
        for i in range(0,len(self.coef)):
            if i==0:
                c.coef[i]=self.coef[i]
            if i>0:
                new_coef=1
                for j in range(0, i):
                    new_coef = new_coef*(j+1)  
                c.coef[i]=self.coef[i]*new_coef
        return c.coef   # estamos retornando solo los coeficientes
        #return c  si deseamos el polinomio como clase
        
        #muestra el resultado de laplace
    def show(self):
        
        if self.degree()==0:
            return str(self.laplace())+'/s'
        s=''
        a=''
        for i in range(0,len(self.laplace())):
            if self.laplace()[i] == 0:
                a=''                
            if self.laplace()[i] != 0:
                if i==0:
                    s=str(self.laplace()[0])+"/s"
                else:
                     s = s+"+"+str(self.laplace()[i])+  "/s^" + str(i+1)
        s=s+a
        s=s.replace('+-','-')   
        if s[0]=='+':
            s=s[1:]           
        return s
                
                
                

            
  
      
            
            
        
