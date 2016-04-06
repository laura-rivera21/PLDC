# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 08:19:37 2016

@author: Velcy Palomino

"""

class Polynomial(object):
                    
    def __init__(self,coefi):
        self.coef=coefi
       
    def degree(self):
        return len(self.coef)-1        
                
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
                for j in range(1, i+1):
                    new_coef = new_coef*(j+1)  
                c.coef[i]=self.coef[i]*new_coef
        return c.coef   # estamos retornando solo los coeficientes
        #return c  si deseamos el polinomio como clase
        
        #muestra el resultado de laplace
    def show(self):
        
        if self.degree()==0:
            return str(self.laplace())+'/s'
                    
        for i in range(0,len(self.laplace())):
            if self.laplace()[i] != 0:
                if i==0:
                    s=str(self.laplace()[0])+"/s"
                else:
                     s = s+"+"+str(self.laplace()[i])+  "/s^" + str(i+1)
        return s
                
                
                

            
  
      
            
            
        