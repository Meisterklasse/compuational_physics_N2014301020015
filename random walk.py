# -*- coding: utf-8 -*-
"""
Created on Thu Jan 05 17:34:34 2017

@author: yjq
"""
import random
import pylab as pl
class rwalk:
    def __init__(self,total_step=100,walkers=2):
        self.x2ave=[]
        self.x=[0]
        self.total_step=total_step
        self.walkers=walkers
        self.t=[]
        self.line=[]
    
    def random_walk(self):
        for i in range(0,self.total_step):
            for j in range(self.walkers):
                r=random.uniform(0,1)
                if(r<0.5): self.x.append(self.x[j]+1)
                if(r>=0.5): self.x.append(self.x[j]-1)
                self.x[j]=self.x[j]**2
            average2=sum(self.x)/self.walkers
            self.x2ave.append(average2)
            self.t.append(i)
            self.line.append(0.55*self.t[i])
                
        
    def show_results(self):
        pl.plot(self.t,self.x2ave,'.')
        pl.plot(self.t,self.line,'--')
        pl.xlabel('step number(= time)')
        pl.ylabel('<x^2>')
        pl.title('Random walk in one dimension')
a=rwalk()
a.random_walk()
a.show_results()